# Copyright (c) Mengning Software. 2023. All rights reserved.
#
# Super IDE licensed under GNU Affero General Public License v3 (AGPL-3.0) .
# You can use this software according to the terms and conditions of the AGPL-3.0.
# You may obtain a copy of AGPL-3.0 at:
#
#    https://www.gnu.org/licenses/agpl-3.0.txt
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the AGPL-3.0 for more details.

import os
import signal
import time

from superide import telemetry
from superide.compat import aio_get_running_loop, is_bytes
from superide.debug import helpers
from superide.debug.exception import DebugInitError
from superide.debug.process.client import DebugClientProcess
from superide import __container_engine__
from superide.toolchain.toolchain import Toolchain

class GDBClientProcess(DebugClientProcess):
    SI_SRC_NAME = ".gdbinit"
    INIT_COMPLETED_BANNER = "Super IDE: Initialization completed"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._target_is_running = False
        self._errors_buffer = b""

    async def run(self,extra_args):  # pylint: disable=arguments-differ
        await super().run()
        # working_dir目前在.superide目录下，目前docker不挂载，这里把生成的.gdbinit文件放到项目目录下
        self.generate_init_script(os.path.join(self.project_dir, self.SI_SRC_NAME))
        gdb_path = __container_engine__
        env_image = 'superide/ubuntu20.04-c-test:latest'
        # start GDB client
        args = [
            gdb_path,
            'run',
            '-i',
            '--rm',
            '--network', 
            'host',
            '-v',
            self.project_dir+':'+self.project_dir,
            env_image,
            'gdb-multiarch',
            '-q',
            '--interpreter=mi2',
            "--directory",
            self.project_dir,
            "-l",
            "10",
            "-x",
            os.path.join(self.project_dir, self.SI_SRC_NAME),
        ]
        args.extend(list(extra_args or []))
        gdb_data_dir = self._get_data_dir(gdb_path)
        if gdb_data_dir:
            args.extend(["--data-directory", gdb_data_dir])
        args.append(self.debug_config.program_path)

        await self.spawn(*args, cwd=self.project_dir, wait_until_exit=True)

    @staticmethod
    def _get_data_dir(gdb_path):
        if "msp430" in gdb_path:
            return None
        gdb_data_dir = os.path.abspath(
            os.path.join(os.path.dirname(gdb_path), "..", "share", "gdb")
        )
        return gdb_data_dir if os.path.isdir(gdb_data_dir) else None

    def generate_init_script(self, dst):
        # default GDB init commands depending on debug tool
        commands = self.debug_config.get_init_script("gdb").split("\n")

        if self.debug_config.init_cmds:
            commands = self.debug_config.init_cmds
        commands.extend(self.debug_config.extra_cmds)

        if not any("define si_reset_run_target" in cmd for cmd in commands):
            commands = [
                "define si_reset_run_target",
                "   echo Warning! Undefined si_reset_run_target command\\n",
                "   monitor reset",
                "end",
            ] + commands
        if not any("define si_reset_halt_target" in cmd for cmd in commands):
            commands = [
                "define si_reset_halt_target",
                "   echo Warning! Undefined si_reset_halt_target command\\n",
                "   monitor reset halt",
                "end",
            ] + commands
        if not any("define si_restart_target" in cmd for cmd in commands):
            commands += [
                "define si_restart_target",
                "   si_reset_halt_target",
                "   $INIT_BREAK",
                "   %s" % ("continue" if self.debug_config.init_break else "next"),
                "end",
            ]

        banner = [
            "echo Super IDE Unified Debugger -> https://\\n",
            "echo Super IDE: debug_tool = %s\\n" % self.debug_config.tool_name,
            "echo Super IDE: Initializing remote target...\\n",
        ]
        footer = ["echo %s\\n" % self.INIT_COMPLETED_BANNER]
        commands = banner + commands + footer

        with open(dst, mode="w", encoding="utf8") as fp:
            fp.write("\n".join(self.debug_config.reveal_patterns(commands)))

    def stdin_data_received(self, data):
        super().stdin_data_received(data)
        if b"-exec-run" in data:
            if self._target_is_running:
                token, _ = data.split(b"-", 1)
                self.stdout_data_received(token + b"^running\n")
                return
            # config和platform部分代码停用
            # if self.debug_config.platform.is_embedded():
            #     data = data.replace(b"-exec-run", b"-exec-continue")

        if b"-exec-continue" in data:
            self._target_is_running = True
        if b"-gdb-exit" in data or data.strip() in (b"q", b"quit"):
            # Allow terminating via SIGINT/CTRL+C
            signal.signal(signal.SIGINT, signal.default_int_handler)
            self.transport.get_pipe_transport(0).write(b"si_reset_run_target\n")
        self.transport.get_pipe_transport(0).write(data)

    def stdout_data_received(self, data):
        super().stdout_data_received(data)
        self._handle_error(data)
        # go to init break automatically
        if self.INIT_COMPLETED_BANNER.encode() in data:
            telemetry.log_debug_started(self.debug_config)
            self._auto_exec_continue()

    def console_log(self, msg):
        if helpers.is_gdbmi_mode():
            msg = helpers.escape_gdbmi_stream("~", msg)
        self.stdout_data_received(msg if is_bytes(msg) else msg.encode())

    def _auto_exec_continue(self):
        auto_exec_delay = 0.5  # in seconds
        if self._last_activity > (time.time() - auto_exec_delay):
            aio_get_running_loop().call_later(0.1, self._auto_exec_continue)
            return

        if not self.debug_config.init_break or self._target_is_running:
            return

        self.console_log(
            "Super IDE: Resume the execution to `debug_init_break = %s`\n"
            % self.debug_config.init_break
        )
        self.console_log(
            "Super IDE: More configuration options -> https://\n"
        )
        # 根据是否是嵌入式程序和mi模式确定不同的启动指令
        # TODO：目前代码没有platform类，需要在ini增加字段或其他处理
        # if self.debug_config.platform.is_embedded():
        # self.transport.get_pipe_transport(0).write(
        #          b"0-exec-continue\n" if helpers.is_gdbmi_mode() else b"continue\n"
        #      )
        # else:
        #     self.transport.get_pipe_transport(0).write(
        #         b"0-exec-run\n" if helpers.is_gdbmi_mode() else b"run\n"
        #     )
        self._target_is_running = True

    def stderr_data_received(self, data):
        super().stderr_data_received(data)
        self._handle_error(data)

    def _handle_error(self, data):
        self._errors_buffer = (self._errors_buffer + data)[-8192:]  # keep last 8 KBytes
        if not (
            self.SI_SRC_NAME.encode() in self._errors_buffer
            and b"Error in sourced" in self._errors_buffer
        ):
            return
        telemetry.log_debug_exception(
            DebugInitError(self._errors_buffer.decode()), self.debug_config
        )
        self.transport.close()

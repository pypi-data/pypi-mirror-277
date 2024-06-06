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

from superide.debug.config.base import DebugConfigBase


class RenodeDebugConfig(DebugConfigBase):
    # 此处暂时要查询补充wsl IP地址
    # DEFAULT_PORT = "172.22.242.241:3333"
    DEFAULT_PORT = ":3333"
    GDB_INIT_SCRIPT = """
define si_reset_halt_target
    monitor machine Reset
    $LOAD_CMDS
    monitor start
end

define si_reset_run_target
    si_reset_halt_target
end

target extended-remote $DEBUG_PORT
$LOAD_CMDS
$INIT_BREAK
monitor start
"""

    @property
    def server_ready_pattern(self):
        return super().server_ready_pattern or (
            "GDB server with all CPUs started on port"
        )

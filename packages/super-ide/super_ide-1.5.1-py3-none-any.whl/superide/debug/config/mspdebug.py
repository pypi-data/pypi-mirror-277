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


class MspdebugDebugConfig(DebugConfigBase):
    DEFAULT_PORT = ":2000"
    GDB_INIT_SCRIPT = """
define si_reset_halt_target
end

define si_reset_run_target
end

target remote $DEBUG_PORT
monitor erase
$LOAD_CMDS
si_reset_halt_target
$INIT_BREAK
"""

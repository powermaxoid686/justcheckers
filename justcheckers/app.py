#
# Copyright (c) 2014 Dorian Pula <dorian.pula@amber-penguin-software.ca>
#
# justCheckers is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# justCheckers is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with justCheckers.  If not, see <http://www.gnu.org/licenses/>.
#
# Please share and enjoy!
#

import logging
import os
import sys

from PySide import QtGui

import justcheckers
from justcheckers.ui.window import DesktopGameWindow


LOG = logging.getLogger(__name__)


def main():
    """Main entry point into the app."""
    app = QtGui.QApplication(sys.argv)
    log_system_and_game_info()
    view = DesktopGameWindow()
    view.show()
    app.exec_()
    sys.exit()


def log_system_and_game_info():
    """Logs information about the game and system running the game."""
    LOG.info('justCheckers -- v{}'.format(justcheckers.__version__))

    message = 'I am running on {os}.\nMy screen is {height}x{width}'
    geometry = QtGui.QDesktopWidget().availableGeometry()

    os_sys = sys.platform
    if sys.platform == 'posix':
        os_name, _, _, _, os_arch = os.uname()
        os_sys = '{name} {arch}'.format(name=os_name, arch=os_arch)

    LOG.info(message.format(os=os_sys, height=geometry.height(), width=geometry.width()))


if __name__ == '__main__':
    main()

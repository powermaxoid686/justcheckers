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

"""
Main window for the game.

:copyright: Copyright 2013, Dorian Pula <dorian.pula@amber-penguin-software.ca>
:license: GPL v3+
"""

import os
import sys

from PySide import QtCore
from PySide import QtGui


class MainMenuView(QtGui.QWidget):
    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(MainMenuView, self).__init__()
        self.setup_components()

    def setup_components(self):
        """Setup the components that make up the widget."""
        print(self.get_system_info())
        self.new_game = QtGui.QPushButton('&New Game', self)
        self.open_game = QtGui.QPushButton('&Open Game', self)
        self.save_game = QtGui.QPushButton('&Save Game', self)
        # TODO Render buttons greyed out.

        self.about_game = QtGui.QPushButton('About Game', self)
        # TODO Add links to site and display license inside about game widget.
        self.settings = QtGui.QPushButton('Settings', self)
        self.exit_button = QtGui.QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.exit_app)

        widget_layout = QtGui.QVBoxLayout(self)
        widget_layout.addStretch()
        widget_layout.addWidget(self.new_game)
        widget_layout.addWidget(self.open_game)
        widget_layout.addWidget(self.save_game)
        widget_layout.addWidget(self.about_game)
        widget_layout.addWidget(self.settings)
        widget_layout.addWidget(self.exit_button)
        widget_layout.addStretch()
        self.setLayout(widget_layout)

    @staticmethod
    def get_system_info():
        """Retrieve information about the system."""
        message = 'I am running on {os}.\nMy screen is {height}x{width}'
        geometry = QtGui.QDesktopWidget().availableGeometry()

        os_sys = sys.platform
        if sys.platform == 'posix':
            os_name, _, _, _, os_arch = os.uname()
            os_sys = '{name} {arch}'.format(name=os_name, arch=os_arch)

        return message.format(os=os_sys, height=geometry.height(), width=geometry.width())

    def exit_app(self):
        """Exits the application."""
        QtCore.QCoreApplication.instance().exit()

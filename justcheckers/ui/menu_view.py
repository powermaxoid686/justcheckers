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


from PySide import QtCore
from PySide import QtGui


class MainMenuView(QtGui.QWidget):
    """Main menu for the game."""

    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(MainMenuView, self).__init__()
        self.setup_components()

    def setup_components(self):
        """Setup the components that make up the widget."""
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

    def exit_app(self):
        """Exits the application."""
        QtCore.QCoreApplication.instance().exit()

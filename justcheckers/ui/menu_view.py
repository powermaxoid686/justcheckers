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

from justcheckers.ui import util

class MainMenuView(QtGui.QWidget):
    """Main menu for the game."""

    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(MainMenuView, self).__init__()
        self.setup_components()

    def setup_components(self):
        """Setup the components that make up the widget."""
        self.init_justcheckers_logo()

        self.new_game = self.create_menu_button('&New Game')
        self.open_game = self.create_menu_button('&Open Game')
        self.save_game = self.create_menu_button('&Save Game')

        self.about_game = self.create_menu_button('About Game')
        # TODO Add links to site and display license inside about game widget.
        self.settings = self.create_menu_button('Settings')
        self.exit_button = self.create_menu_button('Exit', enabled=True)
        self.exit_button.clicked.connect(self.exit_app)

        widget_layout = QtGui.QVBoxLayout(self)
        widget_layout.addStretch()
        widget_layout.addWidget(self.logo_label)
        widget_layout.addStretch()
        widget_layout.addWidget(self.new_game)
        widget_layout.addWidget(self.open_game)
        widget_layout.addWidget(self.save_game)
        widget_layout.addWidget(self.about_game)
        widget_layout.addWidget(self.settings)
        widget_layout.addWidget(self.exit_button)
        widget_layout.addStretch()
        self.setLayout(widget_layout)

    def init_justcheckers_logo(self):

        logo_pixmap = QtGui.QPixmap(util.path_to_asset('logo.png'))
        view_size = self.size()
        image_size = logo_pixmap.size()
        logo_pixmap = logo_pixmap.scaledToWidth(view_size.width())
        logo_pixmap.fill(QtGui.QColor(255, 255, 255, 125))
        logo_pixmap.load(util.path_to_asset('logo.png'))

        self.logo_label = QtGui.QLabel('justCheckers', self)
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)

    def create_menu_button(self, label, enabled=False):
        """Creates a menu button with a consistent look & feel."""
        menu_button = QtGui.QPushButton(label, self)
        menu_button.setFixedHeight(50)
        menu_button.setEnabled(enabled)
        return menu_button

    def exit_app(self):
        """Exits the application."""
        QtCore.QCoreApplication.instance().exit()

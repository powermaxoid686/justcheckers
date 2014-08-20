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


from PySide import QtGui

from justcheckers.ui.info_view import InfoView
from justcheckers.ui.menu_view import MainMenuView
from justcheckers.ui import util

class DesktopGameWindow(QtGui.QMainWindow):
    """Main window for the game."""
    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(DesktopGameWindow, self).__init__()
        self.setWindowTitle('justCheckers')
        self.setGeometry(300, 300, 800, 600)

        self.setWindowIcon(QtGui.QIcon(util.path_to_asset('icon.png')))
        self.setup_components()
        self.add_backdrop()
        self.center()

    def add_backdrop(self):
        """Adds a backdrop image to the game."""
        tile = QtGui.QPixmap(util.path_to_asset('backdrop.jpg'))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, tile)
        self.setPalette(palette)

    def setup_components(self):
        """Setup the components that make up the widget."""
        self.view_stack = QtGui.QStackedWidget()
        self.view_stack.addWidget(MainMenuView())
        self.view_stack.addWidget(InfoView())
        self.setCentralWidget(self.view_stack)

    def center(self):
        """Centers the widget in the middle of the screen."""
        widget_rectangle = self.frameGeometry()
        center_point = QtGui.QDesktopWidget().availableGeometry().center()
        widget_rectangle.moveCenter(center_point)
        self.move(widget_rectangle.topLeft())



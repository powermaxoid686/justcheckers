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
from PySide import QtCore


class GameBoardWidget(QtGui.QGraphicsView):
    def __init__(self, scene):
        super(GameBoardWidget, self).__init__(scene)
        self.scene = scene

    def create_checker_board(self):

        redness = QtGui.QBrush(color=QtCore.Qt.darkRed)
        redness_pen = QtGui.QPen(color=QtCore.Qt.darkRed)
        self.scene.addRect(10, 10, 50, 50, pen=redness_pen, brush=redness)
        self.scene.addText('Hello world...')

    # TODO Add in number of captured pieces and whose turn it is.


class GameView(QtGui.QWidget):
    """Game viewer for the game's license, etc."""

    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(GameView, self).__init__()
        self.setup_components()

    def setup_components(self):
        self.game_board_scene = QtGui.QGraphicsScene()
        self.game_board = GameBoardWidget(self.game_board_scene)

        self.game_board.create_checker_board()
        self.game_board.show()


        exit_button = QtGui.QPushButton('Back to Menu', self)
        exit_button.setFixedHeight(50)
        exit_button.clicked.connect(self.switch_to_menu_view)

        widget_layout = QtGui.QVBoxLayout(self)
        widget_layout.addWidget(self.game_board)

        button_row = QtGui.QHBoxLayout(self)
        button_row.addWidget(exit_button)

        widget_layout.addLayout(button_row)

        self.setLayout(widget_layout)

    def switch_to_menu_view(self):
        self.parentWidget().setCurrentIndex(0)

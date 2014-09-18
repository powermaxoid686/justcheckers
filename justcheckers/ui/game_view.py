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

from collections import namedtuple

from PySide import QtGui
from PySide import QtCore

from justcheckers.game import board


Coordinates = namedtuple('Coordinates', ['x', 'y'])


class BoardSquare(QtGui.QGraphicsItem):
    """A single graphical unit that makes up the checkerboard."""

    def __init__(self, coordinates, game_board, parent=None):
        """
        Create a board square.

        :param coordinates: A tuple with the row and column of board.
        :param game_board: A reference to the game board to display the current state of the game.
        :param parent: The parent widget for this graphical item.
        :return: A graphical item representing a specific square on a checkerboard.
        """
        super(BoardSquare, self).__init__(parent)
        self.color = QtGui.QColor(QtCore.Qt.blue)
        self.pixmap = None
        # self.dragOver = False

        # TODO Add validation that coordinates match a real active game.
        self.coordinates = coordinates
        self.game_board = game_board

        # self.setAcceptDrops(True)

    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasColor() or \
    #             (isinstance(self, RobotHead) and event.mimeData().hasImage()):
    #         event.setAccepted(True)
    #         self.dragOver = True
    #         self.update()
    #     else:
    #         event.setAccepted(False)
    #
    # def dragLeaveEvent(self, event):
    #     self.dragOver = False
    #     self.update()
    #
    # def dropEvent(self, event):
    #     self.dragOver = False
    #     if event.mimeData().hasColor():
    #         self.color = QtGui.QColor(event.mimeData().colorData())
    #     elif event.mimeData().hasImage():
    #         self.pixmap = QtGui.QPixmap(event.mimeData().imageData())
    #
    #     self.update()

    def boundingRect(self):
        # return QtCore.QRectF(-15, -50, 30, 50)
        return QtCore.QRectF()

    def paint(self, painter, option, widget=None):

        # Draw the board
        self.color = QtGui.QColor(QtCore.Qt.black)
        if self.game_board.is_illegal_space(self.coordinates.x, self.coordinates.y):
            self.color = QtGui.QColor(QtCore.Qt.white)

        painter.setPen(QtGui.QPen(QtCore.Qt.darkYellow, 2))
        painter.setBrush(self.color)
        painter.drawRoundedRect(0, 0, 50, 50, 25, 25, QtCore.Qt.RelativeSize)

        # Draw the underlying piece.
        # TODO Escape if empty square.

        # TODO Add in a phantom outline of piece when dragging and dropping between board spaces
        self.token_colour = QtGui.QColor(QtCore.Qt.blue)
        if self.game_board.is_light(self.coordinates.x, self.coordinates.y):
            self.token_colour = QtGui.QColor(QtCore.Qt.lightBlue)



class GameBoardWidget(QtGui.QGraphicsView):
    def __init__(self, scene):
        super(GameBoardWidget, self).__init__(scene)
        self.scene = scene

    def create_checker_board(self):

        # TODO Cleaner implementation of passing in game board.
        game_board = board.Board()
        game_board.setup_new_game()

        redness = QtGui.QBrush(color=QtCore.Qt.darkRed)
        redness_pen = QtGui.QPen(color=QtCore.Qt.darkRed)

        # TODO Create a nicer board behind the "floating" squares
        self.scene.addRect(-5, -5, 55 * 8 + 5, 55 * 8 + 5, pen=redness_pen, brush=redness)

        for x in xrange(8):
            for y in xrange(8):

                board_coords = Coordinates(x=x, y=y)
                current_coords = Coordinates(x=55 * board_coords.x, y=55 * board_coords.y)
                self.scene.addRect(current_coords.x, current_coords.y, 50, 50, pen=redness_pen, brush=redness)

                item = BoardSquare(board_coords, game_board)
                item.setPos(current_coords.x, current_coords.y)
                self.scene.addItem(item)


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

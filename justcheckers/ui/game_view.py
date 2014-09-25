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
from justcheckers.game.rules import Rules


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

        # TODO Add validation that coordinates match a real active game.
        self.coordinates = coordinates
        self.game_board = game_board

    def boundingRect(self):
        return QtCore.QRectF(-15, -50, 30, 50)

    def paint(self, painter, option, widget=None):

        # Draw the board
        self.color = QtGui.QColor(QtCore.Qt.black)
        if self.game_board.is_illegal_space(self.coordinates.x, self.coordinates.y):
            self.color = QtGui.QColor(QtCore.Qt.white)

        painter.setBrush(self.color)
        painter.drawRect(0, 0, 50, 50)

        # Draw the underlying piece.
        if (self.game_board.is_empty(self.coordinates.x, self.coordinates.y)
            or self.game_board.is_illegal_space(self.coordinates.x, self.coordinates.y)):
            return

        # TODO Add in a phantom outline of piece when dragging and dropping between board spaces
        self.token_colour = QtGui.QColor(QtCore.Qt.darkGray)
        if self.game_board.is_light(self.coordinates.x, self.coordinates.y):
            self.token_colour = QtGui.QColor(QtCore.Qt.white)

        painter.setPen(QtGui.QPen(QtCore.Qt.darkYellow, 2))
        painter.setBrush(self.token_colour)
        painter.drawEllipse(5, 5, 40, 40)
        if self.game_board.is_king(self.coordinates.x, self.coordinates.y):
            painter.drawText(15, 15, 'King')


class BoardBackground(QtGui.QGraphicsItem):
    """A graphical unit for the background of the checkerboard."""

    def __init__(self, board_size=Rules.STANDARD_BOARD_SIZE, parent=None):
        """
        Create a board square.

        :param board_size: The size of the board in terms of rows or columns.
        :param parent: The parent widget for this graphical item.
        :return: A graphical item representing the background of a checkerboard.
        """
        super(BoardBackground, self).__init__(parent)
        self.board_size = board_size

    def boundingRect(self):
        return QtCore.QRectF(-15, -50, 30, 50)

    def paint(self, painter, option, widget=None):
        pixel_dimensions = 55 * self.board_size
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))

        # FFC200
        painter.setBrush(QtGui.QColor(255, 194, 0))
        painter.drawRoundedRect(
            -1 * pixel_dimensions,
            -1 * pixel_dimensions,
            pixel_dimensions + 10,
            pixel_dimensions + 10,
            10, 10, QtCore.Qt.RelativeSize)


class GameBoardWidget(QtGui.QGraphicsView):

    mouse_move = QtCore.Signal(int, int)

    def __init__(self, scene):
        super(GameBoardWidget, self).__init__(scene)
        self.scene = scene

    def create_checker_board(self):
        # TODO Cleaner implementation of passing in game board.
        game_board = board.Board()
        game_board.setup_new_game()

        board_background = BoardBackground()
        self.scene.addItem(board_background)

        for row in xrange(8):
            for column in xrange(8):
                board_coords = Coordinates(x=column, y=row)
                current_coords = Coordinates(x=55 * board_coords.x, y=55 * board_coords.y)

                print("{}x{} = board, {}, {} = real".format(board_coords.x, board_coords.y, current_coords.x, current_coords.y))

                item = BoardSquare(board_coords, game_board, parent=board_background)
                item.setPos(-1 * current_coords.x, -1 * current_coords.y)

    # TODO Add in number of captured pieces and whose turn it is.

    def mouseMoveEvent(self, event):
        # msg = '({}, {})'.format(event.x(), event.y())
        # self.mouse_move.emit(msg)
        self.mouse_move.emit(event.x(), event.y())

    def mousePressEvent(self, event):
        self.mouse_move.emit(event.x(), event.y())


class GameView(QtGui.QWidget):
    """Game viewer for the game's license, etc."""

    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(GameView, self).__init__()
        self.spaces_moved = 0
        self.setup_components()

    def setup_components(self):
        self.game_board_scene = QtGui.QGraphicsScene()
        self.game_board_widget = GameBoardWidget(self.game_board_scene)
        self.game_board_widget.mouse_move.connect(self.update_coordinates)

        self.game_board_widget.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(QtCore.Qt.green)))
        self.game_board_widget.create_checker_board()

        exit_button = QtGui.QPushButton('Back to Menu', self)
        exit_button.setFixedHeight(50)
        exit_button.clicked.connect(self.switch_to_menu_view)

        widget_layout = QtGui.QVBoxLayout(self)
        widget_layout.addWidget(self.game_board_widget)

        self.coordinate_label = QtGui.QLabel('Coords: ')

        button_row = QtGui.QHBoxLayout(self)
        button_row.addWidget(self.coordinate_label)
        button_row.addWidget(exit_button)

        widget_layout.addLayout(button_row)

        self.setLayout(widget_layout)

    def switch_to_menu_view(self):
        self.parentWidget().setCurrentIndex(0)

    @QtCore.Slot(int, int)
    def update_coordinates(self, x, y):
        self.spaces_moved += 1
        text = 'Coords: {} {} - Moved: {}'.format(x, y, self.spaces_moved)
        self.coordinate_label.setText(text)
        self.update()

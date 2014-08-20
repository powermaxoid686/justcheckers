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

from enum import Enum

from justcheckers.game import rules


class Square(Enum):
    """Represents the state of a single square on a checkerboard."""
    WHITE = -1
    EMPTY = 0
    LIGHT_PAWN = 1
    LIGHT_KING = 2
    DARK_PAWN = 3
    DARK_KING = 4


class Board(object):
    """
     * Container for the state of the checker board during a game.
     *
     * The size of the board is defined by the number of squares along one side,
     * since all checker boards are square. The board coordinate system has both
     * horizontal and vertical numeric components ranging from 0 to boardSize-1.
     * Depicted on-screen, the horizontal component extends to the right and the
     * vertical component extends downwards, making the upper left square (0, 0) and
     * the lower right square (boardSize-1, boardSize-1).
     *
     * <b>Navigating through the Board</b> Internally, the checker board is
     * organized as a two-dimensional array. So when iterating through the board,
     * you first specify the vertical component and then the horizontal component.
     * Another way of thinking about is first specifying which row you want to look
     * at from top to bottom. Then you specify how across the row you are looking at
     * from left to right.
     *
     * <b>Players Places</b> The light player (the starting player) starts at the
     * top of the board. The dark player starts at the bottom of the board.
     *
     * @author Dorian Pula
     * @author Ross Etchells
    """

    def __init__(self, size=rules.Rules.STANDARD_BOARD_SIZE, mirrored=False):
        self.board_size = size
        self._board = [[Square.EMPTY for y in xrange(0, self.board_size)] for x in xrange(0, self.board_size)]

        # /**
        #  * Clears the board of pieces. Creates a brand new empty board already laid
        #  * out by the rules (regular or mirrored).
        #  */
        for row in xrange(0, size):
            for col in xrange(0, size):

                # Mirrored has opposite setup to a regular board.
                if (row % 2 == 0) and (col % 2 == 0):
                    if mirrored:
                        self._board[row][col] = Square.WHITE
                    else:
                        self._board[row][col] = Square.EMPTY

                elif (row % 2 == 0) and (col % 2 == 1):
                    if mirrored:
                        self._board[row][col] = Square.EMPTY
                    else:
                        self._board[row][col] = Square.WHITE

                elif (row % 2 == 1) and (col % 2 == 0):
                    if mirrored:
                        self._board[row][col] = Square.EMPTY
                    else:
                        self._board[row][col] = Square.WHITE
                else:
                    if mirrored:
                        self._board[row][col] = Square.WHITE
                    else:
                        self._board[row][col] = Square.EMPTY

    def is_inside_board(self, row, col):
        return (0 <= row < self.board_size) and (0 <= col < self.board_size)

    def is_dark(self, row, col):
        """
        /**
         * Determines whether the piece at board coordinate (row, col) is dark. If
         * the coordinates do not exist on the board or are empty, this method will
         * return false.
         *
         * @param row
         *            The row of the square.
         * @param col
         *            The column of the square.
         * @return True if the piece at the specified coordinate is dark. False if
         *         otherwise.
         */
        """
        return self.is_inside_board(row, col) and self._board[row][col] in [Square.DARK_KING, Square.DARK_PAWN]

    def is_empty(self, row, col):
        """
        /**
        * Determines whether the piece at board coordinate (row, col) is empty. If
        * the coordinates do not exist on the board or is illegal, this method will
        * return False.
        *
        * @param row
        *            The row of the square.
        * @param col
        *            The column of the square.
        * @return True if the piece at the specified coordinate is empty. False if
        *         otherwise.
        */
        """
        return self.is_inside_board(row, col) and self._board[row][col] == Square.EMPTY

    def is_illegal_space(self, row, col):
        """
        /**
         * Determines whether the board coordinate (x, y) is used in the game. In
         * most cases, all light spaces on the board will be considered illegal.
         * Also, any coordinate which does not exist is also considered illegal.
         *
         * @param row
         *            The row of the square.
         * @param col
         *            The column of the square.
         * @return True if the specified coordinate is nonexistent or unused in the
         *         current rules. False if otherwise.
         */
         """
        return self.is_inside_board(row, col) and self._board[row][col] == Square.WHITE

    # /**
    #  * Determines whether the piece at board coordinate (row, col) is a king. If
    #  * the coordinates do not exist on the board or are empty, this method will
    #  * return False.
    #  *
    #  * @param row
    #  *            The row of the square.
    #  * @param col
    #  *            The column of the square.
    #  * @return True if the piece at the specified coordinate is a king. False if
    #  *         otherwise.
    #  */
    def is_king(self, row, col):
        return self.is_inside_board(row, col) and self._board[row][col] in [Square.LIGHT_KING, Square.DARK_KING]

    # /**
    #  * Returns if a position specified is legal. Returns true if the position is
    #  * on the board, and if the space is not an illegal white space. Returns
    #  * False otherwise.
    #  *
    #  * @param row
    #  *            The row coordinate of the position.
    #  * @param col
    #  *            The column coordinate of the position.
    #  * @return Returns true if the position is a legal playing position.
    #  */
    def is_legal_position(self, row, col):
        return self.is_inside_board(row, col) and not self.is_illegal_space(row, col)

    # /**
    #  * Determines whether the piece at board coordinate (row, col) is light. If
    #  * the coordinates do not exist on the board or are empty, this method will
    #  * return False.
    #  *
    #  * @param row
    #  *            The row of the square.
    #  * @param col
    #  *            The column of the square.
    #  * @return True if the piece at the specified coordinate is light. False if
    #  *         otherwise.
    #  */
    def is_light(self, row, col):
        return self.is_inside_board(row, col) and self._board[row][col] in [Square.LIGHT_KING, Square.LIGHT_PAWN]

    # /**
    #  * Determines whether the piece at board coordinate (row, col) is a pawn. If
    #  * the coordinates do not exist on the board or are empty, this method will
    #  * return False.
    #  *
    #  * @param row
    #  *            The row of the square.
    #  * @param col
    #  *            The column of the square.
    #  * @return True if the piece at the specified coordinate is a pawn. False if
    #  *         otherwise.
    #  */
    def is_pawn(self, row, col):
        return self.is_inside_board(row, col) and self._board[row][col] in [Square.LIGHT_PAWN, Square.DARK_PAWN]

    # /**
    #  * Moves a pieces from one location to another. This method should be called
    #  * from the Game using this Board. This method does not check for rule
    #  * validity but does check for illegal white spaces. Also checks that the
    #  * destination position is empty.
    #  *
    #  * @param sourceRow
    #  *            The row from where the piece is moving from.
    #  * @param sourceCol
    #  *            The column from where the piece is moving from.
    #  * @param targetRow
    #  *            The row to where the piece is moving to.
    #  * @param targetCol
    #  *            The column to where the piece is moving to.
    #  */
    def move_piece(self, source_row, source_col, target_row, target_col):

        if (self.is_legal_position(source_row, source_col)
                and self.is_legal_position(target_row, target_col)
                and self._board[target_row][target_col] == Square.EMPTY):

            self._board[source_row][source_col], self._board[target_row][target_col] = (
                Square.EMPTY, self._board[source_row][source_col])

    # /**
    #  * Removes a pieces from the specified location. This method should be
    #  * called from the Game using this Board. This method does not check for
    #  * rule validity but does check for illegal white spaces.
    #  *
    #  * @param row
    #  *            The row where the piece is to be removed from.
    #  * @param col
    #  *            The column where the piece is to be removed from.
    #  */
    def remove_piece(self, row, col):
        if self.is_legal_position(row, col):
            self._board[row][col] = Square.EMPTY

    # /**
    #  * Setups the board for a new game. There are three different setups for the
    #  * three different types of boards:
    #  *
    #  * <table>
    #  * <tr>
    #  * <b>
    #  * <td>Name</td>
    #  * <td>Size</td>
    #  * <td>Number of Pieces Per Player</td>
    #  * <td>Number of Rows Per Player</td>
    #  * </b>
    #  * </tr>
    #  * <tr>
    #  * <td>Standard</td>
    #  * <td>8 x 8</td>
    #  * <td>12</td>
    #  * <td>3</td>
    #  * </tr>
    #  * <tr>
    #  * <td>International</td>
    #  * <td>10 x 10</td>
    #  * <td>20</td>
    #  * <td>4</td>
    #  * </tr>
    #  * <tr>
    #  * <td>Canadian</td>
    #  * <td>12 x 12</td>
    #  * <td>30</td>
    #  * <td>5</td>
    #  * </tr>
    #  * </table>
    #  *
    #  * The columns containing the players' tokens alternate between columns. The
    #  * dark player traditionally takes the first few upper rows (0-3). The light
    #  * player takes the last of the lower rows (5-7, 6-9 or 7-11).
    #  *
    #  * Note that the suicide checkers variant has a completely different setup,
    #  * and has a setup function of its own: setupNewSuicideGame().
    #  */
    def setup_new_game(self):

        # Used to decide which rows to fill up.
        # Figure out the size of the board.
        if self.board_size == rules.InternationalRules.INTERNATIONAL_BOARD_SIZE:
            dark_player_bottom_row = 3
            light_player_top_row = 6
        elif self.board_size == rules.CanadianRules.CANADIAN_BOARD_SIZE:
            dark_player_bottom_row = 3
            light_player_top_row = 7
        else:
            # Default board is 8x8 Standard size.
            dark_player_bottom_row = 2
            light_player_top_row = 5

        # Go through the board and set it up.
        for row in xrange(0, self.board_size):
            for col in xrange(0, self.board_size):
                if row <= dark_player_bottom_row and self._board[row][col] == Square.EMPTY:
                    self._board[row][col] = Square.DARK_PAWN
                elif row >= light_player_top_row and self._board[row][col] == Square.EMPTY:
                    self._board[row][col] = Square.LIGHT_PAWN

    # /**
    #  * Setups a checker board according to the suicide "French" rules.
    #  */
    def setup_new_suicide_game(self):
        # TODO: Implement the suicide game setup.
        pass

    # /**
    #  * Returns a string to represent the board state. This string is formatted
    #  * for use as a simple board display in the command window.
    #  *
    #  * <b>Legend</b> ## - White space which the piece can not move on to. __ -
    #  * An empty space. LP - A light pawn. LK - A light king. DP - A dark pawn.
    #  * DK - A dark king.
    #  *
    #  * @return A string representing the current board state.
    #  */
    def __str__(self):

        # Prepare for output with a nice looking to banner.
        output = "   "
        for row in xrange(0, self.board_size):
            if row < 9:
                output = '{} {} '.format(output, row + 1)
            else:
                output = '{} {}'.format(output, row + 1)
        output = output + "\n\n"

        output_atom = {
            Square.WHITE: u"\u2588\u2588\u2588",
            Square.EMPTY: u"   ",
            Square.LIGHT_PAWN: u" \u2659 ",
            Square.LIGHT_KING: u" \u2654 ",
            Square.DARK_PAWN: u" \u265F ",
            Square.DARK_KING: u" \u265A ",
        }

        # Go row by row, printing out the row number and the board's state.
        for row in xrange(0, self.board_size):
            if row < 9:
                output = u'{}{}  '.format(output, row + 1)
            else:
                output = u'{}{} '.format(output, row + 1)

            # // Get current row's state.
            for col in xrange(0, self.board_size):
                output = output + output_atom[self._board[row][col]]

            output = output + "\n"

        return output

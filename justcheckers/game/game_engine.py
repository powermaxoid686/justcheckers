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


def canJump(game, sourceRow, sourceCol, targetRow, targetCol):
    # TODO: Implement me.
    # TODO: Make as private method.
    return False


# /**
#  * Returns if a piece can or cannot move. This move maybe either be a move
#  * or a jump. This method is called by a user interface when a user wants to
#  * moves a piece on screen or over the network. The piece can moved if the
#  * current state of the game allows for it to do so.
#  *
#  * TODO: Add priority for king jumps over pawn jumps for any variants that
#  * do so.
#  *
#  * @param sourceRow
#  *            The row from where the piece is moving from.
#  * @param sourceCol
#  *            The column from where the piece is moving from.
#  * @param targetRow
#  *            The row to where the piece is moving to.
#  * @param targetCol
#  *            The column to where the piece is moving to.
#  * @return True if the piece can move. False if the piece can not move.
#  */
def canMove(game, sourceRow, sourceCol, targetRow, targetCol):

    # // A few things to figure out priorities in moving a piece.
    legalMove = False
                # // Is the proposed move/jump legal?
    realPositions = False
                    # // Are the positions really on the board?
    isJump = False
             # // Is this a jump?

    # // Sanity check.
    if (game.getGameBoard().isLegalPosition(sourceRow, sourceCol)
        and game.getGameBoard().isLegalPosition(targetRow, targetCol)):
        realPositions = True

    # // Is there a jump in progress?
    if (realPositions and game.getJumpInProgress() != None):

        # // Only allow the piece in movement to be moved.
        if (sourceRow == game.getJumpInProgress().getY()
                and sourceCol == game.getJumpInProgress().getX()):
            legalMove = canJump(game, sourceRow, sourceCol, targetRow,
                    targetCol)
            isJump = True

    elif (realPositions):

        # // Go with the regular flow, jumps first then "slides".
        isJump = canPlayerJump(game)
        if isJump:
            legalMove = canJump(game, sourceRow, sourceCol, targetRow,
                    targetCol)
        else:
            legalMove = canSlide(game, sourceRow, sourceCol, targetRow,
                    targetCol)

    return legalMove

def canPlayerJump(game):
    # // TODO: Implement me.
    # TODO Make as private method
    return False

def canSlide(game, sourceRow, sourceCol, targetRow, targetCol):

    # TODO Make private
    legalMove = True
    mustJump = canPlayerJump(game)

    # // Is the move even on the board?
    legalMove = game.getGameBoard().isLegalPosition(sourceRow, sourceCol)\
                and game.getGameBoard().isLegalPosition(targetRow, targetCol)

    # // See if the destination is even empty.
    if (legalMove):
        legalMove = game.getGameBoard().isEmpty(targetRow, targetCol)

    # // If yes, then look if right pieces were chosen.
    if (legalMove and not mustJump):
        if (game.isLightPlayerTurn() and game.getGameBoard().isLight(sourceRow, sourceCol)):

            # // To deal with flying kings.
            if (game.getGameBoard().isKing(sourceRow, sourceCol)
                    and game.getGameRules().canKingsFly()):

                # // FIXME: Fix this!
                pass
            else:
    # //					if ((Math.abs(targetRow - sourceRow) == 1) && (Math.abs(targetRow - sourceRow) == 1)) {
    # //						legalMove = false;

            # // Is the path clear for that move?
                pass

        elif (not game.isLightPlayerTurn() and game.getGameBoard().isDark(sourceRow, sourceCol)):

                # //TODO: Implement me, sometime.
            pass
        else:
            legalMove = False

    return legalMove;


def checkForVictory(game):
    # // TODO: Implement me.
    pass

# /**
#  * Gets if a piece is movable. Returns True if the piece can slide or jump.
#  * This method only calculates slides to the adjacent positions. Similarly,
#  * the method only looks at jumping an adjacent enemy piece. This check is
#  * used by the graphical user interface to determine if a piece can be moved
#  * either for sliding or jumping. The method is aware of whose turn is it to
#  * move.
#  *
#  * @param row
#  *            The row coordinate of the piece to check.
#  * @param col
#  *            The column coordinate of the piece to check.
#  * @return Returns True if the piece can slide or jump in this turn.
#  */
def isMovablePiece(game, row, col):

    # // Fields for determining of a piece is movable.
    moveUpLeft = True
    moveUpRight = True
    moveDownLeft = True
    moveDownRight = True

    # /*
    #  * Checks first if the first colour of piece is being grabbed. Next if
    #  * the piece is blocked by its own pieces. Next if the opponent has
    #  * double blocked off the pieces. Also sanity checks if looking past the
    #  * size of the board.
    #  */
    if (game.isLightPlayerTurn() and game.getGameBoard().isLight(row, col)):

        # // Light player.

        # // Can piece move normally?
        moveDownLeft = canSlide(game, row, col, row + 1, col - 1)
        moveDownRight = canSlide(game, row, col, row + 1, col + 1)

        if (game.getGameBoard().isKing(row, col)):
            moveUpLeft = canSlide(game, row, col, row - 1, col - 1)
            moveUpRight = canSlide(game, row, col, row - 1, col + 1)
        else:
            moveUpLeft = False
            moveUpRight = False

        # // If no slides available try doing the same except for jumps.
        if (not moveDownLeft):
            moveDownLeft = canJump(game, row, col, row + 2, col - 2)
        elif (not moveDownRight):
            moveDownRight = canJump(game, row, col, row + 2, col + 2)
        elif (game.getGameBoard().isKing(row, col)
                or game.getGameRules().canPawnsJumpBackwards()):

            if (not moveUpLeft):
                moveUpLeft = canJump(game, row, col, row - 2, col + 2)
            elif (not moveUpRight):
                moveUpRight = canJump(game, row, col, row - 2, col - 2)

        return moveUpLeft or moveUpRight or moveDownLeft or moveDownRight

    elif (game.isLightPlayerTurn() and game.getGameBoard().isDark(row, col)):
        # // Dark player

        # // Can piece move normally?
        moveUpLeft = canSlide(game, row, col, row - 1, col - 1)
        moveUpRight = canSlide(game, row, col, row - 1, col + 1)

        if (game.getGameBoard().isKing(row, col)):
            moveDownLeft = canSlide(game, row, col, row + 1, col - 1)
            moveDownRight = canSlide(game, row, col, row + 1, col + 1)
        else:
            moveDownLeft = False
            moveDownRight = False

        # // If no slides available try doing the same except for jumps.
        if (not moveUpLeft):
            moveUpLeft = canJump(game, row, col, row - 2, col - 2)
        elif (not moveUpRight):
            moveUpRight = canJump(game, row, col, row - 2, col + 2)
        elif (game.getGameBoard().isKing(row, col)
                or game.getGameRules().canPawnsJumpBackwards()):

            if (not moveDownLeft):
                moveDownLeft = canJump(game, row, col, row + 2, col + 2)
            elif (not moveDownRight):
                moveDownRight = canJump(game, row, col, row + 2, col - 2)

        return moveUpLeft or moveUpRight or moveDownLeft or moveDownRight

    else:
        return False
        # // A wrong coloured piece.

# /**
#  * Moves a pieces from one location to another. This move maybe either be a
#  * move or a jump. This method is called by a user interface when a user
#  * moves a piece on screen or over the network. The piece is moved if the
#  * current state of the game allows for it to do so.
#  *
#  * TODO: Add priority for king jumps over pawn jumps for any variants that
#  * do so. TODO: Implement jumping by piece removal.
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
def movePiece(game, sourceRow, sourceCol, targetRow, targetCol):

    # // If everything checks out... move the piecenot
    if (canMove(game, sourceRow, sourceCol, targetRow, targetCol)):
        if (game.getJumpInProgress() != None):

            # TODO: Implement jumping via removing of piece.
            game.getGameBoard().movePiece(sourceRow, sourceCol, targetRow,
                    targetCol)
        else:
            game.getGameBoard().movePiece(sourceRow, sourceCol, targetRow,
                    targetCol)

        checkForVictory(game)

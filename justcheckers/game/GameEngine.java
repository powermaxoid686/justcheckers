/*****************************************************************************
 	GameEngine.java -- Logic engine for manipulating the state of a game.
 *****************************************************************************

 *****************************************************************************
	This file is part of justCheckers.

    justCheckers is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    justCheckers is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with justCheckers.  If not, see <http://www.gnu.org/licenses/>.
 *****************************************************************************/

package org.justcheckers.game;

/**
 * @author dpula
 *
 */
public class GameEngine {

	// TODO: Add a constructor for games already in progress.
	
	// -- Game methods --------------------------------------------------------
	
	private static boolean canJump(Game game, int sourceRow, int sourceCol, int targetRow,
			int targetCol) {
	
		// TODO: Implement me.
		return false;
	}

	/**
	 * Returns if a piece can or cannot move. This move maybe either be a move
	 * or a jump. This method is called by a user interface when a user wants to
	 * moves a piece on screen or over the network. The piece can moved if the
	 * current state of the game allows for it to do so.
	 * 
	 * TODO: Add priority for king jumps over pawn jumps for any variants that
	 * do so.
	 * 
	 * @param sourceRow
	 *            The row from where the piece is moving from.
	 * @param sourceCol
	 *            The column from where the piece is moving from.
	 * @param targetRow
	 *            The row to where the piece is moving to.
	 * @param targetCol
	 *            The column to where the piece is moving to.
	 * @return True if the piece can move. False if the piece can not move.
	 */
	public static boolean canMove(Game game, int sourceRow, int sourceCol, int targetRow,
			int targetCol) {
	
		// A few things to figure out priorities in moving a piece.
		boolean legalMove = false; // Is the proposed move/jump legal?
		boolean realPositions = false; // Are the positions really on the board?
		boolean isJump = false; // Is this a jump?
	
		// Sanity check.
		if (game.getGameBoard().isLegalPosition(sourceRow, sourceCol)
				&& game.getGameBoard().isLegalPosition(targetRow, targetCol)) {
			realPositions = true;
	
		}
	
		// Is there a jump in progress?
		if (realPositions && game.getJumpInProgress() != null) {
	
			// Only allow the piece in movement to be moved.
			if (sourceRow == game.getJumpInProgress().getY()
					&& sourceCol == game.getJumpInProgress().getX()) {
				legalMove = canJump(game, sourceRow, sourceCol, targetRow,
						targetCol);
				isJump = true;
			}
	
		} else if (realPositions) {
	
			// Go with the regular flow, jumps first then "slides".
			isJump = canPlayerJump(game);
			if (isJump) {
				legalMove = canJump(game, sourceRow, sourceCol, targetRow,
						targetCol);
			} else {
				legalMove = canSlide(game, sourceRow, sourceCol, targetRow,
						targetCol);
			}
	
		}
	
		return legalMove;
	}

	private static boolean canPlayerJump(Game game) {
		// TODO: Implement me.
		return false;
	}

	private static boolean canSlide(Game game, int sourceRow, int sourceCol, int targetRow,
				int targetCol) {
	
			boolean legalMove = true;
			boolean mustJump = canPlayerJump(game);
			
			// Is the move even on the board?
			legalMove = game.getGameBoard().isLegalPosition(sourceRow, sourceCol)
					&& game.getGameBoard().isLegalPosition(targetRow, targetCol);
	
			// See if the destination is even empty.
			if (legalMove) {
				legalMove = game.getGameBoard().isEmpty(targetRow, targetCol);
			}
	
			// If yes, then look if right pieces were chosen.
			if (legalMove && !mustJump) {
				if (game.isLightPlayerTurn()
						&& game.getGameBoard().isLight(sourceRow, sourceCol)) {
	
					// To deal with flying kings.
					if (game.getGameBoard().isKing(sourceRow, sourceCol)
							&& game.getGameRules().canKingsFly()) {
						
						// FIXME: Fix this!
					} else {
	//					if ((Math.abs(targetRow - sourceRow) == 1) && (Math.abs(targetRow - sourceRow) == 1)) {
	//						legalMove = false;
	//					}
					}
	
					// Is the path clear for that move?
	
				} else if (!game.isLightPlayerTurn()
						&& game.getGameBoard().isDark(sourceRow, sourceCol)) {
	
						//TODO: Implement me, sometime.
				} else {
					legalMove = false;
				}
			}
	
			return legalMove;
		}

	private static void checkForVictory(Game game) {
		// TODO: Implement me.
	}

	/**
	 * Gets if a piece is movable. Returns true if the piece can slide or jump.
	 * This method only calculates slides to the adjacent positions. Similarly,
	 * the method only looks at jumping an adjacent enemy piece. This check is
	 * used by the graphical user interface to determine if a piece can be moved
	 * either for sliding or jumping. The method is aware of whose turn is it to
	 * move.
	 * 
	 * @param row
	 *            The row coordinate of the piece to check.
	 * @param col
	 *            The column coordinate of the piece to check.
	 * @return Returns true if the piece can slide or jump in this turn.
	 */
	public static boolean isMovablePiece(Game game, int row, int col) {
	
		// Fields for determining of a piece is movable.
		boolean moveUpLeft = true;
		boolean moveUpRight = true;
		boolean moveDownLeft = true;
		boolean moveDownRight = true;
	
		/*
		 * Checks first if the first colour of piece is being grabbed. Next if
		 * the piece is blocked by its own pieces. Next if the opponent has
		 * double blocked off the pieces. Also sanity checks if looking past the
		 * size of the board.
		 */
		if (game.isLightPlayerTurn() && game.getGameBoard().isLight(row, col)) { // Light
																		// player.
	
			// Can piece move normally?
			moveDownLeft = canSlide(game, row, col, row + 1, col - 1);
			moveDownRight = canSlide(game, row, col, row + 1, col + 1);
	
			if (game.getGameBoard().isKing(row, col)) {
				moveUpLeft = canSlide(game, row, col, row - 1, col - 1);
				moveUpRight = canSlide(game, row, col, row - 1, col + 1);
			} else {
				moveUpLeft = false;
				moveUpRight = false;
			}
	
			// If no slides available try doing the same except for jumps.
			if (!moveDownLeft) {
				moveDownLeft = canJump(game, row, col, row + 2, col - 2);
			} else if (!moveDownRight) {
				moveDownRight = canJump(game, row, col, row + 2, col + 2);
			} else if (game.getGameBoard().isKing(row, col)
					|| game.getGameRules().canPawnsJumpBackwards()) {
	
				if (!moveUpLeft) {
					moveUpLeft = canJump(game, row, col, row - 2, col + 2);
				} else if (!moveUpRight) {
					moveUpRight = canJump(game, row, col, row - 2, col - 2);
				}
	
			}
	
			return moveUpLeft || moveUpRight || moveDownLeft || moveDownRight;
	
		} else if (game.isLightPlayerTurn() && game.getGameBoard().isDark(row, col)) { // Dark
																				// player
	
			// Can piece move normally?
			moveUpLeft = canSlide(game, row, col, row - 1, col - 1);
			moveUpRight = canSlide(game, row, col, row - 1, col + 1);
	
			if (game.getGameBoard().isKing(row, col)) {
				moveDownLeft = canSlide(game, row, col, row + 1, col - 1);
				moveDownRight = canSlide(game, row, col, row + 1, col + 1);
			} else {
				moveDownLeft = false;
				moveDownRight = false;
			}
	
			// If no slides available try doing the same except for jumps.
			if (!moveUpLeft) {
				moveUpLeft = canJump(game, row, col, row - 2, col - 2);
			} else if (!moveUpRight) {
				moveUpRight = canJump(game, row, col, row - 2, col + 2);
			} else if (game.getGameBoard().isKing(row, col)
					|| game.getGameRules().canPawnsJumpBackwards()) {
	
				if (!moveDownLeft) {
					moveDownLeft = canJump(game, row, col, row + 2, col + 2);
				} else if (!moveDownRight) {
					moveDownRight = canJump(game, row, col, row + 2, col - 2);
				}
	
			}
	
			return moveUpLeft || moveUpRight || moveDownLeft || moveDownRight;
	
		} else {
			return false; // A wrong coloured piece.
		}
	
	}

	/**
	 * Moves a pieces from one location to another. This move maybe either be a
	 * move or a jump. This method is called by a user interface when a user
	 * moves a piece on screen or over the network. The piece is moved if the
	 * current state of the game allows for it to do so.
	 * 
	 * TODO: Add priority for king jumps over pawn jumps for any variants that
	 * do so. TODO: Implement jumping by piece removal.
	 * 
	 * @param sourceRow
	 *            The row from where the piece is moving from.
	 * @param sourceCol
	 *            The column from where the piece is moving from.
	 * @param targetRow
	 *            The row to where the piece is moving to.
	 * @param targetCol
	 *            The column to where the piece is moving to.
	 */
	public static void movePiece(Game game, int sourceRow, int sourceCol, int targetRow,
			int targetCol) {
	
		// If everything checks out... move the piece!
		if (canMove(game, sourceRow, sourceCol, targetRow, targetCol)) {
			if (game.getJumpInProgress() != null) {
	
				// TODO: Implement jumping via removing of piece.
				game.getGameBoard().movePiece(sourceRow, sourceCol, targetRow,
						targetCol);
			} else {
				game.getGameBoard().movePiece(sourceRow, sourceCol, targetRow,
						targetCol);
			}
	
			checkForVictory(game);
		}
	
	}

}

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

/**
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
 */
public class Board {

	/** Constant representing a dark king. */
	public static final int DARK_KING = 4;
	/** Constant representing a dark single man. */
	public static final int DARK_PAWN = 3;
	/** Constant representing an empty space. */
	public static final int EMPTY_SPACE = 0;
	// -- Constants ------------------------------------------------------------
	/**
	 * Constant representing an illegal square. That is a white square in
	 * checkers.
	 */
	public static final int ILLEGAL_SPACE = -1;
	/** Constant representing a light king. */
	public static final int LIGHT_KING = 2;
	/** Constant representing a light single man. */
	public static final int LIGHT_PAWN = 1;

	// -- Object Fields --------------------------------------------------------

	/** Is the board mirrored or a regular checker board. */
	private final boolean amIMirrored;
	/**
	 * Holds the positions of the pieces on the board.
	 */
	private final int[][] board;
	/** The size of the board. */
	private final int boardSize;
	/** A reference to the rules being used. */
	private final Rulebook myRules;

	// -- Constructors ---------------------------------------------------------
	/**
	 * Creates a new board for checkers.
	 * 
	 * @param rules
	 *            The rules for this board.
	 */
	public Board(Rulebook rules) {
		this.myRules = rules;
		final int size = this.myRules.getBoardSize();
		this.board = new int[size][size];
		this.boardSize = size;
		this.amIMirrored = this.myRules.isBoardMirrored();
	}

	// -- Public Methods (Setting Up the Board) --------------------------------
	/**
	 * Clears the board of pieces. Creates a brand new empty board already laid
	 * out by the rules (regular or mirrored).
	 */
	public void clearBoard() {
		for (int row = 0; this.boardSize > row; row++) {
			for (int col = 0; this.boardSize > col; col++) {

				// Mirrored has opposite setup to a regular board.
				if (row % 2 == 0 && col % 2 == 0) {
					if (this.amIMirrored) {
						this.board[row][col] = Board.ILLEGAL_SPACE;
					} else {
						this.board[row][col] = Board.EMPTY_SPACE;
					}
				} else if (row % 2 == 0 && col % 2 == 1) {
					if (this.amIMirrored) {
						this.board[row][col] = Board.EMPTY_SPACE;
					} else {
						this.board[row][col] = Board.ILLEGAL_SPACE;
					}
				} else if (row % 2 == 1 && col % 2 == 0) {
					if (this.amIMirrored) {
						this.board[row][col] = Board.EMPTY_SPACE;
					} else {
						this.board[row][col] = Board.ILLEGAL_SPACE;
					}
				} else {
					if (this.amIMirrored) {
						this.board[row][col] = Board.ILLEGAL_SPACE;
					} else {
						this.board[row][col] = Board.EMPTY_SPACE;
					}
				}

			}
		}
	}

	// -- Get/Set Methods ------------------------------------------------------
	/**
	 * Gets the size of the board. The board size is measured as the number of
	 * squares down one side of the board.
	 * 
	 * @return The size of the board.
	 */
	public int getBoardSize() {
		return this.boardSize;
	}

	/**
	 * Provides a reference to a 2 dimensional array representation of the
	 * current board state. This is for use by the user interface. Each
	 * dimension of the array extends from 0 to boardSize - 1. Note that the
	 * referenced array is a clone of the internal board representation. Changes
	 * made to the array will not affect the board state.
	 * 
	 * @return A 2 dimensional array representing the current state of the
	 *         board.
	 */
	public int[][] getBoardState() {
		final int[][] repBoard = new int[this.boardSize][this.boardSize];
		System.arraycopy(this.board, 0, repBoard, 0, this.boardSize);
		return repBoard;
	}

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
	public boolean isDark(int row, int col) {
		if (row >= 0 && row < this.boardSize && col >= 0
				&& col < this.boardSize) {
			return this.board[row][col] == Board.DARK_KING
					|| this.board[row][col] == Board.DARK_PAWN;
		}
		return false;
	}

	/**
	 * Determines whether the piece at board coordinate (row, col) is empty. If
	 * the coordinates do not exist on the board or is illegal, this method will
	 * return false.
	 * 
	 * @param row
	 *            The row of the square.
	 * @param col
	 *            The column of the square.
	 * @return True if the piece at the specified coordinate is empty. False if
	 *         otherwise.
	 */
	public boolean isEmpty(int row, int col) {
		if (row >= 0 && row < this.boardSize && col >= 0
				&& col < this.boardSize) {
			return this.board[row][col] == Board.EMPTY_SPACE;
		}
		return false;
	}

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
	public boolean isIllegalSpace(int row, int col) {
		if (row >= 0 && row < this.boardSize && col >= 0
				&& col < this.boardSize) {
			return this.board[row][col] == Board.ILLEGAL_SPACE;
		}
		return false;
	}

	/**
	 * Determines whether the piece at board coordinate (row, col) is a king. If
	 * the coordinates do not exist on the board or are empty, this method will
	 * return false.
	 * 
	 * @param row
	 *            The row of the square.
	 * @param col
	 *            The column of the square.
	 * @return True if the piece at the specified coordinate is a king. False if
	 *         otherwise.
	 */
	public boolean isKing(int row, int col) {
		if (row >= 0 && row < this.boardSize && col >= 0
				&& col < this.boardSize) {
			return this.board[row][col] == Board.LIGHT_KING
					|| this.board[row][col] == Board.DARK_KING;
		}
		return false;
	}

	/**
	 * Returns if a position specified is legal. Returns true if the position is
	 * on the board, and if the space is not an illegal white space. Returns
	 * false otherwise.
	 * 
	 * @param row
	 *            The row coordinate of the position.
	 * @param col
	 *            The column coordinate of the position.
	 * @return Returns true if the position is a legal playing position.
	 */
	public boolean isLegalPosition(int row, int col) {
		return row >= 0 && row < this.boardSize && col >= 0
				&& col < this.boardSize && !this.isIllegalSpace(row, col);
	}

	/**
	 * Determines whether the piece at board coordinate (row, col) is light. If
	 * the coordinates do not exist on the board or are empty, this method will
	 * return false.
	 * 
	 * @param row
	 *            The row of the square.
	 * @param col
	 *            The column of the square.
	 * @return True if the piece at the specified coordinate is light. False if
	 *         otherwise.
	 */
	public boolean isLight(int row, int col) {
		if (row >= 0 && row < this.boardSize && col >= 0
				&& col < this.boardSize) {
			return this.board[row][col] == Board.LIGHT_KING
					|| this.board[row][col] == Board.LIGHT_PAWN;
		}
		return false;
	}

	/**
	 * Determines whether the piece at board coordinate (row, col) is a pawn. If
	 * the coordinates do not exist on the board or are empty, this method will
	 * return false.
	 * 
	 * @param row
	 *            The row of the square.
	 * @param col
	 *            The column of the square.
	 * @return True if the piece at the specified coordinate is a pawn. False if
	 *         otherwise.
	 */
	public boolean isPawn(int row, int col) {
		if (row >= 0 && row < this.boardSize && col >= 0
				&& col < this.boardSize) {
			return this.board[row][col] == Board.LIGHT_PAWN
					|| this.board[row][col] == Board.DARK_PAWN;
		}
		return false;
	}

	// -- Board Updating Methods -----------------------------------------------
	/**
	 * Moves a pieces from one location to another. This method should be called
	 * from the Game using this Board. This method does not check for rule
	 * validity but does check for illegal white spaces. Also checks that the
	 * destination position is empty.
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
	protected void movePiece(int sourceRow, int sourceCol, int targetRow,
			int targetCol) {

		if (this.isLegalPosition(sourceRow, sourceCol)
				&& this.isLegalPosition(targetRow, targetCol)
				&& this.board[targetRow][targetCol] == Board.EMPTY_SPACE) {

			final int piece = this.board[sourceRow][sourceCol];
			this.board[targetRow][targetCol] = piece;
			this.board[sourceRow][sourceCol] = Board.EMPTY_SPACE;

		}
	}

	/**
	 * Removes a pieces from the specified location. This method should be
	 * called from the Game using this Board. This method does not check for
	 * rule validity but does check for illegal white spaces.
	 * 
	 * @param row
	 *            The row where the piece is to be removed from.
	 * @param col
	 *            The column where the piece is to be removed from.
	 */
	protected void removePiece(int row, int col) {

		if (this.isLegalPosition(row, col)) {
			this.board[row][col] = Board.EMPTY_SPACE;
		}
	}

	/**
	 * Setups the board for a new game. There are three different setups for the
	 * three different types of boards:
	 * 
	 * <table>
	 * <tr>
	 * <b>
	 * <td>Name</td>
	 * <td>Size</td>
	 * <td>Number of Pieces Per Player</td>
	 * <td>Number of Rows Per Player</td>
	 * </b>
	 * </tr>
	 * <tr>
	 * <td>Standard</td>
	 * <td>8 x 8</td>
	 * <td>12</td>
	 * <td>3</td>
	 * </tr>
	 * <tr>
	 * <td>International</td>
	 * <td>10 x 10</td>
	 * <td>20</td>
	 * <td>4</td>
	 * </tr>
	 * <tr>
	 * <td>Canadian</td>
	 * <td>12 x 12</td>
	 * <td>30</td>
	 * <td>5</td>
	 * </tr>
	 * </table>
	 * 
	 * The columns containing the players' tokens alternate between columns. The
	 * dark player traditionally takes the first few upper rows (0-3). The light
	 * player takes the last of the lower rows (5-7, 6-9 or 7-11).
	 * 
	 * Note that the suicide checkers variant has a completely different setup,
	 * and has a setup function of its own: setupNewSuicideGame().
	 */
	public void setupNewGame() {
		this.clearBoard();

		if (this.myRules.getCheckersVariant() == Rulebook.SUICIDE_CHECKERS) {
			this.setupNewSuicideGame();
		} else {

			// Used to decide which rows to fill up.
			int darkPlayerBottomRow;
			int lightPlayerTopRow;

			// Figure out the size of the board.
			if (this.boardSize == Rulebook.INTERNATIONAL_BOARD_SIZE) {
				darkPlayerBottomRow = 3;
				lightPlayerTopRow = 6;
			} else if (this.boardSize == Rulebook.CANADIAN_BOARD_SIZE) {
				darkPlayerBottomRow = 3;
				lightPlayerTopRow = 7;
			} else { // Default board is 8x8 Standard size.
				darkPlayerBottomRow = 2;
				lightPlayerTopRow = 5;
			}

			// Go through the board and set it up.
			for (int row = 0; row < this.boardSize; row++) {
				for (int col = 0; col < this.boardSize; col++) {
					if (row <= darkPlayerBottomRow
							&& this.board[row][col] == Board.EMPTY_SPACE) {
						this.board[row][col] = Board.DARK_PAWN;
					} else if (row >= lightPlayerTopRow
							&& this.board[row][col] == Board.EMPTY_SPACE) {
						this.board[row][col] = Board.LIGHT_PAWN;
					}
				}
			}

		}
	}

	/**
	 * Setups a checker board according to the suicide "French" rules.
	 */
	private void setupNewSuicideGame() {
		// TODO: Implement the suicide game setup.
	}

	// -- Private (Implementation) Methods -------------------------------------

	/**
	 * Returns a string to represent the board state. This string is formatted
	 * for use as a simple board display in the command window.
	 * 
	 * <b>Legend</b> ## - White space which the piece can not move on to. __ -
	 * An empty space. LP - A light pawn. LK - A light king. DP - A dark pawn.
	 * DK - A dark king.
	 * 
	 * @return A string representing the current board state.
	 */
	@Override
	public String toString() {
		// Prepare for output with a nice looking to banner.
		String output = "   ";
		for (int i = 0; i < this.boardSize; i++) {
			if (i < 9) {
				output = output + "  " + (i + 1);
			} else {
				output = output + " " + (i + 1);
			}
		}
		output = output + "\n\n";

		// Go row by row, printing out the row number and the board's state.
		for (int row = 0; row < this.boardSize; row++) {
			if (row < 9) {
				output = output + "  " + (row + 1);
			} else {
				output = output + " " + (row + 1);
			}

			// Get current row's state.
			for (int col = 0; col < this.boardSize; col++) {
				switch (this.board[row][col]) {
				case Board.ILLEGAL_SPACE:
					output = output + "## ";
					break;
				case Board.EMPTY_SPACE:
					output = output + "__ ";
					break;
				case Board.LIGHT_PAWN:
					output = output + "LP ";
					break;
				case Board.LIGHT_KING:
					output = output + "LK ";
					break;
				case Board.DARK_PAWN:
					output = output + "DP ";
					break;
				case Board.DARK_KING:
					output = output + "DK ";
					break;
				}
			}

			output = output + "\n";
		}

		return output;

	}
}

/*****************************************************************************
 	Rulebook.java -- A generic 'rulebook' for a checkers game.
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

package main.java.org.justcheckers.game;

/**
 * The rules for a game of checkers. This class provides a reference object for
 * a game of checkers. This helps deal with the number of variants of checkers.
 * One of the goals of justCheckers is to provide the flexibility of choose
 * between different kinds of checker variants. This class builds a skeleton of
 * the rules by defining what setup, moves, jumps, victory conditions and
 * special moves make up a particular variant of checkers.
 * 
 * @author Dorian Pula
 * @author Chris Bellini
 */
public class Rulebook {

	// -- Constants -----------------------------------------------------------

	// Checkers variants.
	/** Playing by the American rules. */
	public static final int AMERICAN_CHECKERS = 0;
	/** Playing by International (Polish) rules. */
	public static final int INTERNATIONAL_CHECKERS = 1;
	/** Playing by the Brazilian rules. */
	public static final int BRAZILIAN_CHECKERS = 2;
	/** Playing by the Canadian rules. */
	public static final int CANADIAN_CHECKERS = 3;
	/** Playing by Pool (Southern USA) rules. */
	public static final int POOL_CHECKERS = 4;
	/** Playing by the Spanish rules. */
	public static final int SPANISH_CHECKERS = 5;
	/** Playing by the Russian rules. */
	public static final int RUSSIAN_CHECKERS = 6;
	/** Playing by the Italian rules. */
	public static final int ITALIAN_CHECKERS = 7;
	/** Playing by Suicide rules. */
	public static final int SUICIDE_CHECKERS = 8;
	/** Playing by the Ghanaian rules. */
	public static final int GHANAIAN_CHECKERS = 9;
	
	// TODO: Implement special rules for these checkers. Version >0.1.1?
	// Victory conditions.
	/** Victory achieved by capturing all enemy pieces. */
	public static final int CAPTURE_ALL_ENEMIES_VICTORY = 0;
	/**
	 * Victory achieved by capturing all pieces. Only caveat is the three king
	 * versus one king draw rule:
	 * 
	 * In many games at the end one adversary has three kings while the other
	 * one has just one king. In such a case the first adversary must win in
	 * thirteen moves or the game is declared a draw. (Shamelessly stolen from
	 * http://en.wikipedia.org/wiki/Draughts).
	 */
	public static final int SPECIAL_POOL_VICTORY = 1;
	/** Victory achieved some bizarre manner. TODO: Figure out Russian checkers. */
	public static final int SPECIAL_RUSSIAN_VICTORY = 2;
	/** Victory achieved by losing all your pieces. */
	public static final int SPECIAL_SUICIDE_VICTORY = 3;
	/** Victory achieved by not being the first with one piece left. */
	public static final int SPECIAL_GHANAIAN_VICTORY = 4;

	// Checker board sizes.
	/** Using a "standard" American checkers board. */
	public static final int STANDARD_BOARD_SIZE = 8;
	/** Using an international sized checkers board. */
	public static final int INTERNATIONAL_BOARD_SIZE = 10;
	/** Using a Canadian sized checkers board. */
	public static final int CANADIAN_BOARD_SIZE = 12;

	/** The number of variants currently supported. */
	private static final int NUMBER_OF_VARIANTS_SUPPORTED = 2;
	
	/** The size of the board. */
	private int boardSize;
	/** Can kings fly across the board? */
	private boolean canKingsFly;
	/** Can pawns capture backwards? */
	private boolean canPawnsJumpBackwards;
	
	// -- Object Fields --------------------------------------------------------
	/** Stores what kind of checkers variant of rule are we playing? */
	private int checkersVariant;
	/** Does the light player start first? */
	private boolean lightPlayerFirst;
	/** Is the board mirrored? As in white square lower right corner. */
	private boolean mirroredBoard;
	/** Must capture if have opportunity. */
	private boolean mustCapture;
	/** Must player capture the highest number of pieces. */
	private boolean mustCaptureMaxium;
	/** The type of victory conditions. */
	private int victoryConditions;

	// -- Constructors ---------------------------------------------------------
	/**
	 * Creates a rulebook for a checkers game. We use the American variant rules
	 * by default.
	 */
	public Rulebook() {
		this(Rulebook.AMERICAN_CHECKERS);
	}

	/**
	 * Creates a rulebook for a checkers game. If a bad/unsupported variant is
	 * created, the default of American checkers is chosen.
	 * 
	 * @param variant
	 *            The variant of checkers we will play.
	 */
	public Rulebook(int variant) {
		if (variant >= 0 && variant < Rulebook.NUMBER_OF_VARIANTS_SUPPORTED) {
			this.checkersVariant = variant;
		} else {
			this.checkersVariant = Rulebook.AMERICAN_CHECKERS;
		}
		this.setUpRules();
	}

	/**
	 * Returns if kings can fly. That is can kings move as far they wish.
	 * 
	 * @return If kings can fly.
	 */
	public boolean canKingsFly() {
		return this.canKingsFly;
	}

	/**
	 * Returns if pawns can capture backwards.
	 * 
	 * @return If pawns can capture backwards.
	 */
	public boolean canPawnsJumpBackwards() {
		return this.canPawnsJumpBackwards;
	}

	/**
	 * Returns the size of the board.
	 * 
	 * @return The size of the board.
	 */
	public int getBoardSize() {
		return this.boardSize;
	}

	// -- Get/set methods ------------------------------------------------------
	/**
	 * Returns the checkers variant being played.
	 * 
	 * @return The checkers variant being played.
	 */
	public int getCheckersVariant() {
		return this.checkersVariant;
	}

	/**
	 * Returns the victory conditions of this game.
	 * 
	 * @return The victory conditions of this game.
	 */
	public int getVictoryConditions() {
		return this.victoryConditions;
	}

	/**
	 * Returns is the board mirrored in this game.
	 * 
	 * @return Is the board mirrored in this game.
	 */
	public boolean isBoardMirrored() {
		return this.mirroredBoard;
	}

	/**
	 * Returns if the light player starts the game.
	 * 
	 * @return If the light player starts the game.
	 */
	public boolean isLightPlayerFirst() {
		return this.lightPlayerFirst;
	}

	/**
	 * Returns if you must capture a piece if you can.
	 * 
	 * @return If you must capture a piece if you can.
	 */
	public boolean mustCapture() {
		return this.mustCapture;
	}

	/**
	 * Returns if you must capture the maximum number of pieces possible.
	 * 
	 * @return If you must capture the maximum number of pieces possible.
	 */
	public boolean mustCaptureMaxium() {
		return this.mustCaptureMaxium;
	}

	// -- Private implementation methods.
	/**
	 * Setups the rules according to what variant of checkers was chosen.
	 */
	private void setUpRules() {
		// Save my sanity.
		assert this.checkersVariant >= 0;
		assert this.checkersVariant < Rulebook.NUMBER_OF_VARIANTS_SUPPORTED;

		// Set up the rules by the type of variant.
		switch (this.checkersVariant) {
		case Rulebook.AMERICAN_CHECKERS:
			this.boardSize = Rulebook.STANDARD_BOARD_SIZE;
			this.canKingsFly = false;
			this.canPawnsJumpBackwards = false;
			this.lightPlayerFirst = false;
			this.mirroredBoard = false;
			this.mustCapture = true;
			this.mustCaptureMaxium = false;
			this.victoryConditions = Rulebook.CAPTURE_ALL_ENEMIES_VICTORY;
			break;

		case Rulebook.INTERNATIONAL_CHECKERS:
			this.boardSize = Rulebook.INTERNATIONAL_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = true;
			this.lightPlayerFirst = true;
			this.mirroredBoard = false;
			this.mustCapture = true;
			this.mustCaptureMaxium = true;
			this.victoryConditions = Rulebook.CAPTURE_ALL_ENEMIES_VICTORY;
			break;

		case Rulebook.BRAZILIAN_CHECKERS:
			this.boardSize = Rulebook.STANDARD_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = true;
			this.lightPlayerFirst = true;
			this.mirroredBoard = false;
			this.mustCapture = true;
			this.mustCaptureMaxium = true;
			this.victoryConditions = Rulebook.CAPTURE_ALL_ENEMIES_VICTORY;
			break;

		case Rulebook.CANADIAN_CHECKERS:
			this.boardSize = Rulebook.CANADIAN_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = true;
			this.lightPlayerFirst = true;
			this.mirroredBoard = false;
			this.mustCapture = true;
			this.mustCaptureMaxium = false;
			this.victoryConditions = Rulebook.CAPTURE_ALL_ENEMIES_VICTORY;
			break;

		case Rulebook.POOL_CHECKERS:
			this.boardSize = Rulebook.STANDARD_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = true;
			this.lightPlayerFirst = false;
			this.mirroredBoard = false;
			this.mustCapture = true;
			this.mustCaptureMaxium = false;
			this.victoryConditions = Rulebook.SPECIAL_POOL_VICTORY;
			break;

		case Rulebook.SPANISH_CHECKERS:
			this.boardSize = Rulebook.STANDARD_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = false;
			this.lightPlayerFirst = true;
			this.mirroredBoard = true;
			this.mustCapture = true;
			this.mustCaptureMaxium = true;
			this.victoryConditions = Rulebook.CAPTURE_ALL_ENEMIES_VICTORY;
			break;

		case Rulebook.RUSSIAN_CHECKERS:
			// TODO: Needs special freshly-kinged-but-still-can-jump special
			// rule.
			this.boardSize = Rulebook.STANDARD_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = true;
			this.lightPlayerFirst = true;
			this.mirroredBoard = false;
			this.mustCapture = true;
			this.mustCaptureMaxium = false;
			this.victoryConditions = Rulebook.SPECIAL_RUSSIAN_VICTORY;
			break;

		case Rulebook.ITALIAN_CHECKERS:
			// TODO: Special rule on must jump most number of kings per capture.
			this.boardSize = Rulebook.STANDARD_BOARD_SIZE;
			this.canKingsFly = true;
			// TODO: Special rule that pawns can't capture kings.
			this.canPawnsJumpBackwards = false;
			this.lightPlayerFirst = true;
			this.mirroredBoard = true;
			this.mustCapture = true;
			this.mustCaptureMaxium = true;
			this.victoryConditions = Rulebook.CAPTURE_ALL_ENEMIES_VICTORY;
			break;

		case Rulebook.SUICIDE_CHECKERS:
			// TODO: Needs unconventional setup.
			this.boardSize = Rulebook.STANDARD_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = true;
			this.lightPlayerFirst = true;
			this.mirroredBoard = false;
			this.mustCapture = true;
			this.mustCaptureMaxium = true;
			this.victoryConditions = Rulebook.SPECIAL_SUICIDE_VICTORY;
			break;

		case Rulebook.GHANAIAN_CHECKERS:
			// TODO: Special forfeit king if passing up a king's capture
			// opportunity.
			this.boardSize = Rulebook.INTERNATIONAL_BOARD_SIZE;
			this.canKingsFly = true;
			this.canPawnsJumpBackwards = true;
			this.lightPlayerFirst = true;
			this.mirroredBoard = true;
			this.mustCapture = true;
			this.mustCaptureMaxium = false;
			this.victoryConditions = Rulebook.SPECIAL_GHANAIAN_VICTORY;
			break;
		}

	}

}

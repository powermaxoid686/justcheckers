/*****************************************************************************
 	Board.java -- Container for the state of a game in progress.
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

import android.graphics.Point;

/**
 * The main game handling object of GameLoop.
 * 
 * Objects registering as observers on an instance of GameEngine will be
 * notified of a change in either the board state or the turn state. The turn
 * will change automatically when a complete move is made. Multiple jumps are
 * managed by a call to the makeMove method for each jump segment, and the turn
 * will not pass to the other player until the jump sequence is complete.
 * 
 * @author Ross Etchells
 * @author Dorian Pula
 */
public class Game {

	// -- Constants -----------------------------------------------------------
	/** State of the game when the dark player wins. */
	public static final int STATE_DARK_VICTORY = 2;
	/** State of the game when both players draw. */
	public static final int STATE_GAME_DRAWN = 3;
	/** State of the game when game is in progress. */
	public static final int STATE_GAME_IN_PROGRESS = 0;
	/** State of the game when the light player wins. */
	public static final int STATE_LIGHT_VICTORY = 1;

	// -- Object Fields -------------------------------------------------------
	/** Represents the dark (usually defending) player. */
	private Player darkPlayer;
	/** Contains the current checker board used for the game. */
	private Board gameBoard;
	/** Contains the current rules used for playing the game. */
	private Rulebook gameRules;
	/** The state of the game. */
	private int gameState;
	/**
	 * This point holds the coordinates of a piece making a jump. Mostly used
	 * for a piece whose move has not finished after 1 jump. This point is set
	 * to null if not in use.
	 */
	private final Point jumpInProgress;
	/** Represents the light (usually attacking) player. */
	private Player lightPlayer;
	/** Represents whose turn it is. */
	private boolean lightPlayerTurn;

	/*
	 * TODO: Game needs to declare who won or better yet, the state of the game
	 * to be: in progress, light win, dark win or draw.
	 */

	// -- Constructors --------------------------------------------------------
	/**
	 * Create a new game. Uses the defaults of two unnamed players and the
	 * American rules.
	 */
	public Game() {
		this(Rulebook.AMERICAN_CHECKERS, new Player(), new Player());
	}

	/**
	 * Create a new game. Uses the default of two unnamed players. The variant
	 * (which rules) can be set here.
	 * 
	 * @param variant
	 *            Which variant of checkers will this game be.
	 */
	public Game(int variant) {
		this(variant, new Player(), new Player());
	}

	/**
	 * Creates a new game.
	 * 
	 * @param variant
	 *            The variant of checkers to be played.
	 * @param light
	 *            The player playing the light side.
	 * @param dark
	 *            The player playing the dark side.
	 */
	public Game(int variant, Player light, Player dark) {
		// Setup all the components of the game.
		this.gameRules = new Rulebook(variant);
		this.gameBoard = new Board(this.gameRules);
		this.darkPlayer = dark;
		this.lightPlayer = light;

		// Setup the board and start the game.
		this.lightPlayerTurn = this.gameRules.isLightPlayerFirst();
		this.gameBoard.setupNewGame();
		this.jumpInProgress = null; // No moves in progress yet.
		this.gameState = Game.STATE_GAME_IN_PROGRESS;
	}

	// TODO: Add a constructor for games already in progress.

	// -- Game methods --------------------------------------------------------

	/**
	 * Gets the player playing the dark side.
	 * 
	 * @return The player playing the dark side.
	 */
	public Player getDarkPlayer() {
		return this.darkPlayer;
	}

	// -- Get/Set Methods ------------------------------------------------------
	/**
	 * Gets the board used for this game.
	 * 
	 * @return The board used for this game.
	 */
	public Board getGameBoard() {
		return this.gameBoard;
	}

	/**
	 * Gets the rules used for this game.
	 * 
	 * @return The rules used for this game.
	 */
	public Rulebook getGameRules() {
		return this.gameRules;
	}

	/**
	 * Gets the state of the game. The state is defined by the STATE_*
	 * constants.
	 * 
	 * @return The state of the game.
	 */
	public int getGameState() {
		return this.gameState;
	}

	/**
	 * Gets the player playing the light side.
	 * 
	 * @return The player playing the light side.
	 */
	public Player getLightPlayer() {
		return this.lightPlayer;
	}

	/**
	 * Gets if it is the light player's turn. Returns false if it is the dark
	 * player's turn.
	 * 
	 * @return If it is the light player's turn. Returns false if it is the dark
	 *         player's turn.
	 */
	public boolean isLightPlayerTurn() {
		return this.lightPlayerTurn;
	}

	/**
	 * Set the player playing the dark side.
	 * 
	 * @param player
	 *            The player playing the dark side.
	 */
	public void setDarkPlayer(Player player) {
		this.darkPlayer = player;
	}

	/**
	 * Sets the board used for this game.
	 * 
	 * @param board
	 *            The board for this game.
	 */
	public void setGameBoard(Board board) {
		this.gameBoard = board;
	}

	// -- Private Methods ------------------------------------------------------

	/**
	 * Sets the rules used for this game.
	 * 
	 * @param rules
	 *            The rules used for this game.
	 */
	public void setGameRules(Rulebook rules) {
		this.gameRules = rules;
	}

	/**
	 * Sets the state of the game. The state is defined by the STATE_*
	 * constants.
	 * 
	 * @param state
	 *            The state of the game.
	 */
	public void setGameState(int state) {
		this.gameState = state;
	}

	/**
	 * Sets the player playing the light side.
	 * 
	 * @param player
	 *            The player playing the light side.
	 */
	public void setLightPlayer(Player player) {
		this.lightPlayer = player;
	}

	/**
	 * Sets if it is the light player's turn. Set it to false if its the dark
	 * player's turn.
	 * 
	 * @param playerTurn
	 *            If it is the light player's turn.
	 */
	public void setLightPlayerTurn(boolean playerTurn) {
		this.lightPlayerTurn = playerTurn;
	}

	/**
	 * @return the jumpInProgress
	 */
	public Point getJumpInProgress() {
		return jumpInProgress;
	}
}

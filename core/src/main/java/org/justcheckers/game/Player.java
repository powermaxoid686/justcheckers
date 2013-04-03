/*****************************************************************************
 	Player.java -- Data objects for maintaining player information.
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
 * Manages the information of a single player.
 * 
 * @author Chris Bellini
 * @author Dorian Pula
 */
public class Player {

	/** The player's total number of losses. */
	private int gamesLost;
	/** The total number of games played by the player. */
	private int gamesPlayed;
	/** The player's total number of ties. */
	private int gamesTied;
	/** The player's total number of wins. */
	private int gamesWon;
	/** The player's name. */
	private final String playerName;

	/** Creates an unnamed player with a blank record. */
	public Player() {
		this("Unnamed Player", 0, 0, 0, 0);
	}

	/**
	 * Creates a player with a given name and a blank record.
	 * 
	 * @param name
	 *            The name of the player.
	 */
	public Player(String name) {
		this(name, 0, 0, 0, 0);
	}

	/**
	 * Creates a player with a given name and record.
	 * 
	 * @param name
	 *            The name of the player to be created.
	 * @param wins
	 *            Player's total wins.
	 * @param losses
	 *            Player's total losses.
	 * @param ties
	 *            Player's total ties.
	 * @param played
	 *            Total games played by the player.
	 */
	public Player(String name, int wins, int losses, int ties, int played) {
		this.playerName = name;
		this.gamesWon = wins;
		this.gamesLost = losses;
		this.gamesTied = ties;
		this.gamesPlayed = played;
	}

	/** Adds a new loss for the player's total losses. */
	public void addLoss() {
		this.gamesLost++;
		this.gamesPlayed++;
	}

	/** Adds a new tie for the player's total ties. */
	public void addTie() {
		this.gamesTied++;
		this.gamesPlayed++;
	}

	/** Adds a new win for the player's total wins. */
	public void addWin() {
		this.gamesWon++;
		this.gamesPlayed++;
	}

	/**
	 * Gets the player's total losses.
	 * 
	 * @return The player's total losses.
	 */
	public int getLosses() {
		return this.gamesLost;
	}

	/**
	 * Gets the total number of games played by the player.
	 * 
	 * @return The total number of games played by the player.
	 */
	public int getPlayedGames() {
		return this.gamesPlayed;
	}

	/**
	 * Gets the player's total score.
	 * 
	 * @return The player's total score.
	 */
	public int getTies() {
		return this.gamesTied;
	}

	/**
	 * Gets the player's total wins.
	 * 
	 * @return The player's total wins.
	 */
	public int getWins() {
		return this.gamesWon;
	}

	/**
	 * Prints all the data about the player.
	 * 
	 * @return A string representing the player's data.
	 */
	@Override
	public String toString() {
		return "Name: " + this.playerName + "\n" + "Games: Won "
				+ this.gamesWon + " Lost " + this.gamesLost + " Tied "
				+ this.gamesTied;
	}
}
/*****************************************************************************
 	GameStateTest.java -- Unit tests related to managing a game's state.
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

package main.java.org.justcheckers.test.game;

import main.java.org.justcheckers.game.Game;
import main.java.org.justcheckers.game.Rulebook;

/**
 * Test the game state logic.  Tests the NQPOJO (not quite plain old Java 
 * objects) that handle the state of a game.  This includes the Rulebook 
 * (that dictate what rules will be used for a game), the Board (that represents
 * the state of the board, pieces, etc.) and the Game itself.
 * 
 * TestNG version: 5.10
 * 
 * @author dorianpula
 */
public class GameStateTest {
	
	/** A test game of checkers. */
	private Game testGame;
	
	/** 
	 * Sets up a rather plain game of checkers.  Game is based on the American
	 * rules, to make life easier.
	 */
	//@BeforeClass
	public void setUp() {
		this.testGame = new Game();
	}
	
	/** 
	 * Test the rulebook of a default initialized game.
	 */
	//@Test
	public void testDefaultRulebookSetup() {
		Rulebook testRules = this.testGame.getGameRules();
		
		junit.framework.Assert.assertNull(testRules);
		
		//TODO: Test the ruleset that is gets initialized properly.
	}
	
	//TODO: Populate with test cases.
}

/*****************************************************************************
	GameActivity.java - The activity that handles the actual checkers games.
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

package main.java.org.justcheckers.android;

import main.java.org.justcheckers.game.Game;
import main.java.org.justcheckers.game.Rulebook;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;

public class GameActivity extends Activity implements OnClickListener {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		super.onCreate(savedInstanceState);
		
		// Setup the user interface for the main menu.
		
		// Weirdness in orientation values in Galaxy Tab.
		// http://www.ceveni.com/2009/08/how-to-get-screen-orientation-in.html
		int screenOrientation = 
			this.getWindowManager().getDefaultDisplay().getOrientation();
		
		//TODO: Cleaner per device implementation. Developed on Samsung Galaxy S Vibrant.
		if (screenOrientation == 1) {
			// Counter-clockwise landscape 
			this.setContentView(R.layout.game_screen_landscape);
		} else if (screenOrientation == 3) {
			// Clockwise landscape 
			this.setContentView(R.layout.game_screen_landscape);
		} else if (screenOrientation == 0) {
			// Portrait for Samsung Galaxy devices.
			this.setContentView(R.layout.game_screen_portrait);
		}

	}

	public void onClick(View view) {
		//TODO: Stub
	}
	
	/**
	 * Starts a new game with the specified rulebook.
	 * 
	 * @param rules
	 *            The rules for the new game.
	 */
	public static void startGame(Rulebook rules) {
		Game currentGame = new Game(rules.getCheckersVariant());
		/* Instead of specialized UI commands, just a single method
			that updates the UI with the current state of the game. */
//		ui.setCurrentGame(currentGame);
//
//		// Current until different game types are added.
//		ui.clearBoard();
//		ui.placePieces();
	}
	
}

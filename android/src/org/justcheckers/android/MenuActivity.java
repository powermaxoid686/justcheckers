/*****************************************************************************
   	MenuActivity.java - The activity that provides the main menu for the app.
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

package org.justcheckers.android;

import org.justcheckers.common.GlobalConstants;
import org.justcheckers.common.LoggingAndStatistics;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class MenuActivity extends Activity implements OnClickListener {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		super.onCreate(savedInstanceState);
		
		// Setup the user interface for the main menu.
		this.setContentView(R.layout.main_menu);
		
		// Link up all the UI elements with their listeners.
		Button menuButton = (Button) this.findViewById(R.id.game_button);
		menuButton.setOnClickListener(this);
		menuButton = (Button) this.findViewById(R.id.game_button);
		menuButton.setOnClickListener(this);
		menuButton = (Button) this.findViewById(R.id.website_button);
		menuButton.setOnClickListener(this);
		menuButton = (Button) this.findViewById(R.id.settings_button);
		menuButton.setOnClickListener(this);
		menuButton = (Button) this.findViewById(R.id.about_us_button);
		menuButton.setOnClickListener(this);
		menuButton = (Button) this.findViewById(R.id.license_button);
		menuButton.setOnClickListener(this);
		menuButton = (Button) this.findViewById(R.id.quit_button);
		menuButton.setOnClickListener(this);
		
		// TODO: Move logging info in a better place.
//		LoggingAndStatistics.logApplicationInfo(this);
		LoggingAndStatistics.logDeviceAndSystemInfo();
	}

	public void onClick(View view) {
		// Determine which view fired off this event.
		switch (view.getId()) {
		case R.id.game_button:
			this.startGame();
			break;
		case R.id.website_button:
			this.launchWebsite();
			break;
		case R.id.settings_button:
			this.displaySettings();
			break;
		case R.id.about_us_button:
			this.displayInfo(GlobalConstants.FLAG_INFORMATION_DISPLAY_ABOUT_US);
			break;
		case R.id.license_button:
			this.displayInfo(GlobalConstants.FLAG_INFORMATION_DISPLAY_LICENSE);
			break;
		case R.id.quit_button:
			this.quitApp();
			break;
		};
	}

	/**
	 * Quits the application.
	 */
	private void quitApp() {
		this.finish();
	}

	/**
	 * Displays an information screen.
	 */
	private void displayInfo(int infoToDisplay) {
		
		// Validate info.
		if ((infoToDisplay != GlobalConstants.FLAG_INFORMATION_DISPLAY_ABOUT_US) &&
				(infoToDisplay != GlobalConstants.FLAG_INFORMATION_DISPLAY_LICENSE)) {
			infoToDisplay = GlobalConstants.FLAG_INFORMATION_DISPLAY_ABOUT_US;
		}
		
		
		Intent launchDisplay = new Intent(this, InfoActivity.class);
		launchDisplay.putExtra(GlobalConstants.EXTRA_INFORMATION_DISPLAY_FLAG, 
				infoToDisplay);
		startActivity(launchDisplay);
	}

	/**
	 * Displays the settings for the application.
	 */
	private void displaySettings() {
		Intent launchDisplay = new Intent(this, SettingsActivity.class);
		startActivity(launchDisplay);
	}
	
	/**
	 * Starts an external browser to visit the project's website.
	 */
	private void launchWebsite() {
		String url = this.getString(R.string.project_website);
		Intent launcher = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
		startActivity(launcher);
	}

	/**
	 * Starts a new game or continues an existing one.
	 */
	private void startGame() {
		Intent launchDisplay = new Intent(this, GameActivity.class);
		startActivity(launchDisplay);
	}
	
}

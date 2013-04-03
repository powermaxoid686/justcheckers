/*****************************************************************************
 	GameLoop.java - Main controlling class for the justCheckers game.
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

package main.java.org.justcheckers.common;import org.justcheckers.android.R;

import android.app.Activity;
import android.os.Build;
import android.util.Log;

/**
 * Functions for logging errors and gathering statistics.
 * 
 * @author Dorian Pula
 */
public class LoggingAndStatistics {

	/**
	 * Logs information about the program. Displays the game's header and
	 * relevant system properties at runtime.
	 */
	public static void logApplicationInfo(Activity caller) {
	
		String gameVersion = caller.getString(R.string.app_version);
		String gameWebsite = caller.getString(R.string.project_website);
		String appInfo = "justCheckers -- Version:" + gameVersion
				+ " - Website: " + gameWebsite;
		
		Log.i("ApplInfo", appInfo);
	}
	
	/**
	 * Logs information about the device and system, the app is
	 * running on.
	 */
	public static void logDeviceAndSystemInfo() {
		
		// System properties.
		String sysList = "SDK version: " + Build.VERSION.RELEASE 
			+ " - API: " + Build.VERSION.SDK_INT 
			+ " - Device: " + Build.MANUFACTURER + " " + Build.MODEL;

		Log.i("DevSysInfo", sysList);
	}

}
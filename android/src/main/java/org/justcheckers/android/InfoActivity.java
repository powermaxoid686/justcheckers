/*****************************************************************************
	   InfoActivity.java - The activity that provides built-in information.
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

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import main.java.org.justcheckers.common.GlobalConstants;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

public class InfoActivity extends Activity {

	private int flagInformationToDisplay;
	
	//TODO: Clean this up into something more modularized.
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		super.onCreate(savedInstanceState);
		
		// Setup the user interface for the main menu.
		this.setContentView(R.layout.info_screen);
		
		// Figure out which text to load.  The default 
		if (savedInstanceState != null) {
			this.flagInformationToDisplay = 
				savedInstanceState.getInt(GlobalConstants.EXTRA_INFORMATION_DISPLAY_FLAG);

		} else {
			Bundle extras = this.getIntent().getExtras();
			if (extras != null) {
				this.flagInformationToDisplay = 
					extras.getInt(GlobalConstants.EXTRA_INFORMATION_DISPLAY_FLAG);
			}
		}
		
		// Load the right text.
		int rawInfoRes = 0;
		if (this.flagInformationToDisplay == GlobalConstants.FLAG_INFORMATION_DISPLAY_ABOUT_US) {
			rawInfoRes = R.raw.readme;
		} else if (this.flagInformationToDisplay == GlobalConstants.FLAG_INFORMATION_DISPLAY_LICENSE) {
			rawInfoRes = R.raw.gpl_3_license;
		} else {
			rawInfoRes = R.raw.readme;
		}
		
		// Read the raw document into a string.
		InputStream docInfoStream = this.getResources().openRawResource(rawInfoRes);
		BufferedReader reader = new BufferedReader(new InputStreamReader(docInfoStream));
		String result = "Text here";
		
		try {
			// Gather all the data.
			StringBuilder buildDoc = new StringBuilder();
			String docLine = reader.readLine();
			
			while (docLine != null) {
				buildDoc.append(docLine + "\n");
				docLine = reader.readLine();
			}
			
			result = buildDoc.toString();
			
		} catch (IOException e) {
			Log.e("InfoActivity", "Input error: " + e.getMessage());
		}
		
		TextView infoText = (TextView) this.findViewById(R.id.info_text);
		infoText.setText(result);
	}

	@Override
	protected void onSaveInstanceState(Bundle outState) {
		super.onSaveInstanceState(outState);
		outState.putInt(GlobalConstants.EXTRA_INFORMATION_DISPLAY_FLAG, 
				this.flagInformationToDisplay);
	}
	
}

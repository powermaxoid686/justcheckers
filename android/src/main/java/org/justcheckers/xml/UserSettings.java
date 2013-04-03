package main.java.org.justcheckers.xml;

import java.util.HashMap;

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

/**
* Stores the user preferences in the application memory.
* Implements the singleton pattern.
*
* @author Brinick Simmons (brinick@users.sourceforge.net)
*/
final public class UserSettings extends Settings{

	//---------------------------//
	//      Class Fields         //
	//---------------------------//
		
	private static UserSettings us = null;
	private HashMap text = null, attribute = null;
	
	//---------------------------//
	//      Class Methods        //
	//---------------------------//

   // -- Interface ---------------------------------------------------------
	
	/**
	* Accessor method for obtaining the one and only instance of this class
	*/
	public static UserSettings getInstance(){
		if(us==null) loadDefault();
		return us;
	}	
	
	/** 
	* Load the default user settings.
	*/
	public static void loadDefault(){
		us = new UserSettings(new DefaultUserSettings());
		//somehow would have to log that properties have changed
		//so that things can be updated e.g. the UI, or whatever
	}
	
	// -- Private Constructors -----------------------------------------------
	
	private UserSettings(){
		super();
	}
	
	private UserSettings(DefaultUserSettings dus){
		super(dus.getTextMap(), dus.getAttributeMap());
	}
 
 	//////////////////////////////////////
	//   INNER CLASS : DefaultSettings  //
	//////////////////////////////////////
 
 	private static class DefaultUserSettings extends Settings.DefaultSettings{
		private String [][] text = 
		{
			{"usersettings.general.splashOnLaunch","true"},
			{"usersettings.general.maxActiveGames","3"},			
			{"usersettings.audio.activateBkgdOnLaunch","false"},			
			{"usersettings.audio.defaultBkgdSong","song1.wav"},	
			{"usersettings.audio.appSoundsActive","true"},					
			{"usersettings.language.current","english"},
			{"usersettings.appearance.fullScreenOnLaunch","true"},									
			{"usersettings.appearance.activePieceSet","pieceset1"},			
		};
	
		private String [][] attribute = 
		{
			{"usersettings.general.id","3"},
			{"usersettings.general.id2","5"},			
			{"usersettings.language.default","english"},			
			{"usersettings.appearance.pretty","true"},												
		};

		DefaultUserSettings(){
			super();
			super.setFields(text,attribute);
		}
	}
}
package org.justcheckers.xml;

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

/**
* Holds the justCheckers configuration settings.
* @author Brinick Simmons (brinick@users.sourceforge.net)
*/

final public class ConfigSettings extends Settings{

	//---------------------------//
	//      Class Fields         //
	//---------------------------//
		
	private static ConfigSettings cs = null;	
	
	//---------------------------//
	//      Class Methods        //
	//---------------------------//

	//======= PUBLIC ============//
	
	/**
	* Accessor method for obtaining the one 
	* and only instance of this class
	*/
	public static ConfigSettings getInstance(){
		if(cs==null) cs = new ConfigSettings(new DefaultConfigSettings());
		return cs;
	}	
	
	/** 
	* Load the default config settings.
	*/
	public static void loadDefault(){
		cs = new ConfigSettings(new DefaultConfigSettings());
	}

	//======= PRIVATE CONSTRUCTORS ========//
	private ConfigSettings(){
		super();
	}
	
	private ConfigSettings(DefaultConfigSettings cus){
		super(cus.getTextMap(),cus.getAttributeMap());
	}
	
	//======= PRIVATE INNER CLASS ============//
	
	/* The default class from which to get settings */	
	private static class DefaultConfigSettings extends Settings.DefaultSettings{
		private String userHome = System.getProperty("user.home");
		private String userDir  = System.getProperty("user.dir");
		private String [][] text = 
		{
			{"configsettings.directory.configFile",userDir+"/config.xml"},
			{"configsettings.directory.settings",userHome+"/settings/"},			
			{"configsettings.directory.skins",userDir+"/skins/"},			
			{"configsettings.directory.sounds",userDir+"/sounds/"},	
			{"configsettings.directory.language",userDir+"/language/"},					
		};
	
		private String [][] attribute = 
		{
			{"configsettings.general.id","3"},
			{"configsettings.general.id2","5"},			
			{"configsettings.language.default","english"},			
			{"configsettings.appearance.pretty","true"},												
		};

		DefaultConfigSettings(){
			super();
			super.setFields(text,attribute);
		}
	}//end of default class
}
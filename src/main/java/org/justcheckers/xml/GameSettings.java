package org.justcheckers.xml;

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
* Holds the current game settings (Players, moves, etc).
* Currently, only one game may be open at a time.
* Future versions may allow more than one game to be open at
* a given moment.
*
* @author Brinick Simmons (brinick@users.sourceforge.net)
*/
final public class GameSettings extends Settings{

	//---------------------------//
	//      Class Fields         //
	//---------------------------//
	
	private HashMap text = new HashMap(), attribute = new HashMap();
	private static GameSettings gs = null;
	
	//---------------------------//
	//      Class Methods        //
	//---------------------------//

	//======= PUBLIC ============//
	
	/** 
	* Accessor method for reaching the one and only instance of this class. 
	* @return Reference to the GameSettings object
	*/
	public static GameSettings getInstance(){
		if(gs==null) gs = new GameSettings();
		return gs;
	}
	
	/* 
	================ NOTE : ===============================================
	=======================================================================	
	For GameSettings, we need in addition to the inherited Settings methods 
	methods that will be used to fill this object when a new game is started.
	To be able to code these required methods (there will be more than the two
	I give as example below) we need to agree on a format for games XML files.	

	public void addMove(CheckersMove cm){...}	
	public void addPlayer(Player p){...}
	...
	...
	...
	=========================================================================
	
	*/
	
	// -- Private Constructors -----------------------------------------------
	
	private GameSettings(){
		super();
	}
}
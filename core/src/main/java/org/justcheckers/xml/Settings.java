package main.java.org.justcheckers.xml;
 
import java.util.Set;
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
* Defines a common template for all classes that 
* store some sort of Settings. Text, Attribute and Element
* are references to the XML objects as implemented 
* by the JDOM API (http://www.jdom.org).
*
* @author Brinick Simmons (brinick@users.sourceforge.net)
*/
public abstract class Settings{
	//---------------------------//
	//      Class Fields         //
	//---------------------------//

	protected HashMap text = null, attribute = null;

	//---------------------------//
	//      Class Methods        //
	//---------------------------//

	//---------------------------------------------------------------------
	// -- Interface -------------------------------------------------------
	//---------------------------------------------------------------------
	
	public static void loadDefault(){}

	//get/set methods on the HashMaps
	public String getElementText(String key){
		if(!text.containsKey(key)) return null;
		return (String)text.get(key);
	}

	public void setElementText(String key, String value){
		text.put(key,value);
	}
	
	public String getElementAttribute(String key){
		if(!attribute.containsKey(key)) return null;
		return (String)attribute.get(key);
	}
	
	public void setElementAttribute(String key, String value){
		attribute.put(key,value);
	}

	public String getSetting(String key){
		if(text.containsKey(key)) return getElementText(key);
		else if(attribute.containsKey(key)) return getElementAttribute(key);
		return null;
	}

	public Set getTextEntries(){return text.entrySet();}
	public Set getAttributeEntries(){return attribute.entrySet();}

	//---------------------------------------------------------------------
	// -- Constructors ----------------------------------------------------
	//---------------------------------------------------------------------

	protected Settings(){
		text = new HashMap();
		attribute = new HashMap();		
	}
	
	/** 
	* Initiate the two class HashMap member objects with the parameters 
	* @param t The HashMap with which to initiate the "text" member
	* @param a The HashMap with which to initiate the "attribute" member	
	*/
	protected Settings(HashMap t, HashMap a){
		text = t;
		attribute = a;
	}

	////////////////////////////////////
	// INNER CLASS : Default Settings //
	////////////////////////////////////
	/**
	* The outer Settings object employs this nested one to obtain default values
	* for its member HashMap objects "text" and "attribute".
	*/
	protected abstract static class DefaultSettings{
		//------ Class Fields ----------- 
		protected String [][] text = {};
		protected String [][] attribute = {};

		//------ Class Methods ----------		
		protected void setFields(String [][] text, String [][] attribute){
			this.text = text;
			this.attribute = attribute;
		}

		public HashMap getTextMap(){
			HashMap hm = new HashMap(text.length);
			for(int k=0;k<text.length;k++){
				hm.put(text[k][0],text[k][1]);
			}
		
			return hm;
		}

		public HashMap getAttributeMap(){
			HashMap hm = new HashMap(attribute.length);
			for(int k=0;k<attribute.length;k++){
				hm.put(attribute[k][0],attribute[k][1]);
			}
		
			return hm;
		}
	}
}
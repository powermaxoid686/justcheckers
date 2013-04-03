package main.java.org.justcheckers.xml;

import java.io.File;
import java.io.FileFilter;

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

/** 
* XMLFileFilter returns only File objects that represent XML files.
*
* @author Brinick Simmons (brinick@users.sourceforge.net) 
*
*/ 
public class XMLFileFilter implements FileFilter{
	public boolean accept(File f){
		return f.toString().endsWith(".xml");
	}
}
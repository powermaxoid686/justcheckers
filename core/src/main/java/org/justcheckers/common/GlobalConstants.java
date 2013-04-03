/*****************************************************************************
	GlobalConstants.java - Constants for the entire application.
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

package main.java.org.justcheckers.common;

/**
 * Organizational class to keep all the constants in.
 * @author Dorian Pula
 *
 */
public class GlobalConstants {

	/** Flag for the information screen to display a "About Us". */
	public final static int FLAG_INFORMATION_DISPLAY_ABOUT_US = 0;
	/** Flag for the information screen to display the license of the app. */
	public final static int FLAG_INFORMATION_DISPLAY_LICENSE = 1;
	
	/** 
	 * The extras key that contains the information screens needs to display
	 * the right information. 
	 */
	public final static String EXTRA_INFORMATION_DISPLAY_FLAG = "info-display";
}

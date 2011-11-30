package org.justcheckers.xml;

import java.io.File;
import java.net.URL;
import java.util.Iterator;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.Text;

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 
/**
* Abstract version of an "intelligent" XML file. Objects of this class know 
* how to read/write the @see(Settings) information they are associated with, 
* into justCheckers memory/out to disk. The user creates a child object of 
* this class giving the name and location of the File object to be represented
* by this class. 
*
* NOTE : 
* For the time being, data may only be outputted to XML files stored locally.
*
* @author Brinick Simmons (brinick@users.sourceforge.net) 
*/
public abstract class XML_IO{

	//---------------------------//
	//      Class Fields         //
	//---------------------------//
	//protected URL url;
	protected File file;
	protected Settings settings;
	
	//---------------------------//
	//      Class Methods        //
	//---------------------------//

	//---------------------------------------------------------------------
	// -- Interface -------------------------------------------------------
	//---------------------------------------------------------------------
	
	/** 
	* Causes the XML data held within the File object referenced by the class 
	* member variable "file" to be loaded into the Settings object associated 
	* with this class. The reading in of XML data and subsequent transformation
	* is dealt with by the inner reader class of this class.
	*/
	public abstract void load();

	/** 
	* Causes the data held within the Settings object associated with this class
	* to be saved as XML format into the File object referenced by the class 
	* member variable "file". Transformation of Settings data to XML format and 
	* subsequent writing to File is handled by the inner writer class of this 
	* class.
	*/
	public abstract void save();

	/** Sets the member variable File object to the parameter object passed in.
	* @param f The File object with which to set the class member variable "file"
	*/
	protected void setFile(File f){file = f;}

	/** Gets the member variable File object.
	* @return The File object held in the class member variable "file".
	*/	
	protected File getFile(){return file;}	
	
	/* Place holder for a later version	*/
	//	protected void setFile(URL u){}	
	// protected URL getFile(){}

	/** Sets the member variable Settings object to the parameter object passed in.
	* @param s The Settings object with which to set the class member variable "settings"
	*/
	protected void setSettings(Settings s){settings = s;}

	/** Gets the member variable Settings object.
	* @return The Settings object held in the class member variable "settings".
	*/	
	protected Settings getSettings(){return settings;}		

	//---------------------------------------------------------------------
	// -- Constructors ----------------------------------------------------
	//---------------------------------------------------------------------
		
	protected XML_IO(){}	
	protected XML_IO(File f, Settings s){file = f; settings=s;}		
	protected XML_IO(URL u, Settings s){}	

	
	///////////////////////////////////
	//   INNER CLASS : READER        //
	///////////////////////////////////
		
	/**
	 * An abstract class that provides a framework to do any processing of a 
	 * DOM tree created with the JDOM package ( http://www.jdom.org ). It 
	 * provides a recursive traverse with data processing methods that run 
	 * before traversal, after traversal and at each Element object and Text 
	 * object encountered.  The default methods are do-nothing place-holders.
	 * These methods can be over-ridden in a child class that extends this one,
	 * doing what ever data processing needs to be done. Other methods and 
	 * fields can also be added to child classes as needed.
	 * 
	 * @author Dan D'Alimonte  (skwirl@users.sourceforge.net)
	 */		
	protected abstract class XMLFileReader{
    
	    // -- Interface ---------------------------------------------------------
	    
	    /**
	     * Actions to preform before the traversal of the DOM tree begins.
	     * @param e The root Element of the tree.
	     */
	    protected void preRoot( Element e ) {}
	    
	    /**
	     * Actions to preform after the traversal has been completed.
	     * @param e The root Element of the tree.
	     */
	    protected void postRoot( Element e ) {}
	    
	    /**
	     * Actions to preform when an Element object is encountered in the DOM tree.
	     * @param e The Element object to process.
	     */
	    protected void elementHandler( Element e ) {
	    	loadElementIntoSettings(e);
			loadAttributesIntoSettings(e);
	    }
	    
	    protected abstract void loadElementIntoSettings(Element e);
	    protected abstract void loadAttributesIntoSettings(Element e);
	    
	    /**
	     * Actions to preform when a Text object is encountered in the DOM tree.
	     * @param t The Text object to process.
	     */
	    protected void textHandler( Text t ) {}
	    
	    
	    // -- Constructors -------------------------------------------------------
	    
	    /**
	     * Construct a new VisitDOM instance.
	     */
	    public XMLFileReader() {}
	    
	    
	    // -- Public methods ----------------------------------------------------
	    
	    /**
	     * Preform the traversal on the DOM tree, visiting each node and 
	     * processing them in turn.
	     * @param root The root Element of the tree to preform the traversal on.
	     */
	    public void visit( Element root ) {
	        preRoot( root );
	        elementHandler( root );
	        recurse( root );
	        postRoot( root );
	    }	    
	    
	    // -- Protected Methods -------------------------------------------------
	    
	    /**
	     * Traverses to children of Elements, calling appropriate data processing
	     * methods on the child objects, recursing deeper if needed.
	     * @param e The element whose children are to be processed.
	     */
	    protected void recurse( Element e ) {
	        Iterator iElement = e.getChildren().iterator();
	        while ( iElement.hasNext() ) {
	            Object next = iElement.next();
	            if ( next instanceof Element ) {
	                elementHandler( (Element)next );
	                recurse( (Element)next );
	            }
	            else if ( next instanceof Text ) {
	                textHandler( (Text)next );
	            }
	        }   
	    }
	    
	   /*
		* Returns the full path name in the form a.b.c.d 
		* of an Element object d
		*/
		protected String toFullSettingName(Element e){
			String path = e.getName();
			Element currentElement = e;
			while(!currentElement.isRootElement()){
				currentElement = currentElement.getParent();
				path = currentElement.getName() + "." + path;			
			}
			
			return correctKeyForNumber(path);
		}
		
		protected abstract String correctKeyForNumber(String path);
		
	}
	
	///////////////////////////////////
	//   INNER CLASS : WRITER        //
	///////////////////////////////////
	
	/**
	* Abstract framework for creating a DOM tree 
	* (using the JDOM API http://www.jdom.org) from an 
	* in-application memory "Settings" class.
	* The default methods are do-nothing place-holders 
	* that should be over-ridden by a child class.
	* @author Brinick Simmons
	* @see UserSettings
	* @see GameSettings
	*/
	protected abstract class XMLFileWriter{
		
		/** 
		* Creates and returns a JDOM Document object 
		* @return org.jdom.Document object storing Settings information
		*/	
		protected Document createXMLDocument(){
			Element root = createRootElement();
			Document doc = new Document(root);
			addComments(doc);
			addElements(root);
			addAttributes(root);		
			return doc;
		}	
		
		/** 
		* Creates the root org.jdom.Element for the Document in memory
		* @return The newly created root Element
		*/
		abstract protected Element createRootElement();
		
		/** 
		* Adds org.jdom.Comment objects to the Document
		* @param d The Document to which Comments will be added
		*/
		protected void addComments(Document d){}
		
		/** 
		* Builds the tree structure of org.jdom.Element objects in the Document.
		* @param root The tree root Element to which all other 
		*					Elements are (in)directly attached.
		*/
		protected void addElements(Element root){}
		
		/** 
		* Adds any org.jdom.Attribute objects to the appropriate Element objects.
		* @param root The tree root Element.
		*/	
		protected void addAttributes(Element root){}				
	}
}


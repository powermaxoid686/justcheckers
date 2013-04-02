//********************************************************************
// VisitDOM.java -- Abstract class for traversing XML documents. 
// ********************************************************************

// ********************************************************************
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.      
// ********************************************************************

package org.justcheckers.xml;
import java.util.Iterator;
import org.jdom.Element;
import org.jdom.Text;

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
 * @author Dan D'Alimonte
 */
public abstract class VisitDOM {
    
    // -- Interface ---------------------------------------------------------
    
    /**
     * Actions to preform before the traversal of the DOM tree begins.
     * @param e The root Element of the tree.
     */
    protected void preRoot(Element e) {}
    
    /**
     * Actions to preform after the traversal has been completed.
     * @param e The root Element of the tree.
     */
    protected void postRoot(Element e) {}
    
    /**
     * Actions to preform when an Element object is encountered in the DOM tree.
     * @param e The Element object to process.
     */
    protected void elementHandler(Element e) {}
    
    /**
     * Actions to preform when a Text object is encountered in the DOM tree.
     * @param t The Text object to process.
     */
    protected void textHandler(Text t) {}
    
    
    // -- Contructors -------------------------------------------------------
    
    /**
     * Construct a new VisitDOM instance.
     */
    public VisitDOM() {}
    
    
    // -- Public methods ----------------------------------------------------
    
    /**
     * Preform the taversal on the DOM tree, visiting each node and 
     * processing them in turn.
     * @param root The root Element of the tree to preform the traversal on.
     */
    public void visit(Element root) {
        preRoot(root);
        elementHandler(root);
        recurse(root);
        postRoot(root);
    }
    
    
    // -- Protected Methods -------------------------------------------------
    
    /**
     * Traverses to children of Elements, calling appropriate data processing
     * methods on the child objects, recursing deeper if needed.
     * @param e The element whose children are to be processed.
     */
	protected void recurse(Element e) {
        Iterator iElement = e.getChildren().iterator();
        while (iElement.hasNext()) {
            Object next = iElement.next();
            if (next instanceof Element) {
                elementHandler((Element)next);
                recurse((Element)next);
            }
            else if ( next instanceof Text ) {
                textHandler((Text)next);
            }
        }   
    }
    
}
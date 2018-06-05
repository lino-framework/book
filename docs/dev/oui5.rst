.. _lino.dev.oui5:

Openui5 and Lino
================

Lino is designed to work independent of its front end. The front end could be extjs or html or text.
In practiaclity extjs3 and later extjs6 were the only front ends that were useable for anything other then basic read-only sites and doc-test.


In late 2017 after a long period of silence from sencha regarding their GPL distriputation, the Lino team decided to do research into a fesibal alternitive to extjs.


Openui5
-------

Openui5 is a high-level framework, like extjs, designed for enterprise level aplications. It's an open source distriputation of SAPUI5.
Openui5 so far seems to be a good fit as SAP seems more interested in keeping Openui5 maintained, and are regularly adding features from SAPUI5, however there are some major features that are still missing. 

Openui5's grid elements are advanced enough to match extjs, along with their selection elements. 

Differences in application
--------------------------

The main diferance between openui5 and extjs is the time and method in which the layouts and actions are generated from lino python code.
In extjs on inital startup lino generates a lino_XXX.js file which contains definitons for every action and layout, the XXX is in relation to the user's usertype. 
In openui5, rather then having everything be generated in javascript, the layout information is generated into XML and is requested by the client when needed. 
Also a major difference in design in that openui5 is implementing a MCV desgine struture to insure stability, where each major view has it's own javascript controller which has the code needed to have the lino app run proporly.

Chalenges with openui5
======================

Actions
-------

Due to openui5's on-request layout and controller design, when an action button is clicked, the only thing that the client knows is that it should run that action, however it doesn't know what that action should do. 
In extjs, the js code generated for each action and the code knows what the correct course of action is, whether that be opening a window with paramiters or just sending an ajax request to the server to run the action on a partiular set of records. 

Because of this it's needed to clasify actions into a few catigories. 

  #. simple actions
	Actions that require no paramiters and are run on a set of records. 
  #. Param actions 
	Actions that open a window which contains fields that are required for the action to be run, 
	An example being the merge action
  #. Insert actions.
	Actions that opens a window for the submition of a new record. 
	At this time it is unclear how diference this and param actions are
  #. Routing actions.
	Actions that change the view to focus on another view. 
	An example being the grid and detail actions
  #. Dialog actions. 
	Actions which open a dialog to display some data.
	An example being the site's about action, which opens a dalog containing the details about the lino-site.


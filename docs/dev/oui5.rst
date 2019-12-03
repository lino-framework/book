.. _lino.dev.oui5:

================
Openui5 and Lino
================

Note: This page is deprecated because the :ref:`openui5` for Lino
isn't currently maintained.

Lino is designed to work independent of its front end. The front end
could be extjs or html or text.

In practicality extjs3 and later extjs6 were the only front ends that
were usable for anything other then basic read-only sites and
doc-test.

In late 2017 after a long period of silence from sencha regarding
their GPL distribution, the Lino team decided to do research into a
feasible alternitive to extjs.


Openui5
=======

Openui5 is a high-level framework, like extjs, designed for enterprise
level applications. It's an open source distribution of SAPUI5.

Openui5 so far seems to be a good fit as SAP seems more interested in
keeping Openui5 maintained, and are regularly adding features from
SAPUI5, however there are some major features that are still missing.

Openui5's grid elements are advanced enough to match extjs, along with
their selection elements.

Differences in application
==========================

The main difference between openui5 and extjs is the time and method
in which the layouts and actions are generated from lino python code.

In extjs on initial startup lino generates a lino_XXX.js file which
contains definitions for every action and layout, the XXX is in
relation to the user's usertype.

In openui5, rather then having everything be generated in javascript,
the layout information is generated into XML and is requested by the
client when needed.  The client caches the result of these requests
and avoids calling them a second time.

Also a major difference in design in that openui5 is implementing a
MCV design structure to insure stability, where each major view has
it's own javascript controller which has the code needed to have the
lino app run properly.


Challenges with openui5
=======================

Actions
-------

Due to openui5's on-request layout and controller design, when an
action button is clicked, the only thing that the client knows is that
it should run that action, however it doesn't know what that action
should do.

In extjs, the js code generated for each action and the code knows
what the correct course of action is, whether that be opening a window
with paramiters or just sending an ajax request to the server to run
the action on a partiular set of records.

Because of this it's needed to classify actions into a few categories.

  #. simple actions:
     Actions that require no parameters and are run on a set of records.

  #. Param actions: Actions that open a window which contains fields
     that are required for the action to be run, an example being the
     merge action

  #. Insert actions:
     Actions that opens a window for the insertion of a new record.

     They are similar to parameter actions in that they open a popup
     window before actually executing.  The main difference is that
     the fields of an insert action are those of the table while in a
     dialog action you must define parameter fields on the action.

     First thought is that this is a subclass of param actions with a
     different callback method that routes to the new row's detail
     page, however that could be just a normal part of any action
     response.

  #. Routing actions :
     Actions that change the view to focus on another view.
     An example being the grid and detail actions.

     These actions seem like they ought to be used to generate xml
     views, ATM they are only being used as reference to generate
     views, rather than haveing the action itself have methods that
     generate the views.

  #. Dialog actions:

     Actions which open a dialog to display some data.  An example
     being the site's about action, which opens a dalog containing the
     details about the lino-site.


Main Dashboard
--------------

The main dashboard is an important item in any application, and in
lino it's rather lacking.

The docs state that you should create a jinja template which uses
query sets to generate html for the dashboard.

Other working lino apps use the dashboard plugin, which allows for
tables to be represented in html on the dashboard in whichever order
you choose.


Ideally you would want to have complex ui framework elements be in the
dashboard.  In extjs this is not currently possible, however since the
development of the openui5 renderer hasn't gotten too far we need to
figure out the best way to allow for this.

Luc and Tonis brainstormed an idea in which we define new actor types
or parameters which represent complex ui elements which can be
arranged on the dashboard.

Thus you can define some nicer looking buttons as routing links on the
dashboard for important tables, rather then the current html links.

Or can define a layout which includes ui5-tables or graphs.

Layout new or old
-----------------

Ui5 is designed to be mobile first, and their widgets reflect this,
they have automatic overflow handing and other useful features.

One of lino's major needs is to have it be mobile friendly. So this
makes ui5 a good choice, however if we just port the layout system
from extjs to ui5, it won't be mobile friendly.

The two major components that are not mobile friendly are: detail
views, and table elements.

Ui5 has table elements which are mobile friendly, however they are not
true table and miss some features.

Currently lino-ui5 is just porting the existing system to ui5, however
we need to look to see if there is a better way.

Detail editing
--------------

One component which is lacking in ui5 is extjs's dual-combobox, which
allows for choosing, editing, filtering and navigating.

This is a great component, however since it's missing in openui5, we
either need to recreate it or find some alternative method.

Ui5's input widget is a good contender, it allows key-value pairs and
server-side filtering.  However it fails to provide a way to navigate
to the selected object.

One idea is to have a read-mode and an edit-mode, in read-mode, most
actions are available, and selection of linked objects navigates to
their detail view.

In edit mode, they would swtich to editable fields, with only limited
options for actions, (save, cancel).

Both systems have upsides and downsides.

.. doctest docs/dev/workflows.rst
.. _workflows:

=========================
Introduction to Workflows
=========================

This tutorial explains how to define and use workflows.

This tutorial extends the application created in :doc:`watch`, so you
might want follow that tutorial before reading on here.

.. contents::
    :depth: 1
    :local:


About this document
===================

Examples on this page use the :mod:`lino_book.projects.workflows`
sample application.

>>> from lino import startup
>>> startup('lino_book.projects.workflows.settings')
>>> from lino.api.doctest import *

You can play with this application by installing the latest
development version of Lino, then ``cd`` to the workflows demo project
where you can run::

    $ go workflows
    $ python manage.py prep
    $ python manage.py runserver


What is a workflow?
===================

A workflow in Lino is defined by
(1) a "state" field on a model and
(2) a list of "transitions", i.e. actions which change a given object
from one state to another state.

For example consider this workflow:

.. graphviz::

   digraph foo {

    New -> Started;
    New -> Done;
    Started -> Done;
    New -> Sleeping;
    Started -> Sleeping;
    New -> Cancelled;
    Started -> Cancelled;
    Sleeping -> Cancelled;
    Sleeping -> Started[label="Wake up"];
   }

It consists of five *states* (New, Started, Done, Sleeping, Cancelled)
and a series of *transitions*.


Defining the states
===================

We use a choicelist to define the states.
That choicelist must be a special kind of choicelist: a
:class:`Workflow <lino.core.workflows.Workflow>`.  The choices of a
workflow are instances of :class:`State` and behave mostly like normal
choices, but have an additional method :meth:`add_transition
<lino.core.workflows.State.add_transition>` and an additional
(optional) attribute :attr:`button_text
<lino.core.workflows.State.button_text>`.


.. literalinclude:: ../../lino_book/projects/workflows/entries/choicelists.py

Here is the result of above definition:

>>> rt.show(entries.EntryStates)
======= =========== =========== =============
 value   name        text        Button text
------- ----------- ----------- -------------
 10      new         New         ☐
 20      started     Started     ⚒
 30      done        Done        ☑
 40      sleeping    Sleeping    ☾
 50      cancelled   Cancelled   ☒
======= =========== =========== =============
<BLANKLINE>


Defining transitions
====================

We define the transitions in a separate module:

.. literalinclude:: ../../lino_book/projects/workflows/entries/workflows.py

This module is being loaded at startup because its name is defined in
the Site's :attr:`workflows_module
<lino.core.site.Site.workflows_module>`.

Defining explicit transition actions
====================================

Note how the first argument to :meth:`add_transition
<lino.core.workflows.State.add_transition>` can be either a string or
a class.  If it is a class, then it defines an action.  Here are the
actions used in this tutorial:
                    
.. literalinclude:: ../../lino_book/projects/workflows/entries/actions.py

Defining an explicit class for transition action is useful when you
want your application to decide at runtime whether a transition is
available or not.

The :meth:`get_action_permission
<lino.core.actions.Action.get_action_permission>` method, as used by
the ``StartEntry`` action in our example.  It is called once for every
record and thus should not take too much energy.  In the example
application, you can see that the "Start" action is *not* shown for
entries with one of the company, subject or body fields empty.  Follow
the link to the API reference for details.

Note that if you test only the user_type of the requesting user, or
some value from ``settings``, then you'll rather define a
:meth:`get_view_permission
<lino.core.actions.Action.get_view_permission>` method.  That's more
efficient because it is called only once for every user user_type at
server startup.

Why do I  have to declare ``workflow_state_field``?
===================================================

The :attr:`workflow_state_field
<lino.core.models.Model.workflow_state_field>` is required if you want
your permission handlers to get the state argument.

In :file:`models.py` there are only a few changes (compared to
:doc:`watch`), first we need import the :class:`EntryStates` workflow,
and then add a :attr:`state` field to the :class:`Entry` model::

    from .choicelists import EntryStates
    ...
    class Entry(dd.CreatedModified, dd.UserAuthored):
        workflow_state_field = 'state'
        ...
        state = EntryStates.field(blank=True, default='todo')

Showing the workflow actions
============================
        
And finally we added the `workflow_buttons` at different places: in
the detail layout of Entry, and in a `column_names` attribute to
`EntriesByCompany` and `MyEntries`.  Note that `workflow_buttons` is a
:doc:`virtual field </dev/virtualfields>` and therefore not
automatically shown.
      




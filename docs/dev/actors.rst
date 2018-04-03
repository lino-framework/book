==================
Introducing actors
==================

**Tables** and **choicelists** have certain things in common.  When we
refer to them in general, then we call them **actors**.

An **actor** is a globally known unique object that offers **actions**.
Almost every incoming web request in a Lino application requests
execution of a given *action* on a given *actor*.

An alternative name for "Actor" might have been "Resource" or "View",
but these words are already being used very often, so in Lino we talk
about *actors*.

The most common type of actors are **tables**.  But not all actors are
tables.  Another type of actors are *frames* which display some data
in some other form. One such frame actor is the calendar panel,
another one is :class:`EmptyTable`, used to display reports.

See also

- :mod:`lino_book.projects.tables`
- :mod:`lino_book.projects.vtables`
- :mod:`lino_book.projects.actors`


The application namespace
=========================

When we say that actors are "globally known unique objects", then we
refer to what we call the **application namespace**.

Actually the application namespace is split across two places:
:data:`dd.plugins`
:data:`rt.modules`



Actors are classes, not instances
=================================

Actors are never instantiated, we use only the class objects.

Here is an example:

.. literalinclude:: actors1.py

The output will be::

  This is <class '__main__.MyJournals'> with parameters = {'foo': 1, 'bar': 2}


The main reason for this design choice is that it leads to more
readable application code.  But it has some disadvantages:

- Every method of an actor must have a `@classmethod` decorator.

- Concepts like `Parametrizable` are common to actions and actors, but
  need a "class method" and an "instance method" version of their
  logic.

We might decide one day that Lino creates an automatic singleton
instance for each Actor at startup.


Lino will automatically register each subclass of :class:`Actor` as an
actor.



The ``Actor`` class
===================


See :class:`lino.core.actors.Actor`.




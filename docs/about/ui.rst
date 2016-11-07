.. _about.ui:
.. _lino.ui:

==================
The user interface
==================

People tend to judge a framework by it's user interface (UI).  This
approach is not completely wrong since the UI is the first "visible"
part.  But Lino is designed to have many possible user interfaces. 

Lino comes with an extensible collection of **out-of-the-box user
interfaces** because we believe that application developers should
*develop applications* and should not waste their time writing html
templates or css.  It is one of Lino's design goals to **separate
business logic and user interface**.

**In theory** you write a Lino application once, and then you can
"deploy" (or use it yourself) via many different interfaces. For
example

- a more lightweight web interface using some other JS framework than ExtJS
- a web interface optimized for read-only access and publication of
  complex data (something like :ref:`belref`, but we agree that this
  needs more work before becoming really usable)
- a console UI using `ncurses <https://en.wikipedia.org/wiki/Ncurses>`_
- We once started working on an interface that uses the :doc:`Qooxdoo
  library </topics/qooxdoo>`.
- a desktop application using `Qt
  <https://en.wikipedia.org/wiki/Qt_%28software%29>`_ or `wxWidgets
  <https://en.wikipedia.org/wiki/WxWidgets>`_
- an XML or JSON based HTTP interface
- one might consider Lino's :class:`TextRenderer
  <lino.core.renderer.TextRenderer>` (used for writing tested
  functional specifications like `this one
  <http://welfare.lino-framework.org/specs/households.html>`_) as a
  special kind of user interface.

That said, we admit that **in practice**, your choice is currently
limited to the :mod:`lino.modlib.extjs` UI.  Lino applications
currently "look like" those you can see at :doc:`/demos`.  But that's
just because :term:`extjs` is so cool, and because writing and
optimizing a user interface is a rather boring work, and because there
are many other, more interesting tasks that are waiting to be done.


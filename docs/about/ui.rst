.. _about.ui:
.. _lino.ui:

==========================================
Separate business logic and user interface
==========================================

People tend to judge a framework by it's user interface.  This
approach is not completely wrong since the user interface is the first
and almost only "visible" part of an application.

But Lino is designed to have **many possible** user interfaces.  Lino
comes with an extensible collection of *out-of-the-box* user
interfaces.  You can write a Lino application once and then deploy it
via different interfaces. :ref:`noi` is an example of an application
which is deployed using two public UIs.

That said, your only realistic choice is currently the
:mod:`lino.modlib.extjs` UI.  Lino applications currently "look like"
those you can see at :doc:`/demos`.  You might like them or not, but
Lino's beauty lies beyond the user interface.

Writing and optimizing a user interface is a rather boring task, and
there are many other, more interesting tasks that are waiting to be
done, and, last but not least, because :term:`extjs` is so cool.

There are several proofs of concept for alternative user interfaces:

- the :mod:`lino_extjs6` is almost ready for production.
- one might consider Lino's :class:`TextRenderer
  <lino.core.renderer.TextRenderer>` (used for writing :doc:`tested
  functional specifications </dev/doctests>`) as a special kind of
  user interface.

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

There is a more detailed overview on :doc:`what this means for the
developer </dev/ui>`.

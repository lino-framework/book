.. doctest docs/dev/admin_main.rst
.. _dev.admin_main:

===============
The main window
===============

There are several methods for specifying the content of the :term:`main window`:

- define a custom :xfile:`admin_main.html` template (as we did in
  :doc:`/dev/polls/index`)

- override the :meth:`get_main_html
  <lino.core.site.Site.get_main_html>` method of your :class:`Site
  <lino.core.site.Site>` class to return your own chunk of html.

- use the default :xfile:`admin_main.html` template and define :term:`quick
  links <quick link>`, :term:`welcome messages <welcome message>` and
  :term:`dashboard items <dashboard item>`.

In practice you will probably use the latter method.

.. glossary::

  main window

    The window that is presented to the user after signing in and before opening
    any other window.

  quick link

    A shortcut link in the main window.

    See `Quick links`_ below.

  welcome message

    A one-sentence message to inform the user about something that might be
    worth to know after signing in.

    See `Welcome messages`_ below.

  dashboard item

    A table or report that is considered an important entry point to be shown in
    the main window.

    See :doc:`/specs/dashboard`.


The ``admin_main.html`` template file
=====================================

.. xfile:: admin_main_base.html
.. xfile:: admin_main.html

This is the template used to generate the inner content of the home
page.  It is split into two files :srcref:`admin_main.html
<lino/config/admin_main.html>` and :srcref:`admin_main_base.html
<lino/config/admin_main_base.html>`.

For illustration compare the content of the latter template with its
result in the following screenshots (taken from the :mod:`team
<lino_book.projects.noi1e>` demo project which runs :ref:`noi`).

.. figure:: /specs/noi/admin_main_000.png
   :width: 80 %

   Main window for AnonymousUser.

.. figure:: /specs/noi/admin_main_900.png
   :width: 80 %

   Main window for user ``robin``.



Quick links
===========

- override the
  :meth:`setup_quicklinks <lino.core.site.Site.setup_quicklinks>`
  methods of your :class:`Site <lino.core.site.Site>` class.

  See usage examples in the demo projects
  :mod:`min1 <lino_book.projects.min1>`,
  :mod:`min2 <lino_book.projects.min2>` and
  :mod:`min3 <lino_book.projects.min3>`.

Welcome messages
================

The :xfile:`admin_main.html` calls :meth:`get_welcome_messages
<lino.core.site.Site.get_welcome_messages>`.  This code inserts the
"welcome messages" for this user on this site.  As the application
developer you have several methods to define welcome messages:

- Set :attr:`welcome_message_when_count
  <lino.core.actors.Actor.welcome_message_when_count>` of some table
  to some value (usually ``0``).

  For example the :mod:`lino_xl.lib.tickets` uses this to define the
  "You have X items in Tickets to triage" message.

- Define a **custom welcome message** using
  :meth:`dd.add_welcome_handler
  <lino.core.site.Site.add_welcome_handler>`.

  For example the "You are busy with..." message in :ref:`noi` is
  :mod:`lino_xl.lib.working.models`.  Or
  :mod:`lino_xl.lib.stars.models` defines the "Your stars are"
  message.

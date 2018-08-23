.. doctest docs/dev/admin_main.rst
.. _dev.admin_main:

===============
The main window
===============

There are several methods for specifying the content of the main
window:

- define a custom :xfile:`admin_main.html` template (as we did in 
  :doc:`/dev/polls/index`)

- override the :meth:`get_main_html
  <lino.core.site.Site.get_main_html>` method of your :class:`Site
  <lino.core.site.Site>` class to return your own chunk of html.
    
- use the default :xfile:`admin_main.html` template and define *quick
  links*, *welcome messages* and *dashboard items*.

In practice you will probably use the latter method.


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
<lino_book.projects.team>` demo project which runs :ref:`noi`).

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


Dashboard items
===============

How to define your application's dashboard items:

- override the
  :meth:`get_dashboard_items
  <lino.core.site.Site.get_dashboard_items>`
  of your :class:`Site <lino.core.site.Site>` class.

- override the :meth:`get_dashboard_items
  <lino.core.plugin.Plugin.get_dashboard_items>` of your :class:`Plugin
  <lino.core.plugin.Plugin>` classes.

Independently of how you define the dashboard items for your
application, you can additionally opt to install the
:mod:`lino.modlib.dashboard` plugin.
  

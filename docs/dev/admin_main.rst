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
page.  It is split into two files
:srcref:`admin_main.html<lino/config/admin_main.html>` and
:srcref:`admin_main_base.html<lino/config/admin_main_base.html>`.


Exercise: Compare the content of Lino's default
:xfile:`admin_main_base.html` template with its result in the following
screenshots.

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

Welcome messages
================

- The :xfile:`admin_main.html` calls :meth:`get_welcome_messages
  <lino.core.site.Site.get_welcome_messages>`

- :meth:`dd.add_welcome_handler  
  <lino.core.site.Site.add_welcome_handler>`

- Define an :meth:`add_welcome_messages
  <lino.core.actors.Actor.add_welcome_messages>` method on an actor.

- Set :attr:`welcome_message_when_count
  <lino.core.actors.Actor.welcome_message_when_count>` to some value
  (usually ``0``).


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
  

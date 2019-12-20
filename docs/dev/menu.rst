.. doctest docs/dev/menu.rst
.. _dev.menu:

====================
The application menu
====================

As we have seen, a :term:`Lino application` contains :doc:`models <models>`,
:doc:`tables <tables/index>`, :doc:`layouts <layouts/index>` and :doc:`actions <actions>`.
But one important piece is missing: the *application menu*.

The **application menu** specifies how the different functionalities of an
application are structured when presenting them to the user. There is only one
application menu per application, but each user will see only the parts to which
they have access permission.


.. contents::
   :depth: 1
   :local:

A simple application menu
=========================

For simple applications you can define the complete menu by overriding the
:meth:`lino.core.site.Site.setup_menu` method of your application.

An example for this approach is in :ref:`dev.polls.settings`.  Let's have a look
at this application.

>>> from lino import startup
>>> startup('lino_book.projects.polls.mysite.settings')
>>> from lino.api.doctest import *

You have seen the application menu in a browser window. But you can also show it
in a documentation page:

>>> rt.login('robin').show_menu()
- Site : About
- Polls : Questions, Choices

See also :doc:`xlmenu`.

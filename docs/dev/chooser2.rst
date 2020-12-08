======================================
Choosers that need the requesting user
======================================

Sometimes you require the current user to determine the choices for a field.


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.noi1e.settings.doctests')
>>> from lino.api.doctest import *

If your chooser method needs to know the current user to determine the choices
for a field, include a "ar" parameter to your chooser method:

.. literalinclude:: /../../book/lino_book/projects/chooser/ar_chooser.py

For example the chooser for the :attr:`lino_xl.lib.tickets.Ticket.site` field
wants to know who is asking before deciding which sites to display, because not
everybody can see every site.

>>> url = '/choices/tickets/Ticket/site'
>>> show_choices("robin", url) #doctest: +ELLIPSIS
<br/>
pypi

>>> show_choices("luc", url) #doctest: +ELLIPSIS
<br/>
welket
docs

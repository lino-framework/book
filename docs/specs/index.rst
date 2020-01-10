.. _specs:
.. _book.specs:

=====
Specs
=====

This section contains :doc:`technical specifications </dev/specs>` for the
components of the :term:`Lino framework` that are covered by the book.

.. contents::
   :depth: 1
   :local:


.. It has individual subsections for each Lino application maintained by the Lino
   team.  It also has general topic guides and plugin descriptions for
   functionalities that are shared among several applications.

.. _specs.core:

Core plugins
============

The following plugins are part of the :mod:`lino.modlib`:

.. toctree::
   :maxdepth: 1

   users
   printing
   comments
   notify
   about
   search
   checkdata
   dashboard
   gfks
   summaries
   memo
   modlib
   system

The following plugins are currently still part of the :mod:`lino.modlib` but
might be moved to :mod:`lino_xl` some day:

.. toctree::
   :maxdepth: 1


   beid
   ssin
   export_excel
   tinymce

.. _specs.xl:

Plugins of the Extensions library
=================================

.. toctree::
   :maxdepth: 1

   addresses
   ana
   appypod
   b2c
   bevat
   bevats
   c2b
   cal
   calview
   clients
   coachings
   contacts
   countries
   courses
   cv
   eevat
   events/index
   excerpts
   groups
   healthcare
   files
   finan
   households
   humanlinks
   invoicing
   ledger
   lists
   notes
   office
   orders
   phones
   polls
   products
   properties
   sales
   sepa
   sheets
   tickets
   tim2lino
   topics
   trends
   uploads
   userstats
   vat
   weasyprint
   xl


Application specs
=================

Some applications have the privilege of being part of the Lino book, so their
technical documentation is provided and maintained by the Lino core team.

.. toctree::
   :maxdepth: 1


   cosi/index
   noi/index
   avanti/index
   tera/index
   polly
   care
   projects/min
   voga/index


Topic guides
============

.. toctree::
   :maxdepth: 1

   accounting
   human
   born
   holidays
   iban


Technical stuff
===============

.. toctree::
   :maxdepth: 1

   invalid_requests
   projects/mti
   projects/nomti
   projects/lets1
   projects/lets2
   projects/belref
   projects/actors
   uitests
   i18n
   de_BE
   gfktest
   dumps
   migrate
   ajax
   dpy
   jsgen
   html

.. toctree::
   :hidden:

   openui5

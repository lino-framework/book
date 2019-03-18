.. _welfare.specs:

==================
Lino Welfare specs
==================

This section is an exhaustive description of what you can do with
:ref:`welfare`.


General
=======

.. toctree::
   :maxdepth: 1
  
   general
   choicelists
   clients
   coachings
   users
   usertypes
   pcsw
   clients
   newcomers
   households
   dupable_clients
   checkdata
   aids/index
   cbss
   tx25
   xcourses
   debts
   excerpts
   integ
   isip
   isip_chatelet
   jobs
   misc
   polls
   reception/index
   uploads
   main
   addresses
   cal
   tasks
   countries
   notes
   notify
   ddh
   memo
   autoevents
   printing

Eupen
=====

.. toctree::
   :maxdepth: 2
  
   clients_eupen
   eupen
   b2c
   db_eupen
   ledger
   vatless
   finan

Châtelet
========

Is documented separately in :ref:`welcht`.

The courses, esf, art61 and immersion plugins are defined in
:mod:`lino_welfare.modlib` but (currently) used only by :mod:`lino_welcht`.
That's why  the specs for these plugins are in the :ref:`welcht` doctree.  But
we want the source code of a plugin to refer to its specs.  This ref is needed
when building the API for welfare. Which is in book. But the docs of book
cannot refer to the docs of welcht because this would be a circular dependency.
We definitively want the welcht docs be able to refer to the book (don't we?).
So theoretically we should have a demo project in the book which uses these
plugins. But theory is not always the same as reality.  Maybe one day we start
a separate book for lino welfare... En attendant as a quick workaround we
define the following  wrapper pages here:

.. toctree::
   :maxdepth: 2

   art61
   esf
   immersion
   courses

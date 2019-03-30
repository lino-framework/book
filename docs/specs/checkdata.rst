.. doctest docs/specs/checkdata.rst
.. _book.specs.checkdata:

==========================================
``checkdata`` : High-level integrity tests
==========================================

.. currentmodule:: lino.modlib.checkdata

The :mod:`lino.modlib.checkdata` plugin adds support for defining
application-level integrity tests using **data checkers**.

A **data checker** is a piece of code which tests for application-specific
"soft" database integrity problems.  Where "soft" means that it is not detected
by the database engine because it requires application intelligence to detect.

When a data checker finds a problem, then it issues a *problem
message* which is assigned to a *responsible user*.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.core.management import call_command

Which means that code snippets in this document are tested using the
:mod:`lino_book.projects.min9` demo project.


Data checkers
=============

In the web interface you can select :menuselection:`Explorer -->
System --> Data checkers` to see a table of all available
checkers.

.. 
    >>> show_menu_path(checkdata.Checkers)
    Explorer --> System --> Data checkers
    
>>> rt.show(checkdata.Checkers)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
================================= ==================================================
 value                             text
--------------------------------- --------------------------------------------------
 printing.CachedPrintableChecker   Check for missing target files
 countries.PlaceChecker            Check data of geographical places.
 mixins.DupableChecker             Check for missing phonetic words
 addresses.AddressOwnerChecker     Check for missing or non-primary address records
 cal.EventGuestChecker             Entries without participants
 cal.ConflictingEventsChecker      Check for conflicting calendar entries
 cal.ObsoleteEventTypeChecker      Obsolete generated calendar entries
 cal.LongEntryChecker              Too long-lasting calendar entries
================================= ==================================================
<BLANKLINE>


Showing all problems
====================

The demo database deliberately contains some data problems.
In the web interface you can select :menuselection:`Explorer -->
System --> Data problems` to see them.

..
    >>> show_menu_path(checkdata.AllProblems)
    Explorer --> System --> Data problems


>>> rt.show(checkdata.AllProblems)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
================= ===================================== ========================================================= ========================================
 Responsible       Database object                       Message                                                   Checker
----------------- ------------------------------------- --------------------------------------------------------- ----------------------------------------
 Robin Rood        *All Souls' Day (31.10.2014)*         Event conflicts with Petit-déjeuner (31.10.2014 10:20).   Check for conflicting calendar entries
 Romain Raffault   *Petit-déjeuner (31.10.2014 10:20)*   Event conflicts with All Souls' Day (31.10.2014).         Check for conflicting calendar entries
================= ===================================== ========================================================= ========================================
<BLANKLINE>



Filtering data problems
=======================

The user can set the table parameters e.g. to see only problems of a
given type ("checker"). The following snippet simulates the situation
of selecting the :class:`ConflictingEventsChecker
<lino_xl.lib.cal.models.ConflictingEventsChecker>`.

>>> chk = checkdata.Checkers.get_by_value('cal.ConflictingEventsChecker')
>>> rt.show(checkdata.ProblemsByChecker, chk)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ===================================== =========================================================
 Responsible       Database object                       Message
----------------- ------------------------------------- ---------------------------------------------------------
 Robin Rood        *All Souls' Day (31.10.2014)*         Event conflicts with Petit-déjeuner (31.10.2014 10:20).
 Romain Raffault   *Petit-déjeuner (31.10.2014 10:20)*   Event conflicts with All Souls' Day (31.10.2014).
================= ===================================== =========================================================
<BLANKLINE>

See also :doc:`cal` and :doc:`holidays`.


Running the :command:`checkdata` command
========================================

The :mod:`lino.modlib.checkdata` module provides a Django admin
command named :manage:`checkdata`.

>>> call_command('checkdata')
Found 2 and fixed 0 data problems in Calendar entries.
Done 5 checkers, found 2 and fixed 0 problems.

You can see the list of all available checkers also from the command
line using::

    $ python manage.py checkdata --list

>>> call_command('checkdata', list=True)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
================================= ==================================================
 value                             text
--------------------------------- --------------------------------------------------
 printing.CachedPrintableChecker   Check for missing target files
 countries.PlaceChecker            Check data of geographical places.
 mixins.DupableChecker             Check for missing phonetic words
 addresses.AddressOwnerChecker     Check for missing or non-primary address records
 cal.EventGuestChecker             Entries without participants
 cal.ConflictingEventsChecker      Check for conflicting calendar entries
 cal.ObsoleteEventTypeChecker      Obsolete generated calendar entries
 cal.LongEntryChecker              Too long-lasting calendar entries
================================= ==================================================
<BLANKLINE>


>>> call_command('checkdata', 'cal.')
Found 2 and fixed 0 data problems in Calendar entries.
Done 1 checkers, found 2 and fixed 0 problems.

>>> call_command('checkdata', 'foo')
Traceback (most recent call last):
...
Exception: No checker matches ('foo',)




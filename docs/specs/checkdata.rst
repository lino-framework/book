.. doctest docs/specs/checkdata.rst
.. _book.specs.checkdata:

==========================================
``checkdata`` : High-level integrity tests
==========================================

.. currentmodule:: lino.modlib.checkdata

The :mod:`lino.modlib.checkdata` plugin adds support for defining
application-level integrity tests using **data checkers**.

.. glossary::

  data checker

    a piece of code that tests for "soft" database integrity problems.  Where
    "soft" means that it is not detected by the database engine because it
    requires application intelligence to detect.

When a data checker finds a problem, then it issues a *problem message*, which
is assigned to a *responsible user*.

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
 addresses.AddressOwnerChecker     Check for missing or non-primary address records
 cal.ConflictingEventsChecker      Check for conflicting calendar entries
 cal.EventGuestChecker             Entries without participants
 cal.LongEntryChecker              Too long-lasting calendar entries
 cal.ObsoleteEventTypeChecker      Obsolete generated calendar entries
 countries.PlaceChecker            Check data of geographical places.
 memo.PreviewableChecker           Check for previewables needing update
 mixins.DupableChecker             Check for missing phonetic words
 printing.CachedPrintableChecker   Check for missing target files
 system.BleachChecker              Find unbleached html content
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
================= ======================================= =========================================================== ========================================
 Responsible       Database object                         Message                                                     Checker
----------------- --------------------------------------- ----------------------------------------------------------- ----------------------------------------
 Robin Rood        *All Souls' Day (31.10.2014)*           Event conflicts with 4 other events.                        Check for conflicting calendar entries
 Robin Rood        *All Saints' Day (01.11.2014)*          Event conflicts with 2 other events.                        Check for conflicting calendar entries
 Robin Rood        *Armistice with Germany (11.11.2014)*   Event conflicts with Seminar (11.11.2014 11:10).            Check for conflicting calendar entries
 Rando Roosi       *Dinner (31.10.2014 09:40)*             Event conflicts with All Souls' Day (31.10.2014).           Check for conflicting calendar entries
 Romain Raffault   *Petit-déjeuner (31.10.2014 10:20)*     Event conflicts with All Souls' Day (31.10.2014).           Check for conflicting calendar entries
 Robin Rood        *Meeting (01.11.2014 11:10)*            Event conflicts with All Saints' Day (01.11.2014).          Check for conflicting calendar entries
 Robin Rood        *Seminar (11.11.2014 11:10)*            Event conflicts with Armistice with Germany (11.11.2014).   Check for conflicting calendar entries
================= ======================================= =========================================================== ========================================
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
================= ======================================= ===========================================================
 Responsible       Database object                         Message
----------------- --------------------------------------- -----------------------------------------------------------
 Robin Rood        *All Souls' Day (31.10.2014)*           Event conflicts with 4 other events.
 Robin Rood        *All Saints' Day (01.11.2014)*          Event conflicts with 2 other events.
 Robin Rood        *Armistice with Germany (11.11.2014)*   Event conflicts with Seminar (11.11.2014 11:10).
 Rando Roosi       *Dinner (31.10.2014 09:40)*             Event conflicts with All Souls' Day (31.10.2014).
 Romain Raffault   *Petit-déjeuner (31.10.2014 10:20)*     Event conflicts with All Souls' Day (31.10.2014).
 Robin Rood        *Meeting (01.11.2014 11:10)*            Event conflicts with All Saints' Day (01.11.2014).
 Robin Rood        *Seminar (11.11.2014 11:10)*            Event conflicts with Armistice with Germany (11.11.2014).
================= ======================================= ===========================================================
<BLANKLINE>


See also :doc:`cal` and :doc:`holidays`.


Running the :command:`checkdata` command
========================================

The :mod:`lino.modlib.checkdata` module provides a Django admin
command named :manage:`checkdata`.

>>> call_command('checkdata')
Found 7 and fixed 0 data problems in Calendar entries.
Done 18 checks, found 7 and fixed 0 problems.

You can see the list of all available checkers also from the command
line using::

    $ python manage.py checkdata --list

>>> call_command('checkdata', list=True)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
================================= ==================================================
 value                             text
--------------------------------- --------------------------------------------------
 addresses.AddressOwnerChecker     Check for missing or non-primary address records
 cal.ConflictingEventsChecker      Check for conflicting calendar entries
 cal.EventGuestChecker             Entries without participants
 cal.LongEntryChecker              Too long-lasting calendar entries
 cal.ObsoleteEventTypeChecker      Obsolete generated calendar entries
 countries.PlaceChecker            Check data of geographical places.
 memo.PreviewableChecker           Check for previewables needing update
 mixins.DupableChecker             Check for missing phonetic words
 printing.CachedPrintableChecker   Check for missing target files
 system.BleachChecker              Find unbleached html content
================================= ==================================================
<BLANKLINE>


>>> call_command('checkdata', 'cal.')
Found 7 and fixed 0 data problems in Calendar entries.
Done 1 check, found 7 and fixed 0 problems.

>>> call_command('checkdata', 'foo')
Traceback (most recent call last):
...
Exception: No checker matches ('foo',)


Language of checkdata messages
==============================

Every detected checkdata problem is stored in the database in the language of
the responsible user. A possible pitfall with this is the following example.

The checkdata message "Similar clients" appeared in English and not in the
language of the responsible user. That was because the checker did this::

  msg = _("Similar clients: {clients}").format(
      clients=', '.join([str(i) for i in lst]))
  yield (False, msg)

The correct way is like this::

  msg = format_lazy(_("Similar clients: {clients}"),
      clients=', '.join([str(i) for i in lst]))
  yield (False, msg)

See :doc:`/dev/i18n` for details.

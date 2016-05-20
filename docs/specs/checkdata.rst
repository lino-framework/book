.. _book.specs.checkdata:

==========================
Checking for data problems
==========================

.. to test just this doc:

    $ python setup.py test -s tests.SpecsTests.test_checkdata

    >>> from lino import startup
    >>> startup('lino_book.projects.min2.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.core.management import call_command


Data checkers
=============

In the web interface you can select :menuselection:`Explorer -->
System --> Plausibility checkers` to see a table of all available
checkers.

.. 
    >>> show_menu_path(plausibility.Checkers)
    Explorer --> System --> Plausibility checkers
    
>>> rt.show(plausibility.Checkers)
================================= ==================================================
 value                             text
--------------------------------- --------------------------------------------------
 printing.CachedPrintableChecker   Check for missing target files
 countries.PlaceChecker            Check plausibility of geographical places.
 addresses.AddressOwnerChecker     Check for missing or non-primary address records
 mixins.DupableChecker             Check for missing phonetic words
 cal.EventGuestChecker             Check for missing participants
 cal.ConflictingEventsChecker      Check for conflicting events
================================= ==================================================
<BLANKLINE>


Showing all problems
====================

The demo database deliberately contains some data problems.
In the web interface you can select :menuselection:`Explorer -->
System --> Plausibility problems` to see them.

..
    >>> show_menu_path(plausibility.AllProblems)
    Explorer --> System --> Plausibility problems


>>> rt.show(plausibility.AllProblems)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
============= =========================================== ============================================================= ==============================
 Responsible   Controlled by                               Message                                                       Plausibility checker
------------- ------------------------------------------- ------------------------------------------------------------- ------------------------------
 Robin Rood    *Event #30 All Souls' Day (31.10.2014)*     Event conflicts with 2 other events.                          Check for conflicting events
 Robin Rood    *Event #113 Breakfast (31.10.2014 09:40)*   Event conflicts with Event #30 All Souls' Day (31.10.2014).   Check for conflicting events
 Robin Rood    *Event #125 Interview (31.10.2014 11:10)*   Event conflicts with Event #30 All Souls' Day (31.10.2014).   Check for conflicting events
============= =========================================== ============================================================= ==============================
<BLANKLINE>



Filtering data problems
=======================

The user can set the table parameters e.g. to see only problems of a
given type ("checker"). The following snippet simulates the situation
of selecting the :class:`ConflictingEventsChecker
<lino_xl.lib.cal.models.ConflictingEventsChecker>`.

>>> chk = plausibility.Checkers.get_by_value('cal.ConflictingEventsChecker')
>>> rt.show(plausibility.ProblemsByChecker, chk)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
============= =========================================== =============================================================
 Responsible   Controlled by                               Message
------------- ------------------------------------------- -------------------------------------------------------------
 Robin Rood    *Event #30 All Souls' Day (31.10.2014)*     Event conflicts with 2 other events.
 Robin Rood    *Event #113 Breakfast (31.10.2014 09:40)*   Event conflicts with Event #30 All Souls' Day (31.10.2014).
 Robin Rood    *Event #125 Interview (31.10.2014 11:10)*   Event conflicts with Event #30 All Souls' Day (31.10.2014).
============= =========================================== =============================================================
<BLANKLINE>


Running the :command:`checkdata` command
========================================


>>> call_command('checkdata')
Running 3 plausibility checkers on 125 Events...
Found 3 and fixed 0 plausibility problems in Events.
Running 1 plausibility checkers on 0 Excerpts...
No plausibility problems found in Excerpts.
Running 1 plausibility checkers on 100 Notes...
No plausibility problems found in Notes.
Running 1 plausibility checkers on 0 Projects...
No plausibility problems found in Projects.
Running 1 plausibility checkers on 78 Places...
No plausibility problems found in Places.
Running 2 plausibility checkers on 126 Partners...
No plausibility problems found in Partners.


You can see the list of all available checkers also from the command
line using::

    $ python manage.py checkdata --list


>>> call_command('checkdata', list=True)
================================= ==================================================
 value                             text
--------------------------------- --------------------------------------------------
 printing.CachedPrintableChecker   Check for missing target files
 countries.PlaceChecker            Check plausibility of geographical places.
 addresses.AddressOwnerChecker     Check for missing or non-primary address records
 mixins.DupableChecker             Check for missing phonetic words
 cal.EventGuestChecker             Check for missing participants
 cal.ConflictingEventsChecker      Check for conflicting events
================================= ==================================================
<BLANKLINE>


>>> call_command('checkdata', 'cal.')
Running 2 plausibility checkers on 125 Events...
Found 3 and fixed 0 plausibility problems in Events.

>>> call_command('checkdata', 'foo')
Traceback (most recent call last):
...
CommandError: No checker matches ('foo',)




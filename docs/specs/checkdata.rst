.. doctest docs/specs/checkdata.rst
.. _book.specs.checkdata:

==========================================
``checkdata`` : High-level integrity tests
==========================================

.. currentmodule:: lino.modlib.checkdata

The :mod:`lino.modlib.checkdata` plugin adds support for defining
application-level data integrity tests. It provides a Django admin command named
:manage:`checkdata`.



.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.core.management import call_command
>>> from atelier.sheller import Sheller
>>> shell = Sheller("lino_book/projects/min9")

Which means that code snippets in this document are tested using the
:mod:`lino_book.projects.min9` demo project.

Overview
========

A :term:`data problem` is an issue with database integrity that is not detected
by the DBMS because seeing it requires higher business intelligence.  Some data
issues can be fixed automatically, others need human interaction.  Lino provides
a framework for managing and handling data problems in different ways.

The application developer defines the rules for detecting data problems by
writing :term:`data checkers <data checker>`.

Lino automatically adds a button "Update data problems" on objects for which
there is at least one :term:`data checker` available.

The application developer can also add a :class:`ProblemsByOwner`
table to the :term:`detail layout` of any model.


.. glossary::

  data problem

    A "soft" database integrity problem, which is not detected by the database
    engine because it requires application intelligence to detect.

  data checker

    A piece of code that tests for :term:`data problems <data problem>`.

    Data checkers are usually attached to a given database model. If they are
    not attached to a model, they are called **unbound checkers**. Lino has
    different ways to run these checkers.  When a data checker finds a problem,
    Lino creates a :term:`problem message`.

  problem message

    A message that describes one or several :term:`data problems <data problem>`
    detected in a given database object. Problem messages are themselves
    database objects, but considered temporary data and may be updated
    automatically without user confirmation. Each problem message is assigned to
    a *responsible user*.


Data checkers
=============

In the web interface you can select :menuselection:`Explorer --> System --> Data
checkers` to see a table of all available checkers.

..
    >>> show_menu_path(checkdata.Checkers)
    Explorer --> System --> Data checkers

>>> rt.show(checkdata.Checkers)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
=================================== ========================================================
 value                               text
----------------------------------- --------------------------------------------------------
 addresses.AddressOwnerChecker       Check for missing or non-primary address records
 cal.ConflictingEventsChecker        Check for conflicting calendar entries
 cal.EventGuestChecker               Entries without participants
 cal.LongEntryChecker                Too long-lasting calendar entries
 cal.ObsoleteEventTypeChecker        Obsolete generated calendar entries
 countries.PlaceChecker              Check data of geographical places.
 ledger.VoucherChecker               Check integrity of ledger vouchers
 memo.PreviewableChecker             Check for previewables needing update
 mixins.DupableChecker               Check for missing phonetic words
 phones.ContactDetailsOwnerChecker   Check for mismatches between contact details and owner
 printing.CachedPrintableChecker     Check for missing target files
 system.BleachChecker                Find unbleached html content
=================================== ========================================================
<BLANKLINE>


The :class:`lino_xl.lib.countries.PlaceChecker` class is a simple example of how
to write a data checker::

  from lino.api import _
  from lino.modlib.checkdata.choicelists import Checker

  class PlaceChecker(Checker):
      model = 'countries.Place'
      verbose_name = _("Check data of geographical places.")

      def get_checkdata_problems(self, obj, fix=False):
          if obj.name.isdigit():
              yield (False, _("Name contains only digits."))

  PlaceChecker.activate()

..
  >>> print(rt.models.countries.PlaceChecker.verbose_name)
  Check data of geographical places.


More examples of data checkers we recommend to explore:

- :class:`lino_xl.lib.countries.PlaceChecker`
- :class:`lino_xl.lib.beid.mixins.BeIdCardHolderChecker`
- :class:`lino_xl.lib.addresses.AddressOwnerChecker`
- :class:`lino.mixins.dupable.DupableChecker`
- :class:`lino_welfare.modlib.pcsw.models.SSINChecker`
- :class:`lino_welfare.modlib.pcsw.models.ClientCoachingsChecker`
- :class:`lino_welfare.modlib.isip.mixins.OverlappingContractsChecker`
- :class:`lino_welfare.modlib.dupable_clients.models.SimilarClientsChecker`



Showing all data problems
=========================

In the web interface you can select :menuselection:`Explorer -->
System --> data problems` to see all problems.

..
    >>> show_menu_path(checkdata.AllProblems)
    Explorer --> System --> Data problems

The demo database deliberately contains some data problems.

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

The user can set the table parameters e.g. to see only problems of a given type
("checker"). The following snippet simulates the situation of selecting the
:class:`ConflictingEventsChecker <lino_xl.lib.cal.ConflictingEventsChecker>`.

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


>>> call_command('checkdata')
Found 7 and fixed 0 data problems in Calendar entries.
Done 20 checks, found 7 and fixed 0 problems.

You can see the list of all available checkers also from the command
line using::

    $ python manage.py checkdata --list

>>> call_command('checkdata', list=True)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=================================== ========================================================
 value                               text
----------------------------------- --------------------------------------------------------
 addresses.AddressOwnerChecker       Check for missing or non-primary address records
 cal.ConflictingEventsChecker        Check for conflicting calendar entries
 cal.EventGuestChecker               Entries without participants
 cal.LongEntryChecker                Too long-lasting calendar entries
 cal.ObsoleteEventTypeChecker        Obsolete generated calendar entries
 countries.PlaceChecker              Check data of geographical places.
 ledger.VoucherChecker               Check integrity of ledger vouchers
 memo.PreviewableChecker             Check for previewables needing update
 mixins.DupableChecker               Check for missing phonetic words
 phones.ContactDetailsOwnerChecker   Check for mismatches between contact details and owner
 printing.CachedPrintableChecker     Check for missing target files
 system.BleachChecker                Find unbleached html content
=================================== ========================================================
<BLANKLINE>


>>> call_command('checkdata', 'cal.')
Found 7 and fixed 0 data problems in Calendar entries.
Done 1 check, found 7 and fixed 0 problems.

>>> call_command('checkdata', 'foo')
Traceback (most recent call last):
...
Exception: No checker matches ('foo',)

The ``--prune`` option instructs checkdata to remove all existing error messages
before running the tests.  This makes the operation quicker on sites with many
existing data problem messages. Don't use this in combination with a filter
because `--prune` removes *all* messages, not only those that you ask to
rebuild.

>>> shell("python manage.py checkdata --prune")
Prune 7 existing messages...
Found 7 and fixed 0 data problems in Calendar entries.
Done 20 checks, found 7 and fixed 0 problems.

NB the above example uses :mod:`atelier.sheller` instead of :mod:`call_command
<django.core.management.call_command>`. 


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

.. class:: Problem

  Django model used to store a :term:`problem message`.

  .. attribute:: checker

     The :class:`Checker <lino.modlib.checkdata.Checker>` that reported this
     problem.

  .. attribute:: message

     The message text. This is a concatenation of all messages that
     were yielded by the :attr:`checker`.

  .. attribute:: user

     The :class:`user <lino.modlib.users.User>` responsible for fixing this
     problem.

     This field is being filled by the :meth:`get_responsible_user
     <lino.modlib.checkdata.Checker.get_responsible_user>`
     method of the :attr:`checker`.


.. class:: Problems

    The base table for :term:`problem message` objects.


.. class:: Checkers

    The list of data checkers known by this application.

    This was the first use case of a :class:`ChoiceList
    <lino.core.choicelists.ChoiceList>` with a :attr:`detail_layout
    <lino.core.actors.Actor.detail_layout>`.



.. class:: Checker

  Base class for all :term:`data checkers <data checker>`.

  .. attribute:: model

    The model to be checked.  If this is a string, Lino will resolve it at startup.

    If this is an abstract model, :meth:`get_checkable_models`  will
    potentially yield more than one model.

    If this is `None`, the checker is unbound, i.e. the problem messages will
    not be bound to a particular database object.

    You might also define your own
    :meth:`get_checkable_models` method.

  .. classmethod:: check_instance(cls, *args, **kwargs)

    Run :meth:`get_checkdata_problems` on this checker for the given database
    object.

  .. method:: get_checkable_models(self)

    Return a list of the models to check.

    The default implementation uses the :attr:`model`.

  .. classmethod:: activate(cls)

    Creates an instance of this class and adds it as a choice to the
    :class:`Checkers` choicelist.

    Application developers must call this on their subclass in order to
    "register" or "activate" it.

  .. method:: update_problems(self, obj=None, delete=True, fix=False)

    Update the :term:`problem messages <problem message>` of this checker for
    the specified object.

    ``obj`` is `None` on unbound checkers.

    When `delete` is False, the caller is responsible for deleting any existing
    objects.

  .. method:: get_checkdata_problems(self, obj, fix=False)

    Return or yield a series of `(fixable, message)` tuples, each describing a
    data problem. `fixable` is a boolean saying whether this problem can be
    automatically fixed. And if `fix` is `True`, this method is also responsible
    for fixing it.

  .. method:: get_responsible_user(self, obj)

    The site user to be considered responsible for problems detected by this
    checker on the given database object `obj`. This will be stored in
    :attr:`user <lino.modlib.checkdata.Problem.user>`.

    The given `obj` is an instance of :attr:`model`, unless for unbound
    checkers (i.e. whose :attr:`model` is `None`).

    The default implementation returns the *main checkdata
    responsible* defined for this site (see
    :attr:`responsible_user
    <lino.modlib.checkdata.Plugin.responsible_user>`).

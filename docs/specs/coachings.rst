.. doctest docs/specs/coachings.rst
.. _specs.coachings:

==================================
``coachings`` : Managing coachings
==================================

.. currentmodule:: lino_xl.lib.coachings

The :mod:`lino_xl.lib.coachings` plugin adds functionality for managing
"coachings". It is currently used in :ref:`welfare` only.


.. glossary::

  coaching

    When a given site user engages as "coach" in regular, structured
    conversation with a given "client" during a given period.

    (German "Begleitung", French "intervention")

    For example in :ref:`welfare` that user is a social assistant.

  coaching type

    The "type" of a coaching.  In :ref:`welfare` this is named a "Service".

    Can be used for expressing different types of responsibilities. For example
    in :ref:`welfare` they differentiate "General Social Service"
    "Integration Service" and "Debt mediation".


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.avanti1.settings.doctests')
>>> from lino.api.doctest import *


Coachings
=========

.. class:: Coaching

    Django model to represent a :term:`coaching`.

    .. attribute:: user
    .. attribute:: client
    .. attribute:: type
    .. attribute:: end_date
    .. attribute:: start_date
    .. attribute:: primary

      Whether this coaching is primary.   Enabling this field will automatically
      make the other coachings non-primary.

      See `The primary coach`_

    .. attribute:: ending

.. class:: Coachings

    A table showing a set of coachings.

.. class:: CoachingsByClient

    The :class:`Coachings` table in a clients detail.

.. class:: CoachingsByUser


Coachables
==========

.. class:: Coachable

    Base class for coachable client. The model specified as
    :attr:`client_model <Plugin.client_model>` must implement this.

    .. method:: get_coachings(self, period=None, *args, **flt)

        Return a queryset with the coachings of this client. If
        `period` is not `None`, it must be a tuple of two date
        objects. Any additional arguments are applied as filter of the
        queryset.

    .. method:: get_primary_coach(self)

        Return the one and only primary coach of this client (or
        `None` if there's less or more than one).

    .. method:: setup_auto_event(self, evt)

        Implements :meth:`EventGenerator.setup_auto_event
        <lino_xl.lib.cal.EventGenerator.setup_auto_event>`.

        This implements the rule that suggested evaluation events should
        be for the *currently responsible* coach if the contract's
        author no longer coaches that client.  This is relevant if
        coach changes while contract is active.

        The **currently responsible coach** is the user for which
        there is a coaching which has :attr:`does_integ
        <lino_xl.lib.coachings.CoachingType.does_integ>` set to
        `True`..


Coaching types
==============

.. class:: CoachingType

    Django model to represent a :term:`coaching`.

    .. attribute:: does_integ

        Whether coachings of this type are to be considered as
        integration work.

        This is used when generating calendar events for evaluation
        meetings (see
        :meth:`lino_xl.lib.coaching.Coachable.setup_auto_event`)


.. class:: CoachingTypes



Coaching endings
================

.. class:: CoachingEnding

   A **Coaching termination reason** expresses why a coaching has been
   terminated.

.. class:: CoachingEndings

    A list of reasons expressing why a coaching was ended.



Miscellaneous
=============


.. class:: CoachingsUser

    A user who has access to basic coachings functionality.


.. class:: CoachingsStaff

    A user who can configure coachings functionality.

.. class:: ClientChecker
.. class:: ClientCoachingsChecker

    Coached clients should not be obsolete.  Only coached clients
    should have active coachings.


Injects
=======

The :mod:`lino_xl.lib.coachings` plugin injects the following fields
into models of other plugins.

.. currentmodule:: lino.modlib

.. class:: users.User
    :noindex:

    .. attribute:: coaching_type

        The coaching type used for new coachings of this user.

    .. attribute:: coaching_supervisor

        Notify me when a coach has been assigned.


The primary coach
=================

Every client should have a **primary coach**.  This is the main responsible
coach for that client.

Lino verifies that there's at most one primary coach per client. When you check
the :attr:`primary <Coaching.primary>`  field of one coaching, Lino
automatically unchecks it on any other coachings of that client.

Reality is even a bit more complicated: when :attr:`multiple_primary_coachings
<lino_xl.lib.coachings.Plugin.multiple_primary_coachings>` is set to True, the
uniqueness of the primary coaching is no longer just per client but per client
and :term:`coaching type`. As a result you can have multiple primary coachings
per client.

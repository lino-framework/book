.. doctest docs/specs/coachings.rst
.. _specs.coachings:

==================================
``coachings`` : Managing coachings
==================================

.. currentmodule:: lino_xl.lib.coachings

The :mod:`lino_xl.lib.coachings` plugin adds functionality for managing
"coachings".  A coaching is when a "coach" (a system user) engages in regular,
structured conversation with a "client".  It is currently used in
:ref:`welfare` only.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.adg.settings.doctests')
>>> from lino.api.doctest import *


Coachings
=========

.. class:: Coaching

    A Coaching ("Begleitung" in German and "intervention" in French)
    is when a given client is being coached by a given user during a
    given period.

    For example in :ref:`welfare` that user is a social assistant.

    .. attribute:: user
    .. attribute:: client
    .. attribute:: type
    .. attribute:: end_date
    .. attribute:: start_date
    .. attribute:: primary
    .. attribute:: ending
           
.. class:: Coachings
           
    The :class:`Coachings` table in a clients detail.

.. class:: CoachingsByClient
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

    The **type** of a coaching can be used for expressing different
    types of responsibilities. For example in :ref:`welfare` they
    differentiate between "General Social Service" and "Integration
    Service".

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

    

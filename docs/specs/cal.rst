.. _book.specs.cal:

=================
Calendar
=================

.. How to test just this document

    $ doctest docs/specs/cal.rst

    Some initialization:

    >>> from lino import startup
    >>> startup('lino_book.projects.min9.settings.demo')
    >>> from lino.api.doctest import *

This document explains some basic things about Lino's calendar plugin.

.. currentmodule:: lino_xl.lib.cal
                  
Calendar entries
================

An **appointment** is a calendar entry which supposes that another
person is involved.

>>> show_fields(rt.models.cal.Event,
...     'start_date start_time end_date end_time user summary description event_type state')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
+---------------+---------------------+---------------------------------------------------------------+
| Internal name | Verbose name        | Help text                                                     |
+===============+=====================+===============================================================+
| start_date    | Start date          |                                                               |
+---------------+---------------------+---------------------------------------------------------------+
| start_time    | Start time          |                                                               |
+---------------+---------------------+---------------------------------------------------------------+
| end_date      | End Date            |                                                               |
+---------------+---------------------+---------------------------------------------------------------+
| end_time      | End Time            | These four fields define the duration of this entry.          |
|               |                     | Only start_date is mandatory.                                 |
+---------------+---------------------+---------------------------------------------------------------+
| user          | Responsible user    | The responsible user.                                         |
+---------------+---------------------+---------------------------------------------------------------+
| summary       | Short description   | A one-line descriptive text.                                  |
+---------------+---------------------+---------------------------------------------------------------+
| description   | Description         | A longer descriptive text.                                    |
+---------------+---------------------+---------------------------------------------------------------+
| event_type    | Calendar entry type | The type of this entry. Every calendar entry should have this |
|               |                     | field pointing to a given EventType, which holds              |
|               |                     | extended configurable information about this entry.           |
+---------------+---------------------+---------------------------------------------------------------+
| state         | State               | The state of this entry. The state can change according to    |
|               |                     | rules defined by the workflow, that's why we sometimes refer  |
|               |                     | to it as the life cycle.                                      |
+---------------+---------------------+---------------------------------------------------------------+

Lifecycle of a calendar entry
=============================

Every calendar entry has a given **state** which can change The state
of this entry. The state can change according to rules defined by the
workflow, that's why we sometimes refer to it as the life cycle.

The default list of choices for this field contains the following
values.

>>> rt.show(cal.EntryStates)
======= ============ ============ ======== =================== ======== ============= =========
 value   name         text         Symbol   Edit participants   Stable   Transparent   No auto
------- ------------ ------------ -------- ------------------- -------- ------------- ---------
 10      suggested    Suggested    ?        Yes                 No       No            No
 20      draft        Draft        ☐        Yes                 No       No            No
 50      took_place   Took place   ☑        Yes                 Yes      No            No
 70      cancelled    Cancelled    ☒        No                  Yes      Yes           Yes
 40      published    Published    ☼        Yes                 Yes      No            No
======= ============ ============ ======== =================== ======== ============= =========
<BLANKLINE>


Duration units
==============

Lino has a list of duration units :class:`DurationUnits`.

>>> rt.show(cal.DurationUnits)
======= ========= =========
 value   name      text
------- --------- ---------
 s       seconds   seconds
 m       minutes   minutes
 h       hours     hours
 D       days      days
 W       weeks     weeks
 M       months    months
 Y       years     years
======= ========= =========
<BLANKLINE>


>>> from lino_xl.lib.cal.choicelists import DurationUnits
>>> start_date = i2d(20111026)
>>> DurationUnits.months.add_duration(start_date, 2)
datetime.date(2011, 12, 26)

>>> from lino.utils import i2d
>>> start_date = i2d(20111026)
>>> DurationUnits.months.add_duration(start_date, 2)
datetime.date(2011, 12, 26)
>>> DurationUnits.months.add_duration(start_date, -2)
datetime.date(2011, 8, 26)

>>> start_date = i2d(20110131)
>>> DurationUnits.months.add_duration(start_date, 1)
datetime.date(2011, 2, 28)
>>> DurationUnits.months.add_duration(start_date, -1)
datetime.date(2010, 12, 31)
>>> DurationUnits.months.add_duration(start_date, -2)
datetime.date(2010, 11, 30)

>>> start_date = i2d(20140401)
>>> DurationUnits.months.add_duration(start_date, 3)
datetime.date(2014, 7, 1)
>>> DurationUnits.years.add_duration(start_date, 1)
datetime.date(2015, 4, 1)

.. _specs.cal.automatic_events:

Automatic calendar events
=========================

Lino applications can **generate** automatic calendar events.

An **event generator** is something that can generate automatic
calendar events.  The main effect of the :class:`EventGenerator` mixin
is to add the :class:`UpdateEntries` action.

The event generator itself does not necessarily also contain all those
fields needed for specifying **which** events should be
generated. These fields are implemented by another mixin named
:class:`RecurrenceSet`. A
recurrence set is something that specifies which calendar events
should get generated.

For example:

- A *course*, *workshop* or *activity* as used by Welfare, Voga and
  Avanti (subclasses of :class:`lino_xl.lib.courses.models.Course`).

- :class:`lino_xl.lib.rooms.models.Reservation`

- :class:`lino_welfare.modlib.isip.models.Contract` and
  :class:`lino_welfare.modlib.jobs.models.Contract`

- :doc:`Holidays <holidays>`

The generated events are "controlled" by their generator (their
`owner` field points to the generator) and have a non-empty
`auto_type` field.

    
:meth:`get_wanted_auto_events`


Recurrencies
============

When generating automatic calendar events, Lino supports the following
date recurrenies:

>>> rt.show(cal.Recurrencies)
======= ============= ====================
 value   name          text
------- ------------- --------------------
 O       once          once
 D       daily         daily
 W       weekly        weekly
 M       monthly       monthly
 Y       yearly        yearly
 P       per_weekday   per weekday
 E       easter        Relative to Easter
======= ============= ====================
<BLANKLINE>

Addding a duration unit

>>> start_date = i2d(20160327)
>>> cal.Recurrencies.once.add_duration(start_date, 1)
Traceback (most recent call last):
...
Exception: Invalid DurationUnit once

>>> cal.Recurrencies.daily.add_duration(start_date, 1)
datetime.date(2016, 3, 28)

>>> cal.Recurrencies.weekly.add_duration(start_date, 1)
datetime.date(2016, 4, 3)

>>> cal.Recurrencies.monthly.add_duration(start_date, 1)
datetime.date(2016, 4, 27)

>>> cal.Recurrencies.yearly.add_duration(start_date, 1)
datetime.date(2017, 3, 27)

>>> cal.Recurrencies.easter.add_duration(start_date, 1)
datetime.date(2017, 4, 16)


Recurrent events
================

In :mod:`lino_book.projects.min2` we have a database model
:class:`RecurrentEvent <lino_xl.lib.cal.models.RecurrentEvent>` used
to generate holidays.  See also :ref:`xl.specs.holidays`.

We are going to use this model for demonstrating some more features
(which it inherits from :class:`RecurrenceSet` and an
:class:`EventGenerator`)


>>> obj = cal.RecurrentEvent(start_date=i2d(20160628))
>>> isinstance(obj, cal.RecurrenceSet)
True
>>> isinstance(obj, cal.EventGenerator)
True
>>> obj.tuesday = True
>>> obj.every_unit = cal.Recurrencies.weekly
>>> print(obj.weekdays_text)
Every Tuesday

>>> obj.every
1

>>> obj.every = 2
>>> print(obj.weekdays_text)
Every 2nd Tuesday

>>> obj.every_unit = cal.Recurrencies.monthly
>>> print(obj.weekdays_text)
Every 2nd month


>>> rt.show(cal.EventTypes, column_names="id name")
==== ============= ================== ==================
 ID   Designation   Designation (et)   Designation (fr)
---- ------------- ------------------ ------------------
 1    Holidays      Holidays           Jours fériés
 2    Meeting       Meeting            Réunion
==== ============= ================== ==================
<BLANKLINE>

>>> obj.event_type = cal.EventType.objects.get(id=1)
>>> obj.max_events = 5

>>> ses = rt.login('robin')
>>> wanted, unwanted = obj.get_wanted_auto_events(ses)
>>> for num, e in wanted.items():
...     print(dd.fds(e.start_date))
28/06/2016
30/08/2016
01/11/2016
03/01/2017
07/03/2017

Note that above dates are not exactly every 2 months because 

- they are only on Tuesdays
- Lino also avoids conflicts with existing events

>>> cal.Event.objects.order_by('start_date')[0]
Event #1 ("New Year's Day (01.01.2013)")

>>> obj.monday = True
>>> obj.wednesday = True
>>> obj.thursday = True
>>> obj.friday = True
>>> obj.saturday = True
>>> obj.sunday = True
>>> obj.start_date=i2d(20120628)
>>> wanted, unwanted = obj.get_wanted_auto_events(ses)
>>> for num, e in wanted.items():
...     print(dd.fds(e.start_date))
28/06/2012
28/08/2012
28/10/2012
28/12/2012
28/02/2013




Conflicting events
==================


The demo datebase contains two appointments on All Souls' Day 2014:

>>> obj = cal.Event.objects.get(id=30)
>>> print(obj)
All Souls' Day (31.10.2014)

>>> rt.show(cal.ConflictingEvents, obj)
============ ============ ========== ======== ====== ==================
 Start date   Start time   End Time   Person   Room   Responsible user
------------ ------------ ---------- -------- ------ ------------------
 31/10/2014   09:40:00     12:40:00                   Rando Roosi
 31/10/2014   10:20:00     11:20:00                   Romain Raffault
============ ============ ========== ======== ====== ==================
<BLANKLINE>

Conflicting calendar events are also globally visible as data
problems, see :doc:`checkdata`.



Other
=====

The source code is in :mod:`lino_xl.lib.cal`.
Applications can extend this plugin.

See also :mod:`lino_xl.lib.cal.utils`.


Reference
=========


.. class:: RemoteCalendar

    Remote calendars will be synchronized by
    :mod:`lino_xl.lib.cal.management.commands.watch_calendars`,
    and local modifications will be sent back to the remote calendar.


.. class:: Room

    A location where calendar entries can happen.  For a given Room you
    can see the :class:`EntriesByRoom` that happened (or will happen)
    there.  A Room has a multilingual name.

    
    
.. class:: Priority
           
    The priority of a task or entry.
    
.. class:: EventType

    The possible value of the :attr:`Event.type` field.

    .. attribute:: is_appointment

        Whether entries of this type should be considered
        "appointments" (i.e. whose time and place have been agreed
        upon with other users or external parties).

        Certain tables show only entries whose type has the
        `is_appointment` field checked.  See :attr:`show_appointments
        <lino_xl.lib.cal.ui.Entries.show_appointments>`.

    .. attribute:: max_days

        The maximal number of days allowed as duration.

    .. attribute:: locks_user

        Whether calendar entries of this type make the user
        unavailable for other locking events at the same time.

    .. attribute:: max_conflicting

        How many conflicting events should be tolerated.

    .. attribute:: event_label

        Default text for summary of new entries.
           
           
.. class:: GuestRole
.. class:: Calendar
           
.. class:: Subscription

    A Suscription is when a User subscribes to a Calendar.
    It corresponds to what the extensible CalendarPanel calls "Calendars"
    
    :user: points to the author (recipient) of this subscription
    :other_user:
    

.. class:: Task

    A Task is when a user plans to to something
    (and optionally wants to get reminded about it).

    .. attribute:: state
     
        The state of this Task. one of :class:`TaskStates`.


           
.. class:: EventPolicy

    A **recurrency policy** is a rule used for generating automatic
    calendar entries.

    .. attribute:: event_type

        Generated calendar entries will have this type.

           
.. class:: RecurrentEvent

    A **recurring event** describes a series of recurrent calendar
    entries.
    
    .. attribute:: name

        See :attr:`lino.utils.mldbc.mixins.BabelNamed.name`.
    
    .. attribute:: every_unit

        Inherited from :attr:`RecurrentSet.every_unit
        <lino_xl.lib.cal.models.RecurrentSet.every_unit>`.

    .. attribute:: event_type



    .. attribute:: description


.. class:: UpdateGuests

    Populate or update the list of participants for this entry
    according to the suggestions. 


    Calls :meth:`suggest_guests` to instantiate them.

    - No guests are added when loading from dump

    - The entry must be in a state which allows editing the guests

    - Deletes existing guests in state invited that are no longer
      suggested

           
.. class:: Event

    A **calendar entry** is a lapse of time to be visualized in a
    calendar.

    .. attribute:: start_date
    .. attribute:: start_time
    .. attribute:: end_date
    .. attribute:: end_time

        These four fields define the duration of this entry.
        Only :attr:`start_date` is mandatory.

        If :attr:`end_date` is the same as :attr:`start_date`, then it
        is preferrable to leave it empty.

    .. attribute:: summary

         A one-line descriptive text.

    .. attribute:: description

         A longer descriptive text.

    .. attribute:: user

         The responsible user.

    .. attribute:: assigned_to

        Another user who is expected to take responsibility for this
        entry.

        See :attr:`lino.modlib.users.mixins.Assignable.assigned_to`.

    .. attribute:: event_type

         The type of this entry. Every calendar entry should have this
         field pointing to a given :class:`EventType`, which holds
         extended configurable information about this entry.

    .. attribute:: state

        The state of this entry. The state can change according to
        rules defined by the workflow, that's why we sometimes refer
        to it as the life cycle.

    .. attribute:: transparent

        Indicates that this entry shouldn't prevent other entries at
        the same time.

    .. attribute:: when_html

         Shows the date and time of the entry with a link that opens
         all entries on that day (:class:`EntriesByDay
         <lino_xl.lib.cal.ui.EntriesByDay>`).

         Deprecated because it is usually irritating. Use when_text,
         and users open the detail window as usualy by double-clicking
         on the row. And then they have an action on each entry for
         opening EntriesByDay if they want.

    .. attribute:: show_conflicting

         A :class:`ShowSlaveTable <lino.core.actions.ShowSlaveTable>`
         button which opens the :class:`ConflictingEvents
         <lino_xl.lib.cal.ui.ConflictingEvents>` table for this event.

           
.. class:: Guest

    Represents the fact that a given person is expected to attend to a
    given event.

    TODO: Rename this to "Presence".

    .. attribute:: event

        The calendar event to which this presence applies.

    .. attribute:: partner

        The partner to which this presence applies.

    .. attribute:: role

        The role of this partner in this presence.

    .. attribute:: state

        The state of this presence.

           
.. class:: EventGenerator

    Base class for things that generate a series of events.

    See :ref:`specs.cal.automatic_events`.


    .. attribute:: do_update_events

        See :class:`UpdateEntries`.

    .. method:: get_wanted_auto_events(self, ar)

        Return a tuple of two dicts of "wanted" and "unwanted" events.

        Both dicts map a sequence number to an Event instances.
        `wanted` holds events to be saved,
        `unwanted` holds events to be deleted.

        If an event has been manually moved to another date, all
        subsequent events adapt to the new rythm (except those which
        have themselves been manually modified).
                        
           
.. class:: RecurrenceSet

    Mixin for models that express a set of repeating calendar events.
    See :ref:`specs.cal.automatic_events`.

    .. attribute:: start_date
    .. attribute:: start_time
    .. attribute:: end_date
    .. attribute:: end_time

    .. attribute:: every
    .. attribute:: every_unit
    .. attribute:: max_events

    .. attribute:: monday
    .. attribute:: tuesday
    .. attribute:: wednesday
    .. attribute:: thursday
    .. attribute:: friday
    .. attribute:: saturday
    .. attribute:: sunday


    .. attribute:: weekdays_text

        A virtual field returning the textual formulation of the
        weekdays where the recurrence occurs.
    
        Usage examples see :ref:`book.specs.cal`.

           
.. class:: Reservation

    Base class for :class:`lino_xl.lib.rooms.models.Booking` and
    :class:`lino.modlib.courses.models.Course`.

    Inherits from both :class:`EventGenerator` and :class:`RecurrenceSet`.

    .. attribute:: room
    .. attribute:: max_date

.. class:: Component

    Abstract base class for :class:`Event` and :class:`Task`.

    .. attribute:: auto_type

        Contains the sequence number if this is an automatically
        generated component. Otherwise this field is empty.

        Automatically generated components behave differently at
        certain levels.

           

.. class:: Weekdays
           
    A choicelist with the seven days of a week.


.. data:: WORKDAYS    
           
    The five workdays of the week (Monday to Friday).

.. class:: DurationUnit
           
    Base class for the choices in the :class:`DurationUnits`
    choicelist.

    .. method:: add_duration(unit, orig, value)
    
        Return a date or datetime obtained by adding `value`
        times this `unit` to the specified value `orig`.
        Returns None is `orig` is empty.
        
        This is intended for use as a `curried magic method` of a
        specified list item:


.. class:: DurationUnits
           
    A list of possible values for the
    :attr:`lino_xl.lib.cal.Event.duration_unit` field of a calendar
    entry.


.. class:: Recurrencies
           
    List of possible choices for a 'recurrency' field.

    Note that a recurrency (an item of this choicelist) is also a
    :class:`DurationUnit`.

    .. attribute:: easter

        Repeat events yearly, moving them together with the Easter
        data of that year.

        Lino computes the offset (number of days) between this rule's
        :attr:`start_date` and the Easter date of that year, and
        generates subsequent events so that this offset remains the
        same.

.. class:: AccessClasses


.. class:: UpdateEntries
           
    Generate or update the automatic events controlled by this object.

    This action is installed as
    :attr:`EventGenerator.do_update_events`.

.. class:: UpdateEntriesByEvent

    Update all events of this series.

    This is installed as
    :attr:`update_events <Event.update_events>` on :class:`Event`.

           

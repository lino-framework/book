.. doctest docs/specs/cal.rst
.. _book.specs.cal:

================================
``cal`` : Calendar functionality
================================

.. currentmodule:: lino_xl.lib.cal

The :mod:`lino_xl.lib.cal` adds calendar functionality.

.. contents::
  :local:



.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.adg.settings.demo')
>>> from lino.api.doctest import *



Overview
=========

A **calendar entry** is a lapse of time to be visualized in a calendar.

There are different **types of calendar entries**. The list of *calendar entry
types* is configurable. Every entry has a field :attr:`Event.event_type` which
points to its type. The type of a calendar entry can be used to change
application-specific behaviour and rules. An **appointment** (french
"Rendez-vous", german "Termin") is a calendar entry which supposes that another
person is involved. Appointments are defined by assigning them a calendar entry
type that has the :attr:`EventType.is_appointment` field checked.

Calendar entries can have a **state** which can change according to workflow
rules defined by the application.

A calendar entry can have a list of **guests**. A guest is the fact that a
given person is *expected to attend* or *has been present* at a given calendar
entry. Depending on the context the guests of a calendar entry may be labelled
"guests", "participants", "presences"...

Lino can generate **automatic calendar entries**.  The rules for generating
calendar entries are application-specific.  The application developer does this
by defining one or several *calendar generators*.

The **daily planner** is a table showing an overview of calendar entries on a
given day.  Both the rows and the columns can be configured per application or
locally per site.




Calendar entries
================

A **calendar entry** is a lapse of time to be visualized in a calendar. The
internal model name is :class:`Event` for historical reasons, but users see it
as "Calendar entry".

>>> print(rt.models.cal.Event._meta.verbose_name)
Calendar entry


.. class:: Event

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

        See :attr:`lino.modlib.users.Assignable.assigned_to`.

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
         <lino_xl.lib.cal.EntriesByDay>`).

         Deprecated because it is usually irritating. Use when_text,
         and users open the detail window as usualy by double-clicking
         on the row. And then they have an action on each entry for
         opening EntriesByDay if they want.

    .. attribute:: show_conflicting

         A :class:`ShowSlaveTable <lino.core.actions.ShowSlaveTable>`
         button which opens the :class:`ConflictingEvents
         <lino_xl.lib.cal.ConflictingEvents>` table for this event.

    .. method:: update_guests
                
        Populate or update the list of participants for this calendar
        entry according to the suggestions.

        Calls :meth:`suggest_guests` to instantiate them.

        - No guests are added when loading from dump

        - The entry must be in a state which allows editing the guests

        - Deletes existing guests in state invited that are no longer
          suggested


    .. method:: update_events

        Create or update all other automatic calendar entries of this
        series.
                
    .. method:: show_today

    .. method:: get_conflicting_events(self)
                
        Return a QuerySet of calendar entries that conflict with this one.
        Must work also when called on an unsaved instance.
        May return None to indicate an empty queryset.
        Applications may override this to add specific conditions.
        
    .. method:: has_conflicting_events(self)
                
        Whether this entry has any conflicting entries.
        
        This is roughly equivalent to asking whether
        :meth:`get_conflicting_events()` returns more than 0 events.

        Except when this event's type tolerates more than one events
        at the same time.

    .. method:: suggest_guests(self)
           
        Yield the list of unsaved :class:`Guest` instances to be added
        to this calendar entry.

        This method is called from :meth:`update_guests`.

    .. method:: get_event_summary(self, ar)
                
        How this event should be summarized in contexts where possibly
        another user is looking (i.e. currently in invitations of
        guests, or in the extensible calendar panel).

    .. method:: before_ui_save(self, ar)
       
        Mark the entry as "user modified" by setting a default state.
        This is important because EventGenerators may not modify any
        user-modified Events.

    .. method:: auto_type_changed(self, ar)
       
        Called when the number of this automatically generated entry
        (:attr:`auto_type` ) has changed.

        The default updates the summary.
        

    .. method:: get_calendar(self)
                
        Returns the :class:`Calendar` which contains this entry, or
        None if no subscription is found.
        
        Needed for ext.ensible calendar panel.

        The default implementation returns None.
        Override this if your app uses Calendars.
       
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

Every calendar entry has a given **state** which can change according
to rules defined by the application.

The default list of choices for this field contains the following
values.

.. class:: EntryStates

    The possible states of a calendar entry.
    Stored in the :attr:`state <lino_xl.lib.cal.Event.state>` field.
    
    Every choice is an instance of :class:`EntryState` and has some
    attributes.
    
.. class:: EntryState
           
    .. attribute:: edit_guests
                   
        Whether presences are editable when the entry is in this
        state.
        
    .. attribute:: guest_state

        Force the given guest state for all guests when an entry is
        set to this state and when
        :attr:`EventType.force_guest_states` is True.
        
    .. attribute:: noauto
    .. attribute:: transparent
    .. attribute:: fixed

>>> rt.show(cal.EntryStates)
======= ============ ============ ============= =================== ======== ============= =========
 value   name         text         Button text   Edit participants   Stable   Transparent   No auto
------- ------------ ------------ ------------- ------------------- -------- ------------- ---------
 10      suggested    Suggested    ?             Yes                 No       No            No
 20      draft        Draft        ☐             Yes                 No       No            No
 50      took_place   Took place   ☑             Yes                 Yes      No            No
 70      cancelled    Cancelled    ☒             No                  Yes      Yes           Yes
======= ============ ============ ============= =================== ======== ============= =========
<BLANKLINE>


The type of a calendar entry
============================

The :attr:`type <Event.type>` field of a *calendar entry* points to a database
object which holds certain properties that are common to all entries of that
type.

.. class:: EventType

    Django model representing a *calendar entry type*. The possible value of
    the :attr:`Event.type` field.

    .. attribute:: event_label

        Default text for summary of new entries.
           
    .. attribute:: is_appointment

        Whether entries of this type are considered as "appointments"
        (i.e. whose time and place have been agreed upon with other
        users or external parties).

        Certain tables show only entries whose type has the
        `is_appointment` field checked.  See :attr:`show_appointments
        <Entries.show_appointments>`.

    .. attribute:: max_days

        The maximal number of days allowed as duration.

        See also :class:`LongEntryChecker`

    .. attribute:: locks_user

        Whether calendar entries of this type make the user
        unavailable for other locking events at the same time.

    .. attribute:: max_conflicting

        How many conflicting events should be tolerated.

    .. attribute:: transparent

        Allow entries of this type to conflict with other events.

    .. attribute:: force_guest_states

        Whether guest states should be forced to those defined by the
        entry state.

        This will have an effect only if the application programmer
        has defined a mapping from entry state to the guest state by
        setting :attr:`EntryState.guest_state` for at least one entry
        state.

        :ref:`tera` uses this for individual and family therapies
        where they don't want to manage presences of every
        participant.  When an appointment is set to "Took place", Lino
        sets all guests to "Present".  See :doc:`tera/cal` for a usage
        example.

.. class:: EventTypes

    The list of entry types defined on this site.


The daily planner
=================


.. class:: DailyPlanner

    The virtual table used to render the daily planner.
           
>>> rt.show(cal.DailyPlanner)
============ ========== ===============
 Time range   External   Internal
------------ ---------- ---------------
 *AM*
 *PM*                    *13:30 robin*
 *All day*
============ ========== ===============
<BLANKLINE>


.. >>> dd.today()
   datetime.date(2017, 2, 15)


.. class:: PlannerColumns
           
    A choicelist that defines the columns to appear in the daily
    planner. This list can be modified locally.
    
    
A default configuration has two columns in the daily planner:

>>> rt.show(cal.PlannerColumns)
======= ========== ==========
 value   name       text
------- ---------- ----------
 10      external   External
 20      internal   Internal
======= ========== ==========
<BLANKLINE>


.. class:: DailyPlannerRow
           
    A database object that represents one row of the daily planner.
    The default configuration has "AM", "PM" and "All day".

>>> rt.show(cal.DailyPlannerRows)
===== ============= ================== ================== ============ ==========
 No.   Designation   Designation (de)   Designation (fr)   Start time   End time
----- ------------- ------------------ ------------------ ------------ ----------
 1     AM            Vormittags         Avant-midi                      12:00:00
 2     PM            Nachmittags        Après-midi         12:00:00
 3     All day       Ganztags           Journée entière
===== ============= ================== ================== ============ ==========
<BLANKLINE>


.. Tested translations:

    >>> # settings.SITE.languages

    >>> with translation.override('de'):
    ...     rt.show(cal.DailyPlanner, header_level=1)
    ===========
    Tagesplaner
    ===========
    =============== ======== ===============
     Zeitabschnitt   Extern   Intern
    --------------- -------- ---------------
     *Vormittags*
     *Nachmittags*            *13:30 robin*
     *Ganztags*
    =============== ======== ===============
    <BLANKLINE>
   
    >>> rt.show(cal.DailyPlanner, language="fr", header_level=1)
    =======================
    Planificateur quotidien
    =======================
    =================== ========= ===============
     Time range          Externe   Interne
    ------------------- --------- ---------------
     *Avant-midi*
     *Après-midi*                  *13:30 robin*
     *Journée entière*
    =================== ========= ===============
    <BLANKLINE>

    >>> print(cal.Event.update_guests.help_text)
    Populate or update the list of participants for this calendar
    entry according to the suggestions.

    >>> with translation.override('de'):
    ...     print(str(cal.Event.update_guests.help_text))
    ... #doctest: +NORMALIZE_WHITESPACE +REPORT_CDIFF
    Teilnehmerliste für diesen Kalendereintrag füllen entsprechend der Vorschläge.

    >>> cal.Event.update_guests.help_text.__class__
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
    <class 'django.utils.functional...__proxy__'>


Calendars
=========

Calendar entries can be differentiated into different "calendars".


.. class:: Calendar

    the django model representing a *calendar*.

    .. attribute:: color
   
        The color to use for entries of this calendar (in
        :mod:`lino_xl.lib.extensible`).
   
               
.. class:: Calendars

>>> rt.show(cal.Calendars)
==== ============= ================== ================== ============= =======
 ID   Designation   Designation (de)   Designation (fr)   Description   color
---- ------------- ------------------ ------------------ ------------- -------
 1    General       Allgemein          Général                          1
                                                                        **1**
==== ============= ================== ================== ============= =======
<BLANKLINE>


Note that the default implementation has no "Calendar" field per
calendar entry.  The `Event` model instead has a
:meth:`Event.get_calendar` method.

You might extend Event in your plugin as follows::

    from lino_xl.lib.cal.models import *
    class Event(Event):

        calendar = dd.ForeignKey('cal.Calendar')

        def get_calendar(self):
            return self.calendar

But in other cases it would create unnecessary complexity to add such
a field. For example in :ref:`welfare` there is one calendar per User,
and thus the `get_calendar` method is implemented as follows::

    def get_calendar(self):
        if self.user is not None:
            return self.user.calendar

Or in :ref:`voga` there is one calendar per Room. Thus the
`get_calendar` method is implemented as follows::

    def get_calendar(self):
        if self.room is not None:
            return self.room.calendar


.. _specs.cal.automatic_events:

Automatic calendar entries
==========================

An **event generator** is something that can generate automatic
calendar entries.  Examples of event generators include

- :doc:`Holidays <holidays>`

- A *course*, *workshop* or *activity* as used by Welfare, Voga and
  Avanti (subclasses of :class:`lino_xl.lib.courses.models.Course`).

- A reservation of a room in :ref:`voga`
  (:class:`lino_xl.lib.rooms.Reservation`).

- A coaching contract with a client in :ref:`welfare`
  (:class:`lino_welfare.modlib.isip.Contract` and
  :class:`lino_welfare.modlib.jobs.Contract`)

The main effect of the :class:`EventGenerator`
mixin is to add the :class:`UpdateEntries` action.

The event generator itself does not necessarily also contain all those
fields needed for specifying **which** events should be
generated. These fields are implemented by another mixin named
:class:`RecurrenceSet`. A
recurrence set is something that specifies which calendar events
should get generated.

    

.. class:: EventGenerator

    Base class for things that generate a series of events.

    See :ref:`specs.cal.automatic_events`.


    .. method:: update_all_guests

        Update the presence lists of all calendar events generated by
        this.
    
    .. method:: do_update_events
                
        Create or update the automatic calendar entries controlled by
        this generator.

        This is the :guilabel:` ⚡ ` button.
                
        See :class:`UpdateEntries`.

    .. method:: get_wanted_auto_events(self, ar)

        Return a tuple of two dicts of "wanted" and "unwanted" events.

        Both dicts map a sequence number to an Event instances.
        `wanted` holds events to be saved,
        `unwanted` holds events to be deleted.

        If an event has been manually moved to another date, all
        subsequent events adapt to the new rythm (except those which
        have themselves been manually modified).
                        
    .. method:: care_about_conflicts(self, we)
                
        Whether this event generator should try to resolve conflicts
        (in :meth:`resolve_conflicts`)

    .. method:: resolve_conflicts(self, we, ar, rset, until)
                
        Check whether given entry `we` conflicts with other entries
        and move it to a new date if necessary. Returns (a) the
        entry's :attr:`start_date` if there is no conflict, (b) the
        next available alternative date if the entry conflicts with
        other existing entries and should be moved, or (c) None if
        there are conflicts but no alternative date could be found.

        `ar` is the action request who asks for this.  `rset` is the
        :class:`RecurrenceSet`.

           


.. class:: UpdateEntries
           
    Generate or update the automatic events controlled by this object.

    This action is installed as
    :attr:`EventGenerator.do_update_events`.

.. class:: UpdateEntriesByEvent

    Update all events of this series.

    This is installed as
    :attr:`update_events <Event.update_events>` on :class:`Event`.

      
The generated calendar entries are "controlled" by their generator
(their :attr:`owner <Event.owner>` field points to the generator) and
have a non-empty :attr:`Event.auto_type` field.


Recurrencies
============

The **recurrency** expresses how often something is to be repeated.

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


Adding a duration unit

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
:class:`RecurrentEvent <lino_xl.lib.cal.RecurrentEvent>` used
to generate holidays.  See also :ref:`xl.specs.holidays`.

We are going to use this model for demonstrating some more features
(which it inherits from :class:`RecurrenceSet` and 
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
==== =============== ================== ==================
 ID   Designation     Designation (de)   Designation (fr)
---- --------------- ------------------ ------------------
 4    First contact   First contact      First contact
 1    Holidays        Feiertage          Jours fériés
 3    Internal        Intern             Interne
 5    Lesson          Lesson             Lesson
 2    Meeting         Versammlung        Réunion
==== =============== ================== ==================
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

The demo datebase contains two appointments on Ash Wednesday 2017.
These conflicting calendar events are visible as data problems (see
:doc:`checkdata`).

>>> chk = checkdata.Checkers.get_by_value('cal.ConflictingEventsChecker')
>>> rt.show(checkdata.ProblemsByChecker, chk)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ================================ ====================================================
 Responsible       Database object                  Message
----------------- -------------------------------- ----------------------------------------------------
 Robin Rood        *Ash Wednesday (01.03.2017)*     Event conflicts with Seminar (01.03.2017 08:30).
 Robin Rood        *Rosenmontag (27.02.2017)*       Event conflicts with Rencontre (27.02.2017 11:10).
 Romain Raffault   *Rencontre (27.02.2017 11:10)*   Event conflicts with Rosenmontag (27.02.2017).
 Robin Rood        *Seminar (01.03.2017 08:30)*     Event conflicts with Ash Wednesday (01.03.2017).
================= ================================ ====================================================
<BLANKLINE>



>>> obj = cal.Event.objects.get(id=123)
>>> print(obj)
Ash Wednesday (01.03.2017)

>>> rt.show(cal.ConflictingEvents, obj)
============ ============ ========== ======== ====== ==================
 Start date   Start time   End Time   Client   Room   Responsible user
------------ ------------ ---------- -------- ------ ------------------
 01/03/2017   08:30:00     09:45:00                   Robin Rood
============ ============ ========== ======== ====== ==================
<BLANKLINE>


Transparent events
==================

The entry type "Internal" is marked "transparent".

>>> internal = cal.EventType.objects.get(id=3)
>>> internal.transparent
True


The guests  of a calendar entry
===============================


.. class:: Guest

    TODO: Rename this to "Presence".

    .. attribute:: event

        The calendar event to which this presence applies.

    .. attribute:: partner

        The partner to which this presence applies.

    .. attribute:: role

        The role of this partner in this presence.

    .. attribute:: state

        The state of this presence.  See :class:`GuestStates`.

        
    The following three fields are injected by the
    :mod:`reception <lino_xl.lib.reception>` plugin:

    .. attribute:: waiting_since
                   
        Time when the visitor arrived (checked in).
       
    .. attribute:: busy_since

        Time when the visitor was received by agent.
                   
    .. attribute:: gone_since

        Time when the visitor left (checked out).                   



        


Every participant of a calendar entry can have a "role". For example
in a class meeting you might want to differentiate between the teacher
and the pupils.
        
.. class:: GuestRole
           
    The role of a guest expresses what the partner is going to do there.
    
.. class:: GuestRoles

    Global table of guest roles.
           
.. class:: GuestStates

    Global choicelist of possible guest states.

    Possible values for the state of a participation. The list of
    choices for the :attr:`Guest.state` field.

    The actual content can be redefined by other apps,
    e.g. :mod:`lino_xl.lib.reception`.
    

    >>> rt.show(cal.GuestStates)
    ======= ========= ============ ========= =============
     value   name      Afterwards   text      Button text
    ------- --------- ------------ --------- -------------
     10      invited   No           Invited   ?
     40      present   Yes          Present   ☑
     50      missing   Yes          Missing   ☉
     60      excused   No           Excused   ⚕
    ======= ========= ============ ========= =============
    <BLANKLINE>
           


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

    .. attribute:: name

        The designation of the room. This should (but is not required
        to) be unique.

    
.. class:: Rooms

    List of rooms where calendar events can happen.

.. class:: AllRooms
           

    
.. class:: Subscription

    A Suscription is when a User subscribes to a Calendar.
    It corresponds to what the extensible CalendarPanel calls "Calendars"
    
    :user: points to the author (recipient) of this subscription
    :other_user:
    
.. class:: Subscriptions
.. class:: SubscriptionsByUser
.. class:: SubscriptionsByCalendar

.. class:: Task

    A Task is when a user plans to do something
    (and optionally wants to get reminded about it).

    .. attribute:: priority

        How urgent this task is.

        Choicelist field pointing to :class:`lino_xl.lib.xl.Priorities`.

    .. attribute:: state

        The state of this Task. one of :class:`TaskStates`.

.. class:: TaskStates
        
    Possible values for the state of a :class:`Task`. The list of
    choices for the :attr:`Task.state` field.


.. class:: Tasks

    Global table of all tasks for all users.

.. class:: TasksByUser
           
    Shows the list of tasks for this user.
           
.. class:: MyTasks

    Shows my tasks whose start date is today or in the future.
           
.. class:: EventPolicy

    A **recurrency policy** is a rule used for generating automatic
    calendar entries.

    .. attribute:: event_type

        Generated calendar entries will have this type.

.. class:: EventPolicies

    Global table of all possible recurrencly policies.
           
.. class:: RecurrentEvent

    A **recurring event** describes a series of recurrent calendar
    entries.
    
    .. attribute:: name

        See :attr:`lino.utils.mldbc.mixins.BabelNamed.name`.
    
    .. attribute:: every_unit

        Inherited from :attr:`RecurrentSet.every_unit
        <lino_xl.lib.cal.RecurrentSet.every_unit>`.

    .. attribute:: event_type


    .. attribute:: description

    .. method:: care_about_conflicts(self, we)
                
        Recurrent events don't care about conflicts. A holiday won't move
        just because some other event has been created before on that date.

.. class:: RecurrentEvents

    The list of all recurrent events (:class:`RecurrentEvent`).
    
                

.. class:: UpdateGuests

    See :meth:`Event.update_guests`.

           
.. class:: UpdateAllGuests

    See :meth:`EventGenerator.update_all_guests`.


.. class:: Events
           
    Table which shows all calendar events.

    Filter parameters:

    .. attribute:: show_appointments

        Whether only *appointments* should be shown.  "Yes" means only
        appointments, "No" means no appointments and leaving it to
        blank shows both types of events.

        An appointment is an event whose *event type* has
        :attr:`appointment <EventType.appointment>` checked.


.. class:: ConflictingEvents

    Shows events conflicting with this one (the master).           

.. class:: EntriesByDay
           
    This table is usually labelled "Appointments today". It has no
    "date" column because it shows events of a given date.

    The default filter parameters are set to show only *appointments*.

.. class:: EntriesByRoom
           
    Displays the calendar entries at a given :class:`Room`.
           
.. class:: EntriesByController

    Shows the calendar entries controlled by this database object.

    If the master is an :class:`EventGenerator
    <lino_xl.lib.cal.EventGenerator>`, then this includes
    especially the entries which were automatically generated.

.. class:: EntriesByProject
           
.. class:: OneEvent
           
    Show a single calendar event.
           
.. class:: MyEntries

    Table of appointments for which I am responsible.
           
    Table which shows today's and all future appointments of the
    requesting user.  The default filter parameters are set to show
    only appointments.

.. class:: MyEntriesToday

    Like :class:`MyEntries`, but only today.

.. class:: MyAssignedEvents    
    
    The table of calendar entries which are *assigned* to me.  That
    is, whose :attr:`Event.assigned_to` field refers to the requesting
    user.

    This table also causes a :term:`welcome message` "X events have been
    assigned to you" in case it is not empty.
    
.. class:: OverdueAppointments
           
    Shows **overdue appointments**, i.e. appointments whose date is
    over but who are still in a nonstable state.

    :attr:`show_appointments` is set to "Yes", :attr:`observed_event`
    is set to "Unstable", :attr:`end_date` is set to today.

.. class:: MyOverdueAppointments

    Like OverdueAppointments, but only for myself.
    
          
.. class:: MyUnconfirmedAppointments
           
    Shows my appointments in the near future which are in suggested or
    draft state.

    Appointments before today are not shown.  The parameters
    :attr:`end_date` and :attr:`start_date` can manually be modified
    in the parameters panel.

    The state filter (draft or suggested) cannot be removed.
    
           
.. class:: Guests

    The default table of presences.
           
.. class:: GuestsByEvent
.. class:: GuestsByPartner
.. class:: GuestsByRole
.. class:: MyPresences
           
    Shows all my presences in calendar events, independently of their
    state.

.. class:: MyPendingPresences

    Received invitations waiting for my feedback (accept or reject).

           
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

        Maximum number of calendar entries to generate.
        
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

        Don't generate calendar entries beyond this date.

The days of the week
=====================

.. class:: Weekdays
           
    A choicelist with the seven days of a week.

>>> rt.show(cal.Weekdays)
======= =========== ===========
 value   name        text
------- ----------- -----------
 1       monday      Monday
 2       tuesday     Tuesday
 3       wednesday   Wednesday
 4       thursday    Thursday
 5       friday      Friday
 6       saturday    Saturday
 7       sunday      Sunday
======= =========== ===========
<BLANKLINE>


.. data:: WORKDAYS    
           
    The five workdays of the week (Monday to Friday).


Duration units
==============

The calendar plugin defines :class:`DurationUnits` choicelist, a
site-wide list of **duration units**.  In a default configuration it
has the following values:

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


Duration units can be used for aritmetic operation on durations. For
example:

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
           
    A list of possible values for the :attr:`duration_unit
    <lino_xl.lib.cal.Event.duration_unit`> field of a calendar entry.

Miscellaneous
=============

.. class:: AccessClasses

    The sitewide list of access classes.
           
.. class:: ShowEntriesByDay

    Show all calendar events of the same day.


.. class:: Component

    Model mixin inherited by both :class:`Event` and :class:`Task`.

    .. attribute:: auto_type

        Contains the sequence number if this is an automatically
        generated component. Otherwise this field is empty.

        Automatically generated components behave differently at
        certain levels.


Plugin configuration
====================
    

.. class:: Plugin
    

    .. attribute:: partner_model

        The model to use as the guest of a presence.
        
    .. attribute:: ignore_dates_before
           
        Ignore dates before the given date.  

        Default value is `None`, meaning "no limit".

        Unlike :attr:`hide_events_before
        <lino.modlib.system.SiteConfig.hide_events_before>`
        this is not editable through the web interface.

    .. attribute:: ignore_dates_after
           
        Ignore dates after the given date.  This should never be `None`.
        Default value is 5 years after :meth:`today
        <lino.core.site.Site.today>`.


User roles
==========

Most calendar functionality requires
:class:`lino.modlib.office.roles.OfficeUser`


.. class:: CalendarReader

    Can read public calendar entries. This is a kind of minimal
    calendar functionality which can be given to anonymous users,
    as done e.g. by :ref:`vilma`.
        
.. class:: GuestOperator

    Can see presences and guests of a calendar entry.


Data checkers
=============

.. class:: ConflictingEventsChecker

    Check whether this entry conflicts with other events.

.. class:: ObsoleteEventTypeChecker

    Check whether the type of this calendar entry should be updated.

    This can happen when the configuration has changed and there are
    automatic entries which had been generated using the old
    configuration.

.. class:: LongEntryChecker

    Check for entries which last longer than the maximum number of
    days allowed by their type.

.. class:: EventGuestChecker           

    Check for calendar entries without participants.

    :message:`No participants although N suggestions exist.` --
    This is probably due to some problem in the past, so we repair
    this by adding the suggested guests.




    
.. function:: check_subscription(user, calendar)

    Check whether the given subscription exists. If not, create it.


Don't read on
=============
              
>>> cal.Days
lino_xl.lib.cal.models.Days

>>> print(cal.Days.column_names)
day_number long_date detail_pointer *

>>> cal.Days.get_data_elem('detail_pointer')
lino_xl.lib.cal.models.Days.detail_pointer

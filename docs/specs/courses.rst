.. _specs.courses:

=======================
Activities
=======================

.. to test only this doc:

    $ doctest docs/specs/courses.rst

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *

This document describes the :mod:`lino_xl.lib.courses` plugin.

The internal name "courses" of this plugin and its main model is for
historic reasons. In :ref:`welfare` they are called "workshops", in
:ref:`tera` they are called "therapies". In general we call them
"activities".  In :ref:`voga` they are called courses, journeys or
travels.


See also
:doc:`/specs/voga/courses`,
:doc:`/specs/avanti/courses`.
and
:doc:`/specs/tera/courses`
It is also being used in :ref:`welfare`.


An **activity** is a series of scheduled calendar entries where a
given teacher teaches a given group of participants about a given
topic.

There is a configurable list of **topics**.  Activities are grouped
into **activity lines** (meaning "series").  An activity line is a
series of activities having a same **topic**.

The participants of an activity are stored as **Enrolments**.

.. contents::
  :local:


.. currentmodule:: lino_xl.lib.courses


The ``Course`` model
====================

.. class:: Course

    A Course is a group of pupils that regularily meet with a given
    teacher in a given room to speak about a given subject.

    Every meeting is a *calendar entry*, and the course itself is a
    *calendar entry generator*, i.e. it has functionality for managing
    these meetings.

    The subject of a course is expressed by the :class:`Line`.

    Notes about automatic calendar entry generation:

    - When an automatically generated entry is to be moved to another
      date, e.g. because it falls into a vacation period, then you
      simply change it's date.  Lino will automatically adapt all
      subsequent entries.

    - Marking an automatically generated event as "Cancelled" will not
      create a replacement event.

    .. attribute:: start_date

        The start date of the first meeting to be generated.

    .. attribute:: end_date

        The end date *of the first meeting* to be generated.  Leave
        this field empty if the meetings last less than one day.

    .. attribute:: enrolments_until

    .. attribute:: max_places

        Available places. The maximum number of participants to allow
        in this course.

    .. attribute:: free_places

        Number of free places.

    .. attribute:: requested

        Number of requested places.

    .. attribute:: trying

        Number of trying places.

    .. attribute:: confirmed

        Number of confirmed places.


.. class:: Activities

    Base table for all activities.

.. class:: MyActivities
           
    Show the courses authored by me (i.e. where I am the responsible
    manager).  Compare :class:`MyCoursesGiven`.

.. class:: MyCoursesGiven
           
    Show the courses given by me (i.e. where I am the teacher).
    Compare :class:`MyActivities`.

    This requires the :attr:`partner` field in my user settings to
    point to me as a teacher.

    For users whose :attr:`partner` field is empty, this list shows
    all courses without teacher.

.. class:: CoursesByLine
           
    Show the courses per course line.
    
.. class:: CoursesByTopic
           
    Shows the courses of a given topic.


The ``Enrolment`` model
=======================

.. class:: Enrolment
           
    An **enrolment** is when a given pupil plans to participate in a
    given course.

    .. attribute:: course_area
    .. attribute:: course
    .. attribute:: pupil
    .. attribute:: request_date
    .. attribute:: start_date
    .. attribute:: end_date
    .. attribute:: state

        One of :class:`lino_xl.lib.courses.choicelists.EnrolmentStates`.

    .. attribute:: places
    .. attribute:: option
    .. attribute:: remark
    .. attribute:: confirmation_details
    .. attribute:: pupil_info

        Virtual HtmlBox field showing the name and address of the
        participant.

.. class:: Enrolments
           
    Base class for all tables that show :class:`Enrolment`.

.. class:: AllEnrolments
           
    Show global list of all enrolments.
    
.. class:: PendingRequestedEnrolments
           
    Show all requested enrolments.

.. class:: PendingConfirmedEnrolments
           
    Show all confirmed enrolments.

.. class:: EnrolmentsByPupil
           
    Show all enrolments of a given pupil.
    
.. class:: EnrolmentsByCourse
           
    Show all enrolments of a given course.


The ``Slot`` model
==================

.. class:: Slot
    
The ``Line`` model
==================

.. class:: Line

    An **activity line** (or **series**) groups courses into a
    configurable list of categories.

    We chose the word "line" instead of "series" because it has a
    plural form (not sure whether this idea was so cool).

    .. attribute:: name

        The designation of this activity line as seen by the user
        e.g. when selecting the line.

        One field for every :attr:`language <lino.core.site.Site.language>`.

    .. attribute:: excerpt_title

        The text to print as title in enrolments.

        See also
        :attr:`lino_xl.lib.excerpts.mixins.ExcerptTitle.excerpt_title`.

    .. attribute:: body_template

        The body template to use when printing an activity of this
        line.  Leave empty to use the site's default (defined by
        `body_template` on the
        :class:`lino_xl.lib.excerpts.models.ExcerptType` for
        :class:`Course`)

    .. attribute:: course_area

        Pointer to :class:`CourseAreas`.  This is used only when an
        application defines several variants of
        :class:`EnrolmentsByPupil`.

           
    
Choicelists
===========
        
.. class:: CourseAreas

Actions
=======

.. class:: ConfirmAllEnrolments
    
        


Plugin configuration
====================

.. class:: Plugin

    .. attribute:: teacher_model = 'contacts.Person'
    .. attribute:: pupil_model = 'contacts.Person'
           
    .. attribute:: pupil_name_fields = "pupil__name"

    The value to use as :attr:`quick_search_fields
    <lino.core.model.Model.quick_search_fields>` for
    :class:`Enrolment`. 

    Note that this remains a text string while
    :attr:`quick_search_fields
    <lino.core.model.Model.quick_search_fields>` is resolved into a
    tuple of data elements at site startup.

Presence sheet
==============

The **presence sheet** of a course is a printable document
For example :ref:`voga.presence_sheet`.


.. xfile:: presence_sheet.weasy.html

    The template used for printing a presence sheet of an activity
    (both versions pdf and html)




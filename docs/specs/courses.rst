.. doctest docs/specs/courses.rst
.. _specs.courses:

==============================
``courses`` : Managing courses
==============================

.. currentmodule:: lino_xl.lib.courses

The :mod:`courses <lino_xl.lib.courses>` plugin adds functionality for
managing "courses".


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *


What is a course?
===================

A **course** is when a "teacher" meets more or less regularily with a group of
"pupils".  The pupils can be any model (e.g. a :class:`contacts.Person
<lino_xl.lib.contacts.Person>`).  When a pupil participates in a course, we
create an **enrolment**.

A course can automatically generate calendar entries for the meetings of that
course according to recurrency rules.  It helps with managing these meetings:
schedule exceptions and manual date changes.  It can fill the guests or
participants of the meetings, and the teacher can register their presence.
Courses can be grouped into course lines* (series), series into *topics*.

The internal name "courses" is for historic reasons.  There was a time
when I planned to rename "courses" to "activities".  Some table names
remind this time.  In :ref:`welfare` they are called "workshops", in
:ref:`tera` they are called "dossiers", in :ref:`voga` they are called
"activities".

See also
:doc:`/specs/voga/courses`,
:doc:`/specs/avanti/courses`,
:doc:`/specs/tera/courses`
and :ref:`welfare`.


The ``Course`` model
====================

.. class:: Course

    Database fields:

    .. attribute:: start_date

        The start date of the first meeting to be generated.

    .. attribute:: end_date

        The end date *of the first meeting* to be generated.  Leave
        this field empty if the meetings last less than one day.

    .. attribute:: max_date

        Don't generate meeting having their start date beyond this
        date.

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


           
.. class:: Courses

    Base table for all activities.

    Filter parameters:

    .. attribute:: show_exposed

        Whether to show or to hide courses in an exposed state.

        That is, all courses in a state that has
        :attr:`CourseState.is_exposed` set to True.

        This parameter is ignored if the :attr:`state` parameter is also
        specified.

    .. attribute:: state

         

.. class:: MyCourses
           
    Show the courses authored by me (i.e. where I am the responsible
    manager).  Compare :class:`MyCoursesGiven`.

.. class:: MyCoursesGiven
           
    Show the courses given by me (i.e. where I am the teacher).
    Compare :class:`MyCourses`.

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
           
    Show the enrolments of a this course.


Notes about automatic calendar entry generation:

- When an automatically generated entry is to be moved to another
  date, e.g. because it falls into a vacation period, then you
  simply change its date.  Lino will automatically adapt all
  subsequent entries.

- Marking an automatically generated event as "Cancelled" will not
  create a replacement event.
    


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

           
    
Course areas
============

TODO: rename "course area" to "activity layout"?

The :class:`CourseAreas` choicelist is a place for defining different
layouts of courses.  The area of a course determines how this course
is being show on screen and whether presences of the participants are
being managed or not.

The default configuration contains only one choice:

>>> rt.show(courses.CourseAreas)
======= ========= ============ =================
 value   name      text         Table
------- --------- ------------ -----------------
 C       default   Activities   courses.Courses
======= ========= ============ =================
<BLANKLINE>


Usage examples see :doc:`voga/courses` and :doc:`tera/courses`.

.. class:: CourseAreas
           
    The global choicelist of course areas.  Every choice is an
    instance of :class:`CourseArea`.
        
.. class:: CourseArea

    .. attribute:: courses_table

        Which table to use for showing courses in this course area.
        

The state of a course
=====================

>>> rt.show(courses.CourseStates)
======= ========== ========== ========= ========== ============= =================
 value   name       text       Exposed   Editable   Invoiceable   Update calendar
------- ---------- ---------- --------- ---------- ------------- -----------------
 10      draft      Draft      Yes       Yes        No            No
 20      active     Started    Yes       No         Yes           No
 30      inactive   Inactive   No        No         No            No
 40      closed     Closed     No        No         No            No
======= ========== ========== ========= ========== ============= =================
<BLANKLINE>


.. class:: CourseStates
           
   .. attribute:: draft
   .. attribute:: active
   .. attribute:: inactive
   .. attribute:: closed

               
Every course state has itself some additional attributes that are used
to group them at certain places.
   
.. class:: CourseState

   .. attribute:: is_editable
   .. attribute:: is_exposed
   .. attribute:: is_invoiceable
   .. attribute:: auto_update_calendar

For example you can retrieve a list of course states that are to be
considered "exposed" (:attr:`Courses.show_exposed`):

>>> courses.CourseStates.filter(is_exposed=True)
[<CourseStates.draft:10>, <CourseStates.active:20>]

>>> courses.CourseStates.filter(is_exposed=False)
[<CourseStates.inactive:30>, <CourseStates.closed:40>]

As an application developer you can redefine the items of
:class:`CourseStates` in order to adapt it to the needs of your
application.



TODO: Write a tutorial about redefining choicelists.

               
               

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




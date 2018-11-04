.. doctest docs/specs/tera/courses.rst
.. _tera.specs.courses:

=========
Therapies
=========

This document specifies how the :mod:`lino_xl.lib.courses` plugin is
being used in :ref:`tera`.

Activities in :ref:`tera` are called "therapies". There are individual
therapies, "life groups" (families and similar groups who live
together or have lived together) and "therapeutical groups" (groups of
indipendent clients who share a common interest).


.. contents::
  :local:


.. currentmodule:: lino_tera.lib.courses
                   

.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *

>>> dd.plugins.courses
lino_tera.lib.courses (extends_models=['Enrolment', 'Course', 'Line'])

>>> dd.plugins.courses.__class__.__bases__
(<class 'lino_xl.lib.courses.Plugin'>,)


The detail view of a therapy
============================

>>> print(py2rst(courses.Courses.detail_layout))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
(main) [visible for all]:
- **General** (general):
  - (general_1): **Reference** (ref), **Designation** (name), **Invoice recipient** (partner), **Division** (team)
  - (general_2): **Therapy type** (line), **Manager** (user), **Therapist** (teacher), **Workflow** (workflow_buttons)
  - (enrolments_top): **Default attendance fee** (fee), **Print** (print_actions)
  - **Participants** (EnrolmentsByCourse) [visible for secretary therapist admin]
- **Therapy** (therapy):
  - (therapy_1): **Therapy domain** (therapy_domain), **Procurer** (procurer), **Mandatory** (mandatory), **Translator type** (translator_type)
  - (therapy_2) [visible for therapist admin]: **Interests** (topics_InterestsByController), **Notes** (notes_NotesByProject)
- **Appointments** (calendar):
  - (calendar_1): **Recurrency** (every_unit), **Repeat every** (every), **Generate events until** (max_date), **Number of events** (max_events)
  - (calendar_2): **Room** (room), **Start date** (start_date), **End Date** (end_date), **Start time** (start_time), **End Time** (end_time)
  - (calendar_3): **Monday** (monday), **Tuesday** (tuesday), **Wednesday** (wednesday), **Thursday** (thursday), **Friday** (friday), **Saturday** (saturday), **Sunday** (sunday)
  - **Calendar entries** (courses_EntriesByCourse) [visible for secretary therapist admin]
- **Invoicing** (sales):
  - (sales_1): **Client tariff** (tariff), **Payment term** (payment_term), **Paper type** (paper_type), **ID** (id)
  - (sales_2): **State** (state), **Ending reason** (ending_reason)
  - (sales_3) [visible for secretary therapist admin]:
    - **Invoicings** (invoicing.InvoicingsByInvoiceable) [visible for secretary admin]
    - **Existing excerpts** (excerpts_ExcerptsByProject)
- **More** (more):
  - **Remark** (remark)
  - **Tasks** (cal.TasksByProject) [visible for secretary therapist admin]
<BLANKLINE>


Note in particular that topic interests and notes are not visible to
secretary:

>>> show_permissions(topics.InterestsByPartner)
therapist admin

>>> show_permissions(notes.NotesByProject)
therapist admin




Course lines and course layouts
===============================

The :class:`CourseAreas` choicelist in :ref:`tera` populates
:class:`lino_xl.lib.courses.CourseAreas` with the following course
layouts:

>>> rt.show(courses.CourseAreas)
======= ============= ====================== ====================
 value   name          text                   Table
------- ------------- ---------------------- --------------------
 IT      therapies     Individual therapies   courses.Therapies
 LG      life_groups   Life groups            courses.LifeGroups
 OG      default       Other groups           courses.Courses
======= ============= ====================== ====================
<BLANKLINE>


While in Voga or Avanti we can have many course lines, in Lino Tera
there is only one course line per course layout.

>>> print(courses.Line._meta.verbose_name_plural)
Therapy types

Every course line knows which its layout.

>>> rt.show(courses.Lines)
==================== ====================== ================== ================== ======= ====================== ======================== ===================== ============ ==============
 Reference            Designation            Designation (de)   Designation (fr)   Topic   Layout                 Service type             Manage presences as   Recurrency   Repeat every
-------------------- ---------------------- ------------------ ------------------ ------- ---------------------- ------------------------ --------------------- ------------ --------------
                      Individual therapies                                                 Individual therapies   Individual appointment   Attendee              weekly       1
                      Life groups                                                          Life groups            Individual appointment   Attendee              weekly       1
                      Other groups                                                         Other groups           Group meeting            Attendee              weekly       1
 **Total (3 rows)**                                                                                                                                                           **3**
==================== ====================== ================== ================== ======= ====================== ======================== ===================== ============ ==============
<BLANKLINE>

Some course tables have a fixed course layout, some don't.

>>> courses.LifeGroups._course_area
<CourseAreas.life_groups:LG>

>>> print(courses.AllActivities._course_area)
None

When you are in a table with a fixed layout, your choices for the
:attr:`Course.line` field are limited to lines of that layout.


>>> show_choices("robin", "/choices/courses/LifeGroups/line")
<br/>
Life groups

>>> show_choices("robin", "/choices/courses/AllActivities/line")
<br/>
Individual therapies
Life groups
Other groups

Furthermore, when you are in a table with a fixed layout *and there is
only one line object having that layout*, Lino fills the line field
automatically when creating a new course.


>>> fld = courses.Course._meta.get_field('line')
>>> print(fld.verbose_name)
Therapy type

>>> fld.blank
False

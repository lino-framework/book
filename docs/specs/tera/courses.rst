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
  - (general_2): **Patient** (client), **Household** (household), **Organization** (company)
  - (general_3): **Therapy domain** (therapy_domain), **Procurer** (procurer), **Mandatory** (mandatory), **Translator type** (translator_type)
  - (general_4): **Therapy type** (line), **Manager** (user), **Therapist** (teacher), **Workflow** (workflow_buttons)
  - (general_5) [visible for therapist admin]: **Interests** (topics_InterestsByController), **Notes** (notes_NotesByProject)
- **Participants** (enrolments):
  - (enrolments_top): **Enrolments until** (enrolments_until), **Print** (print_actions)
  - **Participants** (EnrolmentsByCourse) [visible for secretary therapist admin]
- **Appointments** (calendar):
  - (calendar_1): **Recurrency** (every_unit), **Repeat every** (every), **Generate events until** (max_date), **Number of events** (max_events)
  - (calendar_2): **Room** (room), **Start date** (start_date), **End Date** (end_date), **Start time** (start_time), **End Time** (end_time)
  - (calendar_3): **Monday** (monday), **Tuesday** (tuesday), **Wednesday** (wednesday), **Thursday** (thursday), **Friday** (friday), **Saturday** (saturday), **Sunday** (sunday)
  - **Calendar entries** (courses_EntriesByCourse) [visible for secretary therapist admin]
- **Notes** (notes):
  - **Remark** (remark)
  - **Tasks** (cal.TasksByProject) [visible for secretary therapist admin]
- **More** (more):
  - (more_1): **Client tariff** (tariff), **Payment term** (payment_term), **Paper type** (paper_type), **ID** (id)
  - (more_2): **State** (state), **Ending reason** (ending_reason)
  - (more_3) [visible for secretary therapist admin]:
    - **Invoicings** (invoicing.InvoicingsByInvoiceable) [visible for secretary admin]
    - **Existing excerpts** (excerpts_ExcerptsByProject)
<BLANKLINE>

Note in particular that topic interests and notes are not visible to
secretary:

>>> show_permissions(topics.InterestsByPartner)
therapist admin

>>> show_permissions(notes.NotesByProject)
therapist admin



Course areas
============

Presences are not managed only for normal group therapies, but for
individual therapies and life groups.  This is implemented using the
:attr:`force_guest_states
<lino_xl.lib.courses.CourseArea.force_guest_states>` attribute of
their activity area (which is given by the activity line).


The :class:`CourseAreas` choicelist in :ref:`tera` populates
:class:`lino_xl.lib.courses.CourseAreas` with the following areas:

>>> rt.show(courses.CourseAreas)
======= ============= ====================== ====================
 value   name          text                   Table
------- ------------- ---------------------- --------------------
 IT      therapies     Individual therapies   courses.Therapies
 LG      life_groups   Life groups            courses.LifeGroups
 OG      default       Other groups           courses.Courses
======= ============= ====================== ====================
<BLANKLINE>


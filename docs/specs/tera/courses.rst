.. doctest docs/specs/tera/courses.rst
.. _tera.specs.courses:

=======================
Activities in Lino Tera
=======================

This document specifies how the :mod:`lino_xl.lib.courses` plugin is
being used in :ref:`tera`.

Activities in :ref:`tera` are called "therapies". There are individual
therapies, "life groups" (families and similar groups who live
together or have lived together) and "therapeutical groups" (groups of
indipendent clients who share a common interest).


.. contents::
  :local:



.. currentmodule:: lino_tera.lib.courses
                   

Implementation
==============

Examples in this document use the :mod:`lino_book.projects.lydia` demo
project.

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *

>>> dd.plugins.courses
lino_tera.lib.courses (extends_models=['Enrolment', 'Course', 'Line'])

>>> dd.plugins.courses.__class__.__bases__
(<class 'lino_xl.lib.courses.Plugin'>,)
    

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


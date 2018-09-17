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

The :class:`CourseAreas` choicelist in :ref:`tera` defines the
following areas:

>>> rt.show(courses.CourseAreas)
======= ============= ====================== ==================== ==================
 value   name          text                   Table                Manage presences
------- ------------- ---------------------- -------------------- ------------------
 10      therapies     Individual therapies   courses.Therapies    No
 20      life_groups   Life groups            courses.LifeGroups   No
 30      default       Other groups           courses.Courses      Yes
======= ============= ====================== ==================== ==================
<BLANKLINE>
        

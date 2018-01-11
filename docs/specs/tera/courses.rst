.. _tera.specs.courses:

=======================
Activities in Lino Tera
=======================

.. to test only this doc:

    $ doctest docs/specs/tera/courses.rst

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *

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

>>> dd.plugins.courses
lino_tera.lib.courses (extends_models=['Enrolment', 'Course', 'Line'])

>>> dd.plugins.courses.__class__.__bases__
(<class 'lino_xl.lib.courses.Plugin'>,)
    


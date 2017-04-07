.. _avanti.specs.courses:

======================
Courses in Lino Avanti
======================

.. How to test just this document:

    $ python setup.py test -s tests.SpecsTests.test_avanti_courses
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *


.. contents::
  :local:
     

Who can modify courses
======================

Note the difference between the *instructor* of a course and the *author*.

The author can *modify* dates and enrol new participants.  The teacher
can just enter presences and absences for existing participants in
existing events.

>>> rt.show('courses.AllActivities')
================= ============ =============== ========== =========== =============
 Activity line     Start date   Instructor      Author     When        Times
----------------- ------------ --------------- ---------- ----------- -------------
 Alphabetisation   26/01/2017   Laura Lieblig   nathalie   Every day   14:00-17:00
 Alphabetisation   26/01/2017   Laura Lieblig   martina    Every day   09:00-12:00
================= ============ =============== ========== =========== =============
<BLANKLINE>


>>> rt.login('laura').show('courses.MyCoursesGiven')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
============================================================= =========== ============= ====== ===========
 overview                                                      When        Times         Room   Actions
------------------------------------------------------------- ----------- ------------- ------ -----------
 `Alphabetisation (26/01/2017) <Detail>`__ / *Laura Lieblig*   Every day   14:00-17:00          **Draft**
 `Alphabetisation (26/01/2017) <Detail>`__ / *Laura Lieblig*   Every day   09:00-12:00          **Draft**
============================================================= =========== ============= ====== ===========
<BLANKLINE>


Note that even though Nathalie is author of the morning course, it is
Laura (the teacher) who is responsible for the individual events.


>>> rt.login('laura').show('cal.MyEntries')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
=========================================== ======== =================================
 overview                                    Client   Actions
------------------------------------------- -------- ---------------------------------
 `Lesson 13 (16.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 13 (16.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 14 (17.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 14 (17.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 15 (20.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 15 (20.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 16 (21.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 16 (21.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 17 (23.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 17 (23.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 18 (24.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 18 (24.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
=========================================== ======== =================================
<BLANKLINE>

Names of participants
=====================

The names of the participants are confidential data in :ref:`avanti`.

System admins can see the full names:

>>> obj = courses.Course.objects.get(pk=1)
>>> rt.login('rolf').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==================== ======================= ============= ======== ==================================================
 Date of request      Client                  Places used   Remark   Actions
-------------------- ----------------------- ------------- -------- --------------------------------------------------
 07/02/2017           ABDI Aatifa (136)       1                      **Requested** → [Confirm] [Cancelled] [Trying]
 09/02/2017           ABDELNOUR Aamir (125)   1                      **Confirmed** → [Cancelled] [Requested] [Trying]
 11/02/2017           ABDALLAH Aaish (127)    1                      **Requested** → [Confirm] [Cancelled] [Trying]
 13/02/2017           ABBASI Aaisha (118)     1                      **Confirmed** → [Cancelled] [Requested] [Trying]
 15/02/2017           ABAD Aabdeen (114)      1                      **Requested** → [Confirm] [Cancelled] [Trying]
 **Total (5 rows)**                           **5**
==================== ======================= ============= ======== ==================================================
<BLANKLINE>

But auditors and coordinators see only the first name and number:

>>> rt.login('martina').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==================== ========================== ============= ======== ================================================
 Date of request      Client                     Places used   Remark   Actions
-------------------- -------------------------- ------------- -------- ------------------------------------------------
 07/02/2017           Aatifa (136) from Eupen    1                      **Requested**
 09/02/2017           Aamir (125) from Eupen     1                      **Confirmed**
 11/02/2017           Aaish (127) from Eupen     1                      **Requested** → [Confirm] [Cancelled] [Trying]
 13/02/2017           Aaisha (118) from Eupen    1                      **Confirmed**
 15/02/2017           Aabdeen (114) from Eupen   1                      **Requested**
 **Total (5 rows)**                              **5**
==================== ========================== ============= ======== ================================================
<BLANKLINE>


Note that teachers *can* see the full names because they must register
presences and absences:

>>> rt.login('laura').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==================== ======================= ============= ======== ==================================================
 Date of request      Client                  Places used   Remark   Actions
-------------------- ----------------------- ------------- -------- --------------------------------------------------
 07/02/2017           ABDI Aatifa (136)       1                      **Requested**
 09/02/2017           ABDELNOUR Aamir (125)   1                      **Confirmed** → [Cancelled] [Requested] [Trying]
 11/02/2017           ABDALLAH Aaish (127)    1                      **Requested**
 13/02/2017           ABBASI Aaisha (118)     1                      **Confirmed**
 15/02/2017           ABAD Aabdeen (114)      1                      **Requested** → [Confirm] [Cancelled] [Trying]
 **Total (5 rows)**                           **5**
==================== ======================= ============= ======== ==================================================
<BLANKLINE>


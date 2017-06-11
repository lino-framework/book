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
================= ======================= ======== ======== ==================================================
 Date of request   Client                  Gender   Remark   Actions
----------------- ----------------------- -------- -------- --------------------------------------------------
 07/02/2017        ABDI Aátifá (136)       Female            **Requested** → [Confirm] [Cancelled] [Trying]
 09/02/2017        ABDELNOUR Aámir (125)   Male              **Confirmed** → [Cancelled] [Requested] [Trying]
 11/02/2017        ABDALLAH Aáish (127)    Male              **Requested** → [Confirm] [Cancelled] [Trying]
 13/02/2017        ABBASI Aáishá (118)     Female            **Confirmed** → [Cancelled] [Requested] [Trying]
 15/02/2017        ABAD Aábdeen (114)      Male              **Requested** → [Confirm] [Cancelled] [Trying]
================= ======================= ======== ======== ==================================================
<BLANKLINE>

But auditors and coordinators see only the first name and number:

>>> rt.login('martina').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ========================== ======== ======== ================================================
 Date of request   Client                     Gender   Remark   Actions
----------------- -------------------------- -------- -------- ------------------------------------------------
 07/02/2017        Aátifá (136) from Eupen    Female            **Requested**
 09/02/2017        Aámir (125) from Eupen     Male              **Confirmed**
 11/02/2017        Aáish (127) from Eupen     Male              **Requested** → [Confirm] [Cancelled] [Trying]
 13/02/2017        Aáishá (118) from Eupen    Female            **Confirmed**
 15/02/2017        Aábdeen (114) from Eupen   Male              **Requested**
================= ========================== ======== ======== ================================================
<BLANKLINE>


Note that teachers *can* see the full names. They need it because they
must register presences and absences:

>>> rt.login('laura').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ======================= ======== ======== ==================================================
 Date of request   Client                  Gender   Remark   Actions
----------------- ----------------------- -------- -------- --------------------------------------------------
 07/02/2017        ABDI Aátifá (136)       Female            **Requested**
 09/02/2017        ABDELNOUR Aámir (125)   Male              **Confirmed** → [Cancelled] [Requested] [Trying]
 11/02/2017        ABDALLAH Aáish (127)    Male              **Requested**
 13/02/2017        ABBASI Aáishá (118)     Female            **Confirmed**
 15/02/2017        ABAD Aábdeen (114)      Male              **Requested** → [Confirm] [Cancelled] [Trying]
================= ======================= ======== ======== ==================================================
<BLANKLINE>


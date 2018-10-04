.. doctest docs/specs/avanti/courses.rst
.. _avanti.specs.courses:

======================
Courses in Lino Avanti
======================

This document specifies how the :mod:`lino_xl.lib.courses` plugin is
being used in :ref:`avanti`.

.. contents::
   :depth: 1
   :local:


Examples in this document use the :mod:`lino_book.projects.adg` demo
project.

>>> import lino
>>> lino.startup('lino_book.projects.adg.settings.doctests')
>>> from lino.api.doctest import *


Dependencies
============

The methods for managing courses and enrolments in Lino Avanti is
implemented by the :mod:`lino_avanti.lib.courses` plugin which extends
:mod:`lino_xl.lib.courses`.

.. currentmodule:: lino_avanti.lib.courses

     
Topics
======

>>> rt.show('courses.Topics')
==== ================== ================== ==================
 ID   Designation        Designation (de)   Designation (fr)
---- ------------------ ------------------ ------------------
 1    Citizen course     Citizen course     Citizen course
 2    Language courses   Language courses   Language courses
==== ================== ================== ==================
<BLANKLINE>

>>> language_courses = courses.Topic.objects.get(pk=2)
>>> rt.show('courses.CoursesByTopic', language_courses)
================================================== =========== ============= ================== =========== ============= =========== ========
 overview                                           When        Times         Available places   Confirmed   Free places   Requested   Trying
-------------------------------------------------- ----------- ------------- ------------------ ----------- ------------- ----------- --------
 *Alphabetisation (16/01/2017)* / *Laura Lieblig*   Every day   09:00-12:00   5                  2           3             3           0
 *Alphabetisation (16/01/2017)* / *Laura Lieblig*   Every day   14:00-17:00   5                  0           2             0           3
 **Total (2 rows)**                                                           **10**             **2**       **5**         **3**       **3**
================================================== =========== ============= ================== =========== ============= =========== ========
<BLANKLINE>

Note that :class:`CoursesByTopic <lino_xl.lib.courses.CoursesByTopic>`
is a table with a remote master key:

>>> courses.CoursesByTopic.master
<class 'lino_xl.lib.courses.models.Topic'>
>>> print(courses.CoursesByTopic.master_key)
line__topic


>>> rt.show('courses.LinesByTopic', language_courses)
==================== ====================== ====================== ====================== ================== ============ ===================== ===================== ============ ==============
 Reference            Designation            Designation (de)       Designation (fr)       Topic              Layout       Calendar entry type   Manage presences as   Recurrency   Repeat every
-------------------- ---------------------- ---------------------- ---------------------- ------------------ ------------ --------------------- --------------------- ------------ --------------
                      Alphabetisation        Alphabetisation        Alphabetisation        Language courses   Activities   Lesson                Pupil                 weekly       1
                      German A1+             German A1+             German A1+             Language courses   Activities   Lesson                Pupil                 weekly       1
                      German A2              German A2              German A2              Language courses   Activities   Lesson                Pupil                 weekly       1
                      German A2 (women)      German A2 (women)      German A2 (women)      Language courses   Activities   Lesson                Pupil                 weekly       1
                      German for beginners   German for beginners   German for beginners   Language courses   Activities   Lesson                Pupil                 weekly       1
 **Total (5 rows)**                                                                                                                                                                 **5**
==================== ====================== ====================== ====================== ================== ============ ===================== ===================== ============ ==============
<BLANKLINE>



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
 Alphabetisation   16/01/2017   Laura Lieblig   nathalie   Every day   14:00-17:00
 Alphabetisation   16/01/2017   Laura Lieblig   martina    Every day   09:00-12:00
================= ============ =============== ========== =========== =============
<BLANKLINE>


>>> rt.login('laura').show('courses.MyCoursesGiven')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
============================================================= =========== ============= ====== ===========
 overview                                                      When        Times         Room   Workflow
------------------------------------------------------------- ----------- ------------- ------ -----------
 `Alphabetisation (16/01/2017) <Detail>`__ / *Laura Lieblig*   Every day   14:00-17:00          **Draft**
 `Alphabetisation (16/01/2017) <Detail>`__ / *Laura Lieblig*   Every day   09:00-12:00          **Draft**
============================================================= =========== ============= ====== ===========
<BLANKLINE>

Calendar entries generated by a course
======================================

Teachers can of course also see the list of calendar entries for a
course.

>>> obj = courses.Course.objects.get(pk=1)
>>> rt.login('laura').show('cal.EntriesByController', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
January 2017: `Mon 16. <Detail>`__☑ `Tue 17. <Detail>`__☑ `Thu 19. <Detail>`__☒ `Fri 20. <Detail>`__☑ `Mon 23. <Detail>`__☑ `Tue 24. <Detail>`__☑ `Thu 26. <Detail>`__☑ `Fri 27. <Detail>`__☑ `Mon 30. <Detail>`__☑ `Tue 31. <Detail>`__☑
February 2017: `Thu 02. <Detail>`__☑ `Fri 03. <Detail>`__☒ `Mon 06. <Detail>`__☑ `Tue 07. <Detail>`__☑ `Thu 09. <Detail>`__? `Fri 10. <Detail>`__? `Mon 13. <Detail>`__? `Tue 14. <Detail>`__? `Thu 16. <Detail>`__? `Fri 17. <Detail>`__? `Mon 20. <Detail>`__? `Tue 21. <Detail>`__? `Thu 23. <Detail>`__? `Fri 24. <Detail>`__?
Suggested : 10 ,  Draft : 0 ,  Took place : 12 ,  Cancelled : 2 **New**



Note that even though Nathalie is author of the morning course, it is
Laura (the teacher) who is responsible for the individual events.


>>> rt.login('laura').show('cal.MyEntries')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
=========================================== ======== =================================
 overview                                    Client   Workflow
------------------------------------------- -------- ---------------------------------
 `Lesson 19 (16.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 19 (16.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 20 (17.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 20 (17.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 21 (20.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 21 (20.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 22 (21.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 22 (21.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 23 (23.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 23 (23.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 24 (24.02.2017 09:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
 `Lesson 24 (24.02.2017 14:00) <Detail>`__            [▽] **Suggested** → [?] [☑] [☒]
=========================================== ======== =================================
<BLANKLINE>

Reference
=========


Models and views
----------------

.. class:: Course
           
    Same as :class:`lino_xl.lib.courses.Course`.

    .. show_fields(courses.Course)    

.. class:: Enrolment

    Inherits from :class:`lino_xl.lib.courses.Enrolment` but adds four
    specific "enrolment options":
           
    .. attribute:: needs_childcare

        Whether this pupil has small children to care about.

    .. attribute:: needs_bus

        Whether this pupil needs public transportation for moving.

    .. attribute:: needs_school

        Whether this pupil has school children to care about.

    .. attribute:: needs_evening

        Whether this pupil is available only for evening courses.


.. class:: PresencesByEnrolment

    Shows the presences of this pupil for this course.
    
.. class:: EnrolmentsByCourse
           
    Same as :class:`lino_xl.lib.courses.EnrolmentsByCourse` but adds
    the gender of the pupil (a remote field) and the enrolment
    options.

.. class:: Reminder

    A **reminder** is when a coaching worker sends a written letter to
    a client reminding him or her that they have a problme with their
    presences.
    
.. class:: Reminders

    The table of all reminders.
   
.. class:: RemindersByPupil

    Shows all reminders that have been issued for this pupil.
    
    This is an example of :ref:`remote_master`.


.. class:: ReminderStates

    The list of possible states of a reminder.

    >>> rt.show(courses.ReminderStates)
    ======= =========== =========== =============
     value   name        text        Button text
    ------- ----------- ----------- -------------
     10      draft       Draft
     20      sent        Sent
     30      ok          OK
     40      final       Final
     90      cancelled   Cancelled
    ======= =========== =========== =============
    <BLANKLINE>
           
    
.. class:: EnrolmentChecker
           
    Checks for the following data problems:

    - :message:`More than 2 times absent.`

    - :message:`Missed more than 10% of meetings.`


Templates
---------

.. xfile:: courses/Enrolment/Default.odt

   Prints an "Integration Course Agreement".
   
.. xfile:: courses/Reminder/Default.odt
           
   Prints a reminder to be sent to the client.


Help texts
==========

Test whether the help texts have been loaded and translated correctly:

>>> fld = courses.EnrolmentsByCourse.model._meta.get_field('needs_childcare')
>>> print(fld.help_text)
Whether this pupil has small children to care about.

Test whether translations of help texts are working correctly:

>>> from django.utils import translation
>>> with translation.override('de'):
...     print(fld.help_text)
Ob dieser Teilnehmer Kleinkinder zu betreuen hat.



Presence sheet
==============


>>> from unipath import Path
>>> url = '/api/courses/Activities/2?'
>>> url += 'fv=01.02.2017&fv=28.02.2017&fv=false&fv=true&'
>>> url += 'an=print_presence_sheet_html&sr=2'
>>> test_client.force_login(rt.login('robin').user)

>>> res = test_client.get(url)  #doctest: +ELLIPSIS
weasy2html render <django.template.backends.jinja2.Template object at ...> -> .../cache/weasy2html/courses.Course-2.html ('en', {})

>>> res.status_code
200
>>> rv = AttrDict(json.loads(res.content.decode()))
>>> url = rv.open_url
>>> print(url)
/media/cache/weasy2html/courses.Course-2.html
>>> url = url[1:]
>>> # print(url)
>>> fn = Path(settings.SITE.cache_dir, Path(url))
>>> html = open(fn).read()
>>> soup = BeautifulSoup(html, "lxml")
>>> links = soup.find_all('a')
>>> len(links)
0

Number of rows:

>>> len(soup.find_all('tr'))
13

Number of columns:

>>> len(soup.find('tr').find_all('td'))
17

Total number of cells is 13*17:

>>> cells = soup.find_all('td')
>>> len(cells)
221

>>> cells[0]
<td>No.</td>
>>> cells[1]
<td>Participant</td>
>>> print(cells[3].decode())  #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
<td>02.02.
<BLANKLINE>
<br/><font size="1">11 (☑)</font>
</td>

>>> cells[17]
<td>1</td>

>>> print(cells[18].decode())
<td><p>Mr Aásim Abdo</p></td>

>>> print(cells[20].decode())  #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
<td align="center" valign="middle">☑
</td>



Course areas
============

The :class:`CourseAreas` choicelist in :ref:`avanti` defines only one
areas.

>>> rt.show(courses.CourseAreas)
======= ========= ============ =================
 value   name      text         Table
------- --------- ------------ -----------------
 C       default   Activities   courses.Courses
======= ========= ============ =================
<BLANKLINE>


Missing rates
=============

.. class:: Course

     .. method:: update_missing_rates(self)
                 
        Calculate the missing rates for al enrolments of this course.

        This action is automatically performed for all courses once per
        day in the evening.

.. _avanti.specs.courses:

======================
Courses in Lino Avanti
======================

..  $ doctest docs/specs/avanti/courses.rst

    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *


.. contents::
   :depth: 1
   :local:

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
1: `16.01.☑ <Detail>`__ 2: `17.01.☑ <Detail>`__ 3: `19.01.☒ <Detail>`__ 4: `20.01.☑ <Detail>`__ 5: `23.01.☑ <Detail>`__ 6: `24.01.☑ <Detail>`__ 7: `26.01.☑ <Detail>`__ 8: `27.01.☑ <Detail>`__ 9: `30.01.☑ <Detail>`__ 10: `31.01.☑ <Detail>`__ 11: `02.02.☑ <Detail>`__ 12: `03.02.☒ <Detail>`__ 13: `06.02.☑ <Detail>`__ 14: `07.02.☑ <Detail>`__ 15: `09.02.? <Detail>`__ 16: `10.02.? <Detail>`__ 17: `13.02.? <Detail>`__ 18: `14.02.? <Detail>`__ 19: `16.02.? <Detail>`__ 20: `17.02.? <Detail>`__ 21: `20.02.? <Detail>`__ 22: `21.02.? <Detail>`__ 23: `23.02.? <Detail>`__ 24: `24.02.? <Detail>`__Suggested : 10 ,  Draft : 0 ,  Took place : 12 ,  Cancelled : 2 **New**


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
    ======= =========== ===========
     value   name        text
    ------- ----------- -----------
     10      draft       Draft
     20      sent        Sent
     30      ok          OK
     40      final       Final
     90      cancelled   Cancelled
    ======= =========== ===========
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
>>> print(repr(cells[3]))
<td>02.02.\n\n<br/><font size="1">11 (\u2611)</font>\n</td>

>>> cells[17]
<td>1</td>

>>> cells[18]
<td><p>Mr A\xe1sim Abdo</p></td>

>>> print(repr(cells[20]))
<td align="center" valign="middle">\u2611\n  </td>


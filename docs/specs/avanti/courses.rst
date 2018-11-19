.. doctest docs/specs/avanti/courses.rst
.. _avanti.specs.courses:

=========================
Activities in Lino Avanti
=========================

This document specifies how activities are being used in
:ref:`avanti`.

.. contents::
   :depth: 1
   :local:

.. include:: /include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.adg.settings.doctests')
>>> from lino.api.doctest import *


The methods for managing courses and enrolments in Lino Avanti is
implemented by the :mod:`lino_avanti.lib.courses` plugin which extends
:mod:`lino_xl.lib.courses`.

.. currentmodule:: lino_avanti.lib.courses

Activities
==========

.. class:: Course
           
    Same as :class:`lino_xl.lib.courses.Course`.


Enrolments
==========

.. class:: EnrolmentsByCourse
           
    Same as :class:`lino_xl.lib.courses.EnrolmentsByCourse` but adds
    the gender of the pupil (a remote field) and the enrolment
    options.

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

    .. attribute:: missing_rate

        How many times the pupil was missing when a lesson took
        place. In percent.


.. class:: PresencesByEnrolment

    Shows the presences of this pupil for this course.
    
     
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
 Description                                        When        Times         Available places   Confirmed   Free places   Requested   Trying
-------------------------------------------------- ----------- ------------- ------------------ ----------- ------------- ----------- --------
 *Alphabetisation (16/01/2017)* / *Laura Lieblig*   Every day   09:00-12:00   5                  3           0             3           2
 *Alphabetisation (16/01/2017)* / *Laura Lieblig*   Every day   14:00-17:00   15                 2           0             4           13
 *Alphabetisation (16/01/2017)* / *Laura Lieblig*   Every day   18:00-20:00   15                 12          0             11          3
 **Total (3 rows)**                                                           **35**             **17**      **0**         **18**      **18**
================================================== =========== ============= ================== =========== ============= =========== ========
<BLANKLINE>


API note: :class:`CoursesByTopic <lino_xl.lib.courses.CoursesByTopic>`
is a table with a remote master key:

>>> courses.CoursesByTopic.master
<class 'lino_xl.lib.courses.models.Topic'>
>>> print(courses.CoursesByTopic.master_key)
line__topic


Course lines
============


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



Instructor versus author
========================

Note the difference between the *instructor* of a course and the *author*.

The author can *modify* dates and enrol new participants.  The teacher
can just enter presences and absences for existing participants in
existing events.

>>> rt.show('courses.AllActivities')
================= ============ =============== ========== =========== =============
 Activity line     Start date   Instructor      Author     When        Times
----------------- ------------ --------------- ---------- ----------- -------------
 Alphabetisation   16/01/2017   Laura Lieblig   sandra     Every day   18:00-20:00
 Alphabetisation   16/01/2017   Laura Lieblig   nathalie   Every day   14:00-17:00
 Alphabetisation   16/01/2017   Laura Lieblig   martina    Every day   09:00-12:00
================= ============ =============== ========== =========== =============
<BLANKLINE>


>>> rt.login('laura').show('courses.MyCoursesGiven')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
============ ============================================================= =========== ============= ====== =============
 Start date   Description                                                   When        Times         Room   Workflow
------------ ------------------------------------------------------------- ----------- ------------- ------ -------------
 16/01/2017   `Alphabetisation (16/01/2017) <Detail>`__ / *Laura Lieblig*   Every day   09:00-12:00          **Started**
 16/01/2017   `Alphabetisation (16/01/2017) <Detail>`__ / *Laura Lieblig*   Every day   14:00-17:00          **Started**
 16/01/2017   `Alphabetisation (16/01/2017) <Detail>`__ / *Laura Lieblig*   Every day   18:00-20:00          **Started**
============ ============================================================= =========== ============= ====== =============
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
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF +ELLIPSIS
=========================================== ======== ===================================
 Description                                 Client   Workflow
------------------------------------------- -------- -----------------------------------
 `Lesson 19 (16.02.2017 09:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
 `Lesson 19 (16.02.2017 14:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
 `Lesson 19 (16.02.2017 18:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
 `Lesson 20 (17.02.2017 09:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
 ...
 `Lesson 23 (23.02.2017 18:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
 `Lesson 24 (24.02.2017 09:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
 `Lesson 24 (24.02.2017 14:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
 `Lesson 24 (24.02.2017 18:00) <Detail>`__            [▽] **? Suggested** → [☐] [☑] [☒]
=========================================== ======== ===================================
<BLANKLINE>




Reminders
=========

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
29

Number of columns:

>>> len(soup.find('tr').find_all('td'))
17

Total number of cells is 13*17:

>>> cells = soup.find_all('td')
>>> len(cells)
493

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
<td><p>Mr Armán Berndt</p></td>

>>> print(cells[20].decode())  #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
<td align="center" valign="middle">⚕
  </td>



Course layouts
==============

The :class:`CourseAreas` choicelist in :ref:`avanti` defines only one
layout.

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

     Adds an action to update the missing rates of all enrolments.

     .. method:: update_missing_rates(self)
                 
        Calculate the missing rates for all enrolments of this course.

        This action is automatically performed for all courses once
        per day in the evening.  Users can run it manually by clicking
        the ☉ button on a course.
        
        >>> print(courses.Course.update_missing_rates.button_text)
         ☉ 
                 
        >>> print(courses.Course.update_missing_rates.label)
        Update missing rates
        
        >>> print(courses.Course.update_missing_rates.help_text)
        Calculate the missing rates for all enrolments of this course.



.. class:: DitchingEnrolments

     List of enrolments with high absence rate for review by their
     coach.

>>> with translation.override("de"):
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
...    print(str(courses.DitchingEnrolments.label))
...    print(str(courses.DitchingEnrolments.help_text))
Abwesenheitskontrolle
Liste der Einschreibungen mit hoher Abwesenheitsrate zwecks Kontrolle durch den Begleiter.

>>> rt.login("romain").show(courses.DitchingEnrolments)
============== ========================== ============================== =================
 Missing rate   Client                     Activity                       Primary coach
-------------- -------------------------- ------------------------------ -----------------
 29,17          ABDO Aásim (138)           Alphabetisation (16/01/2017)   Romain Raffault
 29,17          ABID Abdul Báásid (162)    Alphabetisation (16/01/2017)   Romain Raffault
 25,00          ABBAS Aábid (115)          Alphabetisation (16/01/2017)   Romain Raffault
 25,00          ABDELLA Aákif (128)        Alphabetisation (16/01/2017)   Romain Raffault
 25,00          ABDULLA Abbáás (152)       Alphabetisation (16/01/2017)   Romain Raffault
 25,00          ALTUKHOV Adleshá (117)     Alphabetisation (16/01/2017)   Romain Raffault
 25,00          ARNOLD Alexei (129)        Alphabetisation (16/01/2017)   Romain Raffault
 25,00          BEK-MURZIN Agápiiá (160)   Alphabetisation (16/01/2017)   Romain Raffault
============== ========================== ============================== =================
<BLANKLINE>


Clients with more than one enrolment
====================================

>>> from django.db.models import Count
>>> qs = rt.models.avanti.Client.objects.all()
>>> qs = qs.annotate(
...     ecount=Count('enrolments_by_pupil'))
>>> qs = qs.filter(ecount__gt=1)
>>> obj = qs[0]
>>> rt.show(courses.EnrolmentsByPupil, obj, header_level=4)
Enrolments in Activities of ABAD Aábdeen (114) (Also Cancelled)
===============================================================
================= ============================== =============== ======== ===============
 Date of request   Activity                       Author          Remark   Workflow
----------------- ------------------------------ --------------- -------- ---------------
 13/02/2017        Alphabetisation (16/01/2017)   Laura Lieblig            **Requested**
 13/02/2017        Alphabetisation (16/01/2017)   martina                  **Trying**
================= ============================== =============== ======== ===============
<BLANKLINE>

Note that missing rates are also computed for non-confirmed
enrolments, and that there are even non-zero rates for such cases.

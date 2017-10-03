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

Names of participants
=====================

The names of the participants are confidential data in :ref:`avanti`.

System admins and coordinators can see the full names:

>>> obj = courses.Course.objects.get(pk=1)
>>> rt.login('rolf').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==== ================= ======================= ======== ============= =========== ======== ===== ========= ======== ==================================================
 ID   Date of request   Client                  Gender   Nationality   Childcare   School   Bus   Evening   Remark   Workflow
---- ----------------- ----------------------- -------- ------------- ----------- -------- ----- --------- -------- --------------------------------------------------
 9    07/02/2017        ABDI Aátifá (136)       Female                 No          No       No    No                 **Requested** → [Confirm] [Cancelled] [Trying]
 7    09/02/2017        ABDELNOUR Aámir (125)   Male                   No          No       No    No                 **Confirmed** → [Cancelled] [Requested] [Trying]
 5    11/02/2017        ABDALLAH Aáish (127)    Male                   No          No       No    No                 **Requested** → [Confirm] [Cancelled] [Trying]
 3    13/02/2017        ABBASI Aáishá (118)     Female                 No          No       No    No                 **Confirmed** → [Cancelled] [Requested] [Trying]
 1    15/02/2017        ABAD Aábdeen (114)      Male                   No          No       No    No                 **Requested** → [Confirm] [Cancelled] [Trying]
==== ================= ======================= ======== ============= =========== ======== ===== ========= ======== ==================================================
<BLANKLINE>

But auditors see only the first name, number and place:

>>> rt.login('audrey').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==== ================= ========================== ======== ============= =========== ======== ===== ========= ======== ===============
 ID   Date of request   Client                     Gender   Nationality   Childcare   School   Bus   Evening   Remark   Workflow
---- ----------------- -------------------------- -------- ------------- ----------- -------- ----- --------- -------- ---------------
 9    07/02/2017        Aátifá (136) from Eupen    Female                 No          No       No    No                 **Requested**
 7    09/02/2017        Aámir (125) from Eupen     Male                   No          No       No    No                 **Confirmed**
 5    11/02/2017        Aáish (127) from Eupen     Male                   No          No       No    No                 **Requested**
 3    13/02/2017        Aáishá (118) from Eupen    Female                 No          No       No    No                 **Confirmed**
 1    15/02/2017        Aábdeen (114) from Eupen   Male                   No          No       No    No                 **Requested**
==== ================= ========================== ======== ============= =========== ======== ===== ========= ======== ===============
<BLANKLINE>


Note that teachers *can* see the full names. They need it because they
must register presences and absences:

>>> rt.login('laura').show('courses.EnrolmentsByCourse', obj)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==== ================= ======================= ======== ============= =========== ======== ===== ========= ======== ==================================================
 ID   Date of request   Client                  Gender   Nationality   Childcare   School   Bus   Evening   Remark   Workflow
---- ----------------- ----------------------- -------- ------------- ----------- -------- ----- --------- -------- --------------------------------------------------
 9    07/02/2017        ABDI Aátifá (136)       Female                 No          No       No    No                 **Requested** → [Confirm] [Cancelled] [Trying]
 7    09/02/2017        ABDELNOUR Aámir (125)   Male                   No          No       No    No                 **Confirmed** → [Cancelled] [Requested] [Trying]
 5    11/02/2017        ABDALLAH Aáish (127)    Male                   No          No       No    No                 **Requested** → [Confirm] [Cancelled] [Trying]
 3    13/02/2017        ABBASI Aáishá (118)     Female                 No          No       No    No                 **Confirmed** → [Cancelled] [Requested] [Trying]
 1    15/02/2017        ABAD Aábdeen (114)      Male                   No          No       No    No                 **Requested** → [Confirm] [Cancelled] [Trying]
==== ================= ======================= ======== ============= =========== ======== ===== ========= ======== ==================================================
<BLANKLINE>


Reference
=========

.. currentmodule:: lino_avanti.lib.courses

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
    
    This is an example of :ref:`indirect_master`.
    
.. class:: EnrolmentChecker
           
    Checks for the following plausibility problems:

    - :message:`More than 2 times absent.`

    - :message:`Missed more than 10% of meetings.`


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
>>> rv = AttrDict(json.loads(res.content))
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
>>> cells[3]
<td>02.02.\n\n<br/><font size="1">11 (\u2611)</font>\n</td>

>>> cells[17]
<td>1</td>

>>> cells[18]
<td><p>Mr A\xe1sim Abdo</p></td>

>>> cells[20]  #doctest: +NORMALIZE_WHITESPACE
<td align="center" valign="middle">\u2611\n  </td>

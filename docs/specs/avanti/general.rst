.. doctest docs/specs/avanti/general.rst
.. _avanti.specs.general:

===============================
General overview of Lino Avanti
===============================

.. contents::
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.avanti1.settings.doctests')
>>> from lino.api.doctest import *



Miscellaneous
=============

List of demo users:

>>> rt.show(rt.models.users.Users)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
========== ===================== ============ ===========
 Username   User type             First name   Last name
---------- --------------------- ------------ -----------
 audrey     300 (Auditor)
 laura      100 (Teacher)         Laura        Lieblig
 martina    400 (Coordinator)
 nathalie   200 (Social worker)
 robin      900 (Administrator)   Robin        Rood
 rolf       900 (Administrator)   Rolf         Rompen
 romain     900 (Administrator)   Romain       Raffault
 sandra     410 (Secretary)
========== ===================== ============ ===========
<BLANKLINE>


>>> dd.plugins.beid.holder_model
<class 'lino_avanti.lib.avanti.models.Client'>

The following checks whether the dashboard displays for user robin:

>>> url = "/"
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER="robin")
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, "lxml")
>>> links = soup.find_all('a')
>>> len(links)
0



Here is a text variant of Robin's dashboard.

>>> rt.login('robin').show_dashboard()
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +ELLIPSIS -SKIP
-----------------------------------------------
My appointments **New** `⏏ <My appointments>`__
-----------------------------------------------
<BLANKLINE>
====================================================== ======== ===============================
 Calendar entry                                         Client   Workflow
------------------------------------------------------ -------- -------------------------------
 `Breakfast (15.02.2017 13:30) <Detail>`__                       **☐ Draft** → [☑] [☒]
 `Absent for private reasons (16.02.2017) <Detail>`__            **☑ Took place** → [☐] [☒]
 `Seminar (17.02.2017 10:20) <Detail>`__                         **? Suggested** → [☐] [☑] [☒]
 `Absent for private reasons (19.02.2017) <Detail>`__            **☐ Draft** → [☑] [☒]
 `Interview (19.02.2017 08:30) <Detail>`__                       **☒ Cancelled** → [☐] [☑]
 `Breakfast (21.02.2017 11:10) <Detail>`__                       **☑ Took place** → [☐] [☒]
 `Absent for private reasons (22.02.2017) <Detail>`__            **? Suggested** → [☐] [☑] [☒]
 `Seminar (23.02.2017 09:40) <Detail>`__                         **☐ Draft** → [☑] [☒]
 `Interview (25.02.2017 13:30) <Detail>`__                       **? Suggested** → [☐] [☑] [☒]
 `Breakfast (27.02.2017 10:20) <Detail>`__                       **☒ Cancelled** → [☐] [☑]
 `Seminar (01.03.2017 08:30) <Detail>`__                         **☑ Took place** → [☐] [☒]
 `Interview (03.03.2017 11:10) <Detail>`__                       **☐ Draft** → [☑] [☒]
 `Breakfast (05.03.2017 09:40) <Detail>`__                       **? Suggested** → [☐] [☑] [☒]
 `Seminar (07.03.2017 13:30) <Detail>`__                         **☒ Cancelled** → [☐] [☑]
====================================================== ======== ===============================
<BLANKLINE>
---------------------------------------------------------------
My overdue appointments **New** `⏏ <My overdue appointments>`__
---------------------------------------------------------------
<BLANKLINE>
=========================================== =============== ===================== ===============================
 Calendar entry                              Controlled by   Calendar entry type   Workflow
------------------------------------------- --------------- --------------------- -------------------------------
 `Seminar (30.01.2017 08:30) <Detail>`__                     Internal              **☐ Draft** → [☑] [☒]
 `Interview (01.02.2017 11:10) <Detail>`__                   Meeting               **? Suggested** → [☐] [☑] [☒]
 `Interview (07.02.2017 10:20) <Detail>`__                   Internal              **☐ Draft** → [☑] [☒]
 `Breakfast (09.02.2017 08:30) <Detail>`__                   Meeting               **? Suggested** → [☐] [☑] [☒]
=========================================== =============== ===================== ===============================
<BLANKLINE>
-----------------------------------------------------------------------
My unconfirmed appointments **New** `⏏ <My unconfirmed appointments>`__
-----------------------------------------------------------------------
<BLANKLINE>
===================================== ======== =================== ===============================
 When                                  Client   Short description   Workflow
------------------------------------- -------- ------------------- -------------------------------
 `Wed 01/02/2017 (11:10) <Detail>`__            Interview           **? Suggested** → [☐] [☑] [☒]
 `Tue 07/02/2017 (10:20) <Detail>`__            Interview           **☐ Draft** → [☑] [☒]
 `Thu 09/02/2017 (08:30) <Detail>`__            Breakfast           **? Suggested** → [☐] [☑] [☒]
 `Wed 15/02/2017 (13:30) <Detail>`__            Breakfast           **☐ Draft** → [☑] [☒]
 `Fri 17/02/2017 (10:20) <Detail>`__            Seminar             **? Suggested** → [☐] [☑] [☒]
 `Thu 23/02/2017 (09:40) <Detail>`__            Seminar             **☐ Draft** → [☑] [☒]
 `Sat 25/02/2017 (13:30) <Detail>`__            Interview           **? Suggested** → [☐] [☑] [☒]
===================================== ======== =================== ===============================
<BLANKLINE>
-----------------------------------
Daily planner `⏏ <Daily planner>`__
-----------------------------------
<BLANKLINE>
============ ============================================================== ==================================================
 Time range   External                                                       Internal
------------ -------------------------------------------------------------- --------------------------------------------------
 *All day*    `Rolf Rompen Absent for private reasons Absences <Detail>`__
 *AM*
 *PM*                                                                        `13:30 Robin Rood Breakfast Internal <Detail>`__
============ ============================================================== ==================================================
<BLANKLINE>
---------------------------------------------------------------
My Notification messages **✓** `⏏ <My Notification messages>`__
---------------------------------------------------------------
<BLANKLINE>
=========================== ==================================== ============== ==========
 Created                     Subject                              Message Type   Workflow
--------------------------- ------------------------------------ -------------- ----------
 2017-02-15 ...              The database has been initialized.   System event   [✓]
=========================== ==================================== ============== ==========
<BLANKLINE>
----------------------------
Status Report `⏏ <Detail>`__
----------------------------
<BLANKLINE>
~~~~~~~~~~~~~~~~
Language courses
~~~~~~~~~~~~~~~~
<BLANKLINE>
=========================================== =========== ============= ================== =========== ============= =========== ========
 Activity                                    When        Times         Available places   Confirmed   Free places   Requested   Trying
------------------------------------------- ----------- ------------- ------------------ ----------- ------------- ----------- --------
 `Alphabetisation (16/01/2017) <Detail>`__   Every day   09:00-12:00   5                  3           0             3           2
 `Alphabetisation (16/01/2017) <Detail>`__   Every day   14:00-17:00   15                 2           0             4           13
 `Alphabetisation (16/01/2017) <Detail>`__   Every day   18:00-20:00   15                 12          0             11          3
 **Total (3 rows)**                                                    **35**             **17**      **0**         **18**      **18**
=========================================== =========== ============= ================== =========== ============= =========== ========
<BLANKLINE>

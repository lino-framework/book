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


TODO: The following test is skipped because doctest seems to have a problem
when the only differences are spaces
*and* when +NORMALIZE_WHITESPACE is set
*and* when +ELLIPSIS is being used
*and* when the output contains Non-ASCII text.


>>> show_dashboard('robin')
... #doctest: +REPORT_UDIFF +ELLIPSIS +NORMALIZE_WHITESPACE +SKIP
Quick links: [[Search](javascript:Lino.about.SiteSearch.grid.run\(null\))]
[[My settings](javascript:Lino.users.MySettings.detail.run\(null,{
"record_id": 1 }\) "Open a detail window on this record.")] [[My
Clients](javascript:Lino.avanti.MyClients.grid.run\(null\))] [[New
Client](javascript:Lino.avanti.MyClients.insert.run\(null\) "Open a dialog
window to insert a new Client.")] [[Read eID
card](javascript:Lino.list_action_handler\('/avanti/MyClients','find_by_beid','POST',Lino.beid_read_card_processor\)\(\)
"Find or create card holder from eID card")]
[[Refresh](javascript:Lino.viewport.refresh\(\);)]
<BLANKLINE>
Hi, Robin Rood! [There are 5 data problems assigned to
you.](javascript:Lino.checkdata.MyProblems.grid.run\(null,{ "base_params": {
}, "param_values": { "checker": null, "checkerHidden": null, "user": "Robin
Rood", "userHidden": 1 } }\))
<BLANKLINE>
This is a Lino demo site. Try also the other [demo sites](http://lino-
framework.org/demos.html). Your feedback is welcome to [users@lino-
framework.org](mailto:users@lino-framework.org) or directly to the person who
invited you. **We are running with simulated date set to Wednesday, 15
February 2017.**
<BLANKLINE>
## My appointments
[![add](/static/images/mjames/add.png)](javascript:Lino.cal.MyEntries.insert.run\(null,{
...}\) "Open a dialog window to insert a new Calendar entry.")
[⏏](javascript:Lino.cal.MyEntries.grid.run\(null\) "Show this table in own
window")
<BLANKLINE>
Calendar entry| Client| Workflow
---|---|---
[Breakfast (15.02.2017
13:30)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id": 238
}\))| |  **☒ Cancelled** → [ ☐
](javascript:Lino.cal.MyEntries.wf2\(null,true,238,{  }\) "Draft") [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,238,{  }\) "Took place")
[Absent for private reasons
(16.02.2017)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id":
271 }\))| |  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,271,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,271,{  }\) "Cancelled")
[Seminar (17.02.2017 10:20)](javascript:Lino.cal.MyEntries.detail.run\(null,{
"record_id": 241 }\))| |  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,241,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,241,{  }\) "Cancelled")
[Absent for private reasons
(19.02.2017)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id":
274 }\))| |  **? Suggested** → [ ☐
](javascript:Lino.cal.MyEntries.wf2\(null,true,274,{  }\) "Draft") [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,274,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,274,{  }\) "Cancelled")
[Interview (19.02.2017
08:30)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id": 244
}\))| |  **? Suggested** → [ ☐
](javascript:Lino.cal.MyEntries.wf2\(null,true,244,{  }\) "Draft") [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,244,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,244,{  }\) "Cancelled")
[Breakfast (21.02.2017
11:10)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id": 247
}\))| |  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,247,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,247,{  }\) "Cancelled")
[Absent for private reasons
(22.02.2017)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id":
277 }\))| |  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,277,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,277,{  }\) "Cancelled")
[Seminar (23.02.2017 09:40)](javascript:Lino.cal.MyEntries.detail.run\(null,{
"record_id": 250 }\))| |  **? Suggested** → [ ☐
](javascript:Lino.cal.MyEntries.wf2\(null,true,250,{  }\) "Draft") [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,250,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,250,{  }\) "Cancelled")
[Interview (25.02.2017
13:30)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id": 253
}\))| |  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,253,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,253,{  }\) "Cancelled")
[Breakfast (27.02.2017
10:20)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id": 256
}\))| |  **? Suggested** → [ ☐
](javascript:Lino.cal.MyEntries.wf2\(null,true,256,{  }\) "Draft") [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,256,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,256,{  }\) "Cancelled")
[Seminar (01.03.2017 08:30)](javascript:Lino.cal.MyEntries.detail.run\(null,{
"record_id": 259 }\))| |  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,259,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,259,{  }\) "Cancelled")
[Interview (03.03.2017
11:10)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id": 262
}\))| |  **? Suggested** → [ ☐
](javascript:Lino.cal.MyEntries.wf2\(null,true,262,{  }\) "Draft") [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,262,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,262,{  }\) "Cancelled")
[Breakfast (05.03.2017
09:40)](javascript:Lino.cal.MyEntries.detail.run\(null,{ "record_id": 265
}\))| |  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,265,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,265,{  }\) "Cancelled")
[Seminar (07.03.2017 13:30)](javascript:Lino.cal.MyEntries.detail.run\(null,{
"record_id": 268 }\))| |  **? Suggested** → [ ☐
](javascript:Lino.cal.MyEntries.wf2\(null,true,268,{  }\) "Draft") [ ☑
](javascript:Lino.cal.MyEntries.wf3\(null,true,268,{  }\) "Took place") [ ☒
](javascript:Lino.cal.MyEntries.wf4\(null,true,268,{  }\) "Cancelled")
<BLANKLINE>
## My unconfirmed appointments
[![add](/static/images/mjames/add.png)](javascript:Lino.cal.MyUnconfirmedAppointments.insert.run\(null,{...}\) "Open a dialog window to insert a new Calendar entry.")
[⏏](javascript:Lino.cal.MyUnconfirmedAppointments.grid.run\(null\) "Show this
table in own window")
<BLANKLINE>
When| Client| Short description| Workflow
---|---|---|---
[Thu
16/02/2017](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 271 }\))| | Absent for private reasons|  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,271,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,271,{  }\)
"Cancelled")
[Fri 17/02/2017
(10:20)](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 241 }\))| | Seminar|  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,241,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,241,{  }\)
"Cancelled")
[Sun
19/02/2017](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 274 }\))| | Absent for private reasons|  **? Suggested** → [ ☐
](javascript:Lino.cal.MyUnconfirmedAppointments.wf2\(null,true,274,{  }\)
"Draft") [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,274,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,274,{  }\)
"Cancelled")
[Sun 19/02/2017
(08:30)](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 244 }\))| | Interview|  **? Suggested** → [ ☐
](javascript:Lino.cal.MyUnconfirmedAppointments.wf2\(null,true,244,{  }\)
"Draft") [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,244,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,244,{  }\)
"Cancelled")
[Tue 21/02/2017
(11:10)](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 247 }\))| | Breakfast|  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,247,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,247,{  }\)
"Cancelled")
[Wed
22/02/2017](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 277 }\))| | Absent for private reasons|  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,277,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,277,{  }\)
"Cancelled")
[Thu 23/02/2017
(09:40)](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 250 }\))| | Seminar|  **? Suggested** → [ ☐
](javascript:Lino.cal.MyUnconfirmedAppointments.wf2\(null,true,250,{  }\)
"Draft") [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,250,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,250,{  }\)
"Cancelled")
[Sat 25/02/2017
(13:30)](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 253 }\))| | Interview|  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,253,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,253,{  }\)
"Cancelled")
[Mon 27/02/2017
(10:20)](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 256 }\))| | Breakfast|  **? Suggested** → [ ☐
](javascript:Lino.cal.MyUnconfirmedAppointments.wf2\(null,true,256,{  }\)
"Draft") [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,256,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,256,{  }\)
"Cancelled")
[Wed 01/03/2017
(08:30)](javascript:Lino.cal.MyUnconfirmedAppointments.detail.run\(null,{
"record_id": 259 }\))| | Seminar|  **☐ Draft** → [ ☑
](javascript:Lino.cal.MyUnconfirmedAppointments.wf3\(null,true,259,{  }\)
"Took place") [ ☒
](javascript:Lino.cal.MyUnconfirmedAppointments.wf4\(null,true,259,{  }\)
"Cancelled")
<BLANKLINE>
## Daily planner [⏏](javascript:Lino.calview.DailyPlanner.grid.run\(null\)
"Show this table in own window")
<BLANKLINE>
Time range| External| Internal
---|---|---
 _All day_|
<BLANKLINE>
[ ☑ rolf Absent for private
reasons](javascript:Lino.cal.OneEvent.detail.run\(null,{ "record_id": 270 }\))
<BLANKLINE>
|
<BLANKLINE>
 _AM_|
<BLANKLINE>
[ 08:30 ☑ romain Rencontre](javascript:Lino.cal.OneEvent.detail.run\(null,{
"record_id": 239 }\))
<BLANKLINE>
|
<BLANKLINE>
 _PM_|
<BLANKLINE>
|
<BLANKLINE>
## Recent comments
[![add](/static/images/mjames/add.png)](javascript:Lino.comments.RecentComments.insert.run\(null,{...}\)
"Open a dialog window to insert a new Comment.")
[⏏](javascript:Lino.comments.RecentComments.grid.run\(null\) "Show this table
in own window")
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 108 }\) "Created 2021-01-14 01:33") by **robin** in reply to
**romain** about [ABED Abdul Báári
(159)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id": 159 }\))
: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec interdum
dictum erat. Fusce condimentum erat a pulvinar ultricies. (...)
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 107 }\) "Created 2021-01-14 01:33") by **rolf** in reply to
**romain** about [ABED Abdul Báári
(159)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id": 159 }\))
: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc cursus felis
nisi, eu pellentesque lorem lobortis non. Aenean non sodales neque, vitae
venenatis lectus. In eros dui, gravida et dolor at, pellentesque hendrerit
magna. Quisque vel lectus dictum, rhoncus massa feugiat, condimentum sem.
Donec elit nisl, placerat vitae imperdiet eget, hendrerit nec quam. Ut
elementum ligula vitae odio efficitur rhoncus. Duis in blandit neque. Sed
dictum mollis volutpat. Morbi at est et nisi euismod viverra. Nulla quis lacus
vitae ante sollicitudin tincidunt. Donec nec enim in leo vulputate ultrices.
Suspendisse potenti. Ut elit nibh, porta ut enim ac, convallis molestie risus.
Praesent consectetur lacus lacus, in faucibus justo fringilla vel. (...)
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 106 }\) "Created 2021-01-14 01:33") by **romain** about [ABED
Abdul Báári (159)](javascript:Lino.avanti.Clients.detail.run\(null,{
"record_id": 159 }\)) (2 replies) :  Who| What| Done?
---|---|---
Him| Bar|
Her| Foo the Bar|  **x**
Them| Floop the pig
| x
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 105 }\) "Created 2021-01-14 01:33") by **laura** in reply to
**martina** about [ABDULLAH Afááf
(155)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id": 155 }\))
: Styled comment pasted from word!
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 104 }\) "Created 2021-01-14 01:33") by **sandra** in reply to
**martina** about [ABDULLAH Afááf
(155)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id": 155 }\))
: Two paragraphs of plain text. (...)
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 103 }\) "Created 2021-01-14 01:33") by **nelly** in reply to
**martina** about [ABDULLAH Afááf
(155)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id": 155 }\))
: Some plain text.
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 102 }\) "Created 2021-01-14 01:33") by **nathalie** in reply to
**martina** about [ABDULLAH Afááf
(155)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id": 155 }\))
: (...)
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 101 }\) "Created 2021-01-14 01:33") by **martina** about
[ABDULLAH Afááf (155)](javascript:Lino.avanti.Clients.detail.run\(null,{
"record_id": 155 }\)) (4 replies) : breaking (...)
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 100 }\) "Created 2021-01-14 01:33") by **audrey** in reply to
**robin** about [ABDULLAH Afááf
(155)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id": 155 }\))
: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec interdum
dictum erat. Fusce condimentum erat a pulvinar ultricies. (...)
<BLANKLINE>
[11 hours ago](javascript:Lino.comments.RecentComments.detail.run\(null,{
"record_id": 99 }\) "Created 2021-01-14 01:33") by **robin** about [ABDULLAH
Afááf (155)](javascript:Lino.avanti.Clients.detail.run\(null,{ "record_id":
155 }\)) (1 reply) : Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nunc cursus felis nisi, eu pellentesque lorem lobortis non. Aenean non sodales
neque, vitae venenatis lectus. In eros dui, gravida et dolor at, pellentesque
hendrerit magna. Quisque vel lectus dictum, rhoncus massa feugiat, condimentum
sem. Donec elit nisl, placerat vitae imperdiet eget, hendrerit nec quam. Ut
elementum ligula vitae odio efficitur rhoncus. Duis in blandit neque. Sed
dictum mollis volutpat. Morbi at est et nisi euismod viverra. Nulla quis lacus
vitae ante sollicitudin tincidunt. Donec nec enim in leo vulputate ultrices.
Suspendisse potenti. Ut elit nibh, porta ut enim ac, convallis molestie risus.
Praesent consectetur lacus lacus, in faucibus justo fringilla vel. (...)
<BLANKLINE>
...
<BLANKLINE>
## My Notification messages
[✓](javascript:Lino.list_action_handler\("/notify/MyMessages","mark_all_seen","POST",function\(\)
{return {  };},null,null\)\(\) "Mark all messages as seen.")
[⏏](javascript:Lino.notify.MyMessages.grid.run\(null\) "Show this table in own
window")
<BLANKLINE>
  * [ ✓ ](javascript:Lino.notify.MyMessages.mark_seen\(null,true,6,{  }\) "Mark this message as seen.")15/02/2017 05:48 The database has been initialized.
<BLANKLINE>
## Status Report [⏏](javascript:Lino.courses.StatusReport.show.run\(null,{
"record_id": -99998 }\) "Show this table in own window")
<BLANKLINE>
### Language courses
<BLANKLINE>
Activity| When| Times| Available places| Confirmed| Free places| Requested|
Trying
---|---|---|---|---|---|---|---
[Alphabetisation
(16/01/2017)](javascript:Lino.courses.Activities.detail.run\(null,{
"record_id": 1 }\))| Every day| 09:00-12:00| 5| 3| 0| 3| 2
[Alphabetisation
(16/01/2017)](javascript:Lino.courses.Activities.detail.run\(null,{
"record_id": 2 }\))| Every day| 14:00-17:00| 15| 2| 0| 4| 13
[Alphabetisation
(16/01/2017)](javascript:Lino.courses.Activities.detail.run\(null,{
"record_id": 3 }\))| Every day| 18:00-20:00| 15| 12| 0| 11| 3
 **Total (3 rows)**| | |  **35**|  **17**|  **0**|  **18**|  **18**
<BLANKLINE>
<BLANKLINE>

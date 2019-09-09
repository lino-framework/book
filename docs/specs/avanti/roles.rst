.. doctest docs/specs/avanti/roles.rst
.. _avanti.specs.roles:

=========================
User types in Lino Avanti
=========================

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.avanti1.settings.doctests')
>>> from lino.api.doctest import *



Site administrator
==================

>>> rt.login('robin').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Contacts : Persons, Organizations, Clients, My Clients, Households, Partner Lists
- Calendar : My appointments, Overdue appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar view
- Office : My Comments, Recent comments, My Notification messages, My expiring uploads, My Uploads, My Excerpts, Data problems assigned to me
- Polls : My Polls, My Responses
- Activities : My Activities, Activities, -, Activity lines, Pending requested enrolments, Pending confirmed enrolments, Course planning, Absence control
- Configure :
  - System : Users, Site Parameters, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, Categories, Ending reasons, Household Types, List Types
  - Calendar : Calendars, Rooms, Recurring events, Guest roles, Calendar entry types, Recurrency policies, Remote Calendars, Planner rows, Absence reasons
  - Office : Comment Types, Library volumes, Upload Types, Excerpt Types
  - Clients : Client Contact types
  - Career : Education Types, Education Levels, Job Sectors, Job Functions, Work Regimes, Statuses, Contract Durations, Languages
  - Trends : Trend areas, Trend stages
  - Polls : Choice Sets
  - Activities : Topics, Timetable Slots
- Explorer :
  - System : Authorities, User types, User roles, Notification messages, Changes, Phonetic words, All dashboard widgets, content types, Data checkers, Data problems
  - Contacts : Contact Persons, Partners, Clients, Household member roles, Household Members, List memberships
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Event states, Guest states, Task states
  - Office : Comments, Uploads, Upload Areas, Excerpts
  - Clients : Client Contacts, Known contact types
  - Career : language knowledges, Trainings, Studies, Job Experiences
  - Trends : Trend events
  - Polls : Polls, Questions, Choices, Responses, Answer Choices, Answer Remarks
  - Activities : Activities, Enrolments, Enrolment states, Course layouts, Activity states, Reminders
- Site : About



Coordinator
===========

>>> rt.login('martina').user.user_type
users.UserTypes.coordinator:400

>>> rt.login('martina').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Office : My expiring uploads, My Uploads, My Excerpts, Data problems assigned to me
- Activities : My Activities, Activities, -, Activity lines, Course planning
- Site : About


Secretary
=========

>>> rt.login('sandra').user.user_type
users.UserTypes.secretary:410

>>> rt.login('sandra').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Contacts : Persons, Organizations, Clients, My Clients, Households, Partner Lists
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar view
- Office : My Notification messages, My expiring uploads, My Uploads, My Excerpts, Data problems assigned to me
- Activities : My Activities, Activities, -, Activity lines, Course planning
- Explorer :
  - Contacts : Partners
  - Activities : Reminders
- Site : About



Social worker
=============

>>> rt.login('nathalie').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Contacts : Persons, Organizations, Clients, My Clients, Households, Partner Lists
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar view
- Office : My Comments, Recent comments, My Notification messages, My expiring uploads, My Uploads, My Excerpts, Data problems assigned to me
- Polls : My Polls, My Responses
- Activities : My Activities, Activities, -, Activity lines, Course planning, Absence control
- Configure :
  - Trends : Trend stages
- Explorer :
  - Contacts : Partners, Clients
  - Calendar : Calendar entries, Presences
  - Activities : Activities, Enrolments, Reminders
- Site : About

Teacher
=======

>>> rt.login('laura').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
- Office : My Notification messages, My expiring uploads, My Uploads
- Activities : My Activities, -, My courses given
- Site : About

Supervisor
==========

>>> rt.login('audrey').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
- Office : My Notification messages, My expiring uploads, My Uploads
- Activities : My Activities, Activities, -, Activity lines, Course planning
- Explorer :
  - Contacts : Clients
  - Calendar : Calendar entries
  - Activities : Activities, Enrolments
- Site : About



Windows and permissions
=======================

Each window is **viewable** for a given set of user types.

>>> print(analyzer.show_window_permissions())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- about.About.show : visible for all
- avanti.Clients.detail : visible for user secretary staff admin
- avanti.Clients.merge_row : visible for admin
- cal.Calendars.detail : visible for staff admin
- cal.Calendars.insert : visible for staff admin
- cal.DailyView.detail : visible for user secretary staff admin
- cal.EntriesByGuest.insert : visible for teacher user coordinator secretary staff admin
- cal.EntriesByProject.insert : visible for teacher user coordinator secretary staff admin
- cal.EventTypes.detail : visible for staff admin
- cal.EventTypes.insert : visible for staff admin
- cal.EventTypes.merge_row : visible for admin
- cal.Events.detail : visible for staff admin
- cal.Events.insert : visible for staff admin
- cal.GuestRoles.detail : visible for admin
- cal.GuestRoles.merge_row : visible for admin
- cal.Guests.detail : visible for teacher user staff admin
- cal.Guests.insert : visible for teacher user staff admin
- cal.MonthlyView.detail : visible for user secretary staff admin
- cal.RecurrentEvents.detail : visible for staff admin
- cal.RecurrentEvents.insert : visible for staff admin
- cal.Rooms.detail : visible for staff admin
- cal.Rooms.insert : visible for staff admin
- cal.Tasks.detail : visible for staff admin
- cal.Tasks.insert : visible for staff admin
- cal.WeeklyView.detail : visible for user secretary staff admin
- changes.Changes.detail : visible for admin
- checkdata.Checkers.detail : visible for admin
- checkdata.Problems.detail : visible for teacher user auditor coordinator secretary staff admin
- clients.ClientContactTypes.detail : visible for staff admin
- comments.CommentTypes.detail : visible for staff admin
- comments.CommentTypes.insert : visible for staff admin
- comments.Comments.detail : visible for user staff admin
- comments.Comments.insert : visible for user staff admin
- comments.CommentsByRFC.insert : visible for user staff admin
- contacts.Companies.detail : visible for user secretary staff admin
- contacts.Companies.insert : visible for user secretary staff admin
- contacts.Companies.merge_row : visible for admin
- contacts.Partners.merge_row : visible for admin
- contacts.Persons.create_household : visible for user secretary staff admin
- contacts.Persons.detail : visible for user secretary staff admin
- contacts.Persons.insert : visible for user secretary staff admin
- contacts.Persons.merge_row : visible for admin
- countries.Countries.detail : visible for staff admin
- countries.Countries.insert : visible for staff admin
- countries.Places.detail : visible for staff admin
- courses.Activities.detail : visible for teacher user auditor coordinator secretary staff admin
- courses.Activities.insert : visible for teacher user coordinator secretary staff admin
- courses.Activities.print_presence_sheet : visible for teacher user auditor coordinator secretary staff admin
- courses.Activities.print_presence_sheet_html : visible for teacher user auditor coordinator secretary staff admin
- courses.Enrolments.detail : visible for teacher user auditor coordinator secretary staff admin
- courses.Enrolments.insert : visible for teacher user coordinator secretary staff admin
- courses.EnrolmentsByCourse.insert : visible for teacher user coordinator secretary staff admin
- courses.EnrolmentsByPupil.insert : visible for user coordinator secretary staff admin
- courses.Lines.detail : visible for user auditor coordinator secretary staff admin
- courses.Lines.insert : visible for user coordinator secretary staff admin
- courses.Lines.merge_row : visible for admin
- courses.RemindersByEnrolment.detail : visible for user secretary staff admin
- courses.RemindersByEnrolment.insert : visible for user secretary staff admin
- courses.Slots.detail : visible for admin
- courses.Slots.insert : visible for admin
- courses.StatusReport.show : visible for user auditor coordinator secretary staff admin
- courses.Topics.detail : visible for admin
- cv.Durations.detail : visible for staff admin
- cv.EducationLevels.detail : visible for staff admin
- cv.Experiences.detail : visible for staff admin
- cv.ExperiencesByPerson.insert : visible for user staff admin
- cv.Functions.detail : visible for staff admin
- cv.LanguageKnowledgesByPerson.detail : visible for user staff admin
- cv.LanguageKnowledgesByPerson.insert : visible for user staff admin
- cv.Regimes.detail : visible for staff admin
- cv.Sectors.detail : visible for staff admin
- cv.Statuses.detail : visible for staff admin
- cv.Studies.detail : visible for staff admin
- cv.StudiesByPerson.insert : visible for user staff admin
- cv.StudyTypes.detail : visible for staff admin
- cv.StudyTypes.insert : visible for staff admin
- cv.Trainings.detail : visible for user staff admin
- cv.Trainings.insert : visible for user staff admin
- excerpts.ExcerptTypes.detail : visible for staff admin
- excerpts.ExcerptTypes.insert : visible for staff admin
- excerpts.Excerpts.detail : visible for user coordinator secretary staff admin
- gfks.ContentTypes.detail : visible for admin
- households.Households.detail : visible for user secretary staff admin
- households.Households.insert : visible for user secretary staff admin
- households.Households.merge_row : visible for admin
- households.HouseholdsByType.insert : visible for user secretary staff admin
- households.MembersByPerson.insert : visible for user secretary staff admin
- households.Types.detail : visible for staff admin
- languages.Languages.detail : visible for staff admin
- lists.Lists.detail : visible for user secretary staff admin
- lists.Lists.insert : visible for user secretary staff admin
- lists.Lists.merge_row : visible for admin
- polls.AnswerRemarks.detail : visible for user staff admin
- polls.AnswerRemarks.insert : visible for user staff admin
- polls.ChoiceSets.detail : visible for staff admin
- polls.Polls.detail : visible for user staff admin
- polls.Polls.insert : visible for user staff admin
- polls.Polls.merge_row : visible for admin
- polls.Questions.detail : visible for staff admin
- polls.Responses.detail : visible for user staff admin
- polls.Responses.insert : visible for user staff admin
- system.SiteConfigs.detail : visible for admin
- trends.TrendAreas.detail : visible for staff admin
- trends.TrendStages.detail : visible for user staff admin
- trends.TrendStages.insert : visible for user staff admin
- trends.TrendStages.merge_row : visible for admin
- uploads.AllUploads.detail : visible for staff admin
- uploads.AllUploads.insert : visible for staff admin
- uploads.UploadTypes.detail : visible for staff admin
- uploads.UploadTypes.insert : visible for staff admin
- uploads.Uploads.detail : visible for teacher user auditor coordinator secretary staff admin
- uploads.Uploads.insert : visible for teacher user coordinator secretary staff admin
- uploads.UploadsByClient.insert : visible for user secretary staff admin
- uploads.UploadsByController.insert : visible for teacher user coordinator secretary staff admin
- uploads.Volumes.detail : visible for staff admin
- uploads.Volumes.insert : visible for staff admin
- uploads.Volumes.merge_row : visible for admin
- users.AllUsers.send_welcome_email : visible for admin
- users.Users.change_password : visible for teacher user auditor coordinator secretary staff admin
- users.Users.detail : visible for teacher user auditor coordinator secretary staff admin
- users.Users.insert : visible for teacher user coordinator secretary staff admin
- users.UsersOverview.sign_in : visible for all
<BLANKLINE>


Not everybody can see the names of participants
===============================================

The names of the participants are confidential data in :ref:`avanti`.

System admins can see the full names:

>>> obj = courses.Course.objects.get(pk=1)
>>> rt.login('rolf').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ================= ========================================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
 ID                Date of request   Participant                                Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
----------------- ----------------- ------------------------------------------ -------- ------------- ----------- -------- ----- --------- -------- -------------- --------------------------------------------------
 `31 <Detail>`__   30/01/2017        `ARNOLD Alexei (129) <Detail>`__           Male                   No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `25 <Detail>`__   03/02/2017        `ABDELNOUR Aámir (125) <Detail>`__         Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `22 <Detail>`__   04/02/2017        `ARENT Afánásiiá (124) <Detail>`__         Female                 No          No       No    No                 25,00          **Trying** → [Requested]
 `19 <Detail>`__   06/02/2017        `DEMEULENAERE Dorothée (121) <Detail>`__   Female                 No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `13 <Detail>`__   09/02/2017        `ABBASI Aáishá (118) <Detail>`__           Female                 No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `10 <Detail>`__   11/02/2017        `ALEKSANDROV Akim (116) <Detail>`__        Male                   No          No       No    No                 25,00          **Trying** → [Requested]
 `7 <Detail>`__    12/02/2017        `ABBAS Aábid (115) <Detail>`__             Male                   No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `1 <Detail>`__    15/02/2017        `ABEZGAUZ Adrik (112) <Detail>`__          Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
================= ================= ========================================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
<BLANKLINE>

Teachers and coordinators *can* see the full names (they need it
because they must register presences and absences), but they cannot
click on a name to see any detail.

>>> rt.login('laura').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ================= =============================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
 ID                Date of request   Participant                     Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
----------------- ----------------- ------------------------------- -------- ------------- ----------- -------- ----- --------- -------- -------------- --------------------------------------------------
 `31 <Detail>`__   30/01/2017        *ARNOLD Alexei (129)*           Male                   No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `25 <Detail>`__   03/02/2017        *ABDELNOUR Aámir (125)*         Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `22 <Detail>`__   04/02/2017        *ARENT Afánásiiá (124)*         Female                 No          No       No    No                 25,00          **Trying** → [Requested]
 `19 <Detail>`__   06/02/2017        *DEMEULENAERE Dorothée (121)*   Female                 No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `13 <Detail>`__   09/02/2017        *ABBASI Aáishá (118)*           Female                 No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `10 <Detail>`__   11/02/2017        *ALEKSANDROV Akim (116)*        Male                   No          No       No    No                 25,00          **Trying** → [Requested]
 `7 <Detail>`__    12/02/2017        *ABBAS Aábid (115)*             Male                   No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `1 <Detail>`__    15/02/2017        *ABEZGAUZ Adrik (112)*          Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
================= ================= =============================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
<BLANKLINE>


>>> rt.login('martina').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ================= =============================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
 ID                Date of request   Participant                     Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
----------------- ----------------- ------------------------------- -------- ------------- ----------- -------- ----- --------- -------- -------------- --------------------------------------------------
 `31 <Detail>`__   30/01/2017        *ARNOLD Alexei (129)*           Male                   No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `25 <Detail>`__   03/02/2017        *ABDELNOUR Aámir (125)*         Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `22 <Detail>`__   04/02/2017        *ARENT Afánásiiá (124)*         Female                 No          No       No    No                 25,00          **Trying** → [Requested]
 `19 <Detail>`__   06/02/2017        *DEMEULENAERE Dorothée (121)*   Female                 No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `13 <Detail>`__   09/02/2017        *ABBASI Aáishá (118)*           Female                 No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `10 <Detail>`__   11/02/2017        *ALEKSANDROV Akim (116)*        Male                   No          No       No    No                 25,00          **Trying** → [Requested]
 `7 <Detail>`__    12/02/2017        *ABBAS Aábid (115)*             Male                   No          No       No    No                 25,00          **Confirmed** → [Cancelled] [Requested] [Trying]
 `1 <Detail>`__    15/02/2017        *ABEZGAUZ Adrik (112)*          Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
================= ================= =============================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
<BLANKLINE>


But auditors see only the pupil's number and place:

>>> rt.login('audrey').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ================= ==================== ======== ============= =========== ======== ===== ========= ======== ============== ===============
 ID                Date of request   Participant          Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
----------------- ----------------- -------------------- -------- ------------- ----------- -------- ----- --------- -------- -------------- ---------------
 `31 <Detail>`__   30/01/2017        *(129) from Eupen*   Male                   No          No       No    No                 25,00          **Confirmed**
 `25 <Detail>`__   03/02/2017        *(125) from Eupen*   Male                   No          No       No    No                                **Requested**
 `22 <Detail>`__   04/02/2017        *(124) from Eupen*   Female                 No          No       No    No                 25,00          **Trying**
 `19 <Detail>`__   06/02/2017        *(121) from Eupen*   Female                 No          No       No    No                 25,00          **Confirmed**
 `13 <Detail>`__   09/02/2017        *(118) from Eupen*   Female                 No          No       No    No                                **Requested**
 `10 <Detail>`__   11/02/2017        *(116) from Eupen*   Male                   No          No       No    No                 25,00          **Trying**
 `7 <Detail>`__    12/02/2017        *(115) from Eupen*   Male                   No          No       No    No                 25,00          **Confirmed**
 `1 <Detail>`__    15/02/2017        *(112) from Eupen*   Male                   No          No       No    No                                **Requested**
================= ================= ==================== ======== ============= =========== ======== ===== ========= ======== ============== ===============
<BLANKLINE>



Teachers can see the names of their pupils, but must not see all the clients in
the database.  Accordingly they cannot create new enrolments or new presences
since this would require them to specify a client in the combobox (which would
show all clients). OTHO a teacher *can*  edit other fields on these records
(e.g. change the workflow or write a remark).  Since we cannot make the whoe
record read-only, we disable the fields.

>>> ar = rt.login("laura")
>>> "pupil" in courses.Enrolment.objects.first().disabled_fields(ar)
True
>>> "partner" in cal.Guest.objects.first().disabled_fields(ar)
True

For a coordinator these fields are not disabled:

>>> ar = rt.login("sandra")
>>> "pupil" in courses.Enrolment.objects.first().disabled_fields(ar)
False
>>> "partner" in cal.Guest.objects.first().disabled_fields(ar)
False

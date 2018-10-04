.. doctest docs/specs/avanti/roles.rst
.. _avanti.specs.roles:

=========================
User roles in Lino Avanti
=========================

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

.. contents::
  :local:

    

Site administrator
==================

>>> rt.login('robin').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Contacts : Persons, Organizations, Clients, My Clients, Households, Partner Lists
- Office : My Comments, Recent comments, My Notification messages, My expiring uploads, My Uploads, Data problems assigned to me, My Excerpts
- Calendar : Calendar, My appointments, Overdue appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
- Polls : My Polls, My Responses
- Activities : My Activities, Activities, -, Activity lines, Pending requested enrolments, Pending confirmed enrolments, Course planning, My coached enrolments
- Configure :
  - System : Site Parameters, Users, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, Categories, Ending reasons, Household Types, List Types
  - Office : Comment Types, Upload Types, Excerpt Types
  - Clients : Client Contact types
  - Career : Languages, Education Types, Education Levels, Job Sectors, Job Functions, Work Regimes, Statuses, Contract Durations
  - Trends : Trend areas, Trend stages
  - Polls : Choice Sets
  - Calendar : Calendars, Rooms, Priorities, Recurring events, Guest Roles, Calendar entry types, Recurrency policies, Remote Calendars, Planner rows
  - Activities : Topics, Timetable Slots
- Explorer :
  - System : Authorities, User types, content types, Notification messages, Changes, Phonetic words, Data checkers, Data problems, All dashboard widgets
  - Contacts : Contact Persons, Partners, Clients, Household member roles, Household Members, List memberships
  - Office : Comments, Uploads, Upload Areas, Excerpts
  - Clients : Client Contacts, Known contact types
  - Career : language knowledges, Trainings, Studies, Job Experiences
  - Trends : Trend events
  - Polls : Polls, Questions, Choices, Responses, Answer Choices, Answer Remarks
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Event states, Guest states, Task states
  - Activities : Activities, Enrolments, Enrolment states, Course layouts, Reminders
- Site : About

Coordinator
===========
>>> rt.login('martina').user.user_type
users.UserTypes.coordinator:400

>>> rt.login('martina').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Office : My expiring uploads, My Uploads, Data problems assigned to me, My Excerpts
- Activities : My Activities, Activities, -, Activity lines, Course planning
- Site : About

Teacher
=======

>>> rt.login('laura').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Office : My Notification messages, My expiring uploads, My Uploads
- Calendar : My appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
- Activities : My Activities, -, My courses given
- Site : About

Supervisor
==========

>>> rt.login('audrey').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Office : My Notification messages, My expiring uploads, My Uploads
- Calendar : My appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
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
- avanti.Categories.merge_row : visible for admin
- avanti.Clients.detail : visible for user secretary staff admin
- avanti.Clients.merge_row : visible for admin
- avanti.EndingReasons.merge_row : visible for admin
- avanti.Residences.merge_row : visible for admin
- cal.Calendars.detail : visible for staff admin
- cal.Calendars.insert : visible for staff admin
- cal.Calendars.merge_row : visible for admin
- cal.DailyPlannerRows.merge_row : visible for admin
- cal.EntriesByProject.insert : visible for teacher user coordinator secretary staff admin
- cal.EventPolicies.merge_row : visible for admin
- cal.EventTypes.detail : visible for staff admin
- cal.EventTypes.insert : visible for staff admin
- cal.EventTypes.merge_row : visible for admin
- cal.Events.detail : visible for staff admin
- cal.Events.insert : visible for staff admin
- cal.GuestRoles.detail : visible for admin
- cal.GuestRoles.merge_row : visible for admin
- cal.Guests.detail : visible for teacher user staff admin
- cal.Guests.insert : visible for teacher user staff admin
- cal.Guests.merge_row : visible for admin
- cal.OneEvent.merge_row : visible for admin
- cal.Priorities.merge_row : visible for admin
- cal.RecurrentEvents.detail : visible for staff admin
- cal.RecurrentEvents.insert : visible for staff admin
- cal.RecurrentEvents.merge_row : visible for admin
- cal.RemoteCalendars.merge_row : visible for admin
- cal.Rooms.detail : visible for staff admin
- cal.Rooms.insert : visible for staff admin
- cal.Rooms.merge_row : visible for admin
- cal.Subscriptions.merge_row : visible for admin
- cal.Tasks.detail : visible for staff admin
- cal.Tasks.insert : visible for staff admin
- cal.Tasks.merge_row : visible for admin
- changes.Changes.detail : visible for admin
- changes.Changes.merge_row : visible for admin
- checkdata.Checkers.detail : visible for admin
- checkdata.Problems.detail : visible for teacher user auditor coordinator secretary staff admin
- clients.ClientContactTypes.detail : visible for staff admin
- clients.ClientContactTypes.merge_row : visible for admin
- clients.ClientContacts.merge_row : visible for admin
- comments.CommentTypes.detail : visible for staff admin
- comments.CommentTypes.insert : visible for staff admin
- comments.CommentTypes.merge_row : visible for admin
- comments.Comments.detail : visible for user staff admin
- comments.Comments.insert : visible for user staff admin
- comments.Comments.merge_row : visible for admin
- comments.CommentsByRFC.insert : visible for user staff admin
- contacts.Companies.detail : visible for user secretary staff admin
- contacts.Companies.insert : visible for user secretary staff admin
- contacts.Companies.merge_row : visible for admin
- contacts.CompanyTypes.merge_row : visible for admin
- contacts.Partners.detail : visible for user secretary staff admin
- contacts.Partners.insert : visible for user secretary staff admin
- contacts.Partners.merge_row : visible for admin
- contacts.Persons.create_household : visible for user secretary staff admin
- contacts.Persons.detail : visible for user secretary staff admin
- contacts.Persons.insert : visible for user secretary staff admin
- contacts.Persons.merge_row : visible for admin
- contacts.RoleTypes.merge_row : visible for admin
- contacts.Roles.merge_row : visible for admin
- countries.Countries.detail : visible for staff admin
- countries.Countries.insert : visible for staff admin
- countries.Countries.merge_row : visible for admin
- countries.Places.detail : visible for staff admin
- countries.Places.merge_row : visible for admin
- courses.Activities.detail : visible for teacher user auditor coordinator secretary staff admin
- courses.Activities.insert : visible for teacher user coordinator secretary staff admin
- courses.Activities.merge_row : visible for admin
- courses.Activities.print_presence_sheet : visible for teacher user auditor coordinator secretary staff admin
- courses.Activities.print_presence_sheet_html : visible for teacher user auditor coordinator secretary staff admin
- courses.Enrolments.detail : visible for teacher user auditor coordinator secretary staff admin
- courses.Enrolments.insert : visible for teacher user coordinator secretary staff admin
- courses.Enrolments.merge_row : visible for admin
- courses.EnrolmentsByCourse.insert : visible for teacher user coordinator secretary staff admin
- courses.EnrolmentsByPupil.insert : visible for user coordinator secretary staff admin
- courses.Lines.detail : visible for user auditor coordinator secretary staff admin
- courses.Lines.insert : visible for user coordinator secretary staff admin
- courses.Lines.merge_row : visible for admin
- courses.Reminders.merge_row : visible for admin
- courses.RemindersByEnrolment.detail : visible for user secretary staff admin
- courses.RemindersByEnrolment.insert : visible for user secretary staff admin
- courses.Slots.detail : visible for admin
- courses.Slots.insert : visible for admin
- courses.Slots.merge_row : visible for admin
- courses.StatusReport.show : visible for user auditor coordinator secretary staff admin
- courses.Topics.detail : visible for admin
- courses.Topics.merge_row : visible for admin
- cv.Durations.detail : visible for staff admin
- cv.Durations.merge_row : visible for admin
- cv.EducationLevels.detail : visible for staff admin
- cv.EducationLevels.merge_row : visible for admin
- cv.Experiences.detail : visible for staff admin
- cv.Experiences.merge_row : visible for admin
- cv.ExperiencesByPerson.insert : visible for user staff admin
- cv.Functions.detail : visible for staff admin
- cv.Functions.merge_row : visible for admin
- cv.LanguageKnowledges.merge_row : visible for admin
- cv.LanguageKnowledgesByPerson.detail : visible for user staff admin
- cv.LanguageKnowledgesByPerson.insert : visible for user staff admin
- cv.Regimes.detail : visible for staff admin
- cv.Regimes.merge_row : visible for admin
- cv.Sectors.detail : visible for staff admin
- cv.Sectors.merge_row : visible for admin
- cv.Statuses.detail : visible for staff admin
- cv.Statuses.merge_row : visible for admin
- cv.Studies.detail : visible for staff admin
- cv.Studies.merge_row : visible for admin
- cv.StudiesByPerson.insert : visible for user staff admin
- cv.StudyTypes.detail : visible for staff admin
- cv.StudyTypes.insert : visible for staff admin
- cv.StudyTypes.merge_row : visible for admin
- cv.Trainings.detail : visible for user staff admin
- cv.Trainings.insert : visible for user staff admin
- cv.Trainings.merge_row : visible for admin
- dashboard.Widgets.merge_row : visible for admin
- dupable.PhoneticWords.merge_row : visible for admin
- excerpts.ExcerptTypes.detail : visible for staff admin
- excerpts.ExcerptTypes.insert : visible for staff admin
- excerpts.ExcerptTypes.merge_row : visible for admin
- excerpts.Excerpts.detail : visible for user coordinator secretary staff admin
- excerpts.Excerpts.merge_row : visible for admin
- gfks.ContentTypes.detail : visible for admin
- gfks.ContentTypes.merge_row : visible for admin
- gfks.HelpTexts.merge_row : visible for admin
- households.Households.detail : visible for user secretary staff admin
- households.Households.merge_row : visible for admin
- households.Members.merge_row : visible for admin
- households.MembersByPerson.insert : visible for user secretary staff admin
- households.Types.detail : visible for staff admin
- households.Types.merge_row : visible for admin
- languages.Languages.detail : visible for staff admin
- languages.Languages.merge_row : visible for admin
- lists.ListTypes.merge_row : visible for admin
- lists.Lists.detail : visible for user secretary staff admin
- lists.Lists.insert : visible for user secretary staff admin
- lists.Lists.merge_row : visible for admin
- lists.Members.merge_row : visible for admin
- notify.Messages.merge_row : visible for admin
- polls.AnswerChoices.merge_row : visible for admin
- polls.AnswerRemarks.detail : visible for user staff admin
- polls.AnswerRemarks.insert : visible for user staff admin
- polls.AnswerRemarks.merge_row : visible for admin
- polls.ChoiceSets.detail : visible for staff admin
- polls.ChoiceSets.merge_row : visible for admin
- polls.Choices.merge_row : visible for admin
- polls.Polls.detail : visible for user staff admin
- polls.Polls.insert : visible for user staff admin
- polls.Polls.merge_row : visible for admin
- polls.Questions.detail : visible for staff admin
- polls.Questions.merge_row : visible for admin
- polls.Responses.detail : visible for user staff admin
- polls.Responses.insert : visible for user staff admin
- polls.Responses.merge_row : visible for admin
- sessions.SessionTable.merge_row : visible for admin
- system.SiteConfigs.detail : visible for admin
- system.SiteConfigs.merge_row : visible for admin
- trends.TrendAreas.detail : visible for staff admin
- trends.TrendAreas.merge_row : visible for admin
- trends.TrendEvents.merge_row : visible for admin
- trends.TrendStages.detail : visible for user staff admin
- trends.TrendStages.insert : visible for user staff admin
- trends.TrendStages.merge_row : visible for admin
- uploads.AllUploads.detail : visible for staff admin
- uploads.AllUploads.insert : visible for staff admin
- uploads.UploadTypes.detail : visible for staff admin
- uploads.UploadTypes.insert : visible for staff admin
- uploads.UploadTypes.merge_row : visible for admin
- uploads.Uploads.detail : visible for teacher user auditor coordinator secretary staff admin
- uploads.Uploads.insert : visible for teacher user coordinator secretary staff admin
- uploads.Uploads.merge_row : visible for admin
- uploads.UploadsByClient.insert : visible for user secretary staff admin
- uploads.UploadsByController.insert : visible for teacher user coordinator secretary staff admin
- users.AllUsers.send_welcome_email : visible for admin
- users.Authorities.merge_row : visible for admin
- users.Users.change_password : visible for teacher user auditor coordinator secretary staff admin
- users.Users.detail : visible for teacher user auditor coordinator secretary staff admin
- users.Users.insert : visible for teacher user coordinator secretary staff admin
- users.Users.merge_row : visible for admin
- users.UsersOverview.sign_in : visible for all
<BLANKLINE>


Names of participants
=====================

The names of the participants are confidential data in :ref:`avanti`.

System admins can see the full names:

>>> obj = courses.Course.objects.get(pk=1)
>>> rt.login('rolf').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================ ================= ==================================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
 ID               Date of request   Client                               Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
---------------- ----------------- ------------------------------------ -------- ------------- ----------- -------- ----- --------- -------- -------------- --------------------------------------------------
 `9 <Detail>`__   07/02/2017        `ABDI Aátifá (136) <Detail>`__       Female                 No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `7 <Detail>`__   09/02/2017        `ABDELNOUR Aámir (125) <Detail>`__   Male                   No          No       No    No                                **Confirmed** → [Cancelled] [Requested] [Trying]
 `5 <Detail>`__   11/02/2017        `ABDALLAH Aáish (127) <Detail>`__    Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `3 <Detail>`__   13/02/2017        `ABBASI Aáishá (118) <Detail>`__     Female                 No          No       No    No                 16,67          **Confirmed** → [Cancelled] [Requested] [Trying]
 `1 <Detail>`__   15/02/2017        `ABAD Aábdeen (114) <Detail>`__      Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
                                                                                                                                              **16,67**
================ ================= ==================================== ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
<BLANKLINE>

Teachers and coordinators *can* see the full names (they need it
because they must register presences and absences), but they cannot
click on a name to see any detail.

>>> rt.login('laura').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================ ================= ========================= ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
 ID               Date of request   Client                    Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
---------------- ----------------- ------------------------- -------- ------------- ----------- -------- ----- --------- -------- -------------- --------------------------------------------------
 `9 <Detail>`__   07/02/2017        *ABDI Aátifá (136)*       Female                 No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `7 <Detail>`__   09/02/2017        *ABDELNOUR Aámir (125)*   Male                   No          No       No    No                                **Confirmed** → [Cancelled] [Requested] [Trying]
 `5 <Detail>`__   11/02/2017        *ABDALLAH Aáish (127)*    Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `3 <Detail>`__   13/02/2017        *ABBASI Aáishá (118)*     Female                 No          No       No    No                 16,67          **Confirmed** → [Cancelled] [Requested] [Trying]
 `1 <Detail>`__   15/02/2017        *ABAD Aábdeen (114)*      Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
                                                                                                                                   **16,67**
================ ================= ========================= ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
<BLANKLINE>


>>> rt.login('martina').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================ ================= ========================= ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
 ID               Date of request   Client                    Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
---------------- ----------------- ------------------------- -------- ------------- ----------- -------- ----- --------- -------- -------------- --------------------------------------------------
 `9 <Detail>`__   07/02/2017        *ABDI Aátifá (136)*       Female                 No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `7 <Detail>`__   09/02/2017        *ABDELNOUR Aámir (125)*   Male                   No          No       No    No                                **Confirmed** → [Cancelled] [Requested] [Trying]
 `5 <Detail>`__   11/02/2017        *ABDALLAH Aáish (127)*    Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
 `3 <Detail>`__   13/02/2017        *ABBASI Aáishá (118)*     Female                 No          No       No    No                 16,67          **Confirmed** → [Cancelled] [Requested] [Trying]
 `1 <Detail>`__   15/02/2017        *ABAD Aábdeen (114)*      Male                   No          No       No    No                                **Requested** → [Confirm] [Cancelled] [Trying]
                                                                                                                                   **16,67**
================ ================= ========================= ======== ============= =========== ======== ===== ========= ======== ============== ==================================================
<BLANKLINE>


But auditors see only the pupil's number and place:

>>> rt.login('audrey').show('courses.EnrolmentsByCourse', obj, show_links=True)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
================ ================= ==================== ======== ============= =========== ======== ===== ========= ======== ============== ===============
 ID               Date of request   Client               Gender   Nationality   Childcare   School   Bus   Evening   Remark   Missing rate   Workflow
---------------- ----------------- -------------------- -------- ------------- ----------- -------- ----- --------- -------- -------------- ---------------
 `9 <Detail>`__   07/02/2017        *(136) from Eupen*   Female                 No          No       No    No                                **Requested**
 `7 <Detail>`__   09/02/2017        *(125) from Eupen*   Male                   No          No       No    No                                **Confirmed**
 `5 <Detail>`__   11/02/2017        *(127) from Eupen*   Male                   No          No       No    No                                **Requested**
 `3 <Detail>`__   13/02/2017        *(118) from Eupen*   Female                 No          No       No    No                 16,67          **Confirmed**
 `1 <Detail>`__   15/02/2017        *(114) from Eupen*   Male                   No          No       No    No                                **Requested**
                                                                                                                              **16,67**
================ ================= ==================== ======== ============= =========== ======== ===== ========= ======== ============== ===============
<BLANKLINE>




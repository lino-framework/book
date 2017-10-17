.. _avanti.specs.roles:

=========================
User roles in Lino Avanti
=========================

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

Menus
-----

>>> rt.login('robin').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Contacts : Persons, Organizations, Clients, My Clients, Households, Partner Lists
- Office : My Comments, My Notification messages, My expiring uploads, My Uploads, Plausibility problems assigned to me, My Excerpts
- Calendar : Calendar, My appointments, Overdue appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
- Polls : My Polls, My Responses
- Activities : My Activities, Activities, -, Activity lines, Pending requested enrolments, Pending confirmed enrolments, Course planning
- Configure :
  - System : Site Parameters, Users, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, Household Types, List Types
  - Office : Comment Types, Upload Types, Excerpt Types
  - Coachings : Coaching types, Coaching termination reasons, Client Contact types
  - Career : Languages, Education Types, Education Levels, Job Sectors, Job Functions, Work Regimes, Statuses, Contract Durations
  - Trends : Trend areas, Trend stages
  - Polls : Choice Sets
  - Calendar : Calendars, Rooms, Priorities, Recurring events, Guest Roles, Calendar entry types, Recurrency policies, Remote Calendars
  - Activities : Topics, Timetable Slots
- Explorer :
  - System : Authorities, User types, content types, Notification messages, Changes, Phonetic words, Plausibility checkers, Plausibility problems, All dashboard widgets
  - Contacts : Contact Persons, Partners, Clients, Household member roles, Household Members, List memberships
  - Office : Comments, Uploads, Upload Areas, Excerpts
  - Coachings : Coachings, Client Contacts
  - Career : language knowledges, Trainings, Studies, Job Experiences
  - Trends : Trend events
  - Polls : Polls, Questions, Choices, Responses, Answer Choices, Answer Remarks
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Event states, Guest states, Task states
  - Activities : Activities, Enrolments, Enrolment states, Reminders
- Site : About

>>> rt.login('laura').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Office : My Notification messages, My expiring uploads, My Uploads
- Calendar : My appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
- Activities : My Activities, -, My courses given
- Site : About

>>> rt.login('audrey').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
- Office : My Notification messages, My expiring uploads, My Uploads
- Calendar : My appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments
- Activities : My Activities, Activities, -, Activity lines, Course planning
- Explorer :
  - Contacts : Clients
  - Calendar : Calendar entries, Presences
  - Activities : Activities, Enrolments
- Site : About



Windows and permissions
=======================

Each window layout is **viewable** by a given set of user user_types.

>>> print(analyzer.show_window_permissions())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- about.About.show : visible for all
- about.Models.detail : visible for teacher user staff admin
- avanti.Clients.detail : visible for user staff admin
- cal.Calendars.detail : visible for staff admin
- cal.Calendars.insert : visible for staff admin
- cal.EventTypes.detail : visible for staff admin
- cal.EventTypes.insert : visible for staff admin
- cal.Events.detail : visible for staff admin
- cal.Events.insert : visible for staff admin
- cal.GuestRoles.detail : visible for admin
- cal.Guests.detail : visible for teacher user auditor coordinator staff admin
- cal.Guests.insert : visible for teacher user coordinator staff admin
- cal.RecurrentEvents.detail : visible for staff admin
- cal.RecurrentEvents.insert : visible for staff admin
- cal.Rooms.detail : visible for staff admin
- cal.Rooms.insert : visible for staff admin
- cal.Tasks.detail : visible for staff admin
- cal.Tasks.insert : visible for staff admin
- changes.Changes.detail : visible for admin
- coachings.ClientContactTypes.detail : visible for staff admin
- coachings.CoachingEndings.detail : visible for staff admin
- comments.CommentTypes.detail : visible for staff admin
- comments.CommentTypes.insert : visible for staff admin
- comments.Comments.detail : visible for user staff admin
- comments.Comments.insert : visible for user staff admin
- comments.CommentsByRFC.insert : visible for user staff admin
- contacts.Companies.detail : visible for user staff admin
- contacts.Companies.insert : visible for user staff admin
- contacts.Partners.detail : visible for user staff admin
- contacts.Partners.insert : visible for user staff admin
- contacts.Persons.create_household : visible for user staff admin
- contacts.Persons.detail : visible for user staff admin
- contacts.Persons.insert : visible for user staff admin
- countries.Countries.detail : visible for staff admin
- countries.Countries.insert : visible for staff admin
- countries.Places.detail : visible for staff admin
- courses.Activities.detail : visible for teacher user auditor coordinator staff admin
- courses.Activities.insert : visible for teacher user coordinator staff admin
- courses.Activities.print_presence_sheet : visible for teacher user auditor coordinator staff admin
- courses.Activities.print_presence_sheet_html : visible for teacher user auditor coordinator staff admin
- courses.Enrolments.detail : visible for teacher user staff admin
- courses.Enrolments.insert : visible for teacher user staff admin
- courses.EnrolmentsByCourse.insert : visible for teacher user coordinator staff admin
- courses.EnrolmentsByPupil.insert : visible for user coordinator staff admin
- courses.Lines.detail : visible for user auditor coordinator staff admin
- courses.Lines.insert : visible for user coordinator staff admin
- courses.RemindersByEnrolment.detail : visible for user staff admin
- courses.RemindersByEnrolment.insert : visible for user staff admin
- courses.Slots.detail : visible for admin
- courses.Slots.insert : visible for admin
- courses.StatusReport.show : visible for user auditor coordinator staff admin
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
- cv.Trainings.detail : visible for teacher user staff admin
- cv.Trainings.insert : visible for teacher user staff admin
- excerpts.ExcerptTypes.detail : visible for staff admin
- excerpts.ExcerptTypes.insert : visible for staff admin
- excerpts.Excerpts.detail : visible for user staff admin
- gfks.ContentTypes.detail : visible for admin
- households.Households.detail : visible for user staff admin
- households.Types.detail : visible for staff admin
- languages.Languages.detail : visible for staff admin
- lists.Lists.detail : visible for user staff admin
- lists.Lists.insert : visible for user staff admin
- plausibility.Checkers.detail : visible for admin
- plausibility.Problems.detail : visible for teacher user staff admin
- polls.AnswerRemarks.detail : visible for user staff admin
- polls.AnswerRemarks.insert : visible for user staff admin
- polls.ChoiceSets.detail : visible for staff admin
- polls.Polls.detail : visible for user staff admin
- polls.Polls.insert : visible for user staff admin
- polls.Questions.detail : visible for staff admin
- polls.Responses.detail : visible for user staff admin
- polls.Responses.insert : visible for user staff admin
- system.SiteConfigs.detail : visible for admin
- trends.TrendAreas.detail : visible for staff admin
- trends.TrendStages.detail : visible for user staff admin
- trends.TrendStages.insert : visible for user staff admin
- uploads.AllUploads.detail : visible for staff admin
- uploads.AllUploads.insert : visible for staff admin
- uploads.UploadTypes.detail : visible for staff admin
- uploads.UploadTypes.insert : visible for staff admin
- uploads.Uploads.detail : visible for teacher user auditor coordinator staff admin
- uploads.Uploads.insert : visible for teacher user coordinator staff admin
- uploads.UploadsByClient.insert : visible for user staff admin
- uploads.UploadsByController.insert : visible for teacher user coordinator staff admin
- users.AllUsers.send_welcome_email : visible for admin
- users.Users.change_password : visible for teacher user staff admin
- users.Users.detail : visible for teacher user staff admin
- users.Users.insert : visible for teacher user staff admin
- users.UsersOverview.sign_in : visible for all
<BLANKLINE>

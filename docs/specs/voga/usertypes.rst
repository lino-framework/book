.. doctest docs/specs/voga/usertypes.rst
.. _voga.specs.profiles:

=============
User types
=============

This page documents the user types available in Lino Voga.
It uses the roger demo, the most complex variant.

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.roger.settings.doctests')
>>> from lino.api.doctest import *


Site administrator
==================

Robin is a :term:`site administrator`, he has a complete menu:

>>> ses = rt.login('robin')
>>> ses.user.user_type
<users.UserTypes.admin:900>
>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Outbox, My Excerpts, My Upload files
- Calendar : My appointments, Overdue appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Bookings, Calendar
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Topics, Activity lines, -, Pending requested enrolments, Pending confirmed enrolments
- Sales : Create invoices, Sales invoices (SLS), Sales credit notes (SLC)
- Accounting :
  - Purchases : Purchase invoices (PRC)
  - Wages : Paychecks (SAL)
  - Financial : Bestbank Payment Orders (PMO), Cash book (CSH), Bestbank (BNK)
  - VAT : VAT declarations (VAT)
  - Miscellaneous transactions : Miscellaneous transactions (MSC), Preliminary transactions (PRE)
- Reports :
  - Activities : Status Report
  - Sales : Due invoices, Sales invoice journal
  - Accounting : Debtors, Creditors
  - VAT : Purchase journal, Intra-Community purchases, Intra-Community sales
- Configure :
  - System : Users, Site Parameters, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, List Types
  - Calendar : Calendars, Rooms, Recurring events, Guest roles, Calendar entry types, Recurrency policies, Remote Calendars, Planner rows
  - Activities : Activity types, Instructor Types, Participant Types, Timetable Slots
  - Fees : Fees, Fee categories
  - Sales : Paper types, Flatrates, Invoicing areas
  - Office : Note Types, Event Types, Excerpt Types, Library volumes, Upload types
  - Accounting : Accounts, Journals, Fiscal years, Accounting periods, Payment terms
- Explorer :
  - System : Authorities, User types, User roles, Data checkers, Data problems, Changes, content types
  - Contacts : Contact persons, Partners, Contact detail types, Contact details, List memberships
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Entry states, Presence states, Task states, Planner columns, Access classes, Display colors
  - Activities : Activities, Enrolments, Enrolment states, Course layouts, Activity states
  - Sales : Price factors, Sales invoices, Sales invoice items, Invoicing plans, Sales rules
  - Financial : Bank Statements, Journal Entries, Payment Orders
  - SEPA : Bank accounts
  - Office : Notes, Outgoing Mails, Attachments, Excerpts, Upload files, Upload areas
  - Accounting : Common accounts, Match rules, Vouchers, Voucher types, Movements, Trade types, Journal groups
  - VAT : Special Belgian VAT declarations, Declaration fields, VAT areas, VAT regimes, VAT classes, VAT columns, Invoices, VAT rules
- Site : About


Monique is a secretary.

>>> print(rt.login('monique').user.user_type)
200 (Secretary)

>>> rt.login('monique').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Outbox, My Excerpts, My Upload files
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Activity lines, -, Pending requested enrolments, Pending confirmed enrolments
- Sales : Create invoices, Sales invoices (SLS), Sales credit notes (SLC)
- Accounting :
  - Purchases : Purchase invoices (PRC)
  - Wages : Paychecks (SAL)
  - Financial : Bestbank Payment Orders (PMO), Cash book (CSH), Bestbank (BNK)
  - VAT : VAT declarations (VAT)
  - Miscellaneous transactions : Miscellaneous transactions (MSC), Preliminary transactions (PRE)
- Reports :
  - Activities : Status Report
  - Sales : Due invoices, Sales invoice journal
  - Accounting : Debtors, Creditors
  - VAT : Purchase journal, Intra-Community purchases, Intra-Community sales
- Configure :
  - System : Site Parameters, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, List Types
  - Calendar : Guest roles
  - Activities : Activity types, Instructor Types, Participant Types
  - Fees : Fees, Fee categories
  - Sales : Flatrates
- Explorer :
  - System : Data checkers, Data problems, Changes, content types
  - Contacts : Contact persons, Partners, Contact details, List memberships
  - Calendar : Calendar entries, Presences, Entry states, Presence states, Task states, Planner columns, Access classes, Display colors
  - Activities : Activities, Enrolments
  - Sales : Price factors, Sales invoices
  - VAT : Special Belgian VAT declarations, Declaration fields, Invoices, VAT rules
- Site : About


Marianne is a "simple user".

>>> print(rt.login('marianne').user.user_type)
100 (User)

>>> rt.login('marianne').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Outbox, My Excerpts, My Upload files
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Activity lines
- Sales : Create invoices, Sales invoices (SLS), Sales credit notes (SLC)
- Accounting :
  - Purchases : Purchase invoices (PRC)
  - Wages : Paychecks (SAL)
  - Financial : Bestbank Payment Orders (PMO), Cash book (CSH), Bestbank (BNK)
  - VAT : VAT declarations (VAT)
  - Miscellaneous transactions : Miscellaneous transactions (MSC), Preliminary transactions (PRE)
- Reports :
  - Activities : Status Report
  - Sales : Due invoices, Sales invoice journal
  - Accounting : Debtors, Creditors
  - VAT : Purchase journal, Intra-Community purchases, Intra-Community sales
- Configure :
  - Activities : Activity types, Instructor Types, Participant Types
  - Sales : Flatrates
- Explorer :
  - Contacts : Partners
  - Sales : Price factors, Sales invoices
  - VAT : Special Belgian VAT declarations, Declaration fields, Invoices, VAT rules
- Site : About

>>> rt.login('tom').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Activities : My courses given
- Site : About

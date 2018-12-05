.. doctest docs/specs/voga/usertypes.rst
.. _voga.specs.profiles:

=============
User types
=============

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *


System administrator
====================

Robin is a system administrator, he has a complete menu:

>>> ses = rt.login('robin') 
>>> ses.user.user_type
users.UserTypes.admin:900
>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Uploads, My Outbox, My Excerpts
- Calendar : My appointments, Overdue appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Bookings, Calendar
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Topics, Activity lines, -, Pending requested enrolments, Pending confirmed enrolments
- Sales : Create invoices, Sales invoices (SLS), Sales credit notes (SLC)
- Accounting :
  - Purchases : Purchase invoices (PRC)
  - Financial : Bestbank Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
  - VAT : VAT declarations (VAT)
- Reports :
  - Activities : Status Report
  - Sales : Purchase journal, Intra-Community purchases, Intra-Community sales, Due invoices, Sales invoice journal
  - Accounting : Debtors, Creditors
- Configure :
  - System : Site Parameters, Users, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, List Types
  - Calendar : Calendars, Rooms, Priorities, Recurring events, Guest roles, Calendar entry types, Recurrency policies, Remote Calendars, Planner rows
  - Activities : Activity types, Instructor Types, Participant Types, Timetable Slots
  - Fees : Fees, Fee categories
  - Sales : Paper types, Flatrates
  - Accounting : Accounts, Journals, Fiscal years, Accounting periods, Payment terms
  - Office : Note Types, Event Types, Upload Types, Excerpt Types
- Explorer :
  - System : Authorities, User types, User roles, content types, Data checkers, Data problems, Changes
  - Contacts : Contact Persons, Partners, List memberships
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Event states, Guest states, Task states
  - Activities : Activities, Enrolments, Enrolment states, Course layouts
  - Sales : VAT areas, VAT regimes, VAT classes, VAT columns, Invoices, VAT rules, Sales invoices, Sales invoice items, Invoicing plans, Sales rules
  - Accounting : Common accounts, Match rules, Vouchers, Voucher types, Movements, Trade types, Journal groups
  - Financial : Bank Statements, Journal Entries, Payment Orders
  - SEPA : Bank accounts
  - VAT : Special Belgian VAT declarations, Declaration fields
  - Office : Notes, Uploads, Upload Areas, Outgoing Mails, Attachments, Excerpts
- Site : About


Monique is a secretary.   

>>> print(rt.login('monique').user.user_type)
200 (Secretary)

>>> rt.login('monique').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Uploads, My Outbox, My Excerpts
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Activity lines, -, Pending requested enrolments, Pending confirmed enrolments
- Sales : Create invoices, Sales invoices (SLS), Sales credit notes (SLC)
- Accounting :
  - Purchases : Purchase invoices (PRC)
  - Financial : Bestbank Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
  - VAT : VAT declarations (VAT)
- Reports :
  - Activities : Status Report
  - Sales : Purchase journal, Intra-Community purchases, Intra-Community sales, Due invoices, Sales invoice journal
  - Accounting : Debtors, Creditors
- Configure :
  - System : Site Parameters, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, List Types
  - Calendar : Guest roles
  - Activities : Activity types, Instructor Types, Participant Types
  - Fees : Fees, Fee categories
  - Sales : Flatrates
- Explorer :
  - System : content types, Data checkers, Data problems, Changes
  - Contacts : Contact Persons, Partners, List memberships
  - Calendar : Calendar entries, Presences, Event states, Guest states, Task states
  - Activities : Activities, Enrolments
  - Sales : Invoices, VAT rules, Sales invoices
  - VAT : Special Belgian VAT declarations, Declaration fields
- Site : About


Marianne is a "simple user".

>>> print(rt.login('marianne').user.user_type)
100 (User)

>>> rt.login('marianne').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Uploads, My Outbox, My Excerpts
- Calendar : My appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Activity lines
- Sales : Create invoices, Sales invoices (SLS), Sales credit notes (SLC)
- Accounting :
  - Purchases : Purchase invoices (PRC)
  - Financial : Bestbank Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
  - VAT : VAT declarations (VAT)
- Reports :
  - Activities : Status Report
  - Sales : Purchase journal, Intra-Community purchases, Intra-Community sales, Due invoices, Sales invoice journal
  - Accounting : Debtors, Creditors
- Configure :
  - Activities : Activity types, Instructor Types, Participant Types
  - Sales : Flatrates
- Explorer :
  - Contacts : Partners
  - Sales : Invoices, VAT rules, Sales invoices
  - VAT : Special Belgian VAT declarations, Declaration fields
- Site : About

>>> rt.login('tom').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Activities : My courses given
- Site : About

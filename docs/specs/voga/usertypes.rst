.. _voga.specs.profiles:

=============
User types
=============

.. To run only this test::

    $ doctest docs/specs/usertypes.rst

    doctest init:

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
- Calendar : My appointments, Overdue appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Bookings, Calendar
- Accounting :
  - Sales : Sales invoices (SLS), Sales credit notes (SLC)
  - Purchases : Purchase invoices (PRC)
  - Financial : Bestbank Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
  - VAT : VAT declarations (VAT)
  - Create invoices
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Topics, Activity lines, -, Pending requested enrolments, Pending confirmed enrolments
- Reports :
  - Accounting : Accounting Report, Debtors, Creditors, Purchase journal, Intra-Community purchases, Intra-Community sales, Due invoices, Sales invoice journal
  - Activities : Status Report
- Configure :
  - System : Site Parameters, Users, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, List Types
  - Calendar : Calendars, Rooms, Priorities, Recurring events, Guest Roles, Calendar entry types, Recurrency policies, Remote Calendars
  - Tariffs : Tariffs, Tariff Categories
  - Accounting : Account Groups, Accounts, Journals, Accounting periods, Payment Terms
  - VAT : Paper types
  - Activities : Activity types, Instructor Types, Participant Types, Timetable Slots
  - Office : Note Types, Event Types, Upload Types, Excerpt Types
- Explorer :
  - System : Authorities, User types, content types, Data checkers, Data problems, Changes
  - Contacts : Contact Persons, Partners, List memberships
  - Calendar : Calendar entries, Tasks, Presences, Subscriptions, Event states, Guest states, Task states
  - Accounting : Common accounts, Match rules, Vouchers, Voucher types, Movements, Fiscal Years, Trade types, Journal groups
  - VAT : VAT regimes, VAT Classes, VAT columns, Invoices, VAT rules, Product invoices, Product invoice items, Invoicing plans, Special Belgian VAT declarations, Declaration fields
  - Activities : Activities, Enrolments, Enrolment states
  - Financial : Bank Statements, Journal Entries, Payment Orders
  - SEPA : Bank accounts
  - Office : Notes, Uploads, Upload Areas, Outgoing Mails, Attachments, Excerpts
- Site : About


Monique is a secretary.   

>>> print(rt.login('monique').user.user_type)
Secretary

>>> rt.login('monique').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Uploads, My Outbox, My Excerpts
- Calendar : My appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Accounting :
  - Sales : Sales invoices (SLS), Sales credit notes (SLC)
  - Purchases : Purchase invoices (PRC)
  - Financial : Bestbank Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
  - VAT : VAT declarations (VAT)
  - Create invoices
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Activity lines, -, Pending requested enrolments, Pending confirmed enrolments
- Reports :
  - Accounting : Accounting Report, Debtors, Creditors, Purchase journal, Intra-Community purchases, Intra-Community sales, Due invoices, Sales invoice journal
  - Activities : Status Report
- Configure :
  - System : Site Parameters, Help Texts
  - Places : Countries, Places
  - Contacts : Organization types, Functions, List Types
  - Calendar : Guest Roles
  - Tariffs : Tariffs, Tariff Categories
  - Activities : Activity types, Instructor Types, Participant Types
- Explorer :
  - System : content types, Data checkers, Data problems, Changes
  - Contacts : Contact Persons, Partners, List memberships
  - Calendar : Calendar entries, Presences, Event states, Guest states, Task states
  - VAT : Invoices, VAT rules, Product invoices, Special Belgian VAT declarations, Declaration fields
  - Activities : Activities, Enrolments
- Site : About


Marianne is a "simple user".

>>> print(rt.login('marianne').user.user_type)
User

>>> rt.login('marianne').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Office : Data problems assigned to me, My Notes, My Uploads, My Outbox, My Excerpts
- Calendar : My appointments, Unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Accounting :
  - Sales : Sales invoices (SLS), Sales credit notes (SLC)
  - Purchases : Purchase invoices (PRC)
  - Financial : Bestbank Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
  - VAT : VAT declarations (VAT)
  - Create invoices
- Activities : Participants, Instructors, -, Courses, Hikes, Journeys, -, Activity lines, -
- Reports :
  - Accounting : Accounting Report, Debtors, Creditors, Purchase journal, Intra-Community purchases, Intra-Community sales, Due invoices, Sales invoice journal
  - Activities : Status Report
- Configure :
  - Activities : Activity types, Instructor Types, Participant Types
- Explorer :
  - Contacts : Partners
  - VAT : Invoices, VAT rules, Product invoices, Special Belgian VAT declarations, Declaration fields
- Site : About

>>> rt.login('tom').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Activities : My courses given, -
- Site : About

=========
Lino Mini
=========


The demo projects :mod:`lino_book.projects.min1` to
:mod:`lino_book.projects.min9` are a series of **minimalistic
applications** used by a number of tests and tutorials.

- min1 : just contacts
- min2 : adds calendar functionality
- min3 : replace the single phone, gsm and email fields by multiple
  contact details
- min9 : 


min1
====

A minimalistic application for managing your contacts.

**Features**

- Store your contacts in a database and have them accessible by
  multiple users.
- Differentiate between persons and organizations
- Store the role of a person in an organization

**Implementation notes**

- :mod:`lino.modlib.system`
- :mod:`lino.modlib.users`
- :mod:`lino_xl.lib.contacts` (which needs :mod:`lino_xl.lib.countries`)

  
min2
====

A minimalistic application for managing your contacts and your calendar.

**Features**

- Manage calendar entries for multiple users
- Warn about Unconfirmed and Overdue appointments
- Link calendar entries to your contacts
- Manage invitations to your events  
- Manage presences of your guests to your events
- Export data to `.xlsx` file.
  
**Implementation notes**

- :mod:`lino_xl.lib.cal` (which needs :mod:`lino.modlib.gfks`)
- :mod:`lino.modlib.export_excel`


**Missing features**

- Synchronize with popular contacts and calendar services

  

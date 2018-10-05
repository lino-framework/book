.. doctest docs/specs/cosi/apc.rst
.. _cosi.tested.demo:
.. _specs.cosi.apc:

====================
The apc demo project
====================

..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.apc.settings.doctests')
    >>> from lino.api.doctest import *
    >>> ses = rt.login('robin')

Implementation details
======================
    
>>> print(settings.SETTINGS_MODULE)
lino_book.projects.apc.settings.doctests

>>> print(' '.join([lng.name for lng in settings.SITE.languages]))
de fr en
    

The demo database contains 69 persons and 23 companies.

>>> contacts.Person.objects.count()
69
>>> contacts.Company.objects.count()
24
>>> contacts.Partner.objects.count()
93


>>> print(' '.join(settings.SITE.demo_fixtures))
std few_countries minimal_ledger furniture demo demo_bookings payments demo2



The application menu
====================

Robin is the system administrator, he has a complete menu:

>>> ses = rt.login('robin') 
>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations
- Accounting :
  - Sales : Sales invoices (SLS), Sales credit notes (SLC)
  - Purchases : Purchase invoices (PRC)
  - Financial : Bestbank Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
  - VAT : VAT declarations (VAT)
  - Create invoices
- Products : Products, Product Categories
- Office : My Excerpts
- Reports :
  - Accounting : Debtors, Creditors, Purchase journal, Intra-Community purchases, Intra-Community sales, Due invoices, Sales invoice journal
- Configure :
  - System : Site Parameters, Help Texts, Users
  - Places : Countries, Places
  - Contacts : Organization types, Functions
  - Accounting : Accounts, Journals, Fiscal years, Accounting periods, Payment terms
  - Office : Excerpt Types, My Text Field Templates
  - VAT : Paper types
- Explorer :
  - System : content types, Authorities, User types, User roles
  - Contacts : Contact Persons, Partners
  - Accounting : Common accounts, Match rules, Vouchers, Voucher types, Movements, Trade types, Journal groups
  - SEPA : Bank accounts
  - Office : Excerpts, Text Field Templates
  - VAT : VAT areas, VAT regimes, VAT classes, VAT columns, Invoices, VAT rules, Product invoices, Product invoice items, Invoicing plans, Sales rules, Belgian VAT declarations, Declaration fields
  - Financial : Bank Statements, Journal Entries, Payment Orders
- Site : About


Database structure
==================


>>> from lino.utils.diag import analyzer
>>> print analyzer.show_database_structure()
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +ELLIPSIS +SKIP


Miscellaneous
=============

Person #115 is not a Partner
----------------------------

Person #115 (u'Altenberg Hans') is not a Partner (master_key 
is <django.db.models.fields.related.ForeignKey: partner>)

>>> url = '/bs3/contacts/Person/115'
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200


Slave tables with more than 15 rows
-----------------------------------

When you look at the detail window of Belgium in `Lino Così
<http://demo4.lino-framework.org/api/countries/Countries/BE?an=detail>`_
then you see a list of all places in Belgium.
This demo database contains exactly 48 entries:

>>> be = countries.Country.objects.get(isocode="BE")
>>> be.place_set.count()
48

>>> countries.PlacesByCountry.request(be).get_total_count()
48

>>> url = '/api/countries/PlacesByCountry?fmt=json&start=0&mt=10&mk=BE'
>>> res = test_client.get(url,REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content.decode('utf-8'))
>>> print(len(result['rows']))
15

The 15 is because Lino has a hard-coded default value of  
returning only 15 rows when no limit has been specified.

In versions after :blogref:`20130903` you can change that limit 
for a given table by overriding the 
:attr:`preview_limit <lino.core.tables.AbstractTable.preview_limit>`
parameter of your table definition.
Or you can change it globally for all your tables 
by setting the 
:attr:`preview_limit <ad.Site.preview_limit>`
Site attribute to either `None` or some bigger value.

This parameter existed before but wasn't tested.
In your code this would simply look like this::

  class PlacesByCountry(Places):
      preview_limit = 30

Here we override it on the living object:

>>> countries.PlacesByCountry.preview_limit = 25

Same request returns now 25 data rows:

>>> res = test_client.get(url, REMOTE_USER='robin')
>>> result = json.loads(res.content.decode('utf-8'))
>>> print(len(result['rows']))
25

To remove the limit altogether, you can say:

>>> countries.PlacesByCountry.preview_limit = None

and the same request now returns all 49 data rows:

>>> res = test_client.get(url,REMOTE_USER='robin')
>>> result = json.loads(res.content.decode('utf-8'))
>>> print(len(result['rows']))
49









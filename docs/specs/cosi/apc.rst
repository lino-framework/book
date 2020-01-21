.. doctest docs/specs/cosi/apc.rst
.. _cosi.tested.demo:
.. _specs.cosi.apc:

====================
The apc demo project
====================

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *
>>> ses = rt.login('robin')


>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 32 plugins
- 52 models
- 13 user roles
- 3 user types
- 185 views
- 14 dialog actions
<BLANKLINE>



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
- Office : My Excerpts, My Upload files
- Sales : Sales invoices (SLS), Sales credit notes (SLC)
- Accounting :
  - Purchases : Purchase invoices (PRC)
  - Wages : Paychecks (SAL)
  - Financial : Bestbank Payment Orders (PMO), Cash book (CSH), Bestbank (BNK)
  - VAT : VAT declarations (VAT)
  - Miscellaneous transactions : Miscellaneous transactions (MSC), Preliminary transactions (PRE)
- Reports :
  - Sales : Due invoices, Sales invoice journal
  - Accounting : Accounting Report, Debtors, Creditors
  - VAT : Purchase journal, Intra-Community purchases, Intra-Community sales
- Configure :
  - System : Help Texts, Users, Site Parameters
  - Places : Countries, Places
  - Contacts : Organization types, Functions
  - Office : Excerpt Types, Library volumes, Upload types, My Text Field Templates
  - Sales : Products, Product Categories, Price rules, Paper types
  - Accounting : Sheet items, Accounts, Journals, Fiscal years, Accounting periods, Payment terms
- Explorer :
  - System : content types, Authorities, User types, User roles, Data checkers, Data problems
  - Contacts : Contact Persons, Partners
  - Office : Excerpts, Upload files, Upload areas, Text Field Templates
  - SEPA : Bank accounts
  - Sales : Price factors, Sales invoices, Sales invoice items
  - Financial : Bank Statements, Journal Entries, Payment Orders
  - Accounting : Accounting Reports, Common accounts, Match rules, Vouchers, Voucher types, Movements, Trade types, Journal groups
  - VAT : Belgian VAT declarations, Declaration fields, VAT areas, VAT regimes, VAT classes, VAT columns, Invoices, VAT rules
- Site : About


Database structure
==================


>>> from lino.utils.diag import analyzer
>>> print analyzer.show_database_structure()
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +ELLIPSIS +SKIP


.. _internal_clearings:

Internal clearings
==================

An **internal clearing** is when an employee acts as a temporary cashier by
paying purchase invoices or taking money for sales invoices.  Lino

When a site has a non-empty :attr:`worker_model
<lino_xl.lib.ledger.Plugin.worker_model>`,  Lino adds a field :attr:`worker
<lino_xl.lib.ledger.PaymentTerm.worker>` to each payment term.

When an invoice is registered with a payment term having a :attr:`worker
<lino_xl.lib.ledger.PaymentTerm.worker>`, Lino will book two additional
movements: one which cleans the debit (credit) on the customer (provider) by
booking back the total amount, and a second to book the invoiced amount as a
debit or credit on the worker (using the :attr:`main_account
<lino_xl.lib.ledger.TradeType.main_account>` for :attr:`TradeTypes.wages
<lino_xl.lib.ledger.TradeTypes.wages>`).


>>> rt.show(ledger.PaymentTerms, language="en", column_names="ref name_en months days worker")
==================== ======================================= ======== ========= =================
 Reference            Designation (en)                        Months   Days      Worker
-------------------- --------------------------------------- -------- --------- -----------------
 07                   Payment seven days after invoice date   0        7
 10                   Payment ten days after invoice date     0        10
 30                   Payment 30 days after invoice date      0        30
 60                   Payment 60 days after invoice date      0        60
 90                   Payment 90 days after invoice date      0        90
 EOM                  Payment end of month                    0        0
 P30                  Prepayment 30%                          0        30
 PIA                  Payment in advance                      0        0
 robin                Cash Robin                              0        0         Mr Robin Dubois
 **Total (9 rows)**                                           **0**    **227**
==================== ======================================= ======== ========= =================
<BLANKLINE>

>>> dd.plugins.ledger.worker_model
<class 'lino_xl.lib.contacts.models.Person'>

And as we can see, our worker Robin owes us 9784,48 € because he took money for
7 sales invoices:

>>> robin = dd.plugins.ledger.worker_model.objects.get(first_name="Robin")
>>> rt.show(ledger.MovementsByPartner, master_instance=robin)
**7 offene Bewegungen (7362.36 €)**
>>> rt.show(ledger.MovementsByPartner, master_instance=robin, nosummary=True)
========== =============== ====================================================================== ============== ======== ================= ===========
 Valuta     Beleg           Beschreibung                                                           Debit          Kredit   Match             Beglichen
---------- --------------- ---------------------------------------------------------------------- -------------- -------- ----------------- -----------
 08.03.15   *SLS 11/2015*   *(4800) Internal clearings* | *Radermacher Inge* | *Dubois Robin*      2 039,82                **SLS 11/2015**   Nein
 07.01.15   *SLS 1/2015*    *(4800) Internal clearings* | *Radermacher Alfons* | *Dubois Robin*    31,92                   **SLS 1/2015**    Nein
 07.11.14   *SLS 49/2014*   *(4800) Internal clearings* | *Lazarus Line* | *Dubois Robin*          375,00                  **SLS 49/2014**   Nein
 10.09.14   *SLS 38/2014*   *(4800) Internal clearings* | *Ingels Irene* | *Dubois Robin*          600,00                  **SLS 38/2014**   Nein
 11.06.14   *SLS 29/2014*   *(4800) Internal clearings* | *Evertz Bernd* | *Dubois Robin*          2 299,81                **SLS 29/2014**   Nein
 07.05.14   *SLS 19/2014*   *(4800) Internal clearings* | *Bastiaensen Laurent* | *Dubois Robin*   1 199,85                **SLS 19/2014**   Nein
 10.02.14   *SLS 9/2014*    *(4800) Internal clearings* | *Hans Flott & Co* | *Dubois Robin*       815,96                  **SLS 9/2014**    Nein
                            **Saldo 7362.36 (7 Bewegungen)**                                       **7 362,36**
========== =============== ====================================================================== ============== ======== ================= ===========
<BLANKLINE>



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

This site shows a series of due sales invoices
(:class:`lino_xl.lib.sales.DueInvoices`).

>>> rt.show(sales.DueInvoices)
===================== =========== ========= ======================= =============== ================ ================
 Due date              Reference   No.       Partner                 Total to pay    Balance before   Balance to pay
--------------------- ----------- --------- ----------------------- --------------- ---------------- ----------------
 09/02/2014            SLS         9         Hans Flott & Co         815,96
 06/05/2014            SLS         19        Bastiaensen Laurent     1 199,85
 10/06/2014            SLS         29        Evertz Bernd            2 299,81
 09/09/2014            SLS         38        Ingels Irene            600,00
 06/11/2014            SLS         49        Lazarus Line            375,00
 06/01/2015            SLS         1         Radermacher Alfons      31,92
 14/02/2015            SLS         3         Radermacher Christian   719,60                           719,60
 07/03/2015            SLS         11        Radermacher Inge        2 039,82
 08/03/2015            SLS         12        Radermacher Jean        679,81                           679,81
 16/03/2015            SLS         13        di Rupo Didier          280,00                           280,00
 20/03/2015            SLS         14        da Vinci David          535,00                           535,00
 21/03/2015            SLS         15        da Vinci David          1 110,16        535,00           1 110,16
 05/04/2015            SLS         10        Radermacher Hedi        2 999,85                         2 999,85
 11/04/2015            SLS         6         Radermacher Fritz       1 759,71                         527,91
 12/04/2015            SLS         7         Radermacher Fritz       240,00          1 759,71         -4,80
 **Total (15 rows)**               **236**                           **15 686,49**   **2 294,71**     **6 847,53**
===================== =========== ========= ======================= =============== ================ ================
<BLANKLINE>

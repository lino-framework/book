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
- 3 user types
- 183 views
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
  - Contacts : Contact persons, Partners
  - Office : Excerpts, Upload files, Upload areas, Text Field Templates
  - SEPA : Bank accounts
  - Sales : Price factors, Sales invoices, Sales invoice items
  - Financial : Bank Statements, Journal Entries, Payment Orders
  - Accounting : Accounting Reports, Common sheet items, General account balances, Analytic accounts balances, Partner balances, Sheet item entries, Common accounts, Match rules, Vouchers, Voucher types, Movements, Trade types, Journal groups
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
**7 offene Bewegungen (-8908.45 €)**

>>> rt.show(ledger.MovementsByPartner, master_instance=robin, nosummary=True)
========== =============== ====================================================================== ============== ======== ============= ===========
 Valuta     Beleg           Beschreibung                                                           Debit          Kredit   Match         Beglichen
---------- --------------- ---------------------------------------------------------------------- -------------- -------- ------------- -----------
 08.03.15   *SLS 11/2015*   *(4800) Internal clearings* | *Radermacher Inge* | *Dubois Robin*      2 468,18                SLS 11/2015   Nein
 07.01.15   *SLS 1/2015*    *(4800) Internal clearings* | *Radermacher Alfons* | *Dubois Robin*    38,62                   SLS 1/2015    Nein
 07.11.14   *SLS 49/2014*   *(4800) Internal clearings* | *Lazarus Line* | *Dubois Robin*          453,75                  SLS 49/2014   Nein
 10.09.14   *SLS 38/2014*   *(4800) Internal clearings* | *Ingels Irene* | *Dubois Robin*          726,00                  SLS 38/2014   Nein
 11.06.14   *SLS 29/2014*   *(4800) Internal clearings* | *Evertz Bernd* | *Dubois Robin*          2 782,77                SLS 29/2014   Nein
 07.05.14   *SLS 19/2014*   *(4800) Internal clearings* | *Bastiaensen Laurent* | *Dubois Robin*   1 451,82                SLS 19/2014   Nein
 10.02.14   *SLS 9/2014*    *(4800) Internal clearings* | *Hans Flott & Co* | *Dubois Robin*       987,31                  SLS 9/2014    Nein
                            **Saldo 8908.45 (7 Bewegungen)**                                       **8 908,45**
========== =============== ====================================================================== ============== ======== ============= ===========
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
 09/02/2014            SLS         9         Hans Flott & Co         987,31
 06/05/2014            SLS         19        Bastiaensen Laurent     1 451,82
 10/06/2014            SLS         29        Evertz Bernd            2 782,77
 09/09/2014            SLS         38        Ingels Irene            726,00
 06/11/2014            SLS         49        Lazarus Line            453,75
 06/01/2015            SLS         1         Radermacher Alfons      38,62
 14/02/2015            SLS         3         Radermacher Christian   853,97                           853,97
 07/03/2015            SLS         11        Radermacher Inge        2 468,18
 08/03/2015            SLS         12        Radermacher Jean        822,57                           822,57
 16/03/2015            SLS         13        di Rupo Didier          338,80                           338,80
 20/03/2015            SLS         14        da Vinci David          647,35                           647,35
 21/03/2015            SLS         15        da Vinci David          1 299,08        647,35           1 299,08
 05/04/2015            SLS         10        Radermacher Hedi        3 629,82                         3 629,82
 11/04/2015            SLS         6         Radermacher Fritz       2 129,25                         638,77
 12/04/2015            SLS         7         Radermacher Fritz       290,40          2 129,25         -5,81
 **Total (15 rows)**               **236**                           **18 919,69**   **2 776,60**     **8 224,55**
===================== =========== ========= ======================= =============== ================ ================
<BLANKLINE>


>>> show_choicelists()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========================== ======== ================= ======================= ============================ ====================
 name                        #items   preferred_width   de                      fr                           en
--------------------------- -------- ----------------- ----------------------- ---------------------------- --------------------
 about.TimeZones             1        4                 Zeitzonen               Zeitzonen                    Time zones
 bevat.DeclarationFields     29       4                 Declaration fields      Declaration fields           Declaration fields
 checkdata.Checkers          8        45                Datentests              Tests de données             Data checkers
 contacts.CivilStates        7        27                Zivilstände             Etats civils                 Civil states
 contacts.PartnerEvents      1        18                Beobachtungskriterien   Évènements observés          Observed events
 countries.PlaceTypes        23       16                None                    None                         None
 excerpts.Shortcuts          0        4                 Excerpt shortcuts       Excerpt shortcuts            Excerpt shortcuts
 ledger.CommonAccounts       21       29                Gemeinkonten            Comptes communs              Common accounts
 ledger.DC                   2        6                 Booking directions      Booking directions           Booking directions
 ledger.JournalGroups        6        26                Journalgruppen          Groupes de journaux          Journal groups
 ledger.PeriodStates         2        14                Zustände                États                        States
 ledger.TradeTypes           6        18                Handelsarten            Types de commerce            Trade types
 ledger.VoucherStates        4        14                Belegzustände           Belegzustände                Voucher states
 ledger.VoucherTypes         6        55                Belegarten              Types de pièce               Voucher types
 printing.BuildMethods       5        20                None                    None                         None
 products.DeliveryUnits      3        5                 Delivery units          Delivery units               Delivery units
 products.PriceFactors       0        4                 Price factors           Price factors                Price factors
 products.ProductTypes       1        8                 Product types           Product types                Product types
 sheets.CommonItems          29       49                Common sheet items      Common sheet items           Common sheet items
 sheets.SheetTypes           2        16                Sheet types             Sheet types                  Sheet types
 system.Genders              2        8                 None                    None                         None
 system.PeriodEvents         3        9                 Beobachtungskriterien   Évènements observés          Observed events
 system.YesNo                2        12                Ja oder Nein            Oui ou non                   Yes or no
 uploads.Shortcuts           0        4                 Upload shortcuts        Upload shortcuts             Upload shortcuts
 uploads.UploadAreas         1        7                 Upload-Bereiche         Domaines de téléchargement   Upload areas
 users.UserTypes             3        21                Benutzerarten           Types d'utilisateur          User types
 vat.DeclarationFieldsBase   0        4                 Declaration fields      Declaration fields           Declaration fields
 vat.VatAreas                3        13                MWSt-Zonen              Zones TVA                    VAT areas
 vat.VatClasses              7        31                MwSt.-Klassen           Classes TVA                  VAT classes
 vat.VatColumns              10       39                MWSt-Kolonnen           MWSt-Kolonnen                VAT columns
 vat.VatRegimes              11       24                MwSt.-Regimes           MwSt.-Regimes                VAT regimes
 vat.VatRules                13       182               MwSt-Regeln             MwSt-Regeln                  VAT rules
 xl.Priorities               5        8                 Prioritäten             Priorités                    Priorities
=========================== ======== ================= ======================= ============================ ====================
<BLANKLINE>

Verify whether :ticket:`3657` is fixed:

>>> print(rt.find_config_file("logo.jpg", "weasyprint"))  #doctest: +ELLIPSIS
/.../lino_book/projects/apc/settings/config/weasyprint/logo.jpg

Verify whether :ticket:`3705` is fixed:

>>> for cd in settings.SITE.confdirs.config_dirs:
...     print(cd.name)  #doctest: +ELLIPSIS
/.../lino_book/projects/apc/settings/config
/.../lino_xl/lib/sheets/config
...
/.../lino/modlib/jinja/config
/.../lino/config

.. _cosi.tested.demo:
.. _specs.cosi.apc:

====================
The apc demo project
====================

.. This document is part of the Lino Così test suite. To run only this
   test:

    $ python setup.py test -s tests.SpecsTests.test_apc
    
    doctest init:

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
23
>>> contacts.Partner.objects.count()
92


>>> print(' '.join(settings.SITE.demo_fixtures))
std few_countries minimal_ledger euvatrates furniture demo demo_bookings payments demo2



The application menu
====================

Robin is the system administrator, he has a complete menu:

>>> ses = rt.login('robin') 
>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations
- Products : Products, Product Categories
- Accounting :
  - Sales : Sales invoices (SLS), Sales credit notes (SLC)
  - Purchases : Purchase invoices (PRC)
  - Financial : Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC), VAT declarations (VAT)
  - Create invoices
- Office : My Excerpts
- Reports :
  - Accounting : Situation, Activity Report, Debtors, Creditors
  - VAT : Due invoices
- Configure :
  - System : Site Parameters, Help Texts, Users
  - Places : Countries, Places
  - Contacts : Organization types, Functions
  - Accounting : Account Groups, Accounts, Journals, Accounting periods, Payment Terms
  - Office : Excerpt Types, My Text Field Templates
  - VAT : VAT rules, Paper types
- Explorer :
  - System : content types, Authorities, User types
  - Contacts : Contact Persons, Partners
  - Accounting : Match rules, Vouchers, Voucher types, Movements, Fiscal Years, Trade types, Journal groups
  - SEPA : Bank accounts
  - Office : Excerpts, Text Field Templates
  - VAT : VAT regimes, VAT Classes, Product invoices, Product invoice items, Invoicing plans, VAT declarations
  - Financial : Bank Statements, Journal Entries, Payment Orders
- Site : About

Romain gets the same menu in French:
  
>>> rt.login('romain').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Personnes, Organisationen
- Produkte : Produkte, Produktkategorien
- Comptabilité :
  - Verkauf : Factures vente (SLS), Gutschriften Verkauf (SLC)
  - Einkauf : Factures achat (PRC)
  - Finanzjournale : Zahlungsaufträge (PMO), Caisse (CSH), Bestbank (BNK), Opérations diverses (MSC), Déclarations TVA (VAT)
  - Rechnungen erstellen
- Bureau : Mes Extraits
- Rapports :
  - Comptabilité : Situation, Tätigkeitsbericht, Schuldner, Gläubiger
  - MwSt. : Offene Rechnungen
- Configuration :
  - Système : Paramètres du Site, Textes d'aide, Utilisateurs
  - Endroits : Pays, Endroits
  - Contacts : Types d'organisation, Fonctions
  - Comptabilité : Groupes de comptes, Comptes, Journale, Périodes comptables, Délais de paiement
  - Bureau : Types d'extrait, Mes Einfügetexte
  - MwSt. : MwSt-Regeln, Types de papier
- Explorateur :
  - Système : types de contenu, Procurations, Types d'utilisateur
  - Contacts : Personnes de contact, Partenaires
  - Comptabilité : Ausgleichungsregeln, Belege, Belegarten, Mouvements, Années comptables, Handelsarten, Journalgruppen
  - SEPA : Comptes en banque
  - Bureau : Extraits, Einfügetexte
  - MwSt. : MwSt.-Regimes, MwSt.-Klassen, Produktrechnungen, Produktrechnungszeilen, Fakturationspläne, Déclarations TVA
  - Finanzjournale : Kontoauszüge, Diverse Buchungen, Zahlungsaufträge
- Site : à propos

Rolf gets the same menu in German:
  
>>> rt.login('rolf').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Kontakte : Personen, Organisationen
- Produkte : Produkte, Produktkategorien
- Buchhaltung :
  - Verkauf : Verkaufsrechnungen (SLS), Gutschriften Verkauf (SLC)
  - Einkauf : Einkaufsrechnungen (PRC)
  - Finanzjournale : Zahlungsaufträge (PMO), Kasse (CSH), Bestbank (BNK), Diverse Buchungen (MSC), MwSt.-Erklärungen (VAT)
  - Rechnungen erstellen
- Büro : Meine Auszüge
- Berichte :
  - Buchhaltung : Situation, Tätigkeitsbericht, Schuldner, Gläubiger
  - MwSt. : Offene Rechnungen
- Konfigurierung :
  - System : Site-Parameter, Hilfetexte, Benutzer
  - Orte : Länder, Orte
  - Kontakte : Organisationsarten, Funktionen
  - Buchhaltung : Kontengruppen, Konten, Journale, Buchungsperioden, Zahlungsbedingungen
  - Büro : Auszugsarten, Meine Einfügetexte
  - MwSt. : MwSt-Regeln, Papierarten
- Explorer :
  - System : Datenbankmodelle, Vollmachten, Benutzerarten
  - Kontakte : Kontaktpersonen, Partner
  - Buchhaltung : Ausgleichungsregeln, Belege, Belegarten, Bewegungen, Geschäftsjahre, Handelsarten, Journalgruppen
  - SEPA : Bankkonten
  - Büro : Auszüge, Einfügetexte
  - MwSt. : MwSt.-Regimes, MwSt.-Klassen, Produktrechnungen, Produktrechnungszeilen, Fakturationspläne, MwSt.-Erklärungen
  - Finanzjournale : Kontoauszüge, Diverse Buchungen, Zahlungsaufträge
- Site : Info



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
>>> result = json.loads(res.content)
>>> print(len(result['rows']))
16

The 16 is because Lino has a hard-coded default value of  
returning only 15 rows when no limit has been specified
(there is one extra row for adding new records).

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

Same request returns now 26 data rows:

>>> res = test_client.get(url, REMOTE_USER='robin')
>>> result = json.loads(res.content)
>>> print(len(result['rows']))
26

To remove the limit altogether, you can say:

>>> countries.PlacesByCountry.preview_limit = None

and the same request now returns all 49 data rows (48 + the phantom
row):

>>> res = test_client.get(url,REMOTE_USER='robin')
>>> result = json.loads(res.content)
>>> print(len(result['rows']))
49









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
    

The demo database contains 69 persons and 22 companies.

>>> contacts.Person.objects.count()
69
>>> contacts.Company.objects.count()
22
>>> contacts.Partner.objects.count()
91


>>> print(' '.join(settings.SITE.demo_fixtures))
std few_countries euvatrates furniture minimal_ledger demo demo_bookings payments demo2



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
  - Financial : Payment Orders (PMO), Cash (CSH), Bestbank (BNK), Miscellaneous Journal Entries (MSC)
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
  - VAT : VAT regimes, VAT Classes, Product invoices, Product invoice items, Invoicing plans
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
  - Finanzjournale : Zahlungsaufträge (PMO), Caisse (CSH), Bestbank (BNK), Opérations diverses (MSC)
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
  - MwSt. : MwSt.-Regimes, MwSt.-Klassen, Produktrechnungen, Produktrechnungszeilen, Fakturationspläne
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
  - Finanzjournale : Zahlungsaufträge (PMO), Kasse (CSH), Bestbank (BNK), Diverse Buchungen (MSC)
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
  - MwSt. : MwSt.-Regimes, MwSt.-Klassen, Produktrechnungen, Produktrechnungszeilen, Fakturationspläne
  - Finanzjournale : Kontoauszüge, Diverse Buchungen, Zahlungsaufträge
- Site : Info



Database structure
==================


>>> from lino.utils.diag import analyzer
>>> print analyzer.show_database_structure()
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- accounts.Account : id, ref, seqno, name, sales_allowed, purchases_allowed, wages_allowed, clearings_allowed, group, type, needs_partner, clearable, default_amount, name_fr, name_en
- accounts.Group : id, name, ref, account_type, name_fr, name_en
- contacts.Company : id, email, language, url, phone, gsm, fax, country, city, zip_code, region, addr1, street_prefix, street, street_no, street_box, addr2, name, remarks, payment_term, vat_regime, invoice_recipient, paper_type, partner_ptr, prefix, type, vat_id
- contacts.CompanyType : id, name, abbr, abbr_fr, abbr_en, name_fr, name_en
- contacts.Partner : id, email, language, url, phone, gsm, fax, country, city, zip_code, region, addr1, street_prefix, street, street_no, street_box, addr2, name, remarks, payment_term, vat_regime, invoice_recipient, paper_type
- contacts.Person : id, email, language, url, phone, gsm, fax, country, city, zip_code, region, addr1, street_prefix, street, street_no, street_box, addr2, name, remarks, payment_term, vat_regime, invoice_recipient, paper_type, partner_ptr, title, first_name, middle_name, last_name, gender, birth_date
- contacts.Role : id, type, person, company
- contacts.RoleType : id, name, name_fr, name_en
- contenttypes.ContentType : id, app_label, model
- countries.Country : name, isocode, short_code, iso3, name_fr, name_en
- countries.Place : id, parent, name, country, zip_code, type, name_fr, name_en
- excerpts.Excerpt : id, build_time, build_method, user, company, contact_person, contact_role, owner_type, owner_id, excerpt_type, language
- excerpts.ExcerptType : id, name, build_method, template, attach_to_email, email_template, certifying, remark, body_template, content_type, primary, backward_compat, print_recipient, print_directly, shortcut, name_fr, name_en
- finan.BankStatement : id, user, journal, voucher_date, entry_date, accounting_period, number, narration, state, voucher_ptr, printed_by, item_account, item_remark, last_item_date, balance1, balance2
- finan.BankStatementItem : id, seqno, match, amount, dc, remark, account, partner, date, voucher
- finan.JournalEntry : id, user, journal, voucher_date, entry_date, accounting_period, number, narration, state, voucher_ptr, printed_by, item_account, item_remark, last_item_date
- finan.JournalEntryItem : id, seqno, match, amount, dc, remark, account, partner, date, voucher
- finan.PaymentOrder : id, user, journal, voucher_date, entry_date, accounting_period, number, narration, state, voucher_ptr, printed_by, item_account, item_remark, total, execution_date
- finan.PaymentOrderItem : id, seqno, match, bank_account, amount, dc, remark, account, partner, voucher
- gfks.HelpText : id, content_type, field, help_text
- invoicing.Item : id, plan, partner, first_date, last_date, amount, number_of_invoiceables, preview, selected, invoice
- invoicing.Plan : id, user, journal, today, max_date, partner
- ledger.AccountingPeriod : id, ref, start_date, end_date, state, year, remark
- ledger.Journal : id, ref, seqno, name, build_method, template, trade_type, voucher_type, journal_group, auto_check_clearings, force_sequence, account, printed_name, dc, yearly_numbering, printed_name_fr, printed_name_en, name_fr, name_en, sepa_account
- ledger.MatchRule : id, account, journal
- ledger.Movement : id, voucher, partner, seqno, account, amount, dc, match, cleared, value_date
- ledger.PaymentTerm : id, ref, name, days, months, end_of_month, printed_text, printed_text_fr, printed_text_en, name_fr, name_en
- ledger.Voucher : id, user, journal, voucher_date, entry_date, accounting_period, number, narration, state
- products.Product : id, name, description, cat, delivery_unit, vat_class, description_fr, description_en, name_fr, name_en, sales_account, sales_price, purchases_account
- products.ProductCat : id, name, description, name_fr, name_en
- sales.InvoiceItem : id, seqno, total_incl, total_base, total_vat, vat_class, unit_price, qty, product, description, discount, voucher, title, invoiceable_type, invoiceable_id
- sales.PaperType : id, name, template, name_fr, name_en
- sales.VatProductInvoice : id, user, journal, voucher_date, entry_date, accounting_period, number, narration, state, voucher_ptr, partner, payment_term, match, total_incl, total_base, total_vat, vat_regime, your_ref, due_date, printed_by, language, subject, intro, paper_type
- sepa.Account : id, partner, iban, bic, remark, primary
- system.SiteConfig : id, default_build_method, simulate_today, site_company, next_partner_id, clients_account, sales_vat_account, sales_account, suppliers_account, purchases_vat_account, purchases_account, wages_account, clearings_account
- tinymce.TextFieldTemplate : id, user, name, description, text
- users.Authority : id, user, authorized
- users.User : id, email, language, modified, created, password, last_login, username, user_type, initials, first_name, last_name, remarks, partner
- vat.InvoiceItem : id, seqno, account, total_incl, total_base, total_vat, vat_class, voucher, title
- vat.VatAccountInvoice : id, user, journal, voucher_date, entry_date, accounting_period, number, narration, state, voucher_ptr, partner, payment_term, match, total_incl, total_base, total_vat, vat_regime, your_ref, due_date
- vat.VatRule : id, seqno, start_date, end_date, country, vat_class, vat_regime, rate, can_edit
<BLANKLINE>


Miscellaneous
=============

Person #115 is not a Partner
----------------------------

Person #115 (u'Altenberg Hans') is not a Partner (master_key 
is <django.db.models.fields.related.ForeignKey: partner>)

>>> url = '/bs3/contacts/Person/115'
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









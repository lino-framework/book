.. doctest docs/specs/tera/misc.rst
.. _tera.specs.misc:
.. _presto.specs.psico:

=========================
Lino Tera : miscellaneous
=========================

.. contents::
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db import models


Every :ref:`tera` application has a :xfile:`settings.py` module that
inherits from :mod:`lino_tera.lib.tera.settings`.

>>> from lino_tera.lib.tera.settings import Site
>>> isinstance(settings.SITE, Site)
True

Lino Tera does not have multiple addresses per partner.

>>> dd.is_installed('addresses')
False


Partner types
=============

>>> dd.plugins.contacts
lino_tera.lib.contacts (extends_models=['Person'])


>>> print([m.__name__ for m in rt.models_by_base(rt.models.contacts.Partner)])
['Company', 'Partner', 'Person', 'Household', 'Client']

.. py2rst::

   from lino import startup
   startup('lino_book.projects.lydia.settings.demo')
   from lino.api import rt
   rt.models.contacts.Partner.print_subclasses_graph()


Activities
==========

>>> print(settings.SITE.project_model)
<class 'lino_tera.lib.courses.models.Course'>


.. _tera.specs.teams:

Teams
=====

>>> rt.show(teams.Teams)
=========== ============= ================== ==================
 Reference   Designation   Designation (de)   Designation (fr)
----------- ------------- ------------------ ------------------
 E           Eupen
 S           St. Vith
=========== ============= ================== ==================
<BLANKLINE>


The following just repeats on the first payment order what has been
done for all orders when :mod:`lino_xl.lib.finan.fixtures.demo`
generated them:

>>> ses = rt.login()
>>> obj = rt.models.finan.PaymentOrder.objects.first()
>>> obj
PaymentOrder #250 ('PMO 1/2015')

>>> rv = obj.write_xml.run_from_session(ses)  #doctest: +ELLIPSIS
xml render <django.template.backends.jinja2.Template object at ...> -> .../media/xml/xml/finan.PaymentOrder-250.xml ('en', {})

>>> rv['success']
True
>>> print(rv['open_url'])
/media/xml/xml/finan.PaymentOrder-250.xml

Let's check whether the XML file has been generated and is a valid
SEPA payment initiation:

>>> from unipath import Path
>>> fn = Path(settings.SITE.cache_dir + rv['open_url'])
>>> fn.exists()
True

>>> from etgen.sepa.validate import validate_pain001
>>> validate_pain001(fn)


Voucher types
=============

>>> rt.show(ledger.VoucherTypes)
=============================== ====== ================================================================ ======================================================
 value                           name   text                                                             Model
------------------------------- ------ ---------------------------------------------------------------- ------------------------------------------------------
 ana.InvoicesByJournal                  Analytic invoice (ana.InvoicesByJournal)                         <class 'lino_xl.lib.ana.models.AnaAccountInvoice'>
 bevats.DeclarationsByJournal           Special Belgian VAT declaration (bevats.DeclarationsByJournal)   <class 'lino_xl.lib.bevats.models.Declaration'>
 finan.BankStatementsByJournal          Bank Statement (finan.BankStatementsByJournal)                   <class 'lino_xl.lib.finan.models.BankStatement'>
 finan.JournalEntriesByJournal          Journal Entry (finan.JournalEntriesByJournal)                    <class 'lino_xl.lib.finan.models.JournalEntry'>
 finan.PaymentOrdersByJournal           Payment Order (finan.PaymentOrdersByJournal)                     <class 'lino_xl.lib.finan.models.PaymentOrder'>
 sales.InvoicesByJournal                Sales invoice (sales.InvoicesByJournal)                          <class 'lino_xl.lib.sales.models.VatProductInvoice'>
 vat.InvoicesByJournal                  Invoice (vat.InvoicesByJournal)                                  <class 'lino_xl.lib.vat.models.VatAccountInvoice'>
=============================== ====== ================================================================ ======================================================
<BLANKLINE>


>>> # rt.show(ledger.Journals, filter=models.Q(must_declare=True))



Internal details
=================


The following shows that :ticket:`1975` is a duplicate of
:ticket:`492`:

>>> a = rt.models.ana.InvoicesByJournal._actions_dict.get('wf1')
>>> a.action.auto_save
True




Technical stuff (don't read)
============================

Verify whether we can select an `invoice_recipient` on a client.  It's
an editable remote field.

>>> base = "/choices/tera/Clients/salesrule__invoice_recipient"
>>> show_choices("robin", base + '?query=')  #doctest: +ELLIPSIS
<br/>
AS Express Post
AS Matsalu Veevärk
Alliance nationale des mutualités chrétiennes
Altenberg Hans
Arens Andreas
Arens Annette
...
van Veen Vincent
Ärgerlich Erna
Õunapuu Õie
Östges Otto


>>> rt.show("excerpts.ExcerptTypes")
======================================================== ========= ============ ==================== ====================== ==================== ===================== ============================= ===============
 Model                                                    Primary   Certifying   Designation          Designation (de)       Designation (fr)     Print method          Template                      Body template
-------------------------------------------------------- --------- ------------ -------------------- ---------------------- -------------------- --------------------- ----------------------------- ---------------
 *bevats.Declaration (Special Belgian VAT declaration)*   Yes       Yes          VAT declaration      MwSt.-Erklärung        VAT declaration      WeasyPdfBuildMethod   default.weasy.html
 *contacts.Partner (Partner)*                             No        No           Payment reminder     Zahlungserinnerung     Rappel de paiement   WeasyPdfBuildMethod   payment_reminder.weasy.html
 *contacts.Person (Person)*                               No        No           Terms & conditions   Nutzungsbestimmungen   Terms & conditions   AppyPdfBuildMethod    TermsConditions.odt
 *courses.Enrolment (Enrolment)*                          Yes       Yes          Enrolment            Einschreibung          Inscription
 *finan.BankStatement (Bank Statement)*                   Yes       Yes          Bank Statement       Kontoauszug            Extrait de compte
 *finan.JournalEntry (Journal Entry)*                     Yes       Yes          Journal Entry        Diverse Buchung        Opération diverse
 *finan.PaymentOrder (Payment Order)*                     Yes       Yes          Payment Order        Zahlungsauftrag        Ordre de paiement
 *sales.VatProductInvoice (Sales invoice)*                Yes       Yes          Sales invoice        Verkaufsrechnung       Sales invoice
 *sheets.Report (Accounting Report)*                      Yes       Yes          Accounting Report    Buchhaltungsbericht    Accounting Report    WeasyPdfBuildMethod
======================================================== ========= ============ ==================== ====================== ==================== ===================== ============================= ===============
<BLANKLINE>

.. _cosi.specs.sales:

================
Product invoices
================

.. This document is part of the Lino Così test suite. To run only this
   test:

    $ python setup.py test -s tests.SpecsTests.test_sales
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.pierre.settings.doctests')
    >>> from lino.api.doctest import *
    >>> ses = rt.login('robin')

A **product invoice** is an invoice whose rows usually refer to a
*product* (and provides rules for mapping products to general accounts
if needed).  This is in contrast to *account invoices* which don't
need any products.

The plugin
==========

Lino Così implements product invoices in the
:mod:`lino_xl.lib.sales` plugin.  The internal codename "sales" is
for historical reasons, you might generate product invoices for other
trade types as well.

The plugin --of course-- needs and automatically installs the
:mod:`lino_xl.lib.products` plugin.

It also needs and installs :mod:`lino_xl.lib.vat` (and not
:mod:`lino_xl.lib.vatless`).  Which means that if you want product
invoices, you cannot *not* also install the VAT framework.  If the
site owner is not subject to VAT, you can hide the VAT fields and
define a VAT rate of 0 for everything.

>>> dd.plugins.sales.needs_plugins
['lino_xl.lib.products', 'lino_xl.lib.vat']

This plugin is needed and extended by :mod:`lino_xl.lib.invoicing`
which adds automatic generation of such product invoices.

>>> dd.plugins.invoicing.needs_plugins
['lino_xl.lib.sales']


Trade types
===========

The plugin updates your trade types and defines some additional
database fields to be installed by :func:`inject_tradetype_fields
<lino_xl.lib.ledger.choicelists.inject_tradetype_fields>`.

For example the sales price of a product:

>>> print(ledger.TradeTypes.sales.price_field_name)
sales_price

>>> translation.activate('en')

>>> print(ledger.TradeTypes.sales.price_field_label)
Sales price

>>> products.Product._meta.get_field('sales_price')
<lino.core.fields.PriceField: sales_price>



The invoicing address of a partner
==================================

The plugin also injects a field :attr:`invoice_recipient
<lino.modlib.contacts.models.Partner.invoice_recipient>` to the
:class:`contacts.Partner <lino.modlib.contacts.models.Partner>` model:

.. attribute:: lino.modlib.contacts.models.Partner.invoice_recipient

  The recipient of invoices (invoicing address).




The sales journal
=================

>>> rt.show('ledger.Journals', column_names="ref name trade_type")
=========== ===================== =============================== ============
 Reference   Designation           Designation (en)                Trade type
----------- --------------------- ------------------------------- ------------
 SLS         Factures vente        Sales invoices                  Sales
 SLC         Sales credit notes    Sales credit notes              Sales
 PRC         Factures achat        Purchase invoices               Purchases
 PMO         Payment Orders        Payment Orders                  Purchases
 CSH         Caisse                Cash
 BNK         Bestbank              Bestbank
 MSC         Opérations diverses   Miscellaneous Journal Entries
 VAT         Déclarations TVA      VAT declarations
=========== ===================== =============================== ============
<BLANKLINE>


>>> jnl = rt.models.ledger.Journal.get_by_ref("SLS")
>>> rt.show('sales.InvoicesByJournal', jnl)  #doctest: +ELLIPSIS
===================== ============== ============ ======================= ================= ============== ================
 No.                   Voucher date   Due date     Partner                 Total incl. VAT   Subject line   Actions
--------------------- -------------- ------------ ----------------------- ----------------- -------------- ----------------
 72/2017               11/03/2017     10/05/2017   Radermacher Alfons      770,00                           **Registered**
 71/2017               10/03/2017     09/05/2017   Radermacher Alfons      465,96                           **Registered**
 70/2017               09/03/2017     19/03/2017   Emontspool Erwin        528,86                           **Registered**
 69/2017               08/03/2017     15/03/2017   Emonts Erich            2 974,97                         **Registered**
 68/2017               07/03/2017     06/04/2017   Mießen Michael          495,87                           **Registered**
 67/2017               06/03/2017     04/06/2017   Malmendier Marc         433,88                           **Registered**
 66/2017               13/02/2017     20/02/2017   Lambertz Guido          951,82                           **Registered**
 65/2017               12/02/2017     12/02/2017   Kaivers Karl            1 942,00                         **Registered**
 64/2017               11/02/2017     13/03/2017   Jousten Jan             1 322,25                         **Registered**
 63/2017               10/02/2017     12/03/2017   Jousten Jan             818,18                           **Registered**
 62/2017               09/02/2017     28/02/2017   Jonas Josef             231,33                           **Registered**
 61/2017               08/02/2017     09/05/2017   Johnen Johann           991,61                           **Registered**
 60/2017               07/02/2017     09/03/2017   Jansen Jérémy           2 743,62                         **Registered**
 59/2017               06/02/2017     13/02/2017   Hilgers Henri           442,15                           **Registered**
 58/2017               06/01/2017     05/02/2017   Groteclaes Gregory      231,40                           **Registered**
 57/2016               09/12/2016     09/03/2017   Faymonville Luc         561,82                           **Registered**
 ...
 11/2016               06/04/2016     05/07/2016   Faymonville Luc         1 942,00                         **Registered**
 10/2016               06/03/2016     05/05/2016   Engels Edgar            1 322,25                         **Registered**
 9/2016                09/02/2016     10/03/2016   Emonts Daniel           818,18                           **Registered**
 8/2016                08/02/2016     18/02/2016   Evers Eberhart          231,33                           **Registered**
 7/2016                07/02/2016     14/02/2016   Evertz Bernd            991,61                           **Registered**
 6/2016                06/02/2016     06/04/2016   Dericum Daniel          2 743,62                         **Registered**
 5/2016                10/01/2016     09/02/2016   Chantraine Marc         535,00                           **Registered**
 4/2016                09/01/2016     09/01/2016   Bastiaensen Laurent     231,40                           **Registered**
 3/2016                08/01/2016     07/02/2016   Ausdemwald Alfons       561,82                           **Registered**
 2/2016                07/01/2016     31/01/2016   Altenberg Hans          1 685,80                         **Registered**
 1/2016                06/01/2016     06/03/2016   Arens Andreas           2 479,21                         **Registered**
 **Total (72 rows)**                                                       **81 055,30**
===================== ============== ============ ======================= ================= ============== ================
<BLANKLINE>
 

>>> mt = contenttypes.ContentType.objects.get_for_model(sales.VatProductInvoice).id
>>> obj = sales.VatProductInvoice.objects.get(journal__ref="SLS", number=20)

>>> url = '/api/sales/InvoicesByJournal/{0}'.format(obj.id)
>>> url += '?mt={0}&mk={1}&an=detail&fmt=json'.format(mt, obj.journal.id)
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> # res.content
>>> r = check_json_result(res, "navinfo data disable_delete id title")
>>> print(r['title'])
Sales invoices (SLS) » SLS 20


IllegalText: The <text:section> element does not allow text
===========================================================

The following reproduces a situation which caused above error
until :blogref:`20151111`. 

TODO: it is currently disabled for different reasons: leaves dangling
temporary directories, does not reproduce the problem (probably
because we must clear the cache).

>> obj = rt.modules.sales.VatProductInvoice.objects.all()[0]
>> obj
VatProductInvoice #1 ('SLS#1')
>> from lino.modlib.appypod.appy_renderer import AppyRenderer
>> tplfile = rt.find_config_file('sales/VatProductInvoice/Default.odt')
>> context = dict()
>> outfile = "tmp.odt"
>> renderer = AppyRenderer(ses, tplfile, context, outfile)
>> ar = rt.modules.sales.ItemsByInvoicePrint.request(obj)
>> print(renderer.insert_table(ar))  #doctest: +ELLIPSIS
<table:table ...</table:table-rows></table:table>


>> item = obj.items.all()[0]
>> item.description = """
... <p>intro:</p><ol><li>first</li><li>second</li></ol>
... <p></p>
... """
>> item.save()
>> print(renderer.insert_table(ar))  #doctest: +ELLIPSIS
Traceback (most recent call last):
...
IllegalText: The <text:section> element does not allow text


The language of an invoice
==========================

The language of an invoice not necessary that of the user who enters
the invoice. It is either the partner's :attr:`language
<lino.modlib.contacts.models.Partner.language>` or (if this is empty)
the Site's :meth:`get_default_language
<lino.core.site.Site.get_default_language>`.


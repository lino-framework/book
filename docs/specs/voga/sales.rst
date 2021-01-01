.. doctest docs/specs/voga/sales.rst
.. _voga.specs.sales:

=====================================
The :mod:`lino_voga.lib.sales` plugin
=====================================

The :mod:`lino_voga.lib.sales` plugin extends :mod:`lino_xl.lib.sales`
for usage in :ref:`voga`.

See also :doc:`invoicing`.


About this document
===================

Code examples in this document use the :mod:`lino_book.projects.roger`
demo project:

>>> from lino import startup
>>> startup('lino_book.projects.roger.settings.doctests')
>>> from lino.api.doctest import *

>>> dd.plugins.sales
lino_voga.lib.sales

Here are all our sales invoices:

>>> jnl = rt.models.ledger.Journal.get_by_ref('SLS')
>>> rt.show(sales.InvoicesByJournal, jnl)  #doctest: +ELLIPSIS
===================== ============ =================================== ============== =============== ================
 No.                   Entry date   Partner                             Subject line   Total to pay    Workflow
--------------------- ------------ ----------------------------------- -------------- --------------- ----------------
 26/2015               01/03/2015   di Rupo Didier                                     48,00           **Registered**
 25/2015               01/03/2015   Radermacher Guido                                  100,00          **Registered**
 24/2015               01/03/2015   Emonts-Gast Erna                                   64,00           **Registered**
 ...
 3/2015                01/01/2015   Engels Edgar                                       48,00           **Registered**
 2/2015                01/01/2015   Evers Eberhart                                     48,00           **Registered**
 1/2015                01/01/2015   Charlier Ulrike                                    148,00          **Registered**
 71/2014               01/12/2014   Dupont Jean                                        98,00           **Registered**
 70/2014               01/12/2014   Radermacher Hedi                                   48,00           **Registered**
 ...
 5/2014                01/01/2014   Demeulenaere Dorothée                              60,00           **Registered**
 4/2014                01/01/2014   Dericum Daniel                                     80,00           **Registered**
 3/2014                01/01/2014   Charlier Ulrike                                    356,00          **Registered**
 2/2014                01/01/2014   Bastiaensen Laurent                                20,00           **Registered**
 1/2014                01/01/2014   Altenberg Hans                                     295,00          **Registered**
 **Total (97 rows)**                                                                   **10 401,00**
===================== ============ =================================== ============== =============== ================
<BLANKLINE>

The :class:`lino_xl.lib.sales.DueInvoices` table shows a list of invoices that
aren't (completeley) paid.  Example see :doc:`/specs/cosi/apc`.

Printing invoices
=================

We take a sales invoice, clear the cache, ask Lino to print it and
check whether we get the expected response.

>>> import lxml.usedoctest
>>> ses = settings.SITE.login("robin")
>>> dd.translation.activate('en')
>>> obj = sales.VatProductInvoice.objects.all()[0]
>>> obj.clear_cache()
>>> d = ses.run(obj.do_print)
... #doctest: +ELLIPSIS
appy.pod render .../sales/config/sales/VatProductInvoice/Default.odt -> .../media/cache/appypdf/sales.VatProductInvoice-125.pdf

>>> d['success']
True

>>> print(d['message'])
Your printable document (<a href="/media/cache/appypdf/sales.VatProductInvoice-125.pdf">sales.VatProductInvoice-125.pdf</a>) should now open in a new browser window. If it doesn't, please ask your system administrator.

Your printable document (filename sales.VatProductInvoice-125.pdf) should now open in a new browser window. If it doesn't, please consult <a href="http://www.lino-framework.org/help/print.html" target="_blank">the documentation</a> or ask your system administrator.

Note that this test should fail if you run the test suite without a
LibreOffice server running.


>>> rt.show(invoicing.SalesRules)
==================== =================== ============
 Partner              Invoicing address   Paper type
-------------------- ------------------- ------------
 Arens Annette
 Faymonville Luc      Engels Edgar
 Radermacher Alfons   Emonts-Gast Erna
 Martelaer Mark       Dupont Jean
==================== =================== ============
<BLANKLINE>

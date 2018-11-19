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
===================== ============ ============ =================================== ================= ============== ================
 No.                   Entry date   Due date     Partner                             Total incl. VAT   Subject line   Workflow
--------------------- ------------ ------------ ----------------------------------- ----------------- -------------- ----------------
 26/2015               01/03/2015   01/03/2015   di Rupo Didier                      48,00                            **Registered**
 25/2015               01/03/2015   31/03/2015   Radermacher Guido                   100,00                           **Registered**
 24/2015               01/03/2015   30/04/2015   Emonts-Gast Erna                    64,00                            **Registered**
 ...
 15/2015               01/02/2015   08/02/2015   Kaivers Karl                        50,00                            **Registered**
 14/2015               01/02/2015   02/05/2015   Engels Edgar                        50,00                            **Registered**
 13/2015               01/02/2015   03/03/2015   Dobbelstein-Demeulenaere Dorothée   96,00                            **Registered**
 12/2015               01/02/2015   03/03/2015   Charlier Ulrike                     164,00                           **Registered**
 11/2015               01/01/2015   31/01/2015   Dupont Jean                         98,00                            **Registered**
 10/2015               01/01/2015   01/01/2015   di Rupo Didier                      48,00                            **Registered**
 9/2015                01/01/2015   31/01/2015   Radermacher Guido                   164,00                           **Registered**
 8/2015                01/01/2015   02/03/2015   Emonts-Gast Erna                    50,00                            **Registered**
 7/2015                01/01/2015   08/01/2015   Meier Marie-Louise                  48,00                            **Registered**
 6/2015                01/01/2015   08/01/2015   Kaivers Karl                        50,00                            **Registered**
 5/2015                01/01/2015   31/01/2015   Jonas Josef                         64,00                            **Registered**
 4/2015                01/01/2015   01/04/2015   Jacobs Jacqueline                   48,00                            **Registered**
 3/2015                01/01/2015   01/04/2015   Engels Edgar                        48,00                            **Registered**
 2/2015                01/01/2015   31/01/2015   Evers Eberhart                      48,00                            **Registered**
 1/2015                01/01/2015   31/01/2015   Charlier Ulrike                     148,00                           **Registered**
 71/2014               01/12/2014   31/12/2014   Dupont Jean                         98,00                            **Registered**
 70/2014               01/12/2014   01/03/2015   Radermacher Hedi                    48,00                            **Registered**
 69/2014               01/12/2014   31/12/2014   Radermacher Guido                   50,00                            **Registered**
 68/2014               01/12/2014   30/01/2015   Emonts-Gast Erna                    114,00                           **Registered**
 67/2014               01/12/2014   31/12/2014   Laschet Laura                       48,00                            **Registered**
 66/2014               01/12/2014   08/12/2014   Kaivers Karl                        50,00                            **Registered**
 65/2014               01/12/2014   01/03/2015   Engels Edgar                        50,00                            **Registered**
 64/2014               01/12/2014   31/12/2014   Dobbelstein-Demeulenaere Dorothée   96,00                            **Registered**
 63/2014               01/12/2014   31/12/2014   Charlier Ulrike                     100,00                           **Registered**
 62/2014               01/11/2014   01/12/2014   Dupont Jean                         64,00                            **Registered**
 61/2014               01/11/2014   01/12/2014   Radermacher Jean                    48,00                            **Registered**
 ...
 14/2014               01/01/2014   31/01/2014   Laschet Laura                       296,00                           **Registered**
 13/2014               01/01/2014   08/01/2014   Kaivers Karl                        180,00                           **Registered**
 12/2014               01/01/2014   31/01/2014   Jonas Josef                         64,00                            **Registered**
 11/2014               01/01/2014   01/04/2014   Jacobs Jacqueline                   678,00                           **Registered**
 10/2014               01/01/2014   08/01/2014   Hilgers Hildegard                   80,00                            **Registered**
 9/2014                01/01/2014   01/04/2014   Engels Edgar                        426,00                           **Registered**
 8/2014                01/01/2014   02/03/2014   Emonts Daniel                       240,00                           **Registered**
 7/2014                01/01/2014   31/01/2014   Evers Eberhart                      48,00                            **Registered**
 6/2014                01/01/2014   31/01/2014   Dobbelstein-Demeulenaere Dorothée   116,00                           **Registered**
 5/2014                01/01/2014   31/01/2014   Demeulenaere Dorothée               60,00                            **Registered**
 4/2014                01/01/2014   01/04/2014   Dericum Daniel                      80,00                            **Registered**
 3/2014                01/01/2014   31/01/2014   Charlier Ulrike                     356,00                           **Registered**
 2/2014                01/01/2014   08/01/2014   Bastiaensen Laurent                 20,00                            **Registered**
 1/2014                01/01/2014   31/01/2014   Altenberg Hans                      295,00                           **Registered**
 **Total (97 rows)**                                                                 **10 401,00**
===================== ============ ============ =================================== ================= ============== ================
<BLANKLINE>


The :class:`lino_xl.lib.sales.DueInvoices` table shows a list of
invoices that aren't (completeley) paid.  The following ones are there
obviously due to a payment difference.

>>> rt.show(sales.DueInvoices)
==================== =========== ======= ============== ================= ================ ================
 Due date             Reference   No.     Partner        Total incl. VAT   Balance before   Balance to pay
-------------------- ----------- ------- -------------- ----------------- ---------------- ----------------
 01/04/2015           SLS         3       Engels Edgar   48,00                              0,72
 **Total (1 rows)**               **3**                  **48,00**                          **0,72**
==================== =========== ======= ============== ================= ================ ================
<BLANKLINE>


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
appy.pod render .../sales/config/sales/VatProductInvoice/Default.odt -> .../media/cache/appypdf/sales.VatProductInvoice-6.pdf

>>> d['success']
True

>>> print(d['message'])
Your printable document (<a href="/media/cache/appypdf/sales.VatProductInvoice-6.pdf">sales.VatProductInvoice-6.pdf</a>) should now open in a new browser window. If it doesn't, please ask your system administrator.

Your printable document (filename sales.VatProductInvoice-6.pdf) should now open in a new browser window. If it doesn't, please consult <a href="http://www.lino-framework.org/help/print.html" target="_blank">the documentation</a> or ask your system administrator.

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

.. _voga.specs.sales:

=============================
Sales management in Lino Voga
=============================

.. to test only this doc:

    $ doctest docs/specs/sales.rst

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *
    
See also :doc:`invoicing`.

Here are all our sales invoices:

>>> jnl = rt.models.ledger.Journal.get_by_ref('SLS')
>>> rt.show(sales.InvoicesByJournal, jnl)  #doctest: +ELLIPSIS
===================== ============ ============ =================================== ================= ============== ================
 No.                   Entry date   Due date     Partner                             Total incl. VAT   Subject line   Workflow
--------------------- ------------ ------------ ----------------------------------- ----------------- -------------- ----------------
 97/2015               01/03/2015   31/03/2015   Dupont Jean                         64,00                            **Registered**
 96/2015               01/03/2015   30/05/2015   Radermacher Hedi                    20,00                            **Registered**
 95/2015               01/03/2015   08/03/2015   Bastiaensen Laurent                 48,00                            **Registered**
 94/2015               01/03/2015   08/03/2015   Meier Marie-Louise                  48,00                            **Registered**
 93/2015               01/03/2015   30/05/2015   Brecht Bernd                        48,00                            **Registered**
 92/2015               01/03/2015   30/05/2015   Engels Edgar                        48,00                            **Registered**
 91/2015               01/03/2015   31/03/2015   Charlier Ulrike                     50,00                            **Registered**
 90/2015               01/02/2015   08/02/2015   Meier Marie-Louise                  64,00                            **Registered**
 89/2015               01/02/2015   08/02/2015   Jeanémart Jérôme                    50,00                            **Registered**
 88/2015               01/02/2015   03/03/2015   Radermacher Christian               98,00                            **Registered**
 87/2015               01/02/2015   03/03/2015   Jonas Josef                         50,00                            **Registered**
 86/2015               01/02/2015   02/05/2015   Jacobs Jacqueline                   50,00                            **Registered**
 ...
 24/2014               01/05/2014   31/05/2014   Charlier Ulrike                     64,00                            **Registered**
 23/2014               01/05/2014   31/05/2014   Radermacher Christian               20,00                            **Registered**
 22/2014               01/05/2014   30/06/2014   Emonts-Gast Erna                    50,00                            **Registered**
 21/2014               01/05/2014   31/05/2014   Dupont Jean                         50,00                            **Registered**
 20/2014               01/04/2014   30/06/2014   Radermacher Hedi                    20,00                            **Registered**
 19/2014               01/04/2014   30/06/2014   Jacobs Jacqueline                   20,00                            **Registered**
 18/2014               01/04/2014   31/05/2014   Emonts Daniel                       40,00                            **Registered**
 17/2014               01/04/2014   01/04/2014   di Rupo Didier                      20,00                            **Registered**
 16/2014               01/04/2014   01/05/2014   Dobbelstein-Demeulenaere Dorothée   20,00                            **Registered**
 15/2014               01/04/2014   08/04/2014   Bastiaensen Laurent                 20,00                            **Registered**
 14/2014               01/04/2014   01/05/2014   Radermacher Christian               64,00                            **Registered**
 13/2014               01/04/2014   30/06/2014   Engels Edgar                        50,00                            **Registered**
 12/2014               01/04/2014   31/05/2014   Emonts-Gast Erna                    50,00                            **Registered**
 11/2014               01/04/2014   01/05/2014   Dupont Jean                         50,00                            **Registered**
 10/2014               01/03/2014   08/03/2014   Meier Marie-Louise                  20,00                            **Registered**
 9/2014                01/03/2014   30/05/2014   Engels Edgar                        50,00                            **Registered**
 8/2014                01/03/2014   31/03/2014   Dupont Jean                         50,00                            **Registered**
 7/2014                01/02/2014   02/05/2014   Engels Edgar                        50,00                            **Registered**
 6/2014                01/02/2014   02/04/2014   Emonts-Gast Erna                    50,00                            **Registered**
 5/2014                01/02/2014   03/03/2014   Dupont Jean                         50,00                            **Registered**
 4/2014                01/01/2014   02/03/2014   Emonts-Gast Erna                    150,00                           **Registered**
 3/2014                01/01/2014   01/04/2014   Engels Edgar                        100,00                           **Registered**
 2/2014                01/01/2014   31/01/2014   Dupont Jean                         50,00                            **Registered**
 1/2014                01/01/2014   08/01/2014   Meier Marie-Louise                  64,00                            **Registered**
 **Total (97 rows)**                                                                 **6 828,00**
===================== ============ ============ =================================== ================= ============== ================
<BLANKLINE>


The :class:`lino_cosi.lib.sales.models.DueInvoices` table shows a list
of invoices that aren't (completeley) paid.  The following ones are
there obviously due to a payment difference.

>>> rt.show(sales.DueInvoices)
==================== =========== ======== =============== ================= ================ ================
 Due date             Reference   No.      Partner         Total incl. VAT   Balance before   Balance to pay
-------------------- ----------- -------- --------------- ----------------- ---------------- ----------------
 03/03/2015           SLS         83       Laschet Laura   96,00                              -0,10
 **Total (1 rows)**               **83**                   **96,00**                          **-0,10**
==================== =========== ======== =============== ================= ================ ================
<BLANKLINE>


Printing invoices
=================

We take a sales invoice, clear the cache, ask Lino to print it and 
check whether we get the expected response.

>>> ses = settings.SITE.login("robin")
>>> dd.translation.activate('en')
>>> obj = sales.VatProductInvoice.objects.all()[0]
>>> obj.clear_cache()
>>> d = ses.run(obj.do_print)
... #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
appy.pod render .../sales/config/sales/VatProductInvoice/Default.odt -> .../media/cache/appypdf/sales.VatProductInvoice-125.pdf (language='en',params={'raiseOnError': True, 'ooPort': 8100, 'pythonWithUnoPath': ...}

>>> d['success']
True

>>> print(d['message'])
Your printable document (filename sales.VatProductInvoice-125.pdf) should now open in a new browser window. If it doesn't, please consult <a href="http://www.lino-framework.org/help/print.html" target="_blank">the documentation</a> or ask your system administrator.

Note that this test should fail if you run the test suite without a 
LibreOffice server running.



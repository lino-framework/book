.. _specs.tera.sql:

===================================
Exploring SQL activity in Lino Tera
===================================

..  How to test only this document:
   
    $ doctest docs/specs/tera/ledger.rst

This document shows the AccountingReport for .

We use the :mod:`lino_book.projects.lydia` demo database.
    
>>> import lino
>>> lino.startup('lino_book.projects.lydia.settings.demo')
>>> from lino.api.doctest import *

The accounting report
=====================

The following example shows the balances for three period ranges
"January", "February" and "January-February".

>>> jan = ledger.AccountingPeriod.objects.get(ref="2015-01")
>>> dec = ledger.AccountingPeriod.objects.get(ref="2015-05")
>>> def test(sp, ep=None):
...     pv = dict(start_period=sp, end_period=ep)
...     rt.show(ledger.AccountingReport, param_values=pv)

>>> test(jan, dec)
====================================================
General Account Balances (Periods 2015-01...2015-05)
====================================================
<BLANKLINE>
======================================== ============== =============== === =============== =============== === =============== ===============
 Description                              Debit before   Credit before       Debit           Credit              Debit after     Credit after
---------------------------------------- -------------- --------------- --- --------------- --------------- --- --------------- ---------------
 *(4000) Customers*                                                          13 836,75       18 500,00                           4 663,25
 *(4300) Pending Payment Orders*                                             22 044,44       9 250,00            12 794,44
 *(4400) Suppliers*                                                          27 556,94       22 044,44           5 512,50
 *(4510) VAT due*                                                            297,46          178,24              119,22
 *(4600) Tax Offices*                                                        178,24                              178,24
 *(5500) BestBank*                                                           4 586,75                            4 586,75
 *(6010) Purchase of services*                                                               17 620,40                           17 620,40
 *(6020) Purchase of investments*                                                            3 520,00                            3 520,00
 *(6040) Purchase of goods*                                                                  6 714,00                            6 714,00
 *(7000) Sales*                                                              9 620,00                            9 620,00
 *(7010) Sales on individual therapies*                                      8 880,00                            8 880,00
 **Total (11 rows)**                                                         **87 000,58**   **77 827,08**       **41 691,15**   **32 517,65**
======================================== ============== =============== === =============== =============== === =============== ===============
<BLANKLINE>
==========================================================
Partner Account Balances Sales (Periods 2015-01...2015-05)
==========================================================
<BLANKLINE>
============================= ============== =============== === =============== =============== === ============= ==============
 Description                   Debit before   Credit before       Debit           Credit              Debit after   Credit after
----------------------------- -------------- --------------- --- --------------- --------------- --- ------------- --------------
 *Altenberg Hans*                                                 1 610,00        1 610,00
 *Arens Andreas*                                                  450,00          450,00
 *Arens Annette*                                                  880,00          880,00
 *Ausdemwald Alfons*                                              726,75          765,00                            38,25
 *Auto École Verte*                                               920,00          920,00
 *Bastiaensen Laurent*                                            920,00          920,00
 *Bernd Brechts Bücherladen*                                      1 370,00        1 370,00
 *Bäckerei Ausdemwald*                                            880,00          880,00
 *Bäckerei Mießen*                                                1 370,00        1 370,00
 *Bäckerei Schmitz*                                               240,00          240,00
 *Chantraine Marc*                                                                1 370,00                          1 370,00
 *Charlier Ulrike*                                                                880,00                            880,00
 *Collard Charlotte*                                                              450,00                            450,00
 *Demeulenaere Dorothée*                                                          1 685,00                          1 685,00
 *Dericum Daniel*                                                                 240,00                            240,00
 *Donderweer BV*                                                  920,00          920,00
 *Garage Mergelsberg*                                             765,00          765,00
 *Hans Flott & Co*                                                880,00          880,00
 *Moulin Rouge*                                                   765,00          765,00
 *Reinhards Baumschule*                                           240,00          240,00
 *Rumma & Ko OÜ*                                                  450,00          450,00
 *Van Achter NV*                                                  450,00          450,00
 **Total (22 rows)**                                              **13 836,75**   **18 500,00**                     **4 663,25**
============================= ============== =============== === =============== =============== === ============= ==============
<BLANKLINE>
==============================================================
Partner Account Balances Purchases (Periods 2015-01...2015-05)
==============================================================
<BLANKLINE>
======================= ============== =============== === =============== =============== === ============== ==============
 Description             Debit before   Credit before       Debit           Credit              Debit after    Credit after
----------------------- -------------- --------------- --- --------------- --------------- --- -------------- --------------
 *Bäckerei Ausdemwald*                                      709,00          568,80              140,20
 *Bäckerei Mießen*                                          3 010,00        2 407,80            602,20
 *Bäckerei Schmitz*                                         6 005,00        4 802,60            1 202,40
 *Donderweer BV*                                            585,96          468,61              117,35
 *Garage Mergelsberg*                                       16 210,90       12 970,32           3 240,58
 *Rumma & Ko OÜ*                                            205,50          163,00              42,50
 *Van Achter NV*                                            830,58          663,31              167,27
 **Total (7 rows)**                                         **27 556,94**   **22 044,44**       **5 512,50**
======================= ============== =============== === =============== =============== === ============== ==============
<BLANKLINE>
==========================================================
Partner Account Balances Wages (Periods 2015-01...2015-05)
==========================================================
<BLANKLINE>
No data to display
==========================================================
Partner Account Balances Taxes (Periods 2015-01...2015-05)
==========================================================
<BLANKLINE>
==================================== ============== =============== === ============ ======== === ============= ==============
 Description                          Debit before   Credit before       Debit        Credit       Debit after   Credit after
------------------------------------ -------------- --------------- --- ------------ -------- --- ------------- --------------
 *Mehrwertsteuer-Kontrollamt Eupen*                                      178,24                    178,24
 **Total (1 rows)**                                                      **178,24**                **178,24**
==================================== ============== =============== === ============ ======== === ============= ==============
<BLANKLINE>
==============================================================
Partner Account Balances Clearings (Periods 2015-01...2015-05)
==============================================================
<BLANKLINE>
No data to display
========================================================================
Partner Account Balances Bank payment orders (Periods 2015-01...2015-05)
========================================================================
<BLANKLINE>
No data to display

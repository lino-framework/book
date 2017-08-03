.. _xl.bevats:

================================
Special Belgian VAT declarations
================================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_bevats
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *


This document describes the :mod:`lino_xl.lib.bevats` plugin which
adds functionality for handling **Special** Belgian VAT declarations
to be used by organizations who don't need to introduce "normal"
:doc:`bevat` but a simplified version, described e.g. `here
<https://finances.belgium.be/fr/entreprises/tva/declaration/declaration_speciale>`__.


Table of contents:

.. contents::
   :depth: 1
   :local:

Overview
========

This document uses :mod:`lino_book.projects.lydia` as example data.

.. currentmodule:: lino_xl.lib.bevats

Installing this plugin will automatically install
:mod:`lino_xl.lib.vat`.

>>> dd.plugins.bevats.needs_plugins     
['lino_xl.lib.vat']


>>> rt.show('vat.VatRegimes')
======= ========== ====================
 value   name       text
------- ---------- --------------------
 10      normal     Not subject to VAT
 20      subject    Subject to VAT
 30      intracom   Intra-community
======= ========== ====================
<BLANKLINE>

>>> rt.show('vat.VatColumns')
======= ====== ==============================
 value   name   text
------- ------ ------------------------------
 54             VAT due
 55             VAT returnable
 59             VAT deductible
 71             Purchase of ware
 72             Purchase of new vehicles
 73             Purchase of excised products
 75             Purchase of services
 76             Other purchase
======= ====== ==============================
<BLANKLINE>




Intracommunal purchases
=======================

This site is also an example of an organization which has a VAT id but
is not subject to VAT declaration. This means for them that if they
buy goods or services from other EU member states, they will pay
themselves the VAT in their own country. The provider does not write
any VAT on their invoice, but the customer computes that VAT based on
their national rate and then introduces a special kind of VAT
declaration and pays that VAT directly to the tax collector agency.

Here is an example of such an invoice:

>>> qs = ana.AnaAccountInvoice.objects.filter(vat_regime=vat.VatRegimes.intracom)
>>> obj = qs[0]
>>> print(obj.total_base)
33.06
>>> print(obj.total_vat)
0.00
>>> print(obj.total_incl)
33.06
>>> print(obj.entry_date)
2015-01-03

>>> rt.show(ledger.MovementsByVoucher, obj)
============================= ================= =========== =========== =========== =========
 Account                       Partner           Debit       Credit      Match       Cleared
----------------------------- ----------------- ----------- ----------- ----------- ---------
 (4400) Suppliers              AS Express Post               33,06       **PRC 1**   Yes
 (4510) VAT due                                              6,94                    No
 (6010) Purchase of services                     40,00                               Yes
                                                 **40,00**   **40,00**
============================= ================= =========== =========== =========== =========
<BLANKLINE>


This invoice says that we had **40€** of costs, **33.06€** of which to
be paid to the supplier and **6.94 €** to be paid as due VAT to the
tax office.

After the end of the month they have several such invoices, leading 
the following VAT
declaration:

>>> obj = accounts.Account.get_by_ref("4510")
>>> rt.show(ledger.MovementsByAccount, obj,
...     param_values=dict(start_date=i2d(20150101), end_date=i2d(20150131)))
============ ========= =================================== ======= ============ =======
 Value date   Voucher   Description                         Debit   Credit       Match
------------ --------- ----------------------------------- ------- ------------ -------
 07/01/2015   *PRC 5*   *Eesti Energia AS*                          562,60
 06/01/2015   *PRC 4*   *Eesti Energia AS*                          208,25
 05/01/2015   *PRC 3*   *Eesti Energia AS*                          104,76
 04/01/2015   *PRC 2*   *AS Matsalu Veevärk*                        24,52
 03/01/2015   *PRC 1*   *AS Express Post*                           6,94
                        **Balance -907.07 (5 movements)**           **907,07**
============ ========= =================================== ======= ============ =======
<BLANKLINE>


This credit balance of 907€ is cleared by the VAT declaration of that
month:


>>> obj = bevats.Declaration.objects.get(number=2)
>>> rt.show(ledger.MovementsByVoucher, obj)
==================== ================================== ============ ============ =========== =========
 Account              Partner                            Debit        Credit       Match       Cleared
-------------------- ---------------------------------- ------------ ------------ ----------- ---------
 (4500) Tax offices   Mehrwertsteuer-Kontrollamt Eupen                907,07       **VAT 2**   No
 (4510) VAT due                                          907,07                                No
                                                         **907,07**   **907,07**
==================== ================================== ============ ============ =========== =========
<BLANKLINE>

This declaration says that now we have no more due VAT but we have a
debth towards a tax office.

>>> jnl = rt.models.ledger.Journal.get_by_ref('VAT')
>>> rt.show('bevats.DeclarationsByJournal', jnl)
======== ============ ============== ============ =================== ============== ====== ====== ============== ================
 No.      Entry date   Start period   End period   Accounting period   [80]           [81]   [82]   [83]           Actions
-------- ------------ -------------- ------------ ------------------- -------------- ------ ------ -------------- ----------------
 4        04/04/2015   2015-03                     2015-04             907,31                       907,31         **Registered**
 3        04/03/2015   2015-02                     2015-03             907,44                       907,44         **Registered**
 2        04/02/2015   2015-01                     2015-02             907,07                       907,07         **Registered**
 1        04/01/2015   2014-12                     2015-01                                                         **Registered**
 **10**                                                                **2 721,82**                 **2 721,82**
======== ============ ============== ============ =================== ============== ====== ====== ============== ================
<BLANKLINE>

>>> dcl = rt.models.bevats.Declaration.objects.get(number=4)
>>> rt.show('ledger.MovementsByVoucher', dcl)
==================== ================================== ============ ============ =========== =========
 Account              Partner                            Debit        Credit       Match       Cleared
-------------------- ---------------------------------- ------------ ------------ ----------- ---------
 (4500) Tax offices   Mehrwertsteuer-Kontrollamt Eupen                907,31       **VAT 4**   No
 (4510) VAT due                                          907,31                                No
                                                         **907,31**   **907,31**
==================== ================================== ============ ============ =========== =========
<BLANKLINE>

>>> pv = dict(start_period=dcl.accounting_period)
>>> acc = rt.models.accounts.Account.objects.get(ref='4510')
>>> rt.show('ledger.MovementsByAccount', acc, param_values=pv)
============ ========== ==================================== ============ ============ =======
 Value date   Voucher    Description                          Debit        Credit       Match
------------ ---------- ------------------------------------ ------------ ------------ -------
 08/04/2015   *PRC 20*   *Eesti Energia AS*                                562,42
 07/04/2015   *PRC 19*   *Eesti Energia AS*                                208,68
 06/04/2015   *PRC 18*   *Eesti Energia AS*                                104,51
 05/04/2015   *PRC 17*   *AS Matsalu Veevärk*                              24,33
 04/04/2015   *PRC 16*   *AS Express Post*                                 7,38
 04/04/2015   *VAT 4*    *Mehrwertsteuer-Kontrollamt Eupen*   907,31
                         **Balance -0.01 (6 movements)**      **907,31**   **907,32**
============ ========== ==================================== ============ ============ =======
<BLANKLINE>

TODO: why do we have a difference of 0.01 €?

Note that these movements are not cleared. That's normal. Clearing is
done per partner, not per general account. See :blogref:`20170802`.



Reference
=========

.. class:: Declaration
           
    A VAT declaration. 


.. class:: DeclarationFields
           
    The list of fields in a VAT declaration.
    

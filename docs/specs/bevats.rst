.. _xl.bevats:

================================
Special Belgian VAT declarations
================================

.. to run only this test:

    $ doctest docs/specs/bevats.rst
    
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

The choice lists for VAT regimes and VAT columns are reduced compared
to those defined in :doc:`bevat`:


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
be paid to the supplier and **6.94 €** to be paid as VAT to the tax
office.

Note that our invoice is in January 2015.

>>> obj.accounting_period
AccountingPeriod #1 ('2015-01')

At the end of the month they have several such invoices and we must
declare the sum of their VAT to the tax office.
Here are the VAT declarations in our demo database:

>>> jnl = rt.models.ledger.Journal.get_by_ref('VAT')
>>> rt.show('bevats.DeclarationsByJournal', jnl)
==================== ============ ============== ============ =================== ============== ====== ====== ============== ================
 No.                  Entry date   Start period   End period   Accounting period   [80]           [81]   [82]   [83]           Workflow
-------------------- ------------ -------------- ------------ ------------------- -------------- ------ ------ -------------- ----------------
 3/2015               28/03/2015   2015-03                     2015-03             907,31                       907,31         **Registered**
 2/2015               28/02/2015   2015-02                     2015-02             907,44                       907,44         **Registered**
 1/2015               31/01/2015   2015-01                     2015-01             907,07                       907,07         **Registered**
 **Total (3 rows)**                                                                **2 721,82**                 **2 721,82**
==================== ============ ============== ============ =================== ============== ====== ====== ============== ================
<BLANKLINE>

There is usually one declaration per accounting period.
Let's look at the declaration of our period.

>>> dcl = rt.models.bevats.Declaration.objects.get(accounting_period=obj.accounting_period)

On screen you can see:

>>> for fld in bevats.DeclarationFields.get_list_items():
...    v = getattr(dcl, fld.name)
...    if v:
...        print("[{}] {} : {}".format(fld.value, fld.help_text, v))
[71] Ware : 1280.80
[72] New vehicles : 503.90
[75] Intracom services : 3441.78
[80] Due VAT for 71...76 : 907.07
[83] Total to pay : 907.07

And these are the movements generated by that declaration:

>>> rt.show('ledger.MovementsByVoucher', dcl)
==================== ================================== ============ ============ =========== =========
 Account              Partner                            Debit        Credit       Match       Cleared
-------------------- ---------------------------------- ------------ ------------ ----------- ---------
 (4500) Tax offices   Mehrwertsteuer-Kontrollamt Eupen                907,07       **VAT 1**   No
 (4510) VAT due                                          907,07                                No
                                                         **907,07**   **907,07**
==================== ================================== ============ ============ =========== =========
<BLANKLINE>

A declaration in general moves the sum of all those little amounts of
due VAT in account 4510 into another account, which means that now we
have no more "due VAT to declare" but now we have a "debth towards the
tax office".  From that point on a VAT declaration behaves and is
handled like a purchase invoice which needs to get paid in
time. That will be described in :doc:`cosi/finan`.

We can verify that the VAT declaration did the correct sum by looking
at the history of 4510 of that month:

>>> acc = accounts.Account.get_by_ref("4510")
>>> rt.show(ledger.MovementsByAccount, acc,
...     param_values=dict(start_period=obj.accounting_period))
============ ========= ==================================== ============ ============ =======
 Value date   Voucher   Description                          Debit        Credit       Match
------------ --------- ------------------------------------ ------------ ------------ -------
 31/01/2015   *VAT 1*   *Mehrwertsteuer-Kontrollamt Eupen*   907,07
 07/01/2015   *PRC 5*   *Eesti Energia AS*                                562,60
 06/01/2015   *PRC 4*   *Eesti Energia AS*                                208,25
 05/01/2015   *PRC 3*   *Eesti Energia AS*                                104,76
 04/01/2015   *PRC 2*   *AS Matsalu Veevärk*                              24,52
 03/01/2015   *PRC 1*   *AS Express Post*                                 6,94
                        **Balance 0.00 (6 movements)**       **907,07**   **907,07**
============ ========= ==================================== ============ ============ =======
<BLANKLINE>



Reference
=========

.. class:: Declaration
           
    A VAT declaration. 


.. class:: DeclarationFields
           
    The list of fields in a VAT declaration.
    

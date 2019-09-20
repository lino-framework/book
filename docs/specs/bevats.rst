.. doctest docs/specs/bevats.rst
.. _xl.bevats:

================================================
``bevats`` : Simplified Belgian VAT declarations
================================================

.. currentmodule:: lino_xl.lib.bevats

The :mod:`lino_xl.lib.bevats` plugin adds functionality for handling
**Special** Belgian VAT declarations to be used by organizations who don't need
to introduce "normal" VAT declarations (:doc:`bevat`) but may declare only
purchases. See e.g. `here
<https://finances.belgium.be/fr/entreprises/tva/declaration/declaration_speciale>`__.


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *

Dependencies
============

Installing this plugin will automatically install
:mod:`lino_xl.lib.vat`.

>>> dd.plugins.bevats.needs_plugins
['lino_xl.lib.vat']

The choice lists for VAT regimes and VAT columns are reduced compared
to those defined in :doc:`bevat`:

>>> rt.show('vat.VatRegimes')
======= =============== ==================== ========== ============== ==========
 value   name            text                 VAT area   Needs VAT id   item VAT
------- --------------- -------------------- ---------- -------------- ----------
 10      normal          Not subject to VAT              No             Yes
 20      subject         Subject to VAT       National   Yes            Yes
 30      intracom        Intracom services    EU         Yes            Yes
 35      intracom_supp   Intracom supplies    EU         Yes            Yes
======= =============== ==================== ========== ============== ==========
<BLANKLINE>


>>> rt.show('vat.VatColumns')
======= ============================== ========================= ================================
 value   text                           Common account            Account
------- ------------------------------ ------------------------- --------------------------------
 54      VAT due                        VAT due                   (4510) VAT due
 55      VAT returnable                 VAT returnable            (4511) VAT returnable
 59      VAT deductible                 VAT deductible            (4512) VAT deductible
 71      Purchase of ware               Purchase of goods         (6040) Purchase of goods
 72      Purchase of new vehicles       Purchase of investments   (6020) Purchase of investments
 73      Purchase of excised products
 75      Purchase of services           Purchase of services      (6010) Purchase of services
 76      Other purchase
======= ============================== ========================= ================================
<BLANKLINE>


>>> rt.show('bevats.DeclarationFields')  #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +ELLIPSIS
+-------+------+------+--------------------------------------------+
| value | name | text | Description                                |
+=======+======+======+============================================+
| 71    | F71  | [71] | Intracom supplies |br|                     |
|       |      |      | columns 71 |br|                            |
|       |      |      | MvtDeclarationField Debit |br|             |
+-------+------+------+--------------------------------------------+
| 72    | F72  | [72] | New vehicles |br|                          |
|       |      |      | columns 72 |br|                            |
|       |      |      | MvtDeclarationField Debit |br|             |
+-------+------+------+--------------------------------------------+
| 73    | F73  | [73] | Excised products |br|                      |
|       |      |      | columns 73 |br|                            |
|       |      |      | MvtDeclarationField Debit |br|             |
+-------+------+------+--------------------------------------------+
| 75    | F75  | [75] | Intracom services |br|                     |
|       |      |      | columns 75 |br|                            |
|       |      |      | MvtDeclarationField Debit |br|             |
+-------+------+------+--------------------------------------------+
| 76    | F76  | [76] | Other operations |br|                      |
|       |      |      | columns 76 |br|                            |
|       |      |      | MvtDeclarationField Debit |br|             |
+-------+------+------+--------------------------------------------+
| 77    | F77  | [77] | Credit notes on 71, 72, 73 and 75 |br|     |
|       |      |      | columns 71 72 73 75 |br|                   |
|       |      |      | MvtDeclarationField Credit only |br|       |
+-------+------+------+--------------------------------------------+
| 78    | F78  | [78] | Credit notes on 76 |br|                    |
|       |      |      | columns 76 |br|                            |
|       |      |      | MvtDeclarationField Debit only |br|        |
+-------+------+------+--------------------------------------------+
| 80    | F80  | [80] | Due VAT for 71...76 |br|                   |
|       |      |      | columns 54 |br|                            |
|       |      |      | MvtDeclarationField Credit |br|            |
+-------+------+------+--------------------------------------------+
| 81    | F81  | [81] | Miscellaneous corrections due |br|         |
|       |      |      | WritableDeclarationField Credit |br|       |
+-------+------+------+--------------------------------------------+
| 82    | F82  | [82] | Miscellaneous corrections returnable |br|  |
|       |      |      | WritableDeclarationField Debit |br|        |
+-------+------+------+--------------------------------------------+
| 83    | F83  | [83] | Total to pay |br|                          |
|       |      |      | SumDeclarationField Credit |br|            |
|       |      |      | Sum of F80 F81 F82 |br|                    |
+-------+------+------+--------------------------------------------+
<BLANKLINE>


Intracommunal purchases
=======================

When an organizations with special VAT buys goods or services from other EU
member states, the provider does not write any VAT on their invoice. But the
organization computes that VAT for their VAT declaration based on their
national rate and declares it as due to the VAT office of their own country.

Here is an example of such an invoice:

>>> qs = ana.AnaAccountInvoice.objects.filter(vat_regime=vat.VatRegimes.intracom)
>>> obj = qs[0]
>>> print(obj)
PRC 6/2015

How the data has been entered:

>>> rt.show(ana.ItemsByInvoice, obj)
============================= ============= ==================== ================= ================= ===== ==============
 Account                       Description   Analytical account   VAT class         Total excl. VAT   VAT   Total to pay
----------------------------- ------------- -------------------- ----------------- ----------------- ----- --------------
 (6040) Purchase of goods                    (3000) Investment    Normal VAT rate   61,10                   61,10
 (6010) Purchase of services                 (4100) Wages         Normal VAT rate   82,30                   82,30
 **Total (2 rows)**                                                                 **143,40**              **143,40**
============================= ============= ==================== ================= ================= ===== ==============
<BLANKLINE>

Totals computed by Lino:

>>> print(obj.total_base)
143.40
>>> print(obj.total_vat)
0.00
>>> print(obj.total_incl)
143.40

>>> rt.show(ledger.MovementsByVoucher, obj)
============================= =============== ============ ============ ================ =========
 Account                       Partner         Debit        Credit       Match            Cleared
----------------------------- --------------- ------------ ------------ ---------------- ---------
 (4400) Suppliers              Donderweer BV                143,40       **PRC 6/2015**   Yes
 (4510) VAT due                                             30,11                         Yes
 (6010) Purchase of services                   99,58                                      Yes
 (6040) Purchase of goods                      73,93                                      Yes
                                               **173,51**   **173,51**
============================= =============== ============ ============ ================ =========
<BLANKLINE>

This invoice says that we had **173,51 €** of costs, **143,40 €** of
which to be paid to the supplier and **30,11 €** to be paid as VAT to
the tax office.

Note that our invoice is in January 2015.

>>> print(obj.entry_date)
2015-01-08

>>> obj.accounting_period
AccountingPeriod #1 ('2015-01')

At the end of the month they have several such invoices and we must
declare the sum of their VAT to the tax office.
Here are the VAT declarations in our demo database:

>>> jnl = rt.models.ledger.Journal.get_by_ref('VAT')
>>> rt.show('bevats.DeclarationsByJournal', jnl)
==================== ============ ============== ============ =================== ============ ====== ====== ============ ================
 No.                  Entry date   Start period   End period   Accounting period   [80]         [81]   [82]   [83]         Workflow
-------------------- ------------ -------------- ------------ ------------------- ------------ ------ ------ ------------ ----------------
 3/2015               28/03/2015   2015-03                     2015-03             71,65                      71,65        **Registered**
 2/2015               28/02/2015   2015-02                     2015-02             71,95                      71,95        **Registered**
 1/2015               31/01/2015   2015-01                     2015-01             72,09                      72,09        **Registered**
 **Total (3 rows)**                                                                **215,69**                 **215,69**
==================== ============ ============== ============ =================== ============ ====== ====== ============ ================
<BLANKLINE>


There is usually one declaration per accounting period.
Let's look at the declaration of our period.

>>> dcl = rt.models.bevats.Declaration.objects.get(accounting_period=obj.accounting_period)

On screen you can see:

>>> for fld in bevats.DeclarationFields.get_list_items():
...    v = getattr(dcl, fld.name)
...    if v:
...        print("[{}] {} : {}".format(fld.value, fld.help_text, v))
[71] Intracom supplies : 1354.73
[72] New vehicles : 668.81
[75] Intracom services : 2950.97
[80] Due VAT for 71...76 : 72.09
[83] Total to pay : 72.09

When you print the declaration, Lino also includes the
:class:`IntracomPurchases <lino_xl.lib.vat.IntracomPurchases>`
table for that period:

>>> pv = dict(start_period=dcl.start_period, end_period=dcl.end_period)
>>> rt.show(vat.IntracomPurchases, param_values=pv, header_level=2)
-------------------------
Intra-Community purchases
-------------------------
==================== =============== ================ =================== ================= ===== ==============
 Invoice              Partner         VAT id           VAT regime          Total excl. VAT   VAT   Total to pay
-------------------- --------------- ---------------- ------------------- ----------------- ----- --------------
 *PRC 6/2015*         Donderweer BV   NL957996364B01   Intracom services   143,40                  143,40
 *PRC 7/2015*         Van Achter NV   NL336548370B01   Intracom supplies   199,90                  199,90
 **Total (2 rows)**                                                        **343,30**              **343,30**
==================== =============== ================ =================== ================= ===== ==============
<BLANKLINE>

And these are the movements generated by our declaration:

>>> rt.show('ledger.MovementsByVoucher', dcl)
==================== ================================== =========== =========== ================ =========
 Account              Partner                            Debit       Credit      Match            Cleared
-------------------- ---------------------------------- ----------- ----------- ---------------- ---------
 (4510) VAT due                                          30,11                                    Yes
 (4510) VAT due                                          41,98                                    Yes
 (4600) Tax Offices   Mehrwertsteuer-Kontrollamt Eupen               72,09       **VAT 1/2015**   No
                                                         **72,09**   **72,09**
==================== ================================== =========== =========== ================ =========
<BLANKLINE>

A declaration in general moves the sum of all those little amounts of due VAT
in account 4510 into another account, which means that now we have no more "due
VAT" to declare but now we have a "debth towards the tax office".  From that
point on a VAT declaration behaves and is handled like a purchase invoice which
needs to get paid in time. That will be described in :doc:`finan`.

We can verify that the VAT declaration did the correct sum by looking at the
history of 4510 for that month:

>>> acc = ledger.Account.get_by_ref("4510")
>>> rt.show(ledger.MovementsByAccount, acc,
...     param_values=dict(start_period=obj.accounting_period))
============ ============== ==================================== =========== =========== =======
 Value date   Voucher        Description                          Debit       Credit      Match
------------ -------------- ------------------------------------ ----------- ----------- -------
 31/01/2015   *VAT 1/2015*   *Mehrwertsteuer-Kontrollamt Eupen*   30,11
 31/01/2015   *VAT 1/2015*   *Mehrwertsteuer-Kontrollamt Eupen*   41,98
 09/01/2015   *PRC 7/2015*   *Van Achter NV*                                  41,98
 08/01/2015   *PRC 6/2015*   *Donderweer BV*                                  30,11
                             **Balance 0.00 (4 movements)**       **72,09**   **72,09**
============ ============== ==================================== =========== =========== =======
<BLANKLINE>



Reference
=========

.. class:: Declaration

    Implements :class:`lino_xl.lib.vat.VatDeclaration`.


.. class:: DeclarationFields

    Implements :class:`lino_xl.lib.vat.DeclarationFields`.

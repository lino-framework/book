.. doctest docs/specs/bevats.rst
.. _xl.bevats:

================================================
``bevats`` : Simplified Belgian VAT declarations
================================================

.. currentmodule:: lino_xl.lib.bevats

The :mod:`lino_xl.lib.bevats` plugin
adds functionality for handling **Special** Belgian VAT declarations
to be used by organizations who don't need to introduce "normal"
:doc:`bevat` but a simplified version, described e.g. `here
<https://finances.belgium.be/fr/entreprises/tva/declaration/declaration_speciale>`__.


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst


Code snippets in this document are based on the
:mod:`lino_book.projects.lydia` demo.

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

.. class:: VatRegimes

    The :mod:`lino_xl.lib.betvats` plugin redefines the list of VAT
    regimes:

    >>> rt.show('vat.VatRegimes')
    ======= =============== ====================
     value   name            text
    ------- --------------- --------------------
     10      normal          Not subject to VAT
     20      subject         Subject to VAT
     30      intracom        Intracom services
     35      intracom_supp   Intracom supplies
    ======= =============== ====================
    <BLANKLINE>

.. class:: VatColumns

    The :mod:`lino_xl.lib.betvats` plugin redefines the list of VAT
    columns:

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

.. class:: DeclarationFields
      
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

The :mod:`lino_book.projects.lydia` demo is also an example of an
organization which has a VAT id but is not subject to VAT
declaration. This means for them that if they buy goods or services
from other EU member states, they will pay themselves the VAT in their
own country. The provider does not write any VAT on their invoice, but
the customer computes that VAT based on their national rate and then
introduces a special kind of VAT declaration and pays that VAT
directly to the tax collector agency.

Here is an example of such an invoice:

>>> qs = ana.AnaAccountInvoice.objects.filter(vat_regime=vat.VatRegimes.intracom)
>>> obj = qs[0]
>>> print(obj.total_base)
118.52
>>> print(obj.total_vat)
24.88
>>> print(obj.total_incl)
143.40

>>> rt.show(ledger.MovementsByVoucher, obj)
============================= =============== ============ ============ ================ =========
 Account                       Partner         Debit        Credit       Match            Cleared
----------------------------- --------------- ------------ ------------ ---------------- ---------
 (4400) Suppliers              Donderweer BV                118,52       **PRC 6/2015**   Yes
 (4510) VAT due                                             24,88                         Yes
 (6010) Purchase of services                   82,30                                      Yes
 (6040) Purchase of goods                      61,10                                      Yes
                                               **143,40**   **143,40**
============================= =============== ============ ============ ================ =========
<BLANKLINE>

This invoice says that we had **143,40 €** of costs, **118,52 €** of
which to be paid to the supplier and **24,88 €** to be paid as VAT to
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
 3/2015               28/03/2015   2015-03                     2015-03             59,21                      59,21        **Registered**
 2/2015               28/02/2015   2015-02                     2015-02             59,46                      59,46        **Registered**
 1/2015               31/01/2015   2015-01                     2015-01             59,57                      59,57        **Registered**
 **Total (3 rows)**                                                                **178,24**                 **178,24**
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
[71] Intracom supplies : 1341.90
[72] New vehicles : 703.80
[75] Intracom services : 3524.08
[80] Due VAT for 71...76 : 59.57
[83] Total to pay : 59.57

When you print the declaration, Lino also includes the
:class:`IntracomPurchases <lino_xl.lib.vat.IntracomPurchases>`
table for that period:
       
>>> pv = dict(start_period=dcl.start_period, end_period=dcl.end_period)
>>> rt.show(vat.IntracomPurchases, param_values=pv, header_level=2)
-------------------------
Intra-Community purchases
-------------------------
==================== =============== ======== =================== ================= =========== =================
 Invoice              Partner         VAT id   VAT regime          Total excl. VAT   VAT         Total incl. VAT
-------------------- --------------- -------- ------------------- ----------------- ----------- -----------------
 *PRC 6/2015*         Donderweer BV            Intracom services   118,52            24,88       143,40
 *PRC 7/2015*         Van Achter NV            Intracom supplies   165,21            34,69       199,90
 **Total (2 rows)**                                                **283,73**        **59,57**   **343,30**
==================== =============== ======== =================== ================= =========== =================
<BLANKLINE>


And these are the movements generated by our declaration:

>>> rt.show('ledger.MovementsByVoucher', dcl)
==================== ================================== =========== =========== ================ =========
 Account              Partner                            Debit       Credit      Match            Cleared
-------------------- ---------------------------------- ----------- ----------- ---------------- ---------
 (4510) VAT due                                          24,88                                    Yes
 (4510) VAT due                                          34,69                                    Yes
 (4600) Tax Offices   Mehrwertsteuer-Kontrollamt Eupen               59,57       **VAT 1/2015**   No
                                                         **59,57**   **59,57**
==================== ================================== =========== =========== ================ =========
<BLANKLINE>

A declaration in general moves the sum of all those little amounts of
due VAT in account 4510 into another account, which means that now we
have no more "due VAT to declare" but now we have a "debth towards the
tax office".  From that point on a VAT declaration behaves and is
handled like a purchase invoice which needs to get paid in
time. That will be described in :doc:`finan`.

We can verify that the VAT declaration did the correct sum by looking
at the history of 4510 of that month:

>>> acc = ledger.Account.get_by_ref("4510")
>>> rt.show(ledger.MovementsByAccount, acc,
...     param_values=dict(start_period=obj.accounting_period))
============ ============== ==================================== =========== =========== =======
 Value date   Voucher        Description                          Debit       Credit      Match
------------ -------------- ------------------------------------ ----------- ----------- -------
 31/01/2015   *VAT 1/2015*   *Mehrwertsteuer-Kontrollamt Eupen*   24,88
 31/01/2015   *VAT 1/2015*   *Mehrwertsteuer-Kontrollamt Eupen*   34,69
 09/01/2015   *PRC 7/2015*   *Van Achter NV*                                  34,69
 08/01/2015   *PRC 6/2015*   *Donderweer BV*                                  24,88
                             **Balance 0.00 (4 movements)**       **59,57**   **59,57**
============ ============== ==================================== =========== =========== =======
<BLANKLINE>



Reference
=========

.. class:: Declaration
           
    Implements :class:`lino_xl.lib.vat.VatDeclaration`.


.. class:: DeclarationFields
           
    Implements :class:`lino_xl.lib.vat.DeclarationFields`.
    

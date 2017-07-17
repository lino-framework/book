.. _xl.specs.ana:

=============================
Analytical accounting
=============================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_ana
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *

This plugin defines two models "Analytical accounts" and "Analytical
account groups" which you can see as follows:

>>> show_menu_path('ana.Accounts')
Configure --> Accounting --> Analytical accounts
>>> show_menu_path('ana.Groups')
Configure --> Accounting --> Analytical account groups


>>> rt.show('ana.Accounts')
=========== ================= ====================== ================== ======================
 Reference   Designation       Designation (de)       Designation (fr)   Group
----------- ----------------- ---------------------- ------------------ ----------------------
 1100        Wages             Löhne und Gehälter     Salaires           Operation costs
 1200        Transport         Transport              Transport          Operation costs
 1300        Training          Ausbildung             Formation          Operation costs
 1400        Other costs       Sonstige Unkosten      Other costs        Operation costs
 2100        Secretary wages   Gehälter Sekretariat   Secretary wages    Administrative costs
 2110        Manager wages     Gehälter Direktion     Manager wages      Administrative costs
 2200        Transport         Transport              Transport          Administrative costs
 2300        Training          Ausbildung             Formation          Administrative costs
 3000        Investment        Investierung           Investment         Investments
 4100        Wages             Löhne und Gehälter     Salaires           Project 1
 4200        Transport         Transport              Transport          Project 1
 4300        Training          Ausbildung             Formation          Project 1
 5100        Wages             Löhne und Gehälter     Salaires           Project 2
 5200        Transport         Transport              Transport          Project 2
 5300        Other costs       Sonstige Unkosten      Other costs        Project 2
=========== ================= ====================== ================== ======================
<BLANKLINE>

>>> rt.show('ana.Groups')
=========== ====================== =================== ======================
 Reference   Designation            Designation (de)    Designation (fr)
----------- ---------------------- ------------------- ----------------------
 1           Operation costs        Diplome             Operation costs
 2           Administrative costs   Verwaltungskosten   Administrative costs
 3           Investments            Investierungen      Investments
 4           Project 1              Projekt 1           Project 1
 5           Project 2              Projekt 2           Project 2
=========== ====================== =================== ======================
<BLANKLINE>

The plugin then injects two fields to your general accounts model and
one field into your movments model:

>>> show_fields(accounts.Account, "needs_ana ana_account")
=============== ========================== ===========
 Internal name   Verbose name               Help text
--------------- -------------------------- -----------
 needs_ana       Needs analytical account
 ana_account     Analytical account
=============== ========================== ===========

>>> show_fields(ledger.Movement, "ana_account")
=============== ==================== ===========
 Internal name   Verbose name         Help text
--------------- -------------------- -----------
 ana_account     Analytical account
=============== ==================== ===========

And finally this plugin defines a new voucher type
`ana.AnaAccountInvoice` which is almost the same as
`vat.AccountInvoice` except that it has an additional field per
invoice item where the user can specify an analytic account.  For
example:

>>> obj = ana.AnaAccountInvoice.objects.get(pk=1)
>>> rt.show(ana.ItemsByInvoice, obj)
============================= ============= ==================== =========== ================= ========== =================
 Account                       Description   Analytical account   VAT Class   Total excl. VAT   VAT        Total incl. VAT
----------------------------- ------------- -------------------- ----------- ----------------- ---------- -----------------
 (6010) Purchase of services                 (1100) Wages         Normal      33,06             6,94       40,00
 **Total (1 rows)**                                                           **33,06**         **6,94**   **40,00**
============================= ============= ==================== =========== ================= ========== =================
<BLANKLINE>


Pro Generalkonto kannst du ein einziges Analysekonto angeben, das Lino
von sich aus vorschlagen soll, wenn du eine neue Einkaufsrechnung
(EKR) eingibst. In der EKR kannst du dann immer noch ein anderes AK
auswählen. Du kannst das AK im G-Konto auch leer lassen (selbst wenn
"Braucht AK" angekreuzt ist). Das bedeutet dann, dass Lino in der EKR
keinen Vorschlag machen soll. Dann ist man sozusagen gezwungen, bei
jeder Buchung zu überlegen, welches AK man auswählt.



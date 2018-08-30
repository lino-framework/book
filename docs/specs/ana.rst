.. doctest docs/specs/ana.rst
.. _xl.specs.ana:

=============================
Analytical accounting
=============================

.. currentmodule:: lino_xl.lib.ana

The :mod:`lino_xl.lib.ana` plugin adds analytic accounting to
general ledger.
                   
The plugin defines several models:

- Analytical accounts and their groups
- Analytical invoices and their items


Table of contents:

.. contents::
   :depth: 1
   :local:


About this document
===================

Examples in this document use the :mod:`lino_book.projects.lydia` demo
project.

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *

The plugin requires :mod:`lino_xl.lib.ledger`.

>>> dd.plugins.ana.needs_plugins
['lino_xl.lib.ledger']


Analytical accounts
===================

Both "Analytical accounts" and "Analytical account groups" can be
configured:

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

>>> show_fields(ledger.Account, "needs_ana ana_account")
+---------------+--------------------------+---------------------------------------------------------------+
| Internal name | Verbose name             | Help text                                                     |
+===============+==========================+===============================================================+
| needs_ana     | Needs analytical account | Whether transactions on this account require the user to also |
|               |                          | specify an analytic account.                                  |
+---------------+--------------------------+---------------------------------------------------------------+
| ana_account   | Analytical account       | Which analytic account to suggest for transactions on this    |
|               |                          | account.                                                      |
+---------------+--------------------------+---------------------------------------------------------------+

>>> show_fields(ledger.Movement, "ana_account")
=============== ==================== ===============================================================
 Internal name   Verbose name         Help text
--------------- -------------------- ---------------------------------------------------------------
 ana_account     Analytical account   The analytic account to move together with this transactions.
=============== ==================== ===============================================================

And finally this plugin defines a new voucher type
`ana.AnaAccountInvoice` which is almost the same as
`vat.AccountInvoice` except that it has an additional field per
invoice item where the user can specify an analytic account.  For
example:

>>> obj = ana.AnaAccountInvoice.objects.get(pk=1)
>>> rt.show(ana.ItemsByInvoice, obj)
============================= ============= ==================== =========== ================= ===== =================
 Account                       Description   Analytical account   VAT class   Total excl. VAT   VAT   Total incl. VAT
----------------------------- ------------- -------------------- ----------- ----------------- ----- -----------------
 (6010) Purchase of services                 (1100) Wages         Normal      40,00                   40,00
 **Total (1 rows)**                                                           **40,00**               **40,00**
============================= ============= ==================== =========== ================= ===== =================
<BLANKLINE>


When you change the general account of an invoice item, Lino always
updates the analytical account of that item.





Analytic accounts
=================

.. class:: Account

    .. attribute:: ref

       The unique reference.
                   
    .. attribute:: designation

    .. attribute:: group

        The analytic account group this account belongs to.
                   
Groups of analytic accounts
===========================

.. class:: Group

    .. attribute:: ref
                   
       The unique reference.
       
    .. attribute:: designation

           
Invoices with analytic account
==============================

.. class:: AnaAccountInvoice
           
    
    .. attribute:: make_copy

        The :class:`MakeCopy` action.

.. class:: InvoiceItem

    .. attribute:: voucher           
    .. attribute:: ana_account
    .. attribute:: title
                   

Make a copy of an invoice (:guilabel:`⁂`)
=========================================

           
.. class:: MakeCopy

    You can simplify manual recording of invoices using the :guilabel:`⁂`
    button which creates an invoice using an existing invoice as template.

    Lino then opens the following dialog window:

    .. image:: ana/AnaAccountInvoice.make_copy.de.png

    Wenn man das Fenster bestätigt, wird ohne weitere Fragen eine neue
    Rechnung erstellt und registriert.

    Das Verhalten dieser Aktion hängt teilweise davon ab, ob man den
    Gesamtbetrag (:guilabel:`Total inkl MWSt`) eingibt oder nicht:

    - Wenn man einen Gesamtbetrag eingibt, wird eine einzige
      Rechnungszeile erstellt mit diesem Betrag. Das Generalkonto dieser
      Zeile ist entweder das im Dialogfenster angegebene, oder (falls man
      das Feld dort leer gelassen hat) das G-Konto der ersten Zeile der
      Kopiervorlage.  Ebenso das A-Konto.

    - Wenn man den Gesamtbetrag leer lässt, werden alle Zeilen der
      Kopiervorlage exakt kopiert.


    

    .. attribute:: entry_date
    
        The entry date of the invoice to create.
    
    .. attribute:: partner
    
        The partner of the invoice to create.
        
    .. attribute:: subject
    
        The subject of the invoice to create.
        
    .. attribute:: your_ref
    
        The "your reference" of the invoice to create.
        
    .. attribute:: total_incl

        The total amount of the invoice to create.  Leave blank if you
        want to copy all rows.

        If you enter an amount, 
    
    .. attribute:: account
    
        The general account to use for the item of the invoice if you
        specified a total amount.
        
    .. attribute:: ana_account
    
        The analytical account to use for the item of the invoice if
        you specified a total amount.
        

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

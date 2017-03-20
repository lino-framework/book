.. _noi.specs.faculties:

================================
Faculties management in Lino Noi
================================


.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_faculties
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_noi.projects.team.settings.demo')
    >>> from lino.api.doctest import *


Lino Noi has a notions of **faculties** and **competences** which
might be useful in bigger teams for assigning a ticket to a worker.

They are implemented in :mod:`lino_xl.lib.faculties`.  In the Team
demo database they are not really used.  See also :ref:`care` which
has does more usage of them.


.. contents::
  :local:


>>> rt.show(faculties.TopLevelSkills)
... #doctest: +REPORT_UDIFF
=============== ================== ================== ========= ========== ==============
 Designation     Designation (de)   Designation (fr)   Remarks   Children   Parent skill
--------------- ------------------ ------------------ --------- ---------- --------------
 Analysis        Analysis           Analysis
 Code changes    Code changes       Code changes
 Configuration   Configuration      Configuration
 Documentation   Documentation      Documentation
 Enhancement     Enhancement        Enhancement
 Offer           Offer              Offer
 Optimization    Optimization       Optimization
 Testing         Testing            Testing
=============== ================== ================== ========= ========== ==============
<BLANKLINE>


>>> rt.show('faculties.Offers')
... #doctest: +REPORT_UDIFF
==== ================= =============== ============= ==========
 ID   User              Skill           Description   Affinity
---- ----------------- --------------- ------------- ----------
 1    Jean              Analysis                      100
 2    Jean              Code changes                  100
 3    Jean              Configuration                 100
 4    Luc               Documentation                 100
 5    Luc               Enhancement                   100
 6    Mathieu           Offer                         100
 7    Mathieu           Optimization                  100
 8    Romain Raffault   Testing                       100
 9    Romain Raffault   Analysis                      100
 10   Rolf Rompen       Code changes                  100
 11   Rolf Rompen       Configuration                 100
 12   Rolf Rompen       Documentation                 100
 13   Robin Rood        Enhancement                   100
 14   Jean              Offer                         100
 15   Jean              Optimization                  100
 16   Jean              Testing                       100
 17   Luc               Analysis                      100
 18   Luc               Code changes                  100
 19   Mathieu           Configuration                 100
 20   Mathieu           Documentation                 100
 21   Romain Raffault   Enhancement                   100
 22   Romain Raffault   Offer                         100
 23   Rolf Rompen       Optimization                  100
 24   Rolf Rompen       Testing                       100
 25   Rolf Rompen       Analysis                      100
 26   Robin Rood        Code changes                  100
                                                      **2600**
==== ================= =============== ============= ==========
<BLANKLINE>



>>> show_choices('axel', '/choices/faculties/OffersByEndUser/faculty')
Analysis
Code changes
Configuration
Documentation
Enhancement
Offer
Optimization
Testing

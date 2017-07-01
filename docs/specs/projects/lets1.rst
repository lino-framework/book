===============================
The LETS application specs (v1)
===============================


.. how to test just this document:
    $ python setup.py test -s tests.SpecsTests.test_projects_lets1
    
    doctest init:
    >>> from lino import startup
    >>> startup('lino_book.projects.lets1.settings')
    >>> from lino.api.doctest import *


This document describes the :mod:`lino_book.projets.lets1` demo
project, an application used as example in :doc:`/dev/lets`.

.. contents::
   :local:
   :depth: 2   

  

Master data
===========

Show the list of members:    

>>> rt.show(rt.actors.lets.Members)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
========= ===================== ========== ============================================ ===========================================
 name      email                 place      offered_products                             wanted_products
--------- --------------------- ---------- -------------------------------------------- -------------------------------------------
 Fred      fred@example.com      Tallinn    `Bread <Detail>`__, `Buckwheat <Detail>`__
 Argo      argo@example.com      Haapsalu   `Electricity repair work <Detail>`__
 Peter     peter@example.com     Vigala
 Anne      anne@example.com      Tallinn    `Buckwheat <Detail>`__
 Jaanika   jaanika@example.com   Tallinn
 Henri     henri@example.com     Tallinn    `Electricity repair work <Detail>`__         `Buckwheat <Detail>`__, `Eggs <Detail>`__
 Mari      mari@example.com      Tartu                                                   `Eggs <Detail>`__
 Katrin    katrin@example.com    Vigala
========= ===================== ========== ============================================ ===========================================
<BLANKLINE>

The `Products` table shows all products in alphabetical order:

>>> rt.show(rt.actors.lets.Products)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
==== ========================= ======================================= =======================================
 ID   name                      Offered by                              Wanted by
---- ------------------------- --------------------------------------- ---------------------------------------
 1    Bread                     `Fred <Detail>`__
 2    Buckwheat                 `Fred <Detail>`__, `Anne <Detail>`__    `Henri <Detail>`__
 5    Building repair work
 3    Eggs                                                              `Henri <Detail>`__, `Mari <Detail>`__
 6    Electricity repair work   `Henri <Detail>`__, `Argo <Detail>`__
 4    Sanitary repair work
==== ========================= ======================================= =======================================
<BLANKLINE>

Offers
======

The `Offers` table show all offers.

>>> rt.show(rt.actors.lets.Offers)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
==== ======== ========================= =============
 ID   member   product                   valid until
---- -------- ------------------------- -------------
 1    Fred     Bread
 2    Fred     Buckwheat
 3    Anne     Buckwheat
 4    Henri    Electricity repair work
 5    Argo     Electricity repair work
==== ======== ========================= =============
<BLANKLINE>


The *ActiveProducts* table is an example of how to handle customized
complex filter conditions.  It is a subclass of `Products`, but adds
filter conditions so that only "active" products are shown, i.e. for
which there is at least one offer or one demand.  It also specifies
`column_names` to show the two virtual fields `offered_by` and
`wanted_by`.

>>> rt.show(rt.actors.lets.ActiveProducts)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
========================= ======================================= =======================================
 name                      Offered by                              Wanted by
------------------------- --------------------------------------- ---------------------------------------
 Bread                     `Fred <Detail>`__
 Buckwheat                 `Fred <Detail>`__, `Anne <Detail>`__    `Henri <Detail>`__
 Eggs                                                              `Henri <Detail>`__, `Mari <Detail>`__
 Electricity repair work   `Henri <Detail>`__, `Argo <Detail>`__
========================= ======================================= =======================================
<BLANKLINE>


Menu structure and main page
============================


We can show the main menu in a doctest snippet:

>>> ses = rt.login()
>>> ses.show_menu() #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Master : members, products
- Market : offers, demands
- Configure : places




.. doctest docs/dev/vtables.rst
.. _dev.vtables: 
   
==============
Virtual tables
==============

..
    >>> from lino import startup
    >>> startup('lino_book.projects.vtables.settings')
    >>> from lino.api.doctest import *
    

A virtual table is a table which has no database model.

For this tutorial we will use the :mod:`lino_book.projects.vtables`
demo project.


Here is the :xfile:`models.py` file 

.. literalinclude:: ../../lino_book/projects/vtables/models.py
  

Some setup for doctest:
  
>>> rt.show(vtables.CitiesAndInhabitants)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
========= ========= ============
 Country   City      Population
--------- --------- ------------
 Belgium   Eupen     17000
 Belgium   Liege     400000
 Belgium   Raeren    5000
 Estonia   Tallinn   400000
 Estonia   Vigala    1500
========= ========= ============
<BLANKLINE>


Here is a list of virtual tables in other applications:

- :class:`lino.modlib.ipdict.Connections`
- :class:`lino.modlib.about.models.Models`
- :class:`lino_xl.lib.ledger.DebtorsCreditors`
- :class:`lino_xl.lib.ledger.VouchersByPartnerBase`
- :class:`lino_xl.lib.polls.AnswersByResponse`
  

  

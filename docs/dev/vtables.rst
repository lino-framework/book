.. doctest docs/dev/vtables.rst
.. _dev.vtables: 
   
==============
Virtual tables
==============

..
    >>> from lino import startup
    >>> startup('lino_book.projects.vtables.settings')
    >>> from lino.api.doctest import *
    

A virtual table is a table which which is not connected to any
database model.  Which means that you are responsible for defining
that data.

The **rows** of a virtual table are defined by a method
:meth:`get_data_rows <lino.core.tables.AbstractTable.get_data_rows>`.
In :doc:`database tables </dev/tables/index>` this method has a
default implementation based on the :attr:`model
<lino.core.tables.Table.model>` attribute.

The **columns** of a virtual table must be defined using *virtual
fields*.

Here is an example of a virtual table (taken from the
:mod:`lino_book.projects.vtables` demo project):

.. literalinclude:: ../../lino_book/projects/vtables/models.py

We can show this table in a shell session:
  
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


Usage examples of virtual tables in real applications:

- :class:`lino.modlib.ipdict.Connections`
- :class:`lino.modlib.about.models.Models`
- :class:`lino_xl.lib.ledger.DebtorsCreditors`
- :class:`lino_xl.lib.ledger.VouchersByPartnerBase`
- :class:`lino_xl.lib.polls.AnswersByResponse`
  

  

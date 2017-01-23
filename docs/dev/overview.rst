==============================
Structure overview cheat sheet
==============================

Packages
========

- Atelier : a collection of utilities maintained by the Lino team and
  which might be useful to other (non-Lino) Python
  projects. :mod:`projects <atelier.projects>`, :mod:`invlib
  <atelier.invlib>`, :mod:`rstgen <atelier.rstgen>`
  
- Commondata : an experimental project for storing common data as
  Python code.
  
- Lino : the core framework + the standard plugin library
  (mod:`lino.modlib`) : users, notify, comments, changes, about, ...
  
- XL : Extension library : contacts, countries, cal, ... (see
  :mod:`lino_xl.lib`)
       
- Book : the docs for :mod:`lino` and :mod:`lino_xl`. Not published as
  PyPI package.
  
- Così : Accounting plugins, including a few sample projects.
  
- Noi : tickets, projects, work, votes

- Presto

- Welfare

- Avanti

  
Package dependencies
====================

.. graphviz::

   digraph foo {
   
    commondata -> atelier
    lino -> atelier;
    lino_xl -> lino;
    lino_book -> lino_cosi; 
    lino_book -> commondata; 
    lino_noi -> lino_xl; 
    lino_cosi -> lino_xl; 
    lino_welfare -> lino_cosi;
    lino_voga -> lino_cosi;
    lino_presto -> lino_cosi;
    lino_presto -> lino_noi;
    lino_avanti -> lino_noi;

   }


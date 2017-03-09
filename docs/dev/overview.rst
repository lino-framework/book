.. _dev.overview:

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
       
- ``book`` the docs for :mod:`lino` and :mod:`lino_xl`. Not
  published as PyPI package.
  
- ``noi`` : :ref:`noi`. The application we use for managing our
  collaboration. tickets, projects, time tracking, votes.
  
- :file:`cosi` : :ref:`cosi`. Accounting plugins, including a few
  sample projects.
  
- :ref:`voga`
- :ref:`welfare`
- :ref:`avanti`
- :ref:`presto`
- :ref:`extjs6`.
- :ref:`algus`.



  

  
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


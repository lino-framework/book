.. _dev.overview:

================================
Components of the Lino framework
================================


Packages
========

- Lino : the core framework + the standard plugin library
  (mod:`lino.modlib`) : users, notify, comments, changes, about, ...
  
- XL : the Extensions Library : contacts, countries, calendar,
  accounting, groupware, ... (see :doc:`xl`)
       
- The :mod:`lino_book` repository
  contains the docs and a test suite for the Lino framework.
  The book itself is not published as PyPI package.
  
- Lino applications covered by the Lino Book:
  
    - :mod:`lino_noi` : :ref:`noi`. The application we use for managing our
      collaboration. It's about tickets, projects, time tracking, votes.
    - :mod:`lino_cosi` : :ref:`cosi`, a simple accounting application.
    - :mod:`lino_avanti` : Belgian integration parcours
    - :mod:`lino_tera` : therapies, invoicing, accounting
    - :mod:`lino_care` : Shared contacts and skills management for people who care
    - :mod:`lino_vilma` : Shared Contact management for local communities
    - :ref:`voga` : courses, invoicing, accounting
    - :ref:`amici` : contacts, groups, personal information manager
      
- Independent Lino applications:

    - :ref:`welfare` : used by Belgian social centres
  
- The :ref:`extjs6` project.

- :mod:`atelier` : a collection of utilities maintained by the Lino
  team and which might be useful to other (non-Lino) Python
  projects. :mod:`projects <atelier.projects>`, :mod:`invlib
  <atelier.invlib>`, :mod:`rstgen <atelier.rstgen>`
  
- :mod:`commondata` : an experimental project for storing common data
  as Python code.
  
- `algus <https://github.com/lino-framework/algus>`_
  is a template for new Lino applications


  

  
Package dependencies
====================

.. graphviz::

   digraph foo {

    /**
    {
       node [shape=plaintext, fontsize=16];
       documentation ->
       "independent applications" ->
       applications -> framework -> utilities;
    }
   
    { rank = same;
        applications;
        lino_noi;
        lino_cosi;
        lino_tera;
        lino_care;
        lino_avanti;
    }
    
    { rank = same;
        utilities;
        atelier;
        commondata;
    }

    { rank = same;
        documentation;
        lino_book;
    }

    { rank = same;
        "independent applications";
        lino_voga;
        lino_welfare;
    }
    **/

    /**

    { rank = same;
        framework;
        lino;
        lino_xl;
    }

    **/

    commondata -> atelier;
    lino -> atelier;
    lino_xl -> lino;
    lino_noi -> lino_xl; 
    lino_cosi -> lino_xl; 
    lino_tera -> lino_xl;
    lino_care -> lino_xl;
    lino_avanti -> lino_xl;
    
    lino_book -> lino_noi; 
    lino_book -> lino_cosi; 
    lino_book -> lino_tera; 
    lino_book -> lino_care; 
    lino_book -> lino_avanti; 
    lino_book -> commondata;
    
    lino_voga -> lino_cosi;
    lino_welfare -> lino_cosi;
   }


.. _dev.overview:

================================
Components of the Lino framework
================================


Python packages covered by the Lino Book
========================================

- The core of the framework is in a package called :mod:`lino` which
  includes the standard plugin library (:mod:`lino.modlib`) for adding
  basic features like system users, a notification framework,
  comments, printing, ...
  
- :mod:`lino_xl` is an "extended" plugin collection used by many Lino
  applications: contacts, countries, calendar, accounting, groupware,
  etc. \ .  See :doc:`xl`.
       
- The :mod:`lino_book` package contains the source code of what you
  are reading right now, a collection of demo projects and examples
  (:mod:`lino_book.projects`), and the big test suite for the whole
  Lino framework.  The book package is not published on PyPI because
  that would make no sense.  You use it by cloning the repository from
  GitHub.
  
- Lino applications covered by the Lino Book:
  
    - :mod:`lino_noi` (:ref:`noi`) : the application we use for
      managing our collaboration.  It's about tickets, projects, time
      tracking, votes.
    - :mod:`lino_amici` (:ref:`amici`) : contacts, groups, personal
      information manager
    - :mod:`lino_cosi` (:ref:`cosi`) : a simple accounting application.
      
    - :mod:`lino_tera` (:ref:`tera`) : therapies, invoicing, accounting
    - :mod:`lino_care` (:ref:`care`) : Shared contacts and skills management for people who care
    - :mod:`lino_vilma` (:ref:`vilma`) : Shared Contact management for local communities
    - :mod:`lino_voga` (:ref:`voga`) : courses, invoicing, accounting
    - :mod:`lino_avanti` (:ref:`avanti`) : Belgian integration
      parcours
    - :mod:`lino_welfare` (:ref:`welfare`) :
      A big application used by Belgian social centres.

One day you might want to consult the generated :doc:`API
</api/index>` of these packages.


Python packages maintained by the same team
===========================================

Some projects which might be useful to non-Lino Python projects are
not covered in the Lino Book because they are actually not at all
related to Lino, except that Lino depends on them and that they are
maintained by the Lino team:

- :mod:`atelier` is a collection of utilities (subpackages
  :mod:`projects <atelier.projects>`, :mod:`invlib <atelier.invlib>` and
  :mod:`rstgen <atelier.rstgen>`)

- :mod:`etgen` uses ElementTree for generating HTML or XML.

- :mod:`commondata` is an experimental project for storing and
  managing common data as Python code without any user interface.

  
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

    lino -> atelier;
    lino_xl -> lino;
    lino_noi -> lino_xl; 
    lino_cosi -> lino_xl; 
    lino_tera -> lino_xl;
    lino_care -> lino_xl;
    lino_avanti -> lino_xl;
    lino_voga -> lino_xl;
    lino_welfare -> lino_xl;
    
    lino_book -> lino_noi; 
    lino_book -> lino_cosi; 
    lino_book -> lino_voga; 
    lino_book -> lino_tera; 
    lino_book -> lino_care; 
    lino_book -> lino_avanti; 

    /**
    
    commondata -> atelier;
    lino_book -> commondata;
    
    lino_voga -> lino_cosi;
    lino_welfare -> lino_cosi;
    **/
   }


   
Related projects
================

There are also Lino applications that are *not* covered by the book.


.. _presto:

Lino Presto
------------

An application for managing services with physical on-site presence of
the workers.  For organisations where calendar entries are the base
for writing invoices.

.. _patrols:

Lino Patrols
------------

A project that fell asleep before going to production.

http://patrols.lino-framework.org/


.. _logos:

Lino Logos
----------

A project that fell asleep before going to production.

http://logos.lino-framework.org/


.. _sunto:

Lino Sunto
----------

Lino Sunto is the first free (GPL) Lino application developed by
somebody else than the author. It is hosted at    
https://github.com/ManuelWeidmann/lino-sunto




.. _psico:

Lino Psico
----------

This project is now named :ref:`tera`.

  

.. _extjs6:

ExtJS 6
-------

See https://github.com/lino-framework/extjs6
      
  

.. _algus:

Algus
-----
  
The `algus <https://github.com/lino-framework/algus>`__ repository is
a template for new Lino applications.



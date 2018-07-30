.. _dev.overview:

================================
Components of the Lino framework
================================


Python packages
===============

- :mod:`lino` is the **core framework** which comes with a standard
  plugin library called :mod:`lino.modlib`: users, notification
  framework, comments, printing, ...
  
- :mod:`lino_xl` (:doc:`xl`) is a plugin collection used by many Lino
  applications: contacts, countries, calendar, accounting, groupware,
  ... .
       
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
      


- :mod:`atelier` is a collection of utilities maintained by the Lino
  team and which might be useful to other (non-Lino) Python
  projects. :mod:`projects <atelier.projects>`, :mod:`invlib
  <atelier.invlib>`, :mod:`rstgen <atelier.rstgen>`
  
  
  
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

There are also Lino applications which are *not* covered by the
book.


 - :ref:`welfare` : used by Belgian social centres

.. _patrols:

Lino Patrols
------------

http://patrols.lino-framework.org/


.. _logos:

Lino Logos
----------

http://logos.lino-framework.org/


Lino Polly
----------

See :doc:`/examples/polly/index`


Lino Belref
-----------

See :doc:`/examples/belref/index`


.. _sunto:

Lino Sunto
----------

Lino Sunto is the first free (GPL) Lino application developed by
somebody else than the author. It is hosted at    
https://github.com/ManuelWeidmann/lino-sunto


.. _presto:

Lino Presto
------------

Lino Presto was meant to become an application for managing the work
of organisations where time tracker sessions are the base for writing
invoices. The project was deprecated in favour to :ref:`noi` and
:ref:`cosi`.


.. _psico:

Lino Psico
----------

This project is now named :ref:`tera`.

  

.. _extjs6:

ExtJS 6
-------

See https://github.com/lino-framework/extjs6
      
  

.. _commondata:

commondata
----------


:mod:`commondata` is an experimental project for storing common data
as Python code.

.. _algus:

Algus
-----
  
The `algus <https://github.com/lino-framework/algus>`__ repository is
a template for new Lino applications.



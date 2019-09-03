.. _dev.overview:

================================
Components of the Lino framework
================================

General framework repositories
==============================

- The core of the framework is in a package called :mod:`lino` which
  includes the :doc:`/specs/modlib`.

- The :mod:`lino_xl` package contains the :doc:`xl`.

- The :mod:`getlino` package contains the Lino installer. See :ref:`getlino`.

- The :mod:`lino_book` package contains the source code of what you
  are reading right now, a collection of demo projects and examples
  (:mod:`lino_book.projects`), and the big test suite for the whole
  Lino framework.


Lino applications
=================

Here is a directory of all known :term:`Lino applications <Lino application>`.

Some Lino applications have the privilege of having their technical
documentation in the :ref:`Lino Book <book>`.

- :mod:`lino_noi` (:ref:`noi`) : the application we use for
  managing our collaboration.  It's about tickets, projects and working time.
- :mod:`lino_cosi` (:ref:`cosi`) : a simple accounting application.
- :mod:`lino_voga` (:ref:`voga`) : courses, invoicing, accounting
- :mod:`lino_tera` (:ref:`tera`) : therapies, invoicing, accounting
- :mod:`lino_avanti` (:ref:`avanti`) : Belgian integration parcours
- :mod:`lino_care` (:ref:`care`) : Shared contacts and skills management for people who care
- :mod:`lino_vilma` (:ref:`vilma`) : Shared Contact management for local communities

Some other Lino applications have their own technical documentation, demo projects
and technical specs:

- `Lino Amici <http://amici.lino-framework.org>`_
- `Lino Presto <http://presto.lino-framework.org>`_
- `Lino Pronto <http://pronto.lino-framework.org>`_
- `Lino Welfare <http://welfare.lino-framework.org>`_ currently has two
  variants named `Chatelet <http://welcht.lino-framework.org>`_
  `Eupen <http://weleup.lino-framework.org>`_.
- `Lino Patrols <http://patrols.lino-framework.org/>`_ (fell asleep before going to production)
- `Lino Logos <http://logos.lino-framework.org/>`_ (fell asleep before going to production)
- `Lino Sunto <https://github.com/ManuelWeidmann/lino-sunto>`_ is the first Lino
  application developed by somebody else than the author.


Utilities maintained by the :ref:`lsf`
======================================

Some projects which might be useful to non-Lino Python projects are
not covered in the Lino Book because they are actually not at all
related to Lino, except that Lino depends on them and that they are
maintained by the Lino team:

- :mod:`atelier` is a collection of utilities (subpackages
  :mod:`projects <atelier.projects>`, :mod:`invlib <atelier.invlib>` and
  :mod:`rstgen <atelier.rstgen>`)

- :mod:`etgen` uses ElementTree for generating HTML or XML.

- :mod:`commondata` is an experimental project for storing and
  managing common data as Python code without any front end.


Alternative front ends
======================

.. _react:

React front end
---------------

See https://github.com/lino-framework/react

.. _extjs6:

ExtJS 6 front end
-----------------

See https://github.com/lino-framework/extjs6

Note that this front end is discontinued in favour of the more feature-complete
:ref:`react` front end.


Overview diagram
================

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
        lino_weleup;
        lino_welcht;
    }
    **/

    /**

    { rank = same;
        framework;
        lino;
        lino_xl;
    }

    **/

    { rank = same;
        # applications;
        noi;
        cosi;
        tera;
        avanti;
        voga;
        logos
        weleup;
        welcht;
        amici;
    }

    lino -> atelier;
    xl -> lino;
    logos -> lino;
    noi -> xl;
    cosi -> xl;
    tera -> xl;
    avanti -> xl;
    voga -> xl;
    amici -> xl;
    weleup -> welfare;
    welcht -> welfare;

    book -> noi;
    book -> cosi;
    book -> voga;
    book -> tera;
    book -> avanti;
    # book -> weleup;
    # book -> welcht;

    welfare -> xl;

   }

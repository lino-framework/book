.. _dev.overview:

================================
Components of the Lino framework
================================


General framework repositories
==============================

- The core of the framework is in a package called :mod:`lino` which
  includes the standard plugin library (:mod:`lino.modlib`) for adding
  basic features like system users, a notification framework,
  comments, printing, ...

- :mod:`lino_xl` is an "extended" :term:`plugin library` used by many Lino
  applications.  See :doc:`xl`.

- The :mod:`lino_book` package contains the source code of what you
  are reading right now, a collection of demo projects and examples
  (:mod:`lino_book.projects`), and the big test suite for the whole
  Lino framework.  The book package is not published on PyPI because
  that would make no sense.  You use it by cloning the repository from
  GitHub (which is done automatically by :ref:`getlino`).


Lino applications
=================

Some Lino applications have the privilege of being documented within the
:ref:`Lino Book <book>`.

- :mod:`lino_noi` (:ref:`noi`) : the application we use for
  managing our collaboration.  It's about tickets, projects and working time.
- :mod:`lino_cosi` (:ref:`cosi`) : a simple accounting application.
- :mod:`lino_voga` (:ref:`voga`) : courses, invoicing, accounting
- :mod:`lino_tera` (:ref:`tera`) : therapies, invoicing, accounting
- :mod:`lino_avanti` (:ref:`avanti`) : Belgian integration parcours
- :mod:`lino_care` (:ref:`care`) : Shared contacts and skills management for people who care
- :mod:`lino_vilma` (:ref:`vilma`) : Shared Contact management for local communities

Other Lino applications are more independent in that they have their own
documentation tree, demo projects and technical specs:

- `Lino Welfare <http://welfare.lino-framework.org>`_
- `Lino Welfare Chatelet <http://welcht.lino-framework.org>`_
- `Lino Welfare Eupen <http://weleup.lino-framework.org>`_
- `Lino Amici <http://amici.lino-framework.org>`_
- `Lino Presto <http://presto.lino-framework.org>`_
- `Lino Pronto <http://pronto.lino-framework.org>`_
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


Miscellaneous
=============

.. _algus:

Algus
-----

The `algus <https://github.com/lino-framework/algus>`__ repository is a template
for new Lino applications.  The algus project is not really maintained and now
partly replaced by :ref:`getlino`.


Historic names
==============

.. _manuals:

manuals
-------

Obsolete. The `manuals <https://github.com/lino-framework/manuals>`__
repository no longer exists.


.. _psico:

Lino Psico
----------

Old name of :ref:`tera`.

.. _sunto:

Lino Sunto
----------

Lino Sunto is the first free (GPL) Lino application developed by
somebody else than the author. It is hosted at
https://github.com/ManuelWeidmann/lino-sunto


.. _welfare:

Lino Welfare
------------

See http://welfare.lino-framework.org

.. _presto:

Lino Presto
------------

See http://presto.lino-framework.org

.. _pronto:

Lino Pronto
------------

See http://pronto.lino-framework.org

.. _patrols:

Lino Patrols
------------

Some parts of the book refer to this for historical reasons.
See http://patrols.lino-framework.org

.. _logos:

Lino Logos
----------

Some parts of the book refer to this for historical reasons.
See http://logos.lino-framework.org


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
        weleup;
        welcht;
        amici;
    }

    lino -> atelier;
    xl -> lino;
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

.. _dev.overview:

================================
Components of the Lino framework
================================

The Lino framework consists of about 30 repositories, which are currently hosted
on GitHub under https://github.com/lino-framework.

General framework repositories
==============================

- The :mod:`lino` package contains the core of the framework and includes the
  :doc:`/specs/modlib`, a :term:`plugin library` with basic features like system
  users, notifications, comments, printing and others. These features are
  included in most real-world :term:`Lino applications <Lino application>`.

- The :mod:`lino_xl` package contains the :ref:`xl`,
  a collection of plugins used by many :term:`Lino applications <Lino application>`.

- The :mod:`getlino` package contains the Lino installer.

- The :mod:`lino_book` package contains the source code of what you are reading
  right now, *plus* a collection of **demo projects and examples**
  (see :mod:`lino_book.projects`), *plus* the big test suite for the Lino
  framework.


Lino applications
=================

Here is a directory of all known :term:`Lino applications <Lino application>`.

Some applications have the privilege of having their technical documentation
here in the :ref:`Lino Book <book>`.  This is because explaining a framework is
difficult without examples, and because we thought that applications that are
actually being used in reality are more interesting than a theoretic collection
of demo projects.

- :ref:`noi` (:mod:`lino_noi`) is the application we use for
  managing our collaboration.  It's about tickets, projects and working time.
- :ref:`cosi` (:mod:`lino_cosi`) a simple accounting application.
- :ref:`voga` (:mod:`lino_voga`) is about organizing courses, registering participants, invoicing, accounting
- :ref:`tera` (:mod:`lino_tera`) is about therapies, invoicing, accounting
- :ref:`avanti` (:mod:`lino_avanti`) is used Belgian to manage immigrants with their integration parcours
- :ref:`care` (:mod:`lino_care`) : Shared contacts and skills management for people who care
- :ref:`vilma` (:mod:`lino_vilma`) : Shared contact management for local communities

Newer Lino applications have their own technical documentation, demo projects
and technical specs:

- `Lino Amici <http://amici.lino-framework.org>`_ is a contacts manager for families.

- `Lino Ciao <http://ciao.lino-framework.org>`_ is a meetings manager.

- `Lino Presto <http://presto.lino-framework.org>`_ is an application developed
  for a service provider in Eupen. Group calendar, team management, monthly
  invoicings. No accounting.

- `Lino Pronto <http://pronto.lino-framework.org>`_ is an application developed
  for a provider with delivery notes and with accounting. Not yet uses in production.

- `Lino Welfare <http://welfare.lino-framework.org>`_ is a :term:`plugin library`
  for Belgian Public Social Welfare Centres, currently used by two applications
  `Chatelet <http://welcht.lino-framework.org>`_ and
  `Eupen <http://weleup.lino-framework.org>`_.

- Some applications fell asleep before going to production: `Lino Patrols
  <http://patrols.lino-framework.org/>`_,  `Lino Logos
  <http://logos.lino-framework.org/>`_ and `Lino Sunto
  <https://github.com/ManuelWeidmann/lino-sunto>`_ (the latter was the first
  Lino application developed by somebody else than the author).


Utilities maintained by the Lino team
======================================

Some packages that might be useful to non-Lino Python projects are not covered
in the Lino Book because they are actually not at all related to Lino, except
that Lino depends on them and that they are maintained by the Lino team:

- :mod:`rstgen` is a library to generate reSTructuredText snippets

- :mod:`atelier` is a collection of utilities (subpackages
  :mod:`projects <atelier.projects>`, and :mod:`invlib <atelier.invlib>`)

- :mod:`etgen` uses ElementTree for generating HTML or XML.

- :mod:`commondata` is an experimental project for storing and
  maintaining common data as Python code without any front end.


.. _getlino:

getlino
-------

The :ref:`getlino` package is the Lino installer, a small Python script that
installs Lino in different contexts.

See https://getlino.lino-framework.org



Alternative front ends
======================

.. _react:

React front end
---------------

See https://github.com/lino-framework/react

.. _extjs6:

ExtJS 6 front end
-----------------

A currently deprecated proof of concept for a Lino :term:`front end` that uses
Sencha's ExtJS 6 Javascript toolkit.

See https://github.com/lino-framework/extjs6

.. _openui5:

OpenUI5 front end
-----------------

A currently deprecated proof of concept for a Lino :term:`front end` that
uses SAP's OpenUI toolkit.

See https://github.com/lino-framework/openui5



.. _dev.overview.diagram:

Overview diagram
================

.. graphviz::

   digraph foo {

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
        ciao;
    }

    lino -> atelier;
    xl -> lino;
    noi -> xl;
    cosi -> xl;
    tera -> xl;
    avanti -> xl;
    voga -> xl;
    amici -> xl;
    ciao -> xl;
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

    getlino -> book;
    getlino -> amici;
    getlino -> ciao;
    getlino -> weleup;
    getlino -> welcht;

   }

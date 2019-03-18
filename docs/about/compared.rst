=================================
Lino compared to other frameworks
=================================

The following projects do something similar to Lino.  If you have used or
otherwise know one of them, please write a few sentences about what's
different.

.. contents::
  :local:


.. _tryton:

Odoo / Tryton
=============

Lino can be compared to `Tryton <http://www.tryton.org/>`__ and `Odoo
<https://en.wikipedia.org/wiki/Odoo>`__ (formerly known as OpenERP).

First of all, Odoo is rather a highly configurable and modularized ERP
*application* while Lino is a *framework* for creating such
applications.  Which means that the business target for the two
frameworks are not the same.

Several technical differences could be mentioned:

- Odoo requires Postgresql as a DBMS while Lino could be used with any
  DBMS supported by Django.
  
- Odoo addons or Odoo applications (equivalents of plugins in Lino)
  must be written in the Odoo logic while Lino applications can use
  any Django packages. Which means that Lino is backed by a bigger
  community.
  
- Odoo until now has not yet started to support Python 3 and has no
  clear plan to do so.

- Starting at the v9.0 release, Odoo was split into a proprietary
  enterprise edition with cloud-hosted SaaS and a cut-down community
  edition.


restdb.io
=========

With `restdb.io <https://restdb.io>`__, a company based in Bergen
(Norway), you have "collections" (which correspond to Django's models)
and "pages" (which correspond to Django's views).  With restdb you can
switch to "developer mode" and edit your database structure. There is
a basic user interface for entering data into these collections. And
you have an API for accessing the data from other applications. A nice
tool, certainly useful for certain kinds of applications.

Lino has more complex UI concepts (tables, form layouts, menus,
actions, virtual fields, slave tables, ...).  restdb.io is not meant
for writing e.g. a accounting or calender application.

Lino has no "visual GUI editor".  In Lino you define all these things using
Python code, not via a web interface.


Apache Isis
===========

`Apache Isis <https://isis.apache.org>`__ is a DDD framework in Java.

An example application is `Estatio <http://www.estatio.org>`__
which was developed to fulfill the needs of a big real estate 
company in EU. It is Open source and its main
contributor appears to still be the company that created it. 


Appy framework
==============

- `Appy framework <http://appyframework.org/>`_

  


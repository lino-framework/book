.. doctest docs/specs/tera/invoicing.rst
.. _tera.specs.invoicing:

================================
How Lino Tera generates invoices
================================

In :ref:`tera` every meeting with a therapist is basically
invoiceable.  Unlike in e.g. in :ref:`voga` they are invoiced
afterwards, not in advance.

General functionality for automatically generating invoices is defined
in :mod:`lino_xl.lib.invoicing`.



.. contents:: 
   :local:
   :depth: 2

.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *


Overview
========

For individual and family therapies the *meetings* themselves
(:class:`Event <lino_tera.lib.cal.Event>`) are invoiceable while for
group therapies every individual *presence* (:class:`Guest
<lino_tera.lib.cal.Guest>`) of a meeting is invoiceable.

The **invoice generator** is either the therapy (for individual and
family therapies) or the enrolment (for group therapies).

>>> rt.models_by_base(rt.models.invoicing.InvoiceGenerator)
[<class 'lino_tera.lib.courses.models.Course'>, <class 'lino_tera.lib.courses.models.Enrolment'>]



Lino Tera uses this functionality by extending the models
:class:`Course <lino_xl.lib.courses.Course>` and
:class:`Enrolment <lino_xl.lib.courses.Enrolment>`
so that they inherit from
:class:`InvoiceGenerator <lino_xl.lib.invoicing.InvoiceGenerator>`.



>>> dd.plugins.ledger.start_year
2015


Therapies
=========

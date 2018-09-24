.. doctest docs/specs/tera/invoicing.rst
.. _tera.specs.invoicing:

================================
How Lino Tera generates invoices
================================

The basic invoiceable things in :ref:`tera` are the calendar entries.
Every meeting with a therapist is basically invoiceable.  Unlike in
e.g. in :ref:`voga` they are invoiced afterwards, not in advance.

General functionality for automatically generating invoices is defined
in :mod:`lino_xl.lib.invoicing`.


..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *


.. contents:: 
   :local:
   :depth: 2

Overview
========

For individual and family therapies the *meetings* themselves
(:class:`Event <lino_tera.lib.cal.Event>`) are invoiceable while for
group therapies every individual *presence* (:class:`Guest
<lino_tera.lib.cal.Guest>`) of a meeting is invoiceable.

Lino Tera uses this functionality by extending the models
:class:`cal.Event <lino_xl.lib.cal.Event>` and
:class:`cal.Guest <lino_xl.lib.cal.Guest>`
so that they inherit from
:class:`Invoiceable <lino_xl.lib.invoicing.Invoiceable>`.

>>> rt.models_by_base(rt.models.invoicing.Invoiceable)
[<class 'lino_tera.lib.cal.models.Event'>, <class 'lino_tera.lib.cal.models.Guest'>]


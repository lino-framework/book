.. doctest docs/specs/healthcare.rst
.. _specs.lib.healthcare:

============================================
``healthcare`` : Manage healthcare providers
============================================

.. currentmodule:: lino_xl.lib.healthcare

The :mod:`lino_xl.lib.healthcare` plugin adds functionality for managing health
care situations of your clients.

You specify for each of your clients which tariff and plan they have regarding
health care. Optionally you can have a history of these per client.

You may use this to issue cost-sharing invoices to your clients' health care
providers.

This document uses demo configuration for the context in Belgium.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *


Usage
=====

As the application developer you choose one of the following usages:

- users want to record only the
  current situation of a client. In that case you have your application's client
  model inherit from :class:`HealthcareSubject`.

- users want to record a history of situations per client.
  In that case you add :class:`SituationsByClient`  to the detail layout of your client model and make
  sure to set :attr:`Plugin.client_model`.

Healthcare plans
================

A **healthcare plan** is a method that can be chosen by private persons for
their health insurance.  Depending on national laws the provider can be either
a public institution or a private company.

There is usually a finite number of healthcare plans, usually each plan has a
reference.

>>> rt.show(healthcare.Plans)
=========== =============================================== ========
 Reference   Provider                                        Remark
----------- ----------------------------------------------- --------
 Christian   Alliance nationale des mutualités chrétiennes
 Neutral     Union nationale des mutualités neutres
 Socialist   Union nationale des mutualités socialistes
 Liberal     Union nationale des Mutualités Libérales
 Libre       Union nationale des mutualités libres
=========== =============================================== ========
<BLANKLINE>


.. class:: Plan

    .. attribute:: ref

        An identifying name understood by every user of the site.

    .. attribute:: provider

        The provider who will potentially be invoiced for shared costs.

        A pointer to :class:`lino_xl.lib.contacts.Company`


Tariffs
=======

The **healthcare tariff** of a physical person expresses their status regarding
health care conditions. It is assigned by law, not by a given provider.

>>> rt.show(healthcare.Tariffs)
======= ======== ========
 value   name     text
------- -------- --------
 10      normal   Normal
 20      bim      BIM
 30      omnio    OMNIO
======= ======== ========
<BLANKLINE>

.. class:: Tariffs

    The choicelist with healthcare tariffs available in this application.


Rules
=====

.. class:: Rule

    .. attribute:: healthcare_tariff
    .. attribute:: healthcare_plan

    .. attribute:: client_fee

        The product for which this rule applies.

        This is the client's share of the costs invoiced to the client.

    .. attribute:: provider_fee

        The provider's share of the costs which you will invoice to the
        provider.

    Note that this part is not yet used on the field.  The client_fee might be
    useless, we must maybe rather inject a checkbox field "healthcare_shared"
    to :class:`Product`.


The ``HealthcareSubject`` model mixin
=====================================

.. class:: HealthcareSubject

    Model mixin which adds database fields about a given healthcare subject.

    .. attribute:: healthcare_plan

        The health care provider.

    .. attribute:: healthcare_tariff

        The health care tariff.


Situations history
===================

.. class:: Situation

    .. attribute:: client

    .. attribute:: healthcare_tariff
    .. attribute:: healthcare_plan

    .. attribute:: start_date
    .. attribute:: end_date

.. class:: SituationsByClient



Plugin config
=============

- :attr:`Plugin.client_model`

- :attr:`lino.core.plugin.Plugin.menu_group`


Weblinks
========

https://www.diabetes-online.de/a/krankenkasse-oder-krankenversicherung-grosser-unterschied-1785479
https://www.french-connect.com/147-sante-en-belgique-qu-est-ce-qu-une-intervention-majoree-et-un-statut-omnio.html
http://socialsante.wallonie.be/surendettement/citoyen/?q=node/434


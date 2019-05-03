.. doctest docs/specs/healthcare.rst
.. _specs.lib.healthcare:

============================================
``healthcare`` : Manage healthcare providers
============================================

.. currentmodule:: lino_xl.lib.healthcare

The :mod:`lino_xl.lib.healthcare` plugin adds functionality for managing health
care situations of your clients.

You specify for each of your clients which tariff and provider they have
regarding health care. Optionally you can have a history of these per client.

You may use this to issue cost-sharing invoices to your clients' health care
providers.

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

Tariffs
=======

The **healthcare tariff** of a physical person expresses their status
regarding health care conditions.

It is assigned by law, not by a given provider.

.. class:: Tariffs

    The choicelist with healthcare tariffs available in this application.

    The default implementation uses the context in Belgium (found `here
    <https://www.french-connect.com/147-sante-en-belgique-qu-est-ce-qu-une-intervention-majoree-et-un-statut-omnio.html>`__
    and `here
    <http://socialsante.wallonie.be/surendettement/citoyen/?q=node/434>`__).

    >>> rt.show(healthcare.Tariffs)
    ======= ======== ========
     value   name     text
    ------- -------- --------
     10      normal   Normal
     20      bim      BIM
     30      omnio    OMNIO
    ======= ======== ========
    <BLANKLINE>

.. class:: HealthcareSubject

    Model mixin which adds database fields about a given healthcare subject.

    .. attribute:: healthcare_provider

        The health care provider.

    .. attribute:: healthcare_tariff


.. class:: Rule

    .. attribute:: healthcare_tariff
    .. attribute:: healthcare_provider

    .. attribute:: client_fee

        The product for which this rule applies.

        This is the client's share of the costs invoiced to the client.

    .. attribute:: provider_fee

        The provider's share of the costs which you will invoice to the
        provider.

    Note that this part is not yet used on the field.  The client_fee might be
    useless, we must maybe rather inject a checkbox field "healthcare_shared"
    to :class:`Product`.


Situations history
===================

.. class:: Situation

    .. attribute:: client

    .. attribute:: healthcare_tariff
    .. attribute:: healthcare_provider

    .. attribute:: start_date
    .. attribute:: end_date

.. class:: SituationsByClient



Plugin config
=============

- :attr:`Plugin.client_model`

- :attr:`lino.core.plugin.Plugin.menu_group`

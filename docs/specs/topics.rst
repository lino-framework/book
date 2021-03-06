.. doctest docs/specs/topics.rst
.. _specs.topics:

=========================================
``topics`` : topics and partner interests
=========================================

.. currentmodule:: lino_xl.lib.topics

The :mod:`lino_xl.lib.topics` plugin adds the notions of "topics" and
"interests" of a "partner" in a topic.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q


Overview
========

A **topic** is something a partner can be interested in.  An
**interest** is the fact that a given partner is interested in a given
topic.

Users can see a panel "Interests" (:class:`InterestsByPartner`) in the
detail window of a partner.

They can add a row in that panel to specify that this partner is interested in a
topic.  They can open the panel in a window to delete interests.

A site administrator can configure the list of available topics.

>>> show_menu_path(topics.AllTopics)
Configure --> Topics --> Topics

The detail window of a topic has a panel "Interests"
(:class:`InterestsByTopic`) which shows the partners for which this
topic is interesting.

A site administrator can see a global list of all interests.
This might be useful e.g. for exporting the data.

>>> show_menu_path(topics.AllInterests)
Explorer --> Topics --> Interests


Partner
=======

The :term:`application developer` can decide what a "partner" means for the
topics plugin by setting the :attr:`Plugin.partner_model`.

For example in :ref:`tera` the "partner" who can be interested in a
topic is not Partner but Course.

>>> print(dd.plugins.topics.partner_model)
courses.Course


Database models
===============

.. class:: Topic

    Django model representing a *topic*.

    .. attribute:: ref

        The reference.

        See :attr:`lino.mixins.ref.StructuredReferrable.ref`

    .. attribute:: name

        The designation in different languages.

    .. attribute:: description_text

        Rich text field for a longer multi-line description.

    .. attribute:: description

        Virtual field which includes the formatted structured reference and the
        :attr:`description_text`.

        See :attr:`lino.mixins.ref.StructuredReferrable.description`

    .. attribute:: topic_group

        Deprecated. Don't use.


.. class:: Topics
.. class:: AllTopics
.. class:: TopicsByGroup


.. class:: Interest

    Django model representing an *interest*.

    .. attribute:: owner
    .. attribute:: topic
    .. attribute:: remark

.. class:: Interests
.. class:: InterestsByTopic


.. class:: TopicGroup

    This model is deprecated.  We use the Topic.ref for structuring
    topics.


.. class:: TopicGroups

    Currently not used.


Don't read me
=============


Because :class:`Topic` defines a database field :attr:`Topic.description` the
virtual field :attr:`lino.core.model.Model.description` is hidden:

>>> sorted(rt.models.topics.Topic._meta.private_fields, key=lambda f: str(f))
[lino_xl.lib.topics.models.Topic.description, lino_xl.lib.topics.models.Topic.name_column, lino_xl.lib.topics.models.Topic.overview, lino_xl.lib.topics.models.Topic.workflow_buttons]

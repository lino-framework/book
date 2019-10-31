.. doctest docs/specs/trends.rst
.. include:: /../docs/shared/include/defs.rst
.. _specs.trends:

================================
``trends`` : Managing trends
================================

.. currentmodule:: lino_xl.lib.trends

The :mod:`lino_xl.lib.trends` plugin adds functionality for keeping track of
"trending events" in different "areas".


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.avanti1.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q

Usage
=====

When using this plugin, the application developer should set the
:attr:`Plugin.subject_model` and add :class:`EventsBySubject`
to the detail layout of this model.

Reference
=========


.. class:: TrendArea

    Represents a possible choice for the `trend_area` field of a
    :class:`TrendStage`.

.. class:: TrendStage

  .. attribute:: trend_area

      Pointer to the :class:`TrendArea`.

  .. attribute:: subject_column

      Whether this stage should cause subject column to be added .

      A subject column is a virtual column
      on the :attr:`Plugin.subject_model` that shows
      the date of the first event for a given trend stage and subject.


.. class:: TrendEvent

    .. attribute:: subject

        The subject we are talking about.

    .. attribute:: user

        The user who entered this data.

    .. attribute:: event_date

        The date when the subject reached the stage.

    .. attribute:: trend_area

        Pointer to the :class:`TrendArea`.

    .. attribute:: trend_stage

        Pointer to the :class:`TrendStage`.

    .. attribute:: remark

        A free text field.


.. class:: EventsBySubject

  Shows all trend events of that subject.


.. class:: TrendObservable

  Mixin that should be inherited by the :attr:`Plugin.subject_model` so that
  Lino automatically adds virtual columns for each trend stage having

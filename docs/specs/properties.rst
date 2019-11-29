.. doctest docs/specs/properties.rst
.. _specs.properties:

========================================
``properties`` : configurable properties
========================================

.. currentmodule:: lino_xl.lib.properties

The :mod:`lino_xl.lib.properties` plugin adds the notions of configurable
properties.  **It is probably deprecated.**  The idea was to have a very
customizable set of "properties" that can be used for "everything".  But life
shows that it is usually better to use combinations of customer-specific
choicelists and database models.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.max.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q


Overview
========

A :class:`PropOccurence` is when a given "property owner" has a given
:class:`Property`.  "Property owner" can be anything: a person, a
company, a product, an upload, it depends on the implementation of
:class:`PropOccurence`.  For example
:mod:`lino.projects.pcsw.models.PersonProperty`.

A :class:`Property` defines the configuration of a property.

Examples
========

>>> show_menu_path(properties.PropTypes)
Configure --> Properties --> Property Types

>>> rt.show('properties.PropTypes')
==== ================ ====================== ================== ================== ================== ===================== ================== ==================== =============== ================== ==================
 ID   Designation      Designation (de)       Designation (fr)   Designation (et)   Designation (nl)   Designation (pt-br)   Designation (es)   Choices List         default value   Limit to choices   Multiple choices
---- ---------------- ---------------------- ------------------ ------------------ ------------------ --------------------- ------------------ -------------------- --------------- ------------------ ------------------
 1    Present or not   Vorhanden oder nicht   Présent ou pas     Olemas või mitte   Ja of niet                                                                                       No                 No
 2    Rating           Bewertung              Appréciation(?)    Hinnang            Hoe goed                                                    properties.HowWell   2               No                 No
 3    Division         Abteilung              Division                                                                                                                               No                 No
==== ================ ====================== ================== ================== ================== ===================== ================== ==================== =============== ================== ==================
<BLANKLINE>

>>> rt.show('properties.PropGroups')
No data to display

>>> rt.show('properties.Properties')
No data to display


.. class:: PropType

  The type of the values that a property accepts.
  Each PropType may (or may not) imply a list of choices.

  Examples: of property types:

  - Knowledge (Choices: "merely", "acceptable", "good", "very good",...)
  - YesNo (no choices)

  .. attribute:: choicelist

  .. attribute:: default_value

    The default value to set when creating a :class:`PropertyOccurence`.
    This is currently used only in some fixture...


.. class:: PropChoice

    A Choice for a given PropType.  `text` is the text to be displayed
    in combo boxes.

    `value` is the value to be stored in :attr:`PropValue.value`, it
    must be unique for all PropChoices of a given PropType.

    Choices for a given PropType will be sorted on `value` (we might
    make this more customizable if necessary by adding a new field
    `sort_text` and/or an option to sort on text instead of value)

    When configuring your property choices, be aware of the fact that
    existing property occurences will *not* change when you change the
    `value` of a property choice.

.. class:: PropGroup

    A Property Group defines a list of Properties that fit together
    under a common name.  Examples of Property Groups: Skills, Soft
    Skills, Obstacles There will be one menu entry per Group.

.. class:: Property

  Represents a property.

.. class:: PropertyOccurence


    A Property Occurence is when a Property occurs, possibly having a
    certain value.

    Abstract base class for
    | :class:`lino_welfare.modlib.cv.models.PersonProperty`,
    | :class:`lino_welfare.modlib.cv.models.WantedProperty`,
    | :class:`lino_welfare.modlib.cv.models.AvoidedProperty`,
    | ...


.. class:: HowWell

    A list of possible answers to questions of type "How well ...?":
    "not at all", "a bit", "moderate", "quite well" and "very well"

.. class:: DoYouLike

    A list of possible answers to questions of type "How much do you like ...?".

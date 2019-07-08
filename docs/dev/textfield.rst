.. doctest docs/dev/textfield.rst
.. _dev.textfield:

===========
Text fields
===========


.. currentmodule:: lino.core.fields


Overview
========

A **text field** is a charfield which can contain more than one line of text.
Unlike a charfield it has a flexible height in layouts.

A **plain text field** is a text field without any formatting instructions.

A **rich text fields** can contain simple HTML formatting like character style,
links, tables, headers, enumerations, ... This content can be both *limited**
(see :doc:`/dev/bleach`) and **enhanced** (see :doc:`/specs/memo`).

Both types of text fields are specified using the :class:`RichTextField` class
exposed in :mod:`lino.api.dd`




.. class:: RichTextField

    A thin wrapper around Django's TextField `models.TextField` class, but you
    can specify two additional keyword arguments :attr:`textfield_format` and
    attr:``bleached`.

    You may also specify a keyword ``format`` when instantiating a
    :class:`RichTextField`, which will be stored to :attr:`textfield_format`.

    .. attribute:: textfield_format

        Override the global
        :attr:`lino.core.site.Site.textfield_format` setting.


    .. attribute:: bleached

        See :doc:`/dev/bleach`.




.. doctest docs/specs/excerpts.rst
.. _xl.specs.excerpts:

===============================
``excerpts``: Database excerpts
===============================

.. currentmodule:: lino_xl.lib.excerpts

The :mod:`lino_xl.lib.excerpts` adds the notion of *database excerpts*.

Read also :doc:`printing`.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.max.settings.doctests')
>>> from lino.api.shell import *
>>> from lino.api.doctest import *

What is a database excerpt?
===========================


A **database excerpt** is a database object which represents the fact
that a given user has requested a printable document at a given
moment.  Lino keeps all these requests in a global database table
defined by the :class:`Excerpt` model.

Users can see a :attr:`printed` a history of
their database excerpts.

.. currentmodule:: lino_xl.lib.excerpts

Usage
=====
- add lino_xl.lib.excerpts to your
  :meth:`lino.core.Site.get_installed_apps`.
- Add the virtual field `printed`

Lino does not automatically add an action per model to make the
excerpt history visible from a model. If you want this, add yourself
your preferred variant.

This can be either using a :class:`ShowSlaveTable
<lino.core.actions.ShowSlaveTable>` button in the toolbar::

    show_excerpts = dd.ShowSlaveTable('excerpts.ExcerptsByOwner')
    show_excerpts = dd.ShowSlaveTable('excerpts.ExcerptsByProject')

Or by adding :class:`excerpts.ExcerptsByOwner <ExcerptsByOwner>` or
:class:`excerpts.ExcerptsByProject <ExcerptsByProject>` (or both, or
your own subclass of one of them) to the :attr:`detail_layout
<lino.core.actors.Actor.detail_layout>`.

In addition to the main template, excerpt types can specify a **body
template**.
Before rendering the main template, Lino
When the main template is being rendered, it has a context
variable ``body`` which

As a :class:`SiteAdmin <lino.core.roles.SiteAdmin>` user (and when
:mod:`lino.modlib.davlink` is installed) you can easily modify the
main template which has been used to print a given excerpt using the
:class:`Edit Template <lino.mixins.printable.EditTemplate>` button in
the detail window of that :class:`Excerpt` object.


If you want to configure *which* document to use as main template,
then you must use the `Configuration` menu:

- :menuselection:`Configuration --> Excerpt types`


Lino has a main template named :xfile:`excerpts/Default.odt` which is


Excerpts
========

A **database excerpt** is a database object which represents the fact
that a given user has requested a printable document at a given
moment.  Lino keeps all these requests in a global database table
defined by the :class:`Excerpt` model.

Users can see a history of these database excerpts using the following
menu commands:

- :menuselection:`Office --> My excerpts`
- :menuselection:`Explorer --> All excerpts`

.. class:: Excerpt

    A printable document that describes some aspect of the current
    situation.

    .. attribute:: excerpt_type

        The type of this excerpt (ForeignKey to :class:`ExcerptType`).

    .. attribute:: owner

      The object being printed by this excerpt.
      See :attr:`Controllable.owner
      <lino.modlib.gfks.mixins.Controllable.owner>`.

    .. attribute:: company

      The optional company of the :attr:`recipient` of this
      excerpt.  See :attr:`ContactRelated.company
      <lino_xl.lib.contacts.mixins.ContactRelated.company>`.

    .. attribute:: contact_person

      The optional contact person of the :attr:`recipient` of this
      excerpt.  See :attr:`ContactRelated.contact_person
      <lino_xl.lib.contacts.mixins.ContactRelated.contact_person>`.

    .. attribute:: recipient

      The recipient of this excerpt.  See
      :attr:`ContactRelated.recipient
      <lino_xl.lib.contacts.mixins.ContactRelated.recipient>`

    .. attribute:: language

      The language used for printing this excerpt.

    .. attribute:: date

    .. attribute:: time

    .. method:: get_address_html

        See
        :meth:`lino_xl.lib.contacts.mixins.ContactRelated.get_address_html`.

        Return the address of the :attr:`recipient` of this excerpt.



.. class:: ExcerptDetail

.. class:: Excerpts

    Base class for all tables on :class:`Excerpt`.

.. class:: AllExcerpts
.. class:: MyExcerpts

.. class:: ExcerptsByType
.. class:: ExcerptsByOwner

    Shows all excerpts whose :attr:`owner <Excerpt.owner>` field is
    this.

.. class:: ExcerptsByProject

    Only used if :attr:`lino.core.site.Site.project_model` is set.


Excerpt types
=============

Lino also has a table of **excerpt types** where the system
administrator can configure which types of database excerpts are
available on a site. You can see this list via

- :menuselection:`Configuration --> Excerpt types`

The detailed structure of this table is documented on the
:mod:`excerpts.ExcerptType <lino_xl.lib.excerpts.models.ExcerptType>`
model.

When a Lino process starts up, it automatically reads this table and
installs a "Print" action on every model of a site for which there
is an *excerpt type*.


.. class:: ExcerptType

    The type of an excerpt. Every excerpt has a mandatory field
    :attr:`Excerpt.excerpt_type` which points to an :class:`ExcerptType`
    instance.

    .. attribute:: name

        The designation of this excerpt type.
        One field for every :attr:`language <lino.core.site.Site.language>`.

    .. attribute:: content_type

        The database model for which this excerpt type is to be used.

    .. attribute:: build_method

        See :attr:`lino.modlib.printing.mixins.PrintableType.build_method`.

    .. attribute:: template

        The main template to be used when printing an excerpt of this type.

    .. attribute:: body_template

        The body template to use when printing an excerpt of this type.

    .. attribute:: email_template

        The template to use when sending this an excerpt of this type
        by email.

    .. attribute:: shortcut

        Optional pointer to a shortcut field.  If this is not empty, then
        the given shortcut field will manage excerpts of this type.

        See also :class:`Shortcuts`.
        See also :class:`lino_xl.lib.excerpts.choicelists.Shortcuts`.


.. class:: ExcerptTypes

    Displays all rows of :class:`ExcerptType`.


Model mixins
============

.. class:: Certifiable

    Any model which inherits from this mixin becomes "certifiable".

    That is:

      - it has a :attr:`printed_by` field and a corresponding virtual
        field :attr:`printed` which point to the excerpt that is the
        "definitive" ("Certifying") printout of this object.

      - It may define a list of "certifiable" fields by providing a
        :meth:`get_certifiable_fields` method.

    Usage example::

        from lino_xl.lib.excerpts.mixins import Certifiable

        class MyModel(dd.UserAuthored, Certifiable, dd.Duplicable):
            ...

    The :mod:`lino_xl.lib.excerpts.fixtures.std` fixture automatically
    creates a certifying :class:`ExcerptType` instance for every model
    which inherits from :class:`Certifiable`.


    .. attribute:: printed

      Displays information about when this certifiable has been printed.
      Clicking on it will display the excerpt pointed to by
      :attr:`printed_by`.

    .. attribute:: printed_by

      ForeignKey to the :class:`Excerpt` which certifies this instance.

      A :class:`Certifiable` is considered "certified" when this this is
      not `None`.

      Note that this field is a nullable ForeignKey with `on_delete
      <https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete>`__
      set to ``SET_NULL``.


    .. method:: on_duplicate(self, ar, master)

        After duplicating e.g. a budget which had been printed, we don't
        want the duplicate point to the same
        excerpt. :meth:`lino.mixins.duplicable.Duplicable.on_duplicate`.

    .. method:: get_certifiable_fields(cls)

        A class method. Expected to return a string with a
        space-separated list of field names.  These files will
        automaticaly become disabled (readonly) when the document is
        "certified". The default implementation returns an empty
        string, which means that no field will become disabled when
        the row is "certified".

        For example::

          @classmethod
          def get_certifiable_fields(cls):
              return 'date user title'

    .. method:: def get_excerpt_title(self)

        A string to be used in templates as the title of the
        certifying document.

    .. method:: get_excerpt_templates(self, bm)

        Return either `None` or a list of template names to be used
        when printing an excerpt controlled by this object.

.. class:: ExcerptTitle

    Mixin for models like
    :class:`lino_welfare.modlib.aids.models.AidType` and
    :class:`lino_xl.lib.courses.models.Line`.

    .. attribute:: name

        The designation of this row as seen by the user e.g. when
        selecting an instance of this model.

        One field for every :attr:`language <lino.core.site.Site.language>`.

    .. attribute:: excerpt_title

        The text to print as title in confirmations.
        One field for every :attr:`language <lino.core.site.Site.language>`.
        If this is empty, then :attr:`name` is used.


Shortcuts
=========

.. class:: Shortcut
.. class:: Shortcuts

    A choicelists of **excerpt shortcut fields**.  An excerpt shortcut
    field is a virtual display field with actions for quickly
    managing, from a given database object, the excerpt for this
    object of a given type.

    These virtual fields are being installed during pre_analyze by
    :func:`set_excerpts_actions`.





Templates
=========


.. xfile:: excerpts/Default.odt

This template is the default value, used by many excerpt types in
their :attr:`template <ExcerptType.template>` field.  It is designed
to be locally overridden by local site administrators in order to
match their letter paper.

Fields
======

.. class:: BodyTemplateContentField

Actions
=======

.. class:: CreateExcerpt

    Create an excerpt in order to print this data record.


.. class:: ClearPrinted

    Clear any previously generated printable document.  Mark this
    object as not printed. A subsequent call to print will generate a
    new cache file.


Signal handlers
===============

.. function:: set_excerpts_actions

    A receiver for the :data:`lino.core.signals.pre_analyze` signal.

    Installs (1) print management actions on models for which there is
    an excerpt type and (2) the excerpt shortcut fields defined in
    :class:`lino_xl.lib.excerpts.choicelists.Shortcuts`.

    Note that excerpt types for a model with has MTI children, the
    action will be installed on children as well.  For example a
    :class:`lino_avanti.lib.avanti.Client` in
    :mod:`lino_book.projects.adg` can get printed either as a
    :xfile:`TermsConditions.odt` or as a :xfile:`final
    report.body.html`.


.. function:: post_init_excerpt

    This is called for every new Excerpt object and it sets certain
    default values.

    For the default language, note that the :attr:`owner` overrides
    the :attr:`recipient`. This rule is important e.g. for printing
    aid confirmations in Lino Welfare.

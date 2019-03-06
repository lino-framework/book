.. doctest docs/specs/gfks.rst
.. _book.specs.gfks:

============================================
``gfks`` : Utilites for Generic Foreign Keys
============================================

.. currentmodule:: lino.modlib.gkfs

The :mod:`lino.modlib.gkfs` plugin adds some utilities for working with Generic
Foreign Keys. You should install it if your models contain GenericForeignKey
fields or inherit from the :class:`Controllable` mixin.


.. contents::
  :local:

.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *

Which means that code snippets in this document are tested using the
:mod:`lino_book.projects.min9` demo project.


The ``Controllable`` mixin
==========================

.. class:: Controllable

    Mixin for models that are "controllable" by another database object.

    Defines three fields :attr:`owned_type`, :attr:`owned_id` and
    :attr:`owned`. And a class attribute :attr:`owner_label`.

    For example in :mod:`lino.modlibs.cal`, the owner of a Task or Event
    is some other database object that caused the task's or event's
    creation.

    Or in :mod:`lino.modlib.sales` and :mod:`lino.modlib.purchases`,
    an invoice may cause one or several Tasks to be automatically generated
    when a certain payment mode is specified.

    Controllable objects are "governed" or "controlled" by their
    controller (stored in a field called :attr:`owner`): If the
    controller gets modified, it may decide to delete or modify some
    or all of her controlled objects.

    Non-automatic tasks always have an empty :attr:`owner` field.
    Some fields are read-only on an automatic Task because it makes no
    sense to modify them.

    .. attribute:: owner

    .. attribute:: owner_id
    .. attribute:: owner_type

    .. method:: update_controller_field(cls, verbose_name=None, **kwargs)

        Update attributes of the :attr:`owner` field and its underlying
        fields :attr:`owner_id` and :attr:`owner_type`.

        This can be used to make the controller optional (i.e. specify
        whether the :attr:`owner` field may be NULL). Example::

            class MyModel(Controllable):
                ....

            MyModel.update_controller_field(blank=False, null=False)

        When `verbose_name` is specified, all three fields will be
        updated, appending " (object)" and " (type)" to
        :attr:`owner_id` and :attr:`owner_type` respectively.

    .. method:: update_owned_instance(self, controllable)

        If this (acting as a controller) is itself controlled, forward the
        call to the controller.


    .. attribute:: owner_label

        Deprecated. This is (and always was) being ignored. Use
        :meth:`update_controller_field` instead.
        The labels (`verbose_name`) of the fields `owned_type`, `owned_id`
        and `owned` are derived from this attribute which may be overridden by
        subclasses.
    .. attribute:: controller_is_optional = True

        Deprecated. This is (and always was) being ignored. Use
        :meth:`update_controller_field` instead.


The ``ContentTypes`` table
==========================

The :class:`ContentTypes` table shows all models defined in your application.

>>> rt.show(gfks.ContentTypes) #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
==== ================== =========================
 ID   app label          python model class name
---- ------------------ -------------------------
 1    system             siteconfig
 2    contenttypes       contenttype
 3    gfks               helptext
 4    excerpts           excerpttype
 5    excerpts           excerpt
 6    countries          country
 7    countries          place
 ...
 45   notify             message
 46   changes            change
 ...
 49   uploads            volume
 50   uploads            uploadtype
 51   uploads            upload
 52   sessions           session
==== ================== =========================
<BLANKLINE>


.. class:: ContentTypes

    Lino installs this as the default table for
    :class:`django.contrib.ContentType`.


    .. attribute:: base_classes

        Display a clickable list of all MTI parents, i.e. base models

Customizable help texts
=======================

.. class:: HelpText

    A custom help text to be displayed for a given field.

Broken GFKs
===========

.. class:: BrokenGFKs

    Shows all database objects who have a broken GeneriForeignKey field.


Fields
======

.. class:: GenericForeignKey

    Add verbose_name and help_text to Django's GFK.

    Used by :class:`Controllable`.

.. class:: GenericForeignKeyIdField

    Use this instead of `models.PositiveIntegerField` for fields that
    are part of a :term:`GFK` and you want Lino to render them using a
    Combobox.

    Used by :class:`lino.modlib.gfks.mixins.Controllable`.

    Note: `type_field` is a mandatory argument, but you can specify
    anything because it is being ignored.


The :func:`gfk2lookup` function
===============================

The :func:`gfk2lookup <lino.core.gfks.gfk2lookup>` function is mostly
internal use, but occasionally you might want to use it.

>>> from lino.core.utils import full_model_name as fmn
>>> from lino.core.gfks import gfk2lookup
>>> from lino.modlib.gfks.mixins import Controllable

List of models which inherit from :class:`Controllable
<lino.modlib.gfks.mixins.Controllable>`:

>>> print(' '.join([fmn(m) for m in rt.models_by_base(Controllable)]))
cal.Event cal.Task checkdata.Problem comments.Comment excerpts.Excerpt notes.Note notify.Message uploads.Upload

>>> obj = contacts.Person.objects.all()[0]
>>> d = gfk2lookup(notes.Note.owner, obj)
>>> d['owner_type']
<ContentType: Person>
>>> d['owner_id']
201

{'owner_type': <ContentType: Person>, 'owner_id': 201}

If the object has a non-integer primary key, then it cannot be target
of a GFK.  In this case we filter only on the content type because
anyway the list will be empty.  `countries.Country` is actually the
only model with a non-integer primary key.

>>> obj = countries.Country.objects.all()[0]
>>> gfk2lookup(notes.Note.owner, obj)
{'owner_type': <ContentType: Country>}

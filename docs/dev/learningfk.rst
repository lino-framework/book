.. doctest docs/dev/learningfk.rst
.. _dev.learningfk:

=====================
Learning foreign keys
=====================

The :term:`application developer` can turn any foreign key field into a
:term:`learning foreign key`.

.. glossary::

  Learning foreign key

    A foreign key that can "learn", i.e. add new items to its list of
    choices.

.. contents::
   :depth: 1
   :local:

Usage
=====

- Define a chooser for the field by defining a :meth:`FOO_choices` method on the
  model and decorating it with :meth:`@dd.chooser <lino.core.choosers.chooser>`.

- Define an instance :meth:`create_FOO_choice
  <lino.core.model.Model.create_FOO_choice>` method on the model.


You can disable a :term:`learning foreign key` by setting the
:attr:`lino.core.model.Model.disable_create_choice` model attribute to `True`.


Examples
========

The :attr:`city <lino_xl.lib.countries.CountryCity.city>` field of a postal
address. When you specify the name of a city that does not yet exist, you simply
leave the "invalid" city name in the combobox (Lino accepts it) and save the
partner. Lino will then silently create a city of that name.  Note that you must
at least set the :attr:`country`, otherwise Lino refuses to automatically create
a city. This behaviour is defined in the  :class:`countries.CountryCity
<lino_xl.lib.countries.CountryCity>` model mixin, which is inherited e.g. by
:class:`contacts.Partner <lino_xl.lib.lib.contacts.Partner>`. or
:class:`addresses.Address <lino_xl.lib.lib.addresses.Address>`

Or the :attr:`lino_xl.lib.contacts.Role.person` field.  You can see the new
feature in every application with contacts.  For example
:mod:`lino_book.projects.min1`. In the detail of a company, you have the
:class:`RolesByCompany <lino_xl.lib.contacts.RolesByCompany>` slave table. In
the Person column of that table you can type the name of a person that does
not yet exist in the database.  Lino will create it silently, and you can then
click on the pointer to edit more information.
Some examples in :ref:`specs.contacts.learningfk`.

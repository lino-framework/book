.. doctest docs/dev/learningfk.rst
.. _dev.learningfk:

=====================
Learning foreign keys
=====================

The :term:`application developer` can turn any foreign key field into a
:term:`learning foreign key`.

.. glossary::

  learning foreign key

    A foreign key that can "learn", i.e. add new items to its list of
    choices.

  learning chooser

    The chooser associated to a :term:`learning foreign key`.

.. contents::
   :depth: 1
   :local:

Usage
=====

- Define a chooser for the field by defining a :meth:`FOO_choices` method on the
  model and decorating it with :meth:`@dd.chooser <lino.core.choosers.chooser>`.

- Define an instance method :meth:`create_FOO_choice
  <lino.core.model.Model.create_FOO_choice>` on the model.

  Example from :class:`lino_xl.lib.countries.CountryCity`::

    def create_city_choice(self, text):
        if self.country is not None:
            return rt.models.countries.Place.lookup_or_create(
                'name', text, country=self.country)

        raise ValidationError(
            "Cannot auto-create city %r if country is empty", text)

  Example from :class:`lino_xl.lib.contacts.Person`::

    def create_person_choice(self, text):
        return rt.models.contacts.Person.create_from_choice(text)

  When you use the :meth:`lino.core.model.Model.create_from_choice` method, you
  probably want to override the model's
  :attr:`lino.core.model.Model.choice_text_to_dict` method of the related model.


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


Implementation details
======================

When a method is decorated with the chooser decorator, Lino creates a
:class:`lino.utils.choosers.Chooser` instance. The  :attr:`can_create_choice
<lino.utils.choosers.Chooser.can_create_choice>` attribute of this instance will
automatically be set to `True` when the field's model also has a method named
:meth:`create_FOO_choice <lino.core.model.Model.create_FOO_choice>`
(`FOO` being the field name).

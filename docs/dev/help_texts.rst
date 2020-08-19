.. doctest docs/dev/help_texts.rst
.. _help_texts:

==========
Help Texts
==========

.. glossary::

  help text

    A short explanation to be displayed as tooltip when the user hovers over a
    form field, a menu item, or a toolbar button.

Help texts should be
(1) helpful to the :term:`end user`,
(2) translated and
(3) maintainable.  Lino provides several approaches for reaching these
goals.

.. contents::
   :local:
   :depth: 2


The primitive way
=================

Help texts can be defined and maintained by the  :term:`application developer`
by setting the :attr:`help_text` attribute of a
:attr:`field <django.db.models.Field.help_text>`,
:attr:`actor <lino.core.actors.Actor.help_text>`
or :attr:`action <lino.core.actions.Action.help_text>`.  As a developer you should wrap that
string into :func:`gettext` to have it translatable.  Fictive example::

    from lino.api import dd, _

    class MyModel(dd.Model):
        """MyModel is an important example."""

        universe = models.CharField(_("First field"),
            blank=True, max_length=100, help_text=_("""
    The first field contains an optional answer to the
    question about life, the universe and everything.
    """))

Having help texts maintained by the end users
=============================================

Help texts can be customized locally per site by the :term:`end users <end
user>` as :term:`customized help text`.  This feature is not being used
seriously on any known :term:`production site`.


Using the help texts extractor
==============================

In bigger projects we want to differentiate between application development and
authoring of :term:`end user` documentation. That's why the :term:`application
developer` can delegate help text maintenance to the documentation maintainer.

This is where we use the :term:`help texts extractor`.

.. glossary::

  help texts extractor

    A Sphinx extension that extracts help texts from your Sphinx documentation
    to :xfile:`help_texts.py` files, which Lino will load at startup.

.. rubric:: Writing the help texts

With the :term:`help texts extractor` you write the help texts in your
documentation using :term:`prosa style`::

  .. class:: MyModel

      MyModel is an important example.

      .. attribute:: universe

          The first field contains an optional answer to the
          question about life, the universe and everything.

          This field is a simple char field. Blabla more documentation.

Write help texts so that extractor can find them.

Note that only the *first* paragraph of the content of every :rst:dir:`class`
and :rst:dir:`attribute` directive is taken as help text, and that any
formatting and links are removed.

.. currentmodule:: lino_xl.lib.contacts

Help texts are stored on the field descriptor object, which in case of MTI
children can bring a surprising behaviour.  As an example, compare the fields
:attr:`Partner.name` and :attr:`Person.name` (in the :mod:`lino_xl.lib.contacts`
plugin) The Sphinx docs defines documentation for both fields. Obviously we
don't want the help text for the name field on Partner became that of the
Person.


.. rubric:: Extracting the help texts

When you run :cmd:`inv bd` on a Sphinx doctree that has
:mod:`help_texts_extractor <lino.sphinxcontrib.help_texts_extractor>` installed,
Sphinx takes the first paragraph of every object description in your Sphinx
documentation and writes it to a :xfile:`help_texts.py` file.

Configure the :term:`help texts extractor`  in the :xfile:`conf.py` of your
doctree by adding :mod:`lino.sphinxcontrib.help_texts_extractor` to your
``extensions`` and defining a :envvar:`help_texts_builder_targets` setting.  For
example::

    extensions += ['lino.sphinxcontrib.help_texts_extractor']
    help_texts_builder_targets = {
        'lino_algus.': 'lino_algus.lib.algus'
    }


.. rubric:: Translate help texts

After having extracted help texts, the application developer can run :cmd:`inv
mm` and start translating them.

.. rubric:: Loading help texts at startup

Lino will load these :xfile:`help_texts.py` files at startup and "inject" them
to the fields, actions and actors as if they had been defined by the application
source code.

More precisely, when a Lino :class:`Site <lino.core.site.Site>` initializes, it
looks for a file named :xfile:`help_texts.py` in every plugin directory.  If
such a file exists, Lino imports it and expects it to contain a :class:`dict` of
the form::

    from lino.api import _
    help_texts = {
        'foo': _("A foo is a bar without baz.")
    }



Advantages
==========

- Better readability, better maintainability.

- As an application developer you don't need to worry about Python
  syntax consideration when editing your help text

- Same source is used for both the docs and the user interface. You
  don't need to write (and maintain) these texts twice.

Pitfalls
========

When the database structure changes in the code and you forget to adapt the
specs accordingly, your help texts may "disappear" without notice. You can avoid
this by making your test suite cover the help texts.

You do this by simply showing the help texts of a model or actor in your
functional specifications using the :func:`show_fields
<lino.api.doctest.show_fields>`  or :func:`show_columns
<lino.api.doctests.show_columns>` function.

Example:

>>> import lino
>>> lino.startup('lino_book.projects.min2.settings.doctests')
>>> from lino.api.doctest import *

>>> show_fields(contacts.Person)
+---------------+----------------------------+-----------------------------------------------------------------+
| Internal name | Verbose name               | Help text                                                       |
+===============+============================+=================================================================+
| email         | e-mail address             | The primary email address.                                      |
+---------------+----------------------------+-----------------------------------------------------------------+
| language      | Language                   | The language to use when communicating with this partner.       |
+---------------+----------------------------+-----------------------------------------------------------------+
| phone         | Phone                      | The primary phone number.                                       |
+---------------+----------------------------+-----------------------------------------------------------------+
| gsm           | GSM                        | The primary mobile phone number.                                |
+---------------+----------------------------+-----------------------------------------------------------------+
| city          | Locality                   | The locality, i.e. usually a village, city or town.             |
+---------------+----------------------------+-----------------------------------------------------------------+
| addr1         | Address line before street | Address line before street                                      |
+---------------+----------------------------+-----------------------------------------------------------------+
| street_prefix | Street prefix              | Text to print before name of street, but to ignore for sorting. |
+---------------+----------------------------+-----------------------------------------------------------------+
| street        | Street                     | Name of street, without house number.                           |
+---------------+----------------------------+-----------------------------------------------------------------+
| street_no     | No.                        | House number.                                                   |
+---------------+----------------------------+-----------------------------------------------------------------+
| street_box    | Box                        | Text to print after street number on the same line.             |
+---------------+----------------------------+-----------------------------------------------------------------+
| addr2         | Address line after street  | Address line to print below street line.                        |
+---------------+----------------------------+-----------------------------------------------------------------+
| prefix        | Name prefix                | An optional name prefix. For organisations this is inserted     |
|               |                            | before the name, for persons this is inserted between first     |
|               |                            | name and last name.                                             |
+---------------+----------------------------+-----------------------------------------------------------------+
| name          | Name                       | The full name of this partner. Used for alphabetic sorting.     |
+---------------+----------------------------+-----------------------------------------------------------------+
| title         | Title                      | Used to specify a professional position or academic             |
|               |                            | qualification like "Dr." or "PhD".                              |
+---------------+----------------------------+-----------------------------------------------------------------+
| first_name    | First name                 | The first name, also known as given name.                       |
+---------------+----------------------------+-----------------------------------------------------------------+
| middle_name   | Middle name                | A space-separated list of all middle names.                     |
+---------------+----------------------------+-----------------------------------------------------------------+
| last_name     | Last name                  | The last name, also known as family name.                       |
+---------------+----------------------------+-----------------------------------------------------------------+
| gender        | Gender                     | The sex of this person (male or female).                        |
+---------------+----------------------------+-----------------------------------------------------------------+
| birth_date    | Birth date                 | Uncomplete dates are allowed, e.g.                              |
|               |                            | "00.00.1980" means "some day in 1980",                          |
|               |                            | "00.07.1980" means "in July 1980"                               |
|               |                            | or "23.07.0000" means "on a 23th of July".                      |
+---------------+----------------------------+-----------------------------------------------------------------+
| age           | Age                        | Virtual field displaying the age in years.                      |
+---------------+----------------------------+-----------------------------------------------------------------+
| mti_navigator | See as                     | A virtual field which defines buttons for switching between the |
|               |                            | different views.                                                |
+---------------+----------------------------+-----------------------------------------------------------------+
| municipality  | Municipality               | The municipality, i.e. either the city or a parent of it.       |
+---------------+----------------------------+-----------------------------------------------------------------+

Because the above text is now in your specifications, doctest will warn you
whenever any of the help tests changes.

When you give an actor as argument to show_fields, it will show the parameter
fields of that actor.

>>> show_fields(contacts.Persons)
================ ================ ===============================
 Internal name    Verbose name     Help text
---------------- ---------------- -------------------------------
 observed_event   Observed event   Extended filter criteria
 start_date       Period from      Start date of observed period
 end_date         until            End date of observed period
================ ================ ===============================

>>> show_columns(contacts.Persons)
=============== ================ ============================
 Internal name   Verbose name     Help text
--------------- ---------------- ----------------------------
 email           e-mail address   The primary email address.
=============== ================ ============================

>>> show_columns(contacts.Persons, all=True)
================ ================ ============================
 Internal name    Verbose name     Help text
---------------- ---------------- ----------------------------
 address_column   Address
 email            e-mail address   The primary email address.
 id               ID
================ ================ ============================

A real-world example are the specs of
:class:`lino_avanti.lib.avanti.AllClients`, which include a call to
:func:`lino.api.doctests.show_columns`.



The :xfile:`help_texts.py` file
===============================

.. xfile:: help_texts.py

The :xfile:`help_texts.py` file contains object descriptions to be installed as
:term:`help texts <help text>` of user interface widgets.  The file is
automatically generated from the documentation.

The file is generated only by a *full build*, i.e. when *all* pages of the
doctree were built. If you want to be sure, you must run :cmd:`inv clean` before
running :cmd:`inv bd`.  So in practice you will say :cmd:`inv clean -b bd`


.. envvar:: help_texts_builder_targets

  A setting in the :xfile:`conf.py` of your doctree.  A dictionary mapping
  beginnings of module names to the full name of the Python package where the
  :xfile:`help_texts.py` is to be written.


See also
========

- How it all started: :blogref:`20160620`

- :meth:`lino.core.site.Site.install_help_text`

- :meth:`lino.core.site.Site.load_help_texts`

- The ExtJS front end displays help texts as tooltips
  only when :attr:`lino.core.site.Site.use_quicklinks` is `True`.



Accessing help texts from your code
===================================

>>> import lino
>>> lino.startup('lino_book.projects.min2.settings.doctests')
>>> from lino.api.doctest import *

Here is how Lino internally accesses the help text of a database field:

>>> fld = rt.models.contacts.Partner._meta.get_field('name')
>>> print(fld.help_text)  #doctest: +NORMALIZE_WHITESPACE
The full name of this partner. Used for alphabetic sorting.

Above text is the first sentence extracted from the documentation of
the :attr:`lino_xl.lib.contacts.Partner.name` field.

The following is not true::

  >> fld = rt.models.contacts.Person._meta.get_field('name')
  >> print(fld.help_text)  #doctest: +NORMALIZE_WHITESPACE
  The full name of this person, used for sorting.




Don't read on
=============

>>> from lino.api import _
>>> from lino.utils.jsgen import py2js
>>> x = dict(tooltip=_("""This is a "foo", IOW a bar."""))
>>> print(py2js(x))
{ "tooltip": "This is a \"foo\", IOW a bar." }

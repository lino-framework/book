.. doctest docs/dev/help_texts.rst
.. _help_texts:

Help Texts
==========

.. glossary::

  Help text

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

Help texts can be customized locally per site by the end users as
:term:`customized help text`.  This feature is not being used seriously on any
known :term:`production site`.


The help texts extractor
========================

In bigger projects we want to differentiate between application development and
authoring of :term:`end user` documentation. That's why  the :term:`application
developer` can delegate help text maintenance to the documentation maintainer.

This is where we use the :term:`help texts extractor`.

.. glossary::

  help texts extractor

    A Sphinx extension that extracts help texts from your Sphinx documentation
    to :xfile:`help_texts.py` files, which Lino will load at startup.

With the :term:`help texts extractor` you write the help texts in your
documentation using :term:`prosa style`::

  .. class:: MyModel

      MyModel is an important example.

      .. attribute:: universe

          The first field contains an optional answer to the
          question about life, the universe and everything.

          This field is a simple char field. Blabla more documentation.


How it works
============

When you run :cmd:`inv bd` on a Sphinx doctree that has
:mod:`help_texts_extractor <lino.sphinxcontrib.help_texts_extractor>` installed,
Sphinx takes the first paragraph of every object description in your Sphinx
documentation and write it to a :xfile:`help_texts.py` file.

Note that only the *first* paragraph of the content of every :rst:dir:`class`
and :rst:dir:`attribute` directive is taken as help text, and that any
formatting and links are removed.

After having extracted help texts, the application developer can run :cmd:`inv
mm` and start translating them.

Lino will load these :xfile:`help_texts.py`  files at startup and "inject" them
to the fields, actions and actors as if they had been defined by the application
code.

Advantages
==========

- Better readability, better maintainability.

- As an application developer you don't need to worry about Python
  syntax consideration when editing your help text

- Same source is used for both the docs and the user interface. You
  don't need to write (and maintain) these texts twice.


The :xfile:`help_texts.py` file
===============================

.. xfile:: help_texts.py

The :xfile:`help_texts.py` file contains object descriptions to be installed as
the `help_text` attribute of certain UI widgets: actors, actions and database
fields.

It is automatically generated when a full build is being done.

Note that this is done only when *all* pages of the doctree were built, i.e.
when you ran :cmd:`inv clean` before running :cmd:`inv bd`.

Note that the :term:`help texts extractor` needs to be configured properly: see
the :envvar:`help_texts_builder_targets` variable in the :xfile:`conf.py` of the
book.

When a Lino :class:`Site <lino.core.site.Site>` initializes, it looks for a file
named :xfile:`help_texts.py` in every plugin directory.  If such a file exists,
Lino imports it and expects it to contain a :class:`dict` of the form::

    from lino.api import _
    help_texts = {
        'foo': _("A foo is a bar without baz.")
    }


See also
========

- How it all started: :blogref:`20160620`

- :meth:`lino.core.site.Site.install_help_text`

- :meth:`lino.core.site.Site.load_help_texts`

- The ExtJS front end displays help texts as tooltips
  only when :attr:`lino.core.site.Site.use_quicklinks` is `True`.



Using help texts
================

>>> import lino
>>> lino.startup('lino_book.projects.min2.settings.doctests')
>>> from lino.api.doctest import *

Here is how Lino internally accesses the help text of a database field:

>>> fld = rt.models.contacts.Partner._meta.get_field('name')
>>> print(fld.help_text)  #doctest: +NORMALIZE_WHITESPACE
The full name of this partner. Used for alphabetic sorting.

Above text is the first sentence extracted from the documentation of
the :attr:`lino_xl.lib.contacts.Partner.name` field.

You can show and test all help texts of a model or actor in functional
specifications using the :func:`show_fields
<lino.api.doctest.show_fields>` function:

>>> show_fields(rt.models.contacts.Partner)
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



Don't read on
=============

>>> from lino.api import _
>>> from lino.utils.jsgen import py2js
>>> x = dict(tooltip=_("""This is a "foo", IOW a bar."""))
>>> print(py2js(x))
{ "tooltip": "This is a \"foo\", IOW a bar." }

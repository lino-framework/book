.. doctest docs/dev/help_texts.rst
.. _help_texts:

Help Texts
==========

Help texts are the short explanations to be displayed as tooltips when
the user hovers over a form field, menu item, or toolbar button.

The challenge with help texts is that they must be helpful to
end-users, up-to-date and translated.

.. contents::
   :local:
   :depth: 2


Introduction
============

Help texts can be simply defined and maintained by the application
developer by setting the :attr:`help_text` attribute of a database
field, :attr:`actor <lino.core.actors.Actor.help_text>` or
:attr:`action <lino.core.actions.Action.help_text>`.  You should wrap
that string into :func:`gettext` to have it translatable.  Fictive
example::
      
    class MyModel(dd.Model):
        """MyModel is an important example."""

        universe = models.CharField(_("First field"),
            blank=True, max_length=100, help_text=_("""
    The first field contains an optional answer to the
    question about life, the universe and everything.
    """))

Help texts can be customized locally per site by the users using
:class:`HelpText <lino.modlib.system.HelpText>` table.  This feature
exists but is not seriously used in reality.
       
For bigger projects we recommend to use the :mod:`help_texts_extractor
<lino.sphinxcontrib.help_texts_extractor>` module which delegates help
text authoring and maintenance to the documentation author.

The help text extractor is a Sphinx extension which extracts help
texts from your Sphinx documentation to a :xfile:`help_texts.py` file
which Lino will load at startup.

With help text extractor you write the help texts in your
documentation using prosa style::


    .. class:: MyModel
               
        MyModel is an important example.

        .. attribute:: universe

            The first field contains an optional answer to the
            question about life, the universe and everything.


Advantages:

- Better readability.

- As an application developer you don't need to worry about Python
  syntax consideration when editing your help text

- Same source is used for both the docs and the user interface. You
  don't need to write (and maintain) these texts twice.

Note that only the *first* paragraph of the content of every
:rst:dir:`class` and :rst:dir:`attribute` directive is taken as help
text, and that any links are being removed.

Note also that any formatting is removed.


The :xfile:`help_texts.py` file
===============================

.. xfile:: help_texts.py

The :xfile:`help_texts.py` file contains object descriptions to be
installed as the `help_text` attribute of certain UI widgets (actions,
database fields, ...)

It is automatically generated when a full build is being done.

When a Lino :class:`Site <lino.core.site.Site>` initializes, it looks
for a file named :xfile:`help_texts.py` in every plugin directory.  If
such a file exists, Lino imports it and expects it to contain a
:class:`dict` of the form::

    from lino.api import _
    help_texts = {
        'foo': _("A foo is a bar without baz.")
    }


See also
========

- How it all started: :blogref:`20160620`
- :meth:`lino.core.site.Site.install_help_text`
- :meth:`lino.core.site.Site.load_help_texts`
- The ExtJS user interface displays help texts as tooltips
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
Subclasses may hide this field and fill it automatically,
e.g. saving a Person will automatically set her
name field to "last_name, first_name".

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
| phone         | Phone                      | The primary phone number.  Note that Lino does not ignore       |
|               |                            | formatting characters in phone numbers when searching.  For     |
|               |                            | example, if you enter "087/12.34.56" as a phone number, then a  |
|               |                            | search for phone number containing "1234" will not find it.     |
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
|               |                            | name and last name (see                                         |
|               |                            | lino.mixins.human.Human.get_last_name_prefix()).                |
+---------------+----------------------------+-----------------------------------------------------------------+
| name          | Name                       | The full name of this partner. Used for alphabetic sorting.     |
|               |                            | Subclasses may hide this field and fill it automatically,       |
|               |                            | e.g. saving a Person will automatically set her                 |
|               |                            | name field to "last_name, first_name".                          |
+---------------+----------------------------+-----------------------------------------------------------------+


Don't read on
=============

>>> from lino.api import _
>>> from lino.utils.jsgen import py2js
>>> x = dict(tooltip=_("""This is a "foo", IOW a bar."""))
>>> print(py2js(x))
{ "tooltip": "This is a \"foo\", IOW a bar." }


.. doctest docs/dev/bleach.rst

=========
Bleaching
=========

Bleaching means to remove all unknown tags when saving the content of a
:class:`RichHtmlField <lino.core.fields.RichHtmlField>`.



.. contents::
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> import os
>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.doctests')
>>> from lino.api.doctest import *


The problem
===========

When copying rich text from other applications into Lino, the text can
contain styles and other things which can cause side effects when
displaying or printing them.

A possible strategy for avoiding such problems is to bleach any
content, i.e. allow only simple plain HTML formatting.

To activate bleaching of all rich text fields, you basically simply say::

      textfield_bleached = True

in your :xfile:`settings.py` file.  See :attr:`lino.core.site.Site.textfield_bleached`.

Installation
============

When you use this feature, you must manually install the `bleach
<http://bleach.readthedocs.org/en/latest/>`_ Python module (unless the
application has added it to its :ref:`install_requires`)::

    $ pip install bleach


Note that `bleach` until 20170225 required html5lib` version
`0.9999999` (7*"9") while the current version is `0.999999999`
(9*"9"). Which means that you might inadvertently break `bleach` when
you ask to update `html5lib`::

    $ pip install -U html5lib
    ...
    Successfully installed html5lib-0.999999999
    $ python -m bleach
    Traceback (most recent call last):
      File "/usr/lib/python2.7/runpy.py", line 163, in _run_module_as_main
        mod_name, _Error)
      File "/usr/lib/python2.7/runpy.py", line 111, in _get_module_details
        __import__(mod_name)  # Do not catch exceptions initializing package
      File "/site-packages/bleach/__init__.py", line 14, in <module>
        from html5lib.sanitizer import HTMLSanitizer
    ImportError: No module named sanitizer


As an application developer you can force bleaching to be activated or not for
a specific field by explicitly saying a :attr:`bleached
<lino.core.fields.RichTextfield.bleached>` argument when declaring the field.


Fine-tuning
============

You can configure which HTML tags are allowed by changing the
:attr:`bleach_allowed_tags <lino.core.site.Site.bleach_allowed_tags>` site
attribute.

>>> settings.SITE.bleach_allowed_tags
['a', 'b', 'i', 'em', 'ul', 'ol', 'li', 'strong', 'p', 'br', 'span', 'pre', 'def', 'table', 'th', 'tr', 'td', 'thead', 'tfoot', 'tbody']



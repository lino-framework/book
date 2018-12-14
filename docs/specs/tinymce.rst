.. doctest docs/specs/tinymce.rst
.. _lino.tested.tinymce:

====================================
``tinymcs`` : Add the TinyMCE editor
====================================

.. currentmodule:: lino.modlib.tinymce

The :mod:`lino.modlib.tinymce` plugin activates usage of the TinyMCE editor for
HTML text fields (:class:lino.core.fields.RichTextField`) instead of the
built-in `Ext.form.HtmlEditor` editor that comes with ExtJS.


.. contents::
  :local:

.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.demo')
>>> from lino.api.doctest import *


Configuration
=============

See :class:`lino.modlib.tinymce.Plugin`

The :class:`Templates` table
============================

The :class:`Templates` is designed to make usage of TinyMCE's
`external_template_list_url
<http://www.tinymce.com/wiki.php/Configuration3x:external_template_list_url>`__
setting.



>>> url = "/tinymce/templates/notes/MyNotes/69/body"
>>> test_client.force_login(rt.login('robin').user)
>>> response = test_client.get(url, REMOTE_USER='robin')
>>> response.status_code
200
>>> print(response.content.decode())
... #doctest: +NORMALIZE_WHITESPACE
var tinyMCETemplateList = [ 
[ "hello", "/tinymce/templates/notes/MyNotes/69/body/1", "Inserts 'Hello, world!'" ], 
[ "mfg", "/tinymce/templates/notes/MyNotes/69/body/2", "None" ] 
];

>>> url = "/tinymce/templates/notes/MyNotes/69/body/1"
>>> response = test_client.get(url, REMOTE_USER='robin')
>>> response.status_code
200
>>> print(response.content.decode())
... #doctest: +NORMALIZE_WHITESPACE
<div>Hello, world!</div>


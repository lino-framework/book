.. doctest docs/specs/tinymce.rst
.. _lino.tested.tinymce:

====================================
``tinymce`` : Add the TinyMCE editor
====================================

.. currentmodule:: lino.modlib.tinymce

The :mod:`lino.modlib.tinymce` plugin activates usage of the TinyMCE editor for
HTML text fields (:class:lino.core.fields.RichTextField`) instead of the
built-in `Ext.form.HtmlEditor` editor that comes with ExtJS.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.demo')
>>> from lino.api.doctest import *

Dependencies
============

This plugin makes sense only if :mod:`lino.modlib.extjs` is also installed. It
also requires the :mod:`lino.modlib.office` plugin because it adds entries to
the :menuselection`Office` menu.

>>> dd.plugins.tinymce.needs_plugins
['lino.modlib.office', 'lino.modlib.extjs']



Configuration
=============


When serving static files from a different subdomain, TinyMCE needs
to know about this.

Typical usage is to specify this in your :xfile:`lino_local.py` file::

    def setup_site(self):
        ...
        from lino.api.ad import configure_plugin
        configure_plugin('tinymce', document_domain="mydomain.com")

Currently when using this, **you must also manually change** your
static :xfile:`tiny_mce_popup.js` file after each `collectstatic`.

.. xfile:: tiny_mce_popup.js

The factory version of that file contains::

    // Uncomment and change this document.domain value if you are loading the script cross subdomains
    // document.domain = 'moxiecode.com';

Uncomment and set the ``document.domain`` to the same value as
your :attr:`document_domain`.



See :class:`lino.modlib.tinymce.Plugin`

The ``Templates`` table
==========================


.. class:: TextFieldTemplate

    A reusable block of text that can be selected from a text editor to
    be inserted into the text being edited.

.. class:: TextFieldTemplates
.. class:: MyTextFieldTemplates


.. class:: Templates

The :class:`Templates` is designed to make usage of TinyMCE's
`external_template_list_url
<http://www.tinymce.com/wiki.php/Configuration3x:external_template_list_url>`__
setting.

It is called by TinyMCE (`template_external_list_url
<http://www.tinymce.com/wiki.php/configuration:external_template_list_url>`_)
to fill the list of available templates.



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


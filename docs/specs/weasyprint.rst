.. $ doctest docs/specs/weasyprint.rst
.. _specs.weasyprint:

===================================
Printing documents using WeasyPrint
===================================

The :mod:`lino.modlib.weasyprint` plugin installs two build methods
for generating printable documents using `weasyprint
<http://weasyprint.org/>`__.

Applications which use this plugin must also add `'weasyprint'` to
their :ref:`install_requires`.

The build methods defined by this plugin both have the same input
template, whose ending must be :xfile:`.weasy.html`.  Both methods
then render the input template through Jinja with the standard context
variables (defined by :meth:`get_printable_context
<lino.core.model.Model.get_printable_context>`.  The base build method
:class:`WeasyBuildMethod
<lino.modlib.weasyprint.choicelists.WeasyBuildMethod>` then returns
this HTML output "as is", the other method runs weasyprint over the
HTML file to convert it to a :file:`.pdf` file.

Examples in this document use the :mod:`lino_book.projects.lydia` demo
project.

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.shell import *
>>> from lino.api.doctest import *

See also :doc:`printing`.

Build methods
=============

This plugin defines no models, it just adds to build methods to 
:class:`lino.modlib.printing.BuildMethods`
(the global list of build methods).


.. currentmodule:: lino.modlib.weasyprint

.. class:: WeasyBuildMethod
           
    The base class for both build methods.
    

.. class:: WeasyHtmlBuildMethod

    Renders the input template and returns the unmodified output as
    plain HTML.
    
.. class:: WeasyPdfBuildMethod
           
    Like :class:`WeasyBuildMethod`, but the rendered HTML is then
    passed through weasyprint which converts from HTML to PDF.


Templates
=========


.. xfile weasyprint/base.weasy.html

    Defines the general HTML page to be included by every template.
    This is meant to be included by the actual templates.

    You can look at the `source code
    <https://github.com/lino-framework/lino/blob/master/lino/modlib/weasyprint/config/weasyprint/base.weasy.html>`__

Templates defined by other plugins:    

- :mod:`lino_xl.lib.excerpts` --
  :xfile:`excerpts/base.weasy.html`

- :mod:`lino_xl.lib.sheets` --
  :xfile:`sheets/Report/default.weasy.html`
  
- :mod:`lino_xl.lib.bevats` --
  :xfile:`bevats/Declaration/default.weasy.html`
  
- :mod:`lino_xl.lib.lists` --
  :xfile:`lists/List/list_members.weasy.html`
  
- :mod:`lino_xl.lib.courses` --
  :xfile:`courses/Course/presence_sheet.weasy.html`
  
- :mod:`lino_xl.lib.ledger` --
  :xfile:`contacts/Partner/payment_reminder.weasy.html`

- :mod:`lino_xl.lib.working` --
  :xfile:`working/ServiceReport/default.weasy.html`
         
- :ref:`welfare` also uses it.


Warnings about Cairo and Pango
==============================

This plugin installs a warnings filter for the `cffi.model` module in
order to get rid of a disturbing warning :message:`There are known
rendering problems with Cairo <= 1.14.0` and :message:`@font-face
support needs Pango >= 1.38` issued by weasyprint.

.. (Probably obsolete:) They should also add `'cairocffi<0.7'` (see
   :ticket:`1119`) or install it using pip::

      $ pip install 'cairocffi<0.7' weasyprint



    

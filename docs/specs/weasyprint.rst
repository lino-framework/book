.. $ doctest docs/specs/weasyprint.rst
.. _specs.weasyprint:

===================================================
``weasyprint``: Printing documents using WeasyPrint
===================================================

The :mod:`lino.modlib.weasyprint` plugin installs two build methods
for generating printable documents using `weasyprint
<http://weasyprint.org/>`__.

Applications that use this plugin will have `'weasyprint'` in their
:ref:`install_requires`.

The two build methods defined by this plugin both use the same input template,
whose ending must be :xfile:`.weasy.html`.  Both methods then render the input
template through Jinja with the standard context variables (defined by
:meth:`get_printable_context <lino.core.model.Model.get_printable_context>`.
The base build method :class:`WeasyBuildMethod
<lino.modlib.weasyprint.choicelists.WeasyBuildMethod>` then returns this HTML
output "as is", the other method runs weasyprint over the HTML file to convert
it to a :file:`.pdf` file.

Examples in this document use the :mod:`lino_book.projects.lydia` demo
project.

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.shell import *
>>> from lino.api.doctest import *

See also :doc:`printing`.



Build methods
=============

This plugin defines no models, it just adds two build methods to your the global
list of build methods (:class:`lino.modlib.printing.BuildMethods`).


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


.. xfile:: weasyprint/base.weasy.html

Defines the general HTML page to be included by every template.
This is meant to be included by the actual templates.

Source code:
https://github.com/lino-framework/lino/blob/master/lino/modlib/weasyprint/config/weasyprint/base.weasy.html

The template defines the following blocks:

- pagesize
- bottomright
- bottomleft
- header
- intro
- main


Weasyprint templates defined by other plugins
=============================================

- :mod:`lino_xl.lib.bevats` --
  :xfile:`bevats/Declaration/default.weasy.html`

  In demo project lydia, go to :menuselection:`Accounting --> VAT Declarations`
  and print one of them.

- :mod:`lino_xl.lib.courses` --
  :xfile:`courses/Course/presence_sheet.weasy.html`

  In demo project roger, open the detail view of some course and click on one of
  the `Presence sheet` links.

- :mod:`lino_xl.lib.ledger` --
  :xfile:`contacts/Partner/payment_reminder.weasy.html`

- :mod:`lino_xl.lib.lists` --
  :xfile:`lists/List/list_members.weasy.html`

- :mod:`lino_xl.lib.sheets` --
  :xfile:`sheets/Report/default.weasy.html`

- :mod:`lino_xl.lib.working` --
  :xfile:`working/ServiceReport/default.weasy.html`

Here is a list of the weasy templates included with the :ref:`xl`:

>>> import lino_xl
>>> from os.path import dirname
>>> from atelier.sheller import Sheller
>>> shell = Sheller(dirname(lino_xl.__file__))
>>> shell("find -name '*.weasy.html' | sort")
./lib/bevats/config/bevats/Declaration/default.weasy.html
./lib/courses/config/courses/Course/presence_sheet.weasy.html
./lib/excerpts/config/excerpts/base.weasy.html
./lib/ledger/config/contacts/Partner/payment_reminder.weasy.html
./lib/lists/config/lists/List/list_members.weasy.html
./lib/orders/config/orders/Order/base.weasy.html
./lib/orders/config/orders/Order/default.weasy.html
./lib/sales/config/sales/VatProductInvoice/base.weasy.html
./lib/sales/config/sales/VatProductInvoice/default.weasy.html
./lib/sheets/config/sheets/Report/default.weasy.html
./lib/working/config/working/ServiceReport/default.weasy.html

Note that `excerpts`, `orders` and `sales` have their own
:file:`FOO/base.weasy.html` template, which inherits from  the main base
:xfile:`weasyprint/base.weasy.html`.


For other usage examples see the specs of :ref:`welfare`.


Warnings about Cairo and Pango
==============================

This plugin installs a warnings filter for the `cffi.model` module in
order to get rid of a disturbing warning :message:`There are known
rendering problems with Cairo <= 1.14.0` and :message:`@font-face
support needs Pango >= 1.38` issued by weasyprint.


.. _specs.weasyprint.logo:

How to customize your logo in the header or footer
==================================================

This section explains how headers and footers are configured in
:mod:`lino.modlib.weasyprint` templates (and how you can customize them).

You can automagically add a logo to all your weasyprint documents by adding a
local :xfile:`config` directory with a subdirectory :file:`weasyprint`
containing a file named :file:`logo.jpg`.   The logo will get printed in the top
right area of every page (unless you change the template).

How it all works
================

What happens when I print an invoice?

When Lino starts up, it finds the :term:`excerpt type` for sales invoices  (more
precisely the :class:`sales.VatProductInvoice
<lino_xl.lib.sales.VatProductInvoice>` model) and therefore installs the print
action on that model. This is why you a have a print button per invoice.

The :term:`excerpt type` tells Lino which :term:`build method` you want to use
for building your printable document. The default build method is ``weasypdf``.

When we know the build method, we can compute the name of the template to use.
This name is a combination
of ``sales/VatProductInvoice`` (the plugin and model name) and
``default.weasy.html`` (the default template filename for weasypdf when
:class:`lino_xl.lib.excerpts.ExcerptType.template` is empty).

Lino now searches for a file named :xfile:`sales/VatProductInvoice/default.weasy.html`.
This file can exist under any :xfile:`config` directory.
If you have a local :xfile:`config` directory, this is searched first.
Otherwise Lino uses a default file from the source code directory.
More about config directories in :doc:`/admin/config_dirs`.

Now look at the default :xfile:`sales/VatProductInvoice/default.weasy.html`
template file.  The first line is::

  {%- extends "weasyprint/base.weasy.html" -%}

Which means that Lino first loads yet another template, called
:xfile:`weasyprint/base.weasy.html`.


How weasyprint templates work
=============================

The weasyprint template uses the CSS @-rules
`@page <https://www.quackit.com/css/at-rules/css_page_at-rule.cfm>`__ and
`@bottom-right
<https://www.quackit.com/css/at-rules/css_bottom-right_at-rule.cfm>`__,
which
define styles to apply to individual pages when printing the document.
That is, they are used to apply styles for *paged media* only,
not for continuous media like a browser window.

List of all ``page-margin`` properties:
https://www.quackit.com/css/at-rules/css_page-margin_properties_list.cfm

Setting the height attribute in HTML is called a "presentational hint"
and it's now recommended not to use them and use CSS instead.
Presentational hints are ignored by WeasyPrint by default,
but you can handle them using the --presentational-hints CLI parameter.
https://github.com/Kozea/WeasyPrint/issues/872

Lino currently doesn't use arbitrary "complex" HTML in headers and footers (as
`documented here
<https://weasyprint.readthedocs.io/en/latest/tips-tricks.html#include-header-and-footer-of-arbitrary-complexity-in-a-pdf>`__).
The standard system with at-rules works well for us.

It contains pseudo-elements for styling the first page as well as the
left and right margins of the page.

It can contain something like this::

  <style type="text/css">
  @page {
      @top-right {
        height: 20mm;
        padding: 0px;
        text-align: right;
        content: url(file://{{logo_file}});
      }
  </style>

More readings:

- https://www.qhmit.com/css/at-rules/
- https://www.quackit.com/css/properties/css_content.cfm
- https://stackoverflow.com/questions/39941967/generate-pdf-with-weasyprint-having-common-header-footer-and-pagination
- https://github.com/Kozea/WeasyPrint/blob/gh-pages/samples/invoice/invoice.css
- https://gist.github.com/pikhovkin/5642563 complex headers

.. _lino.admin.appypod:
.. _lino.admin.appy_templates:

========================
Using Appy POD templates
========================

When a printable document (`.pdf`, `.odt` or `.rtf`) is being
generated using a subclass of :class:`AppyBuildMethod
<lino_xl.lib.appypod.AppyBuildMethod>`, then you can provide a
document as template in `.odt` format which you can edit using
LibreOffice Writer.

This template document contains special instructions defined by the
`appy.pod <http://appyframework.org/pod.html>`__ library.



Context
=======


.. currentmodule:: lino_xl.lib.appypod.context

The Appy renderer installs additional functions to be used in `do
text|section|table from
<http://appyframework.org/podWritingAdvancedTemplates.html>`__
statements.

.. function:: jinja(template_name)

    Render the template named `template_name` using Jinja.
    The template is supposed to produce HTML markup.

    If `template_name` contains no dot, then the default filename extension
    :file:`.body.html` is added.


.. function:: restify(s)

    Render a string `s` which contains reStructuredText markup.

    The string is first passed to
    :func:`lino.utils.restify.restify` to convert it to XHTML,
    then to `appy.pod`'s built-in :func:`xhtml` function.
    Without this, users would have to write each time something like::

        do text
        from xhtml(restify(self.body).encode('utf-8'))

.. function:: html(html)

    Render a string that is in HTML (not XHTML).

.. function:: ehtml(e)

    Render an ElementTree node
    (generated using :mod:`etgen.html`)
    into this document.
    This is done by passing it to :mod:`lino.utils.html2odf`.

.. function:: table(ar, column_names=None)`

    Render an :class:`lino.core.tables.TableRequest` as a
    table. Example::

        do text
        from table(ar.spawn('auth.UsersOverview'))

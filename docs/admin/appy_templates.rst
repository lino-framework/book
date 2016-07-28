.. _lino.admin.appypod:
.. _lino.admin.appy_templates:

========================
Using Appy POD templates
========================

When a printable document is being generated using
:class:`AppyBuildMethod
<lino_xl.lib.appypod.choicelists.AppyBuildMethod>` or a subclass
thereof, then you provide an :term:`appy.pod template` which Lino
renders as a `.pdf`, `.odt` or `.rtf` printable.

Vocabulary
==========

.. glossary::
 
    appy.pod template

        An `.odt` file which contains special instructions defined by
        Gaëtan Delannay's 
        `appy.pod <http://appyframework.org/pod.html>`__ library.






Context
=======


.. currentmodule:: lino_xl.lib.appypod.context

installs additional
functions to be used in `do text|section|table from
<http://appyframework.org/podWritingAdvancedTemplates.html>`__
statements.

.. function:: jinja(template_name)

  Render the template named `template_name` using Jinja.
  The template is supposed to produce HTML markup.

  I `template_name` contains no dot, then the default filename
  extension `.body.html` is added.


- `restify(s)`:
  Render a string `s` which contains reStructuredText markup.
  The string is first passed to
  :func:`lino.utils.restify.restify` to convert it to XHTML,
  then to `appy.pod`'s built in `xhtml` function.
  Without this, users would have to write each time something like::

    do text
    from xhtml(restify(self.body).encode('utf-8'))

- `html(s)` :
  Render a string that is in HTML (not XHTML).

- `ehtml(e)` :
  Render an ElementTree node
  (generated using :mod:`lino.utils.xmlgen.html`)
  into this document. 
  This is done by passing it to :mod:`lino.utils.html2odf`.

- `table(ar, column_names=None)` : render an
  :class:`lino.core.tables.TableRequest` as a table. Example::

    do text
    from table(ar.spawn('users.UsersOverview'))



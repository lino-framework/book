===========================
Sphinx doctree dependencies
===========================

*Technical documentation* includes topic guides, :doc:`/dev/specs`, the changelog
and generated API documentation. For some applications we maintain also *end-user
documentation* in different languages. These are independant doctrees, not a
translation of the technical docs.

The technical documentation for :mod:`lino` and :mod:`lino_xl` is grouped in the
"Lino Book". The book repository contains Python source code for a package
:mod:`lino_book`. This package is not installable via PyPI because it contains
only fictive example projects.

The book also includes the technical documentation for a set of "privileged"
applications (:ref:`noi`, :ref:`tera`, :ref:`avanti`, ...) because it's
difficult to explain Lino without examples, and because real applications are
the best example.

Otherwise every newer typical Lino application has its own doctree.
`Lino Amici <http://amici.lino-framework.org>`_ is an example.
The doctree of amici can refer to the book via Intersphinx.

We also maintain the :mod:`atelier` and :mod:`etgen` packages, which come
"before" Lino in the dependency chain. These packages have their own doctree,
which doesn't "know" about Lino. But the book "knows" about them and wants to
refer to them.

Most :xfile:`conf.py` files use :func:`atelier.interproject.configure`  to
configure intersphinx dependencies, and :func:`atelier.sphinxconf.configure` to
install default Sphinx settings that are common to all doctrees.

Python dependencies :

- book -> xl -> lino
- book -> noi -> lino
- lino -> etgen -> atelier
- amici -> xl -> lino

Doctree intersphinx dependencies:

- amici -> book -> atelier

Documenting Django apps has the particular challenge that they cannot be
imported without a :envvar:`DJANGO_SETTINGS_MODULE`, and this setting may not
change within one Sphinx doctree.  The doctree of the book uses
:mod:`lino_book.projects.max` as its  :envvar:`DJANGO_SETTINGS_MODULE` during
build.

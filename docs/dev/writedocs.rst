.. _writedocs:

=====================
Writing documentation
=====================

Writing documentation about Lino is a complex topic. Some
considerations:

End user documentation must be written per application by the customer
or the product owner.  We generally recommend a LibreOffice document.

The Lino team tries to provide useful documentation for a rather wide
audience:

- trainers, consultants and application developers need topic
  overviews as well as reference documentation about every plugin.
  
- core developers additionally need documentation about the Lino
  internals.

The Lino book contains "API docs" and "Specifications".  These are two
fundamentally different beasts.  The "API docs" are automatically
generated using autodoc which extracts the docstrings from source code
while the Specifications are written in prosa style.
  
Plugins generally cannot be documented using autodoc because they are
extensible and because Django would refuse to import two variants of a
same plugin within a same Sphinx build process.  So prosa style is
needed for plugins.

Prosa style documentation has the advantage of being more readable
since the author can decide about the documents' structure.

The challenge with prosa style is that it needs extra care when some
code changes.

.. toctree::
   :maxdepth: 1

   sphinx/intro
   builddocs
   doctests
   docstrings
   help_texts


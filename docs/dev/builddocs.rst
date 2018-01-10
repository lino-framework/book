.. _lino.dev.bd:

======================
Building the Lino Book
======================

This page explains how to build the Lino Book, i.e. how to generate
the html pages you are reading right now.

The Lino Book is *static* html which is visible at different places,
e.g. at http://www.lino-framework.org\ , at `lino.readthedocs.io
<http://lino.readthedocs.io/en/latest/>`__ or (when you've built it)
locally on your computer.


Theoretically it's easy
=======================

Theoretically it's easy to build the Lino Book: you just run :cmd:`inv
bd` in the root directory of your ``book`` repository::

  $ go book
  $ inv bd

This will tell Sphinx to read the `.rst` source files and to generate
:file:`.html` files into the :file:`docs/.build` directory.  Voilà.

If you get some error message, then you need to check whether your
development environment is correctly installed as explained in
:doc:`install`.


Otherwise you can then start your browser on the generated files::

  $ firefox docs/.build/html/index.html

Or jump directly to your local copy of this page:  

  $ firefox docs/.build/html/team/builddocs.html


Introducing Sphinx
==================

Lino makes heavy usage of **Sphinx**, the dominant documentation
system in the Python world.  Sphinx is a tool that "makes it easy to
create intelligent and beautiful documentation" and that "actually
makes programmers **want** to write documentation!"
(`www.sphinx-doc.org <http://www.sphinx-doc.org>`__).

For example, the "source code" of the page your are reading right now
is in a file `docs/dev/builddocs.rst
<https://github.com/lino-framework/book/blob/master/docs/dev/actions.rst>`__.

Read more about the markup used by Sphinx in `reStructuredText Primer
<http://sphinx-doc.org/rest.html>`_.
Also `The build configuration file <http://sphinx-doc.org/config.html>`_.

  

Let's play
==========

Let's play a bit:  
  
Open the source file of this page::

  $  nano docs/team/builddocs.rst

Edit something in that file and save your changes. Then build the book
again::

  $ inv bd

Then hit :kbd:`Ctrl-R` in your browser and check whether the HTML
output changes as expected.

You can undo all your local changes using::

  $ git checkout docs/team/builddocs.rst

Or, if you agree to :doc:`contribute <contrib>` your changes to the
Lino project, you can :doc:`submit a pull request <request_pull>` as
you would do with code changes.

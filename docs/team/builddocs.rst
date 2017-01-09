.. _lino.dev.bd:

======================
Building the Lino Book
======================

This page explains how to build the Lino Book (i.e. the pages visible
below http://www.lino-framework.org).

Note that Sphinx currently has a subtle problem which requires that
you use the development version. Quick cheat sheet::

  $ pip uninstall sphinx
  $ cd ~/repositories
  $ git clone https://github.com/sphinx-doc/sphinx.git
  $ cd sphinx
  $ pip install -e .

.. The following is probably no longer needed: and apply the patch
   described under `#2336
   <https://github.com/sphinx-doc/sphinx/issues/2336>`_.

      $ wget https://github.com/sphinx-doc/sphinx/files/136248/20160218.txt
      $ patch -p1 < 20160218.txt

Otherwise you just run :cmd:`inv bd` in the root of your ``book``
repository::

  $ go book
  $ inv bd

This uses Sphinx to read the `.rst` source files and to generate
:file:`.html` files into the :file:`docs/.build` directory.

You can then start your browser on the generated files::

  $ firefox docs/.build/html/index.html

Or jump directly to your local copy of this page:  

  $ firefox docs/.build/html/team/builddocs.html


Let's play a bit:  
  
Open the source file of this page::

  $  nano docs/team/builddocs.rst

Edit something in that file and save your changes. The build the book
again::

  $ inv bd

Then hit :kbd:`Ctrl-R` in your browser and check whether the HTML
output changes as expected.

Read more about the markup used by Sphinx in
`reStructuredText Primer <http://sphinx-doc.org/rest.html>`_)-

Undo all your local changes using::

  $ git checkout docs/team/builddocs.rst

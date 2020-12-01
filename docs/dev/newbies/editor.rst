.. _dev.editor:

===================
Which editor to use
===================

Software developers spend most of their time inside a source code editor.

If you haven't yet made up your choice about which editor to use, then we
recommend to start with :ref:`atom`.  See below.
Atom satisfies everything you need to be successful.
Luc still uses just Atom.

There are other choices, most notably PyCharm. Don't waste too much of your time
with single-file editors like `joe
<https://en.wikipedia.org/wiki/Joe%27s_Own_Editor>`__ or `nano
<https://www.nano-editor.org/>`__. These are good for occasional changes in
files on a server that you access via a terminal, but they are not designed for
jumping back and forth in a repository with thousands of source code files.

.. _atom:

Atom
====

"A hackable text editor for the 21st Century". https://atom.io/

Installation::

  $ sudo apt install atom

Install the `python-tools <https://atom.io/packages/python-tools>`__ package and
configure its "Path to Python directory" to point to your default virtualenv
(which you defined in :ref:`dev.default_venv`).

Select :menuselection:`File --> Add project folder...` and add your
:xfile:`~/lino` directory. This will cause Atom to index all files below this
directory.

Some useful keyboard shortcuts:

- :kbd:`Ctrl+P` open an existing file using fuzzy file name search within all files of the project.
- :kbd:`Shfit+Ctrl+F` find (and optionally replace) a text string in all files (or in some)
- :kbd:`Alt+Q` reflow selection
- :kbd:`Ctrl+Alt+G` go to definition

Other useful packages to install:

- `tidy-tabs <https://atom.io/packages/tidy-tabs>`__ causes Atom to close tabs
  that you haven't visited for some time. Useful because otherwise Atom can
  become a memory waster.

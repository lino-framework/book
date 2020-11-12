.. _dev.editor:

===================
Which editor to use
===================

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

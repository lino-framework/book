.. _xl.install:

==================
Installing Lino XL
==================

Lino XL is installed automatically when you use `pip
<http://www.pip-installer.org>`__ to install your Lino application.

This document describes some additional installation requirements
which might apply to you.

- If your application uses :mod:`lino.utils.html2xhtml`, then you must
  manually install the `HTML Tidy library
  <http://tidy.sourceforge.net/>`__ to yoursystem. Under Debian this
  means::

    $ sudo apt-get install tidy

- If you want to produce :file:`.pdf` files from :file:`odt`
  templates, then you need :doc:`oood`.

.. toctree::
   :hidden:

   oood
   

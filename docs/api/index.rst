===
API
===

.. _lino:

The Lino core
=============

The **Lino Core** is the bare minimum you need to write a Lino
applicaton.

.. py2rst::

  import lino
  print(lino.SETUP_INFO['long_description'])

.. automodule:: lino


.. _xl:

Lino Extensions Library
=======================

Most Lino projects also require the **Lino Extensions Library**, a
collection of plugins which are not part of the core because they add
a given set of solutions for "Enterprise" style applications.

.. py2rst::

  import lino_xl
  print(lino_xl.SETUP_INFO['long_description'])


.. automodule:: lino_xl

The Lino book
=============

.. py2rst::

  import lino_book
  print(lino_book.SETUP_INFO['long_description'])




.. automodule:: lino_book


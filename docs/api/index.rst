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

.. raw:: html

   <a href="https://travis-ci.org/lino-framework/xl" target="_blank"><img src="https://travis-ci.org/lino-framework/xl.svg?branch=master"/></a>

.. py2rst::

  import lino_xl
  print(lino_xl.SETUP_INFO['long_description'])

.. automodule:: lino_xl
                
                
.. _book:

The Lino book
=============

.. py2rst::

  import lino_book
  print(lino_book.SETUP_INFO['long_description'])

.. automodule:: lino_book



.. _commondata:

The commondata packages
=======================


- https://github.com/lsaffre/commondata
- https://github.com/lsaffre/commondata-be
- https://github.com/lsaffre/commondata-ee
- https://github.com/lsaffre/commondata-eg

.. automodule:: commondata
                
.. automodule:: commondata.be
                
.. automodule:: commondata.ee
                
.. automodule:: commondata.eg
                


                

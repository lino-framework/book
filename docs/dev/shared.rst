.. _dev.shared:

=======================
Shared Sphinx resources
=======================

The **shared Sphinx resources** is a folder with files we use when building our
document trees.  The folder is shared over several repositories.

.. xfile:: /shared

The :xfile:`/shared` folder of a doctree.


.. xfile:: tested.rst

The :xfile:`tested.rst` file is used by adding the following line before the
startup block::

  .. include:: /../docs/shared/include/tested.rst

.. xfile:: defs.rst

The :xfile:`defs.rst` file is used by adding the following line to the top of
the document::

  .. include:: /../docs/shared/include/defs.rst


A doctree which uses :ref:`dev.shared`  should add the following to its
:xfile:`conf.py` file::

    exclude_patterns = ['.build/*', 'shared/include/*']

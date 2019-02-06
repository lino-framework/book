.. doctest docs/specs/files.rst
.. _xl.specs.files:
   
=================================
``files`` : Manage external files
=================================

.. currentmodule:: lino_xl.lib.files

The :mod:`lino_xl.lib.files` plugin adds functionality for managing external
files stored somewhere in a file system.

.. contents::
  :local:

.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *

Overview
========


A **volume** is a folder on the file system that is to be observed by Lino. The
:class:`Volumes` choicelist holds the volumes and gives the base URL where
these files are expected to be served.

For every file found in a *volume*, Lino will create an instance of the
:class:`File` model which represents the file.

The :class:`Receivable` mixins is what we are going to use on invoices in
:ref:`cosi`.


The :class:`PendingReceivables` table shows all receivables that need a receipt
but don't have any.

The :class:`DanglingFiles` table shows all unused files (i.e. which aren't referred

Volumes
=======

To use this plugin, the local site administrator must define *volumes* by
populating the :class:`Volumes` choicelist.  This can be done e.g. in the
workflows module (:attr:`lino.core.site.Site.workflows_module`)::

    from lino_xl.lib.files.choicelists import Volumes
    add = Volumes.add_item
    add("media", "/media/disk/shared", "Media on disk", "https://static.example.com/media")
    add("luc", "/home/luc/shared", "Luc's files", "https://static.example.com/luc")



.. class:: Volume

     Every item of the :class:`Volumes` choicelist is an instance of this
     class.

    .. attribute:: value

        The primary key used to point to this volume from a database object.
        Should be a short unique name.

    .. attribute:: name

        The full path of the root folder.

    .. attribute:: text

        A descriptive text.

    .. attribute:: base_url

        The base URL where files of this volume are being served.

    .. attribute:: backend

        The file backend used to access the files on this volume.

        Currently this is ignored, Lino supports only the "local filesystem"
        backend.


.. class:: File

     The Django model representing a file.

    .. attribute:: id

        Internal ID to be used as primary key.

    .. attribute:: volume

        The volume where this file is stored.

    .. attribute:: name

        The full path name relative to the root folder of the volume.

    .. attribute:: state



.. class:: Receivable

    Being "receivable" means that every database object should have a scan or pdf
    file of the "receipt", i.e. the document serving as the legal proof of this
    database object.

    Receivables without such a receipt will appear in the
    :class:`PendingReceivables` table.

    .. attribute:: receipt

        The file which serves as receipt for this database object.

    .. method:: needs_receipt

        Return `True` if this database object needs a receipt.


Receivable folders
==================

A **receivable folder** is a folder with files that should be used as
receivables.  any file in such a folder which is not used by some
:class:`Receivable` will be mentioned in the :class:`DanglingReceipts`  table.

The local system administrator can specify a receivable folder like this::

    AccountInvoice.add_receivable_folder("luc", "/receipts", "EKR")



.. class:: PendingReceivables

    Shows all receivables that need a receipt but don't have any.

.. class:: DanglingReceipts

    Shows all files that are a receipt but aren't used as such by any
    receivable.

.. class:: BrokenFiles

    Shows all unused files (i.e. which aren't referred to by any database
    object).


.. function:: check_volumes

   Scan all volumes and create descriptors for every file that doesn't yet have
   one.  Mark file descriptors as dangling if the file they describe does no
   longer exist.


.. doctest docs/specs/files.rst

=================================
``files`` : Manage external files
=================================

Deprecated. This plugin was never used. See :blogref:`20190207`.

.. currentmodule:: lino.modlib.files

The :mod:`lino.modlib.files` plugin adds functionality for managing references
to external files stored somewhere in a file system.

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

To use this plugin, the local site administrator must define *volumes*.

A **volume** is a folder on the file system that is to be observed by Lino.
The volume gives the base URL where these files are expected to be served.


.. class:: Volume

    The Django model representing a file volume.


    .. attribute:: id

        The primary key used to point to this volume from a database object.

    .. attribute:: ref

        The full path of the root folder.

    .. attribute:: text

        A descriptive text.

    .. attribute:: base_url

        The base URL where files of this volume are being served.

    .. attribute:: backend

        The file backend used to access the files on this volume.

        Currently this is ignored, Lino supports only the "local filesystem"
        backend.

Files and directories
=====================

.. class:: File

     The Django model representing a file or directory on a file system.

    .. attribute:: id

        Internal ID to be used as primary key.

    .. attribute:: volume

        The volume where this file is stored.

    .. attribute:: parent

        The parent directory.

        This may be null only for the root folder of a volume.

    .. attribute:: is_folder

        Whether this is a directory, i.e. a special file which contains other
        files and has no content on its own.

    .. attribute:: name

        The name of this file.  Must be unique among siblings of a same parent.

    .. attribute:: full_name

        The full path name relative to the root folder of the volume.

        This field is a read-only summary field. And gets automatically updated
        e.g. when the name of a parent changes.

    .. attribute:: broken

        Whether the file no longer exists on the file system.

    .. attribute:: state

        The state of this file, used to control the workflow.

        This can be one of the values in :class:`FileStates`.

Usages of a file
================

One of the main purposes of this plugin is to show where a given file is being
referred to in our database.

.. class:: UsagesByFile


.. class:: FileStates

    A choicelist with the possible states of a file.



.. class:: Receivable

    A mixin for models that require their every object to have a scan or pdf
    file of the "receipt", i.e. the document serving as the legal proof of this
    database object.  A usage example are purchase invoices in an accounting
    system.

    Receivables without such a receipt will appear in the
    :class:`PendingReceivables` table.

    .. attribute:: receipt

        The file which serves as receipt for this database object.

    .. method:: needs_receipt(self)

        Return `True` if this database object needs a receipt.

        Application developer can define rules for exempting a given database
        object from needing a receipt by overriding this method.


Updating the database from the file system
===========================================

When new files are stored to the file system, the :func:`scan_volumes`
function detects them adds a new :class:`File` object for each of them.

That function also checks whether the files found on previous scans still exist
and marks them as broken.


.. function:: scan_volumes

   Scan the file system below all volumes and create descriptors for every file
   that doesn't yet have one.  Mark file descriptors as broken if the file
   they describe does no longer exist.

   This function is automatically run by :manage:`linod`.

Navigating the files
====================

The detail of a volume shows its root folder


Assign new receipts to their receivable
=======================================


.. class:: PendingReceivables

    Shows all receivables that need a receipt but don't have any.



.. class:: BrokenFiles

    Shows all unused files (i.e. which aren't referred to by any database
    object).



Receipts folders
================

This is an idea to be discussed later. Not yet implemented.

A **receipts folder** is a folder with files that should be used as
receivables.  any file in such a folder which is not used by some
:class:`Receivable` will be mentioned in the :class:`DanglingReceipts`  table.

The local system administrator can specify a receipts folder like this::

    AccountInvoice.add_receivable_folder("luc", "/receipts", "EKR")




.. class:: DanglingReceipts

    Shows all files that are a receipt but aren't used as such by any
    receivable.


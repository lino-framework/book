.. doctest docs/specs/uploads.rst
.. _specs.uploads:

=====================================
``uploads`` : Managing uploaded files
=====================================

.. currentmodule:: lino.modlib.uploads

The :mod:`lino.modliblib.uploads` plugin adds functionality for managing
"uploads".

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.doctests')
>>> from lino.api.doctest import *



Uploads
=======

.. class:: Upload

    Django model representing an upload.

    .. attribute:: type

        The type of this upload.

        Pointer to :class:`UploadType`. The choices for this field are usually
        limited to those in the same *upload area*.

    .. attribute:: file

        Pointer to the uploaded file. See
        :attr:`lino.mixins.uploadable.Uploadable.file`


    .. attribute:: description

        A short description entered manually by the user.

    .. attribute:: description_link

        Almost the same as :attr:`description`, but if :attr:`file` is
        not empty, the text is clickable, and clicking on it opens the
        uploaded file in a new browser window.

.. class:: AreaUploads

    Mixin for tables of uploads where the *area* is known. Inherited by
    :class:`UploadsByController`.

    The summary displays the uploads related to this controller as a list grouped
    by uploads type.

    Note that this also works on
    :class:`lino_welfare.modlib.uploads.models.UploadsByClient`
    and their subclasses for the different `_upload_area`.


.. class:: MyUploads

    Shows my uploads (i.e. those whose author is the current user).

.. class:: UploadsByController

    Shows the uploads controlled by this database object.





Upload areas
============

The application developper can define **upload areas**.  Every upload area has
its list of upload types.  The default has only one upload area.

>>> rt.show(uploads.UploadAreas)
======= ========= =========
 value   name      text
------- --------- ---------
 90      general   Uploads
======= ========= =========
<BLANKLINE>

For example :ref:`welfare` extends this list.


Upload types
============

.. class:: UploadType

    The type of an upload.

    .. attribute:: shortcut

        Optional pointer to a virtual **upload shortcut** field.  If
        this is not empty, then the given shortcut field will manage
        uploads of this type.  See also :class:`Shortcuts`.

.. class:: UploadTypes

    The table with all existing upload types.

    This usually is accessible via the `Configure` menu.

UploadController
================


.. class:: UploadController


    .. method:: show_uploads(self, obj, ar=None)

        Show uploads in a grid table.

        🖿


Upload shortcuts
================

The application developper can define **upload shortcuts**.  Every upload
shortcut will create an **upload shortcut field**, a virtual field with a set
of actions for quickly uploading or viewing uploads of a particular type for a
given database object.

Usage:

- Declare your Site's upload shortcuts from within your
  :attr:`workflows_module
  <lino.core.site.Site.workflows_module>`. For example::

      from lino.modlib.uploads.choicelists import add_shortcut as add
      add('contacts.Person', 'uploaded_foos', _("Foos"))

- Using the web interface, select :menuselection:`Configure --> Office
  --> Upload types`, create an upload type named "Foo" and set its
  `shortcut` field to "Foos".




- Upload a file from your PC to the server.
- Open the uploaded file in a new browser window


.. class:: Shortcuts

    The list of upload shortcut fields which have been declared on this
    Site.

>>> rt.show(uploads.Shortcuts)
No data to display


.. function:: add_shortcut(*args, **kw)

    Declare an upload shortcut field. This is designed to be called from within
    your :attr:`workflows_module <lino.core.site.Site.workflows_module>`.

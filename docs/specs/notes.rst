.. doctest docs/specs/notes.rst
.. _specs.notes:

=====
Notes
=====

The :mod:`lino_xl.lib.niotes` plugin adds a multipurpose concept of
**notes**.

Examples in this document have been tested against the
:mod:`lino_book.projects.pierre` demo project.

>>> from lino import startup
>>> startup('lino_book.projects.pierre.settings.demo')
>>> from lino.api.doctest import *


.. contents::
   :depth: 1
   :local:

      
      

Notes
=====


.. class:: Note
      
    A **note** is a dated and timed document written by its author (a
    user). For example a report of a meeting or a phone call, or just
    some observation.  Notes are usually meant for internal use.

    .. attribute:: date
    .. attribute:: time
    .. attribute:: type
    .. attribute:: event_type
    .. attribute:: subject
    .. attribute:: body
    .. attribute:: language


Two types of type
=================

A note has two fields "note type" and "event type".

.. class:: NoteType
           
    .. attribute:: name
    .. attribute:: important
    .. attribute:: remark
    .. attribute:: special_type


.. class:: EventType
                   
    A possible choice for :attr:`Note.event_type`.

    .. attribute:: remark
    .. attribute:: body


           
.. class:: NoteTypes
.. class:: NoteTypes


Choicelists
===========
           
.. class:: SpecialTypes

    The list of special note types which have been declared on this
    Site.

           
.. class:: SpecialType

    Represents a special note type.
           

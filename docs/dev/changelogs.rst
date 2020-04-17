.. _dev.changes:

===================
Documenting changes
===================

The :file:`docs/changes` directory of a Lino application contains:

- one file per year (:file:`2019.rst`, :file:`2020.rst`) with the :term:`change log`.
- optionally one file with :term:`release notes` for each documented release
- an :file:`index.rst` file with a toctree directive.


.. glossary::

  change log

    A document that lists the changes in a given application in chronological order.

  release notes

    A document that describes the changes in given version of a given application.

.. _dev.changelogs:

Writing change logs
===================

Changes are grouped by date. Every new day gives a new heading.

There should never be more than one paragraph per change. Several related
changes should be in a same paragraph. If a change deserves more documentation,
this should be written in another place, and the change log should just link to
this place.

Every release should be mentioned. If a release has release notes, we create a
separate document and the change log will have a link to it.


.. _dev.release_notes:

Writing release notes
=====================

The :term:`application carrier` decides for every release whether
:term:`release notes` should be written, and how detailed it should be. Some
customers don't want us to write release notes, a simple email with a summary of
the changes, written by the :term:`site maintainer`, is enough for them.

Some releases are just a bugfix release, the :term:`change log` is enough in that case
because nobody wants to read a release notes page containing a single sentence.

Subheadings of a release notes document:

- Overview. The minimum to be read by the site operator's responsible contact person.

- Possible pitfalls. The first section to be read by the local support team
  after upgrading a production site.

- Requested changes. Refer to the tickets that have been fixed or that have been
  worked on.

- Changes that were not requested.  For example changes caused by changes in
  third-party technologies. Optimizations introduced by other site operators.

- Data migration notes. What has changed in the database schema.

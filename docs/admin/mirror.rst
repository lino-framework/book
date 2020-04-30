.. _hosting.mirror:

=====================
Mirroring a Lino site
=====================

To **mirror** a :term:`Lino site` means that you copy "everything" from one Lino
site to another site.  The other site might be either on the same server or on
another server.  If the other site runs a newer version of the application,
mirroring also includes :term:`data migration`. "Everything" means database
content, uploaded files, local configuration files (but the details may vary).

Mirroring is referred to in two other documents, :doc:`preview` and :doc:`move`.

.. contents::
  :local:


.. xfile:: restore2preview.py

The file :xfile:`restore2preview.py` is in the :xfile:`snapshot` of your
production project and used by the :xfile:`initdb_from_prod.sh` script.

You create this file as a copy of the :xfile:`restore.py` file.  You will modify
it as needed and maintain it until the preview site has become production.

.. xfile:: initdb_from_prod.sh

The :xfile:`initdb_from_prod.sh` script creates a snapshot of production and
then restores that snapshot to preview. It also mirrors media files from prod to
preview.

You create this file in the project root of the target site, with the following
content, and manually adapt it manually as needed:

.. literalinclude:: initdb_from_prod.sh



Troubleshooting
===============

- rsync: failed to set times on "...": Operation not permitted (1)

  rsync tries to change the timestamps of directories because that helps
  detecting changes.  But that doesn't work when the file owner is different
  from the user who runs the migration script. Because it's not allowed to
  change the timestamp of a file you don't own, even when you have write
  permission. --> That's why we use the ``--omit-dir-times`` option.

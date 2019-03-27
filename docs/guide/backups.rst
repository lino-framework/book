.. include:: /shared/include/defs.rst

=====================
Managing your backups
=====================

If your Lino application is hosted with snapshots enabled. We maintain on our
server an archive of snapshot files of the last 30 days (see
:xfile:`make_snapshot.sh`). Write documentation (in the Lino users Guide) about
how a windows user can install an automatic job which downloads their latest
snapshot.zip (or all).

Select :menuselection:`Site --> Snapshots`.

This shows a table which shows available snapshots.

- Click |insert| button to manually create a snapshot.

- On each snapshot (1) an action to download the zip file and
  (2) an action to restore this snapshot. Restoring a snapshot maybe for later.
  Needs of course a double check and confirmation.


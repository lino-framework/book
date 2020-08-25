.. _admin.snapshot:

====================================
Making a snapshot of a Lino database
====================================

Every Lino project directory created with :cmd:`getlino startsite` contains a
file named :xfile:`make_snapshot.sh`.

This script makes a **snapshot** of this Lino site, i.e. an archive
file which contains the current state of a Lino database, including:

- a Python dump made with :manage:`dump2py`
- a file :file:`requirements.txt` containing the output of :cmd:`pip freeze`
- other local files (configuration, local fixtures, uploads, etc.)
- and possibly a `mysqldump`

The snapshot file is named :file:`snapshot.zip`.  If a file
:file:`snapshot.zip` already existed before (probably from a previous
run), then the script renames that file based on its time stamp and
moves it to an **archive directory** before creating a new file.

If that *archive directory* contains any **snapshots older than 60
days**, the script removes them.  This is important because
:xfile:`make_snapshot.sh` usually also runs as a daily :doc:`cron job
<cron>`.  If we didn't take care of removing old snapshots, our server
might run out of disk space some time in a far future when we long
have forgotten that your daily job is adding a new file every day.

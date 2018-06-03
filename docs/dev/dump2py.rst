======================
What are Python dumps?
======================

A *database dump* is an image of the data in a database which you can
use e.g. to backup and restore your data.  While Django's
:manage:`dumpdata` command lets you make database dumps in *json* and
*xml* format, Lino extends this by letting you make a database dump in
*Python* format. This is what we call a **Python dump**.

To make a Python dump of your database, you simply use the
:manage:`dump2py` command.  This Django admin command creates a
directory of Python modules with one main module :xfile:`restore.py`.

Another important thing is that you can use such a backup for
:doc:`data migrations <datamig>`.



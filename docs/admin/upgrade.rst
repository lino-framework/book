.. _admin.upgrade:

=====================
Upgrading a Lino site
=====================

Generic instructions for upgrading an existing Lino site 
to a new version.


- Go to your project directory::

    $ go myproject

  See :cmd:`go` if you don't know that command.

- Stop the web server::

    $ sudo service apache2 stop

  Or whatever is appropriate on your site.
    
- Make a snapshot::
    
    $ ./make_snapshot.sh

  See :doc:`/admin/snapshot` for details.

- Update the source code::

    $ ./pull.sh

That's all if there is no change in the database structure. But if
there was (or if you don't know whether there was) some change which
requires a data migration, then you must continue:

- Activate the python environment (we usually have a shell alias
  :cmd:`a` which expands to ``. env/bin/activate``)::

    $ a

- Restore the snapshot::

    $ python manage.py run snapshot/restore.py

  If the restore fails with a traceback, this just means that there
  was a database change for which no migrator has been defined.  See
  :doc:`/dev/dump2py` for details.



.. _admin.upgrade:

=====================
Upgrading a Lino site
=====================

Generic instructions for upgrading a Lino production site to a new
version.


- Go to your project directory::

    $ go myproject

  See :cmd:`go` if you don't know that command.

- Activate the python environment (we usually have a shell alias
  :cmd:`a` which expands to ``. env/bin/activate``)::

    $ a

- Stop the web server::

    $ sudo service apache2 stop

  Or whatever is appropriate on your site.
    
- Make a snapshot of your database::
    
    $ ./make_snapshot.sh

  See :doc:`/admin/snapshot` for details.

- Update the source code::

    $ ./pull.sh

- Run the :manage:`collectstatic` command::

    $ python manage.py collectstatic

    
That's all **if there is no change in the database structure**. But if
there was (or if you don't know whether there was) some change which
requires a data migration, then you must continue:

- Restore the snapshot::

    $ python manage.py run snapshot/restore.py


Note that a :xfile:`restore.py` can take considerable time depending
on the size of your database.  So if you *believe* but are not
absolutely sure there was *no change* in the database structure, then
you can check whether you need to run :xfile:`restore.py` by doing a
second temporary snapshot and then comparing their :xfile:`restore.py`
files.  If nothing has changed, then you don't need to run it::
    
    $ python manage.py dump2py -o t
    $ diff snapshot/restore.py t/restore.py    
    

Technical background information in the Developer's Guide:
:doc:`/dev/datamig`

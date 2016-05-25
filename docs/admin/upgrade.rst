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

- Restore the snapshot::

    $ python manage.py run snapshot/restore.py

  See :manage:`dump2py` for details.

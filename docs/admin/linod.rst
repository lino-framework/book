.. _admin.linod:

=======================================
Installing :manage:`linod` as a service
=======================================

This document explains how to install :manage:`linod` as a service on
a production server.

- Install the `Supervisor <http://www.supervisord.org/index.html>`_
  package::

      $ sudo apt-get install supervisor

  The supervisor package is being installed system-wide, it is not
  related to any specific project.

- Create a file :file:`myprj_linod.conf` in
  :file:`/etc/supervisor/conf.d/` with this content::

    [program:myprj_linod]
    command=python /path/to/myprj/manage.py linod
    username = www-data

  On a server which hosts several Lino applications, we use to create
  one such file per project.

- Restart :program:`supervisord`::

    $ sudo service supervisord restart

- Have a look at the log files in :file:`/var/log/supervisord`.




.. _admin.linod:

======================================
Installing :manage:`linod` as a daemon
======================================

This document explains how to install :manage:`linod` as a daemon on a
production server.

- Install the `Supervisor <http://www.supervisord.org/index.html>`_
  package::

      $ sudo apt-get install supervisor

- Create a file :file:`myprj_linod.conf` in :file:`/etc/supervisor/conf.d/`

    [program:myprj_linod]
    command=python /path/to/myprj/manage.py linod
    username = www-data

  On a server which hosts several Lino applications, we recommend to
  create one such file per project.

- Restart :program:`supervisord`::

    $ sudo service supervisord restart

- Have a look at the log files in :file:`/var/log/supervisord`.


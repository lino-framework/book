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

- Create a shell script in your project directory::

    #!/bin/bash
    set -e  # exit on error
    cd /path/to/myprj
    . env/bin/activate
    exec python manage.py linod

  Note: the `exec
  <http://wiki.bash-hackers.org/commands/builtin/exec>`_ command is
  needed here in order to avoid :ticket:`1086`. Thanks to `Paul
  Lockaby
  <https://lists.supervisord.org/pipermail/supervisor-users/2016-July/001636.html>`_

- Create a file :file:`linod_myprj.conf` in
  :file:`/etc/supervisor/conf.d/` with this content::

    [program:linod_myprj]
    command=/path/to/myprj/linod.sh
    username = www-data

- Restart :program:`supervisord`::

    $ sudo service supervisor restart

- Have a look at the log files in :file:`/var/log/supervisor`.


.. _admin.linod:

======================================
Installing :manage:`linod` as a daemon
======================================

This document explains how to install :manage:`linod` as a daemon on a
production server.

- Install the python-daemon package::

      $ go myproject
      $ . env/bin/activate
      $ pip install python-daemon

- Create a directory :file:`/path/to/myproject/linod`.
 
  On a server which hosts several Lino applications, you must run one
  :manage:`linod` per project.

- Copy the file :srcref:`bash/run_linod.sh` to this directory and
  adapt it to your needs.  This file invokes ``python manage.py
  linod`` with the proper command-line arguments for this project.

- Copy the file :srcref:`bash/linod.sh` to your server's
  :file:`/etc/init.d` directory and adpt it to your needs.

In both files you must edit at least the content of variable
`PROJECT`.  

Don't forget to give execution permission for these scripts using
something like ``chmod 755``.

Check manually whether the script works correctly::

  $ sudo /etc/init.d/linod.sh start
  $ sudo /etc/init.d/linod.sh stop
  $ sudo /etc/init.d/linod.sh restart

And finally::

  # update-rc.d linod.sh defaults
  

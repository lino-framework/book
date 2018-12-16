.. _admin.umask:

=====================
The ``umask`` command
=====================

Before you do anything on a new production server or any machine where
the web server process runs as another user than you, we recommend to
configure your `umask` correctly.

When a process with a too restrictive umask runs some code of a
repository with Python source files, it will create `.pyc` files. And
when you later try to upgrade that repository, you get questions of
style::

  rm: remove write-protected regular file `./lino_noi/lib/noi/roles.pyc'?

The same is valid for other files created by some process: log files,
snapshots, ...

The default umask on most systems is 022, which causes any new files
created by a process to not be writable for other group members.

A umask 002 makes sure that every user running a Python process in
this environment will create new files so that they are writable for
other group members.

The umask is used to mask (disable) certain file permissions from any
new file created by a given user.  All system users on a Lino site
should have a umask `002` or `007` (not `022` or `077` as is the
default value).

How to configure umask
=======================

- Maintainers : Edit either the file :file:`~/.bashrc` of each system user or
  the file :file:`/etc/bash.bashrc` (site-wide for all users) and add the
  following line at the end::

    umask 002
 
- Apache : Add one line to your :file:`/etc/apache2/envvars` file::

    umask 002

- Supervisor :  set username = www-data in your job confiruation files

- cron : when calling a task from cron.daily the user is cron, so we must set
  umask in every process.  When calling tasks from a crontab, we can set the user
  to www-data there.


More about umask
================

The `umask` is a group of bits which specifies which permissions are
to be *masked* (not given) when a given user creates a new file.


For example an octal umask value of ``022`` (``000 010 010`` in
binary) means that the permissions "group write" and "others write"
will be masked (not set) on new files. If you change ``022`` to
``002`` (or ``007``), then the group write will be set. Here is an
illustrative table::
  
    ===== ===== ===== =====
    umask user  group other
    ===== ===== ===== =====
          R W X R W X R W X
    ----- ----- ----- -----
    022   - - - - 1 - - 1 -
    002   - - - - - - - 1 -
    007   - - - - - - 1 1 1
    ===== ===== ===== =====




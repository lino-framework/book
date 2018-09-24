.. _lino.admin.fileperm:

================
File permissions
================

Understanding what's needed
===========================

A Lino production site involves several processes running on a server.
These processes share files on the file system which they can read,
create, delete and modify.  This is why we need to care about file
permissions as soon as we are on a production site.

For example if Lino's :xfile:`lino.log` file doesn't exist, then the
running process will create a new file.

This process can be a maintainer who launches manually
e.g. :manage:`prep` or :manage:`dump2py`, it can be the Apache web
server, the :manage:`linod` daemon, a cron job like ``logrotate`` or
:xfile:`make_snapshot.sh`, ...

The files created by any such process must be writable by other users
of the `www-data` group as well.

One possible cause of problems is when the `setgid flag
<https://en.wikipedia.org/wiki/Setuid>`_ is not set on directories
which should have it.

``chmod g+s`` sets the SGID to ensure that when a new file is created
in the directory it will be group-owned by the group owning the
directory.


Discovering problems
====================

- Find files and directories which are not group-owned by www-data::

    $ find ! -group www-data

  If this produces some output, you probably want to fix it::
    
    $ find ! -group www-data -exec chgrp www-data '{}' +
    
- Show directories which don't have the `setgid flags
  <https://en.wikipedia.org/wiki/Setuid>`_ set::

    $ find -type d ! -perm /g=s

  If this produces some output, you probably want to fix it::

    $ find -type d ! -perm /g=s -exec chmod g+s '{}' +

- Show files which are not *writable* for other group members::
    
    $ find ! -perm /g=w

  If this produces some output, you probably want to fix it::

    $ find ! -perm /g=w -exec chmod g+w '{}' +

- Show files which are not *readable* for other group members::
    
    $ find ! -perm /g=r

  If this produces some output, you probably want to fix it::

    $ find ! -perm /g=r -exec chmod g+r '{}' +

- Show directories which are not *executable* for other group members::
    
    $ find -type d ! -perm /g=x
    
  If this produces some output, you probably want to fix it::

    $ sudo find -type d ! -perm /g=x -exec chmod g+x '{}' +

- Show files which are not *readable* for other group members::
    
    $ find ! -perm /g=r

  If this produces some output, you probably want to fix it::

    $ find ! -perm /g=r -exec chmod g+r '{}' +

More general diagnostics:

- Show the permissions of all directories::

    $ find -L env/repositories -type d -exec ls -ld {} + | less

- Find `.pyc` files which are not group-writable (but should)::

    $ find -name '*.pyc' ! -perm /g=w
    

Fixing problems
===============

#.  Every maintainer must be member of the `www-data` group::

        $ sudo adduser $USER www-data

    Note that `adduser` is a wrapper around the more low-level utility
    `useradd`.  If called with two non-option arguments, it will add an
    existing user to an existing group. That's what we want here.

#.  Your repositories must be group-owned by `www-data`::

        $ sudo chown -R $USER:www-data ~/repositories
    
#.  Every user, including the Apache server, must have `umask 002` or
    `007` (not the default `022` or `077`).  See :doc:`umask`.




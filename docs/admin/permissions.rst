.. _lino.admin.fileperm:

================
File permissions
================

Understanding what's needed
===========================

Lino consists of Python processes running on a server. These processes
can read, create, delete and modify files on the file system.

For example if Lino's `.log` file doesn't exist, `www-data` (the user
under which Apache is running) will create a new file, and that file
should be writable by other users of the `www-data` group.

Or the other way: if you launch manually some process which creates
files, e.g. :manage:`initdb` or :manage:`dump2py`, then the web server
(user `www-data`) must also have write access to this file.

Such problems can come when the `setgid flag
<https://en.wikipedia.org/wiki/Setuid>`_ is not set on directories
which should have it.

``chmod g+s`` sets the SGID to ensure that when a new file is created
in the directory it will inherit the group of the directory.


Discovering problems
====================

- Find files and directories which are not group-owned by www-data::

    $ find ! -group www-data    

- Show directories which don't have the `setgid flags
  <https://en.wikipedia.org/wiki/Setuid>`_ set::

    $ find -type d ! -perm /g=s

  If this produces some output, you probably want to fix it::

    $ find -type d ! -perm /g=s -exec chmod g+s '{}' +

- Show files which are not *writable* for other group members::
    
    $ find ! -perm /g=w

  If this produces some output, you probably want to fix it::

    $ find ! -perm /g=w -exec chmod g+w '{}' +

- Show directories which are not *executable* for other group members::
    
    $ find -type d ! -perm /g=x
    
  If this produces some output, you probably want to fix it::

    $ sudo find -type d ! -perm /g=x -exec chmod g+x '{}' +

- Show the permissions of all directories::    

    $ find -L env/repositories -type d -exec ls -ld {} + | less

- Find `.pyc` files which are not group-writable (but should)::

    $ find -name '*.pyc' ! -perm /g=w
   
    

Fixing problems
===============

#.  You must be member of the `www-data` group::

        $ sudo adduser $USER www-data

    Note that `adduser` is a wrapper around the more low-level utility
    `useradd`.  If called with two non-option arguments, it will add an
    existing user to an existing group. That's what we want here.

#.  Your repositories must be group-owned by `www-data`::

        $ sudo chown -R $USER:www-data ~/repositories
    
#.  Apache must use `umask 002` or `007` (not the default `022` or
    `077`).  Add one line to your :file:`/etc/apache2/envvars` file::

        umask 002




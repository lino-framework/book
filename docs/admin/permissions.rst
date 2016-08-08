.. _lino.admin.fileperm:

================
File permissions
================

The problem
===========

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

Show directories which don't have the `setgid flags
<https://en.wikipedia.org/wiki/Setuid>`_ set::

    $ find -L env -type d ! -perm /g=s

If this produces some output, you probably want to fix it::

    $ find -L env/repositories -type d ! -perm /g=s -exec chmod g+ws '{}' +
    

Show directories which are not executable for other group members::
    
    $ find -L env -type d ! -perm /g=x

Show the permissions of all directories::    

    $ find -L env/repositories -type d -exec ls -ld {} + | less

Find `.pyc` files which are not group-writable::

    $ find -L env/local/lib/python2.7/site-packages -name '*.pyc' ! -perm /g=w
    $ find -L env/repositories/ -name '*.pyc' ! -perm /g=w
   
    

Fixing problems
===============
    
You'll probably need to add `umask 002` to your
`/etc/apache2/envvars`.

You'll maybe have to do something like this::

  $ sudo addgroup myusername www-data
  

Set up Mercurial
================

Add in your `/etc/mercurial/hgrc`::

  [trusted]
  groups = www-data



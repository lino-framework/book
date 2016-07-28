.. _admin.virtualenv:

==================
Using `virtualenv`
==================

When you create a new virtual environment on a production server or
any machine where the Web server process runs as another user than
you, we recommend to add the following line to the :xfile:`activate`
script::

  umask 002  # make new files writable for other group members

Without above trick you would need to set the umask individually for
all candiates: Apache, Supervisor, and the login shells of all users.

When a process with a too restrictive umask runs some code of a
repository with Python source files, it will create `.pyc` files. And
when you later try to upgrade that repository, you get questions of
style::

  rm: remove write-protected regular file `./lino_noi/lib/noi/roles.pyc'?

The same is valid for other files created by some process: log files,
snapshots, ...

The default umask on most systems is 022, which causes any new files
created by a process to not be writable for other group members.  

A umaks 002 makes sure that every user running a Python process in
this environment will create new files so that they are writable for
other group members.

The `umask` is a group of bits which specifies which permissions are
to be *masked* (not given) when creating new files. 

Examples::

    ===== ===== ===== =====
    umask user  group other
    ===== ===== ===== =====
          R W X R W X R W X
    ----- ----- ----- -----
    022   - - - - 1 - - 1 -
    002   - - - - - - - 1 -
    007   - - - - - - 1 1 1
    ===== ===== ===== =====


.. _admin.virtualenv:

==================
Using `virtualenv`
==================

When you create a new virtual environment on a production server or
any machine where the Web server process runs as another user than
you, we recommend to add the following line to the :xfile:`activate`
script::

  umask 0007  # make new files writable for other group members

This makes sure that every user running a Python process in this
environment will create new files so that they are writable for other
group members.

The default umask causes any new files created by a process to not be
writable for other group members. When such a process runs some code
of a repository with Python source files, it will create `.pyc`
files. And when you later try to upgrade that repository, you get
questions of style::

  rm: remove write-protected regular file `./lino_noi/lib/noi/roles.pyc'?

Without above trick you would need to set the umask individually for
all candiates: Apache, Supervisor, and the login shells of all users.


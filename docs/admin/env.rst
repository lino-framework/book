.. _lino.admin.env:

===================================
Organizing your Python environments
===================================

When your server is going to host several production sites, then it is
likely that every project needs its own Python environment. This
differs from what we said in :ref:`lino.dev.env`.

You will then create a new environment for every project and store it
below the project directory.  We recommend to always use the same
name, e.g. :xfile:`env`.


The :xfile:`env` directory
==========================

.. xfile:: env

By convention, on a production server hosting several projects, every
project directory has a subdirectory :xfile:`env` which contains the
Python environment used by that project.

Such a convention allows you for example to create an alias command
like the following in your :xfile:`.bash_aliases` file::

  alias a='. env/bin/activate'

Also the bash script templates in :srcref:`bash` are based on this
convention.

Shared environments
===================

OTOH every environment takes approximately 300 MB of disk space. So on
a server with many production projects you might consider the
possibility to offer **shared environments**. For example you would
offer three environments `old`, `stable` and `testing`::

        $ virtualenv ~/virtualenvs/old
        $ virtualenv ~/virtualenvs/stable
        $ virtualenv ~/virtualenvs/testing

And then the :xfile:`env` of your projects would be a symbolic link to
one of these environments.

When you use shared environments and update one of them, then you must
of course migrate every project database which use that environment.


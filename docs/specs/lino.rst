.. doctest docs/specs/lino.rst
.. include:: /../docs/shared/include/defs.rst
.. _specs.lino:

==================================
``lino`` : Lino core functionality
==================================

The :mod:`lino` package is automatically installed as a plugin on every
:term:`Lino site`. It adds no database models, but a series of admin commands as
well as the translations for messages of the :mod:`lino` package.


.. currentmodule:: lino


.. contents::
   :depth: 1
   :local:


.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.min1.settings.doctests')
>>> from atelier.sheller import Sheller
>>> shell = Sheller()

.. _specs.lino.admin_commands:

Django admin commands added by the ``lino`` plugin
==================================================

The source code of these commands is in the :mod:`lino.management.commands`
package.


Useful commands
---------------

.. management_command:: linod

Run a Lino daemon for this :term:`site <Lino site>`. See :doc:`/admin/linod`.

.. management_command:: run

Run a Python script within the Django environment for this site.

>>> shell("django-admin run --help")  #doctest: +NORMALIZE_WHITESPACE
usage: django-admin run [-h] [--version] [-v {0,1,2,3}] [--settings SETTINGS] [--pythonpath PYTHONPATH] [--traceback] [--no-color] [--force-color] ...
<BLANKLINE>
Run a Python script within the Django environment for this site.
<BLANKLINE>
positional arguments:
  filename              The script to run.
<BLANKLINE>
optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output
  --settings SETTINGS   The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the DJANGO_SETTINGS_MODULE environment variable will be used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
  --force-color         Force colorization of the command output.


``manage.py run myscript.py`` is almost the same as redirecting stdin
of Django's ``shell`` command (i.e. doing ``manage.py shell <
myscript.py``), but with the possibility of using **command line
arguments**.

For example if you have a file `myscript.py` with the following content...

::

  import sys
  from myapp.models import Partner
  print(Partner.objects.get(pk=sys.args[1]))

... then you can run this script using::

    $ python manage.py run myscript.py 101
    Bäckerei Ausdemwald

This command modifies `sys.args`, `__file__` and `__name__` so that
the invoked script sees them as if it had been called directly.

It is similar to the `runscript
<http://django-extensions.readthedocs.org/en/latest/runscript.html>`_
command which comes with `django-extensions
<http://django-extensions.readthedocs.org/en/latest/index.html>`__.

This is yet another answer to the frequently asked Django question
about how to run standalone Django scripts
(`[1] <http://stackoverflow.com/questions/4847469/use-django-from-python-manage-py-shell-to-python-script>`__,
`[2] <http://www.b-list.org/weblog/2007/sep/22/standalone-django-scripts/>`__).


.. management_command:: install

Run 'pip install --upgrade' for all Python packages required by this site.

>>> shell("django-admin install --help")  #doctest: +NORMALIZE_WHITESPACE
usage: django-admin install [-h] [--noinput] [-l] [--version] [-v {0,1,2,3}] [--settings SETTINGS] [--pythonpath PYTHONPATH] [--traceback] [--no-color] [--force-color]
<BLANKLINE>
Run 'pip install --upgrade' for all Python packages required by this site.
<BLANKLINE>
optional arguments:
  -h, --help            show this help message and exit
  --noinput             Do not prompt for input of any kind.
  -l, --list            Just list the requirements, don't install them.
  --version             show program's version number and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output
  --settings SETTINGS   The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the DJANGO_SETTINGS_MODULE environment variable will be used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
  --force-color         Force colorization of the command output.


.. management_command:: prep

  Flush the database and load the default demo fixtures.

Calls :manage:`initdb` using the site's
:attr:`lino.core.site.Site.demo_fixtures`.

Introduction see :ref:`lino.tutorial.hello`.

.. management_command:: initdb

  Flush the database and load the specified fixtures.

See the page about :manage:`initdb` in the Developer's Guide.

The command performs three actions in one:

- it flushes the database specified in your :xfile:`settings.py`,
  i.e. issues a ``DROP TABLE`` for every table used by your application.

- it runs Django's :manage:`migrate` command to re-create all tables,

- it runs Django's :manage:`loaddata` command to load the specified
  fixtures.

This also adds a `warning filter
<https://docs.python.org/2/library/warnings.html#warning-filter>`__ to
ignore Django's warnings about empty fixtures. (See
:djangoticket:`18213`).

This reimplements a simplified version of Django's `reset` command,
without the possibility of deleting *only some* data (the thing which
caused so big problems that Django 1.3. decided to `deprecate this
command <https://docs.djangoproject.com/en/3.1/releases/1.3\
/#reset-and-sqlreset-management-commands>`__.

Deleting all data and table definitions from a database is not always
trivial. It is not tested on PostgreSQL. In MySQL we use a somewhat
hackerish and MySQL-specific DROP DATABASE and CREATE DATABASE because
even with `constraint_checks_disabled` we had sporadic errors. See
:blogref:`20150328`

Note that Lino does not use Django's migration framework, so
:manage:`initdb` runs Django's `migrate` command with the
`--run-syncdb
<https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-option---run-syncdb>`_
option which "allows creating tables for apps without
migrations".
The Django docs add that "While this isn’t recommended, the
migrations framework is sometimes too slow on large projects with
hundreds of models."  Yes, we go the way which is not recommended.

.. management_command:: dump2py

  Write a Python dump of this site. See :doc:`/dev/dump2py`.

.. management_command:: qtclient

Run a Qt client for this :term:`site <Lino site>`.  See :doc:`/dev/qtclient`.

.. management_command:: diag

  Write a diagnostic status report about this site.

This is a command-line shortcut for calling
:meth:`lino.core.site.Site.diagnostic_report_rst`.

This is deprecated. You should use :manage:`status` instead.

.. management_command:: show

  Show the content of a specified table to standard output.

.. management_command:: resetsequences

Reset the database sequences for all plugins.

This is required (and automatically called) on a postgres after
restoring from a snapshot (:xfile:`restore.py`) because this operation
specifies explicit primary keys.

Unlike Django's :manage:`sqlsequencereset` command this does not just
output the SQL statements, it also executes them.  And it works always
on all plugins so you don't need to specify their names.

This is functionally equivalent to the following::

  python manage.py sqlsequencereset APP1 APP2... | python manage.py shell

On SQLite or MySQL this command does nothing.

In PostgreSQL, Sequence objects are special single-row tables created
with CREATE SEQUENCE. Sequence objects are commonly used to generate
unique identifiers for rows of a table (exceprt from `PostgreSQL docs
<https://www.postgresql.org/docs/current/static/functions-sequence.html>`__).

See :blogref:`20170907`, :blogref:`20170930`.


.. management_command:: makemigdump

Create a dump for migration tests.

Calls :manage:`dump2py` to create python dump in a
`tests/dumps/<version>` directory. See :doc:`/dev/migtests`


Experimental commands
---------------------

.. management_command:: mergedata

Takes the full name of a python module as argument. It then imports
this module and expects it to define a function `objects` in its
global namespace. It calls this function and expects it to yield a
series of Django instance objects which have not yet been saved. It
then compares these objects with the "corresponding data" in the
database and prints a summary to stdout. It then suggests to merge the
new data into the database.

- It never *deletes* any stored records.
- All incoming objects either replace an existing (stored) object, or
  will be added to the database.
- If an incoming object has a non-empty primary key, then it replaces
  the corresponding stored object. Otherwise, if the model has
  `unique` fields, then these cause potential replacement.

Currently the command is only partly implemented, it doesn't yet
update existing records.  But it detects whether records are new, and
adds only those.

.. management_command:: monitor

  Experimental work. Don't use this.
  Writes a status report about this Site.
  Used to monitor a production database.


Historical commands
-------------------


.. management_command:: configure

    Old name for :manage:`install`.


.. management_command:: initdb_demo

    Old name for :manage:`prep`.

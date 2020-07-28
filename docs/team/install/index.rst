.. _getlino.install.contrib:
.. _contrib.install:

=========================================
Setting up a Lino contributor environment
=========================================

We assume that you have :doc:`installed a developer environment
</dev/install/index>` and now want to convert it into a :term:`contributor
environment`.

The main new thing as a contributor is that you have a local clone of each Lino
code repository because you are going to do local modifications and submit pull
requests.  Getlino does the tedious work of cloning and installing them as
editable (with `pip install -e`) into your virtualenv.

Run getlino to clone Lino repositories
======================================

We are going to throw away your developer virtualenv
and replace it by a new one.

.. code-block:: console

  $ mv ~/lino/env ~/lino/old_env
  $ python3 -m venv ~/lino/env
  $ source ~/lino/env/bin/activate
  $ pip install -U pip setuptools

Note that after moving a virtualenv to another directory you cannot use it
anymore. Python virtualenvs are not designed to support renaming.  But you may
rename it back to its old name in case you want to go back.

You are now in a new virgin Python virtualenv.  You can say :cmd:`pip freeze` to
verify.

Note that this virgin virtualenv is now your :ref:`default virtualenv
<dev.default_venv>`.

In case you have used getlino on your machine before (maybe another virtualenv,
but the same machine), then you might want to delete your configuration file
before going on::

  rm ~/.getlino.conf

Run :cmd:`getlino` with the following options:

.. code-block:: console

  $ getlino configure --clone --devtools --redis

For details see the documentation about :ref:`getlino`.

Try one of the demo projects:

.. code-block:: console

  $ cd ~/lino/env/repositories/book/lino_book/projects/team
  $ python manage.py prep
  $ python manage.py runserver

Point your browser to http://localhost:8000

You can now ``cd`` to any subdir of :mod:`lino_book.projects` and run a
development server.  Before starting a development server on a project for the
first time, you must initialize its database using the :manage:`prep` command.

You can run the :manage:`prep` command for all demo projects by going to the
root directory of the book project and saying :cmd:`inv prep`:

.. code-block:: console

Note the difference between :cmd:`inv prep` and the :manage:`prep` command.
:cmd:`inv prep` runs the :manage:`prep` command for each demo project of a
repository.  The demo projects of a repository are declared in the
:xfile:`tasks.py` file.

Exercises
=========

#.  Sign in and play around.

#.  Create some persons and organizations. Don't enter lots of data
    because we are going to throw it away soon.

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

.. highlight:: console


Run getlino to clone Lino repositories
======================================

We are going to throw away your developer virtualenv
and replace it by a new one::

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

  $ rm ~/.getlino.conf
  $ sudo rm /etc/getlino/getlino.conf

Run :cmd:`getlino` with the following options::

  $ getlino configure --clone --devtools --redis

.. For details see the documentation about :ref:`getlino`.

It will say "The following command was not executed because you cannot sudo",
followed by an "apt-get install" command.

Add manually the following line to your :xfile:`.bashrc` file::

  source ~/.lino_bash_aliases

This will also install the :ref:`Lino Book <book>` project.  That's a special
project.  It is not an application, and it is not released on PyPI. It makes
sense only for contributors.  It contains the main test suite for Lino. It
contains a lot of demo projects.  Some of these  demo projects require
additional Python packages. The easiest way to get them installed all at once is
to say::

  $ cd ~/lino/env/repositories/book
  $ pip install -r requirements-include.txt

You can now ``cd`` to any subdir of :mod:`lino_book.projects` and run a
development server.  Before starting a development server on a project for the
first time, you must initialize its database using the :manage:`prep` command.

Try one of the demo projects::

  $ cd ~/lino/env/repositories/book/lino_book/projects/team
  $ python manage.py prep
  $ python manage.py runserver

Point your browser to http://localhost:8000

You can run the :manage:`prep` command for all demo projects by going to the
root directory of the book project and saying :cmd:`inv prep`::

  $ cd ~/lino/env/repositories/book
  $ inv prep

Note the difference between :cmd:`inv prep` and the :manage:`prep` command.
:cmd:`inv prep` runs the :manage:`prep` command for each demo project of a
repository.  The demo projects of a repository are declared in the
:xfile:`tasks.py` file.

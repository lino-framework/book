.. _lino.dev.install:
.. _dev.install:

===============
Installing Lino
===============

.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _fabric: http://www.fabfile.org/
.. _invoke: http://www.pyinvoke.org/
.. _pycrypto: https://pypi.python.org/pypi/pycrypto
.. _atelier: http://atelier.lino-framework.org/
.. _git: http://git-scm.com/downloads
.. _lxml: http://lxml.de/

This document describes how to install Lino.  

It assumes you are familiar with the Linux shell at least
for basic file operations like :cmd:`ls`, :cmd:`cp`, :cmd:`mkdir`,
:cmd:`rmdir`, file permissions, environment variables, bash scripts
etc.  Otherwise we suggest to learn about :ref:`Working in a UNIX shell <learning.unix>`.

.. contents::
    :depth: 1
    :local:


System requirements
===================

#.  Lino theoretically works under **Python 3**, but we currently
    still recommend **Python 2**.  If you just want it to work, then
    choose Python 2. Otherwise consider giving it a try under Python 3
    and report your experiences.

#.  We assume you have pip_ installed. `pip` is not automatically
    bundled with Python 2, but it has become the de-facto standard.

#.  You will need to install git_ on your computer to get the source
    files.

#.  Lino requires lxml_, which has some extra requirements before you
    can install it with pip_::

      $ sudo apt-get build-dep lxml

#.  Similar requirement for applications which use
    :mod:`lino.modlib.weasyprint`::

      $ sudo apt-get install libffi-dev



Get the sources
===============

You might theoretically install Lino using ``pip install lino``, but
this method isn't currently being tested very thoroughly. So in most
cases we currently recommend to use the development version because
you will probably want to use Lino's newest features before they get
officially released on PyPI.

Create a directory (e.g. :file:`~/repositories`) meant to hold your
working copies of version-controlled software projects, `cd` to that
directory and and do::

  $ mkdir ~/repositories
  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/lino.git
  $ git clone https://github.com/lino-framework/xl.git
  $ git clone https://github.com/lino-framework/book.git

You should now have three directories called `~/repositories/lino`,
`~/repositories/xl` and `~/repositories/book`, each of which contains
a file :xfile:`setup.py`, a file :xfile:`README.rst` and a whole tree
of other files and directories.

One possible problem here is that the Lino repository has a big
size. If you just want to try out the latest version and will never
submit any pull request, then you can reduce this from 300MB to to
63MB by adding ``--depth 1`` option (as explained in `this question on
stackoverflow
<http://stackoverflow.com/questions/1209999/using-git-to-get-just-the-latest-revision>`__
or Nicola Paolucci's blog entry `How to handle big repositories with
git
<http://blogs.atlassian.com/2014/05/handle-big-repositories-git/>`_).

.. _lino.dev.env:


Set up a Python environment
===========================

Before we actually install Lino into your Python, let's speak about
*Python environments*.  We recommend to use virtualenv_ and to create
a new Python environment for getting started with Lino.

On a Debian system this means something like::

        $ sudo pip install virtualenv
        $ mkdir ~/virtualenvs
        $ virtualenv ~/virtualenvs/a

To activate this environment, you will type::

        $ . ~/virtualenvs/a/bin/activate

You might add above line to your :xfile:`.bashrc` file if you
currently don't plan to work on any other project which requires a
different environment.

We chose ``a`` as name for this environment. You might prefer
``lino``, ``dev`` or ``my_first_environment``.

You might prefer to create a new environment for every project and
store it below your project directory (see below `Project
directories`_).  This makes sense on a production server (more about
this in :ref:`lino.admin.env`.), but on a developer machine it is
usually not necessary and would be a waste of disk space.

Installation
============

Now you are ready to "install" Lino, i.e. to tell your Python
interpreter where the source file are, so that you can import them
from within any Python program.

Commands::

  $ pip install -e lino
  $ pip install -e xl
  $ pip install -e book

These commands take some time because they will download and install
all Python packages needed by Lino.

Notes:

- The `-e
  <https://pip.pypa.io/en/latest/reference/pip_install.html#cmdoption-e>`_
  command-line switch for :command:`pip` causes it to use the "development"
  mode.  Development mode means that these modules run "directly from
  source".  `pip` does not *copy* the sources to your Python
  `site_packages`, but instead adds a link to them.  The first
  argument after ``-e`` is not a *project name* but a *directory*.

- Alternatively (without pip_) you could have done::

      $ cd lino ; python setup.py develop ; cd ..


Telling your Lino version
=========================

A quick test when you want to see whether Lino is installed is to say
"hello" to Lino:

.. py2rst::

   self.shell_block(["python", "-m", "lino.hello"])

In case you didn't know: Python's `-m
<https://docs.python.org/2/using/cmdline.html#cmdoption-m>`_
command-line switch instructs it to just *import* the specified module
(here :mod:`lino.hello`) and then to return to the command line.

.. _dev.git_pull:

Updating your copy of the Lino sources
======================================

Actually the Lino version is not enough when using a developer
installation of Lino.  The Lino codebase repository changes almost
every day, but the version is incremented only when we do an official
release to PyPI.

As a developer you will simply update your copy of the code repository
often. In order to get the latest version, you need to run::

  $ cd ~/repositories/lino ; git pull 
  $ cd ~/repositories/xl ; git pull 
  $ cd ~/repositories/book ; git pull 
  $ find ~/repositories -name '*.pyc' -delete

Note that you **don't need to reinstall** the packages in Python after
such an upgrade since you used the ``-e`` option of `pip install`
above. The new versions will automatically become active.

See the documentation of `git pull
<https://git-scm.com/docs/git-pull>`_ for more information.

The last line runs :cmd:`find` in order to remove all :file:`.pyc`
(compiled Python) files. See e.g. `here
<http://stackoverflow.com/questions/785519/how-do-i-remove-all-pyc-files-from-a-project>`_
for other methods.  This is not necessary most of the time because
Python automatically recompiles them when needed, but there are
situations where you get problems caused by dangling :file:`.pyc`
files.


Project directories
===================

You are going to write more than only one Lino applications, aren't
you? 

Every project has its own **project directory** which contains the
files necessary for that specific project.  In this chapter we are
going to use some of the projects defined in the Lino Book, and we are
going to use them directly from within the code repository.

You will create your first project directory of your own in the next
chapter (:doc:`/tutorials/hello/index`).


Defining a cache directory for Lino
===================================

Before going on, you should prepare a place where Lino can store
temporary files like the SQLite database file, static files and
dynamically generated files of miscellaneous types like `.js`, `.pdf`,
`.xls`.

You do this by creating an empty directory where you have write
permission, and then set the :envvar:`LINO_CACHE_ROOT` environment
variable to point to it.

The safest place for this directory is below your virtual
environment::

  $ cd ~/virtualenvs/a
  $ mkdir lino_cache

And then to add the following line to your
:file:`~/virtualenvs/a/bin/activate` script::

   export LINO_CACHE_ROOT=$VIRTUAL_ENV/lino_cache

Don't forget to re-run the script in order to activate these changes.
You can verify whether the variable is set using this command::

    $ set | grep LINO

More about this in :doc:`cache`.


Initialize the demo databases
=============================

We are now ready to initialize the **demo databases**.  The easiest
way to do this is to run the :cmd:`inv initdb` command::

    $ cd ~/repositories/book
    $ inv initdb

The ``inv`` command has been installed on your system (more precisely:
into your Python environment) by the invoke_ package, which itself has
been required by atelier_, which is another Python package developed
by Luc.

The ``inv`` command is a kind of make tool which works by looking for
a file named :xfile:`invoke.yaml`. The Lino repository contains such a
file, and this file uses :mod:`atelier.fablib`, which defines a whole
series of tasks like `initdb` and `test`.



Running your first Lino site
============================

You can now ``cd`` to any subdir of :mod:`lino_book.projects` and run
a development server ::

  
    $ cd lino_book/projects/min1
    $ python manage.py runserver

Now start your browser, point it to http://127.0.0.1:8000/ and play
around.

Don't stay in :mod:`min1 <lino_book.projects.min1>`, Also try
:mod:`min2 <lino_book.projects.min2>`, :mod:`min2
<lino_book.projects.polly>` etc...


Run Lino's test suite
=====================

In order to check whether everything worked well, we are now going to
run the test suite.

Make sure that your demo databases are initialized and that you did
not do any manual changes therein.  Because the test suite has many
test cases which would fail if these demo databases were missing or
not in their virgin state.  In case you *did* write into some database
during the previous section, just run :cmd:`inv initdb` once more.

And here we go for the test suite itself::

    $ inv test

The :cmd:`inv test` command is a short for ``python setup.py test``
which simply runs the test suite.  The output should be something like
this::

    [localhost] local: python setup.py -q test
    .....................................................................
    ----------------------------------------------------------------------
    Ran 74 tests in 52.712s
    OK
    Done.


Congratulations if you got the test suite to pass!  As your next step,
we now suggest to :doc:`/tutorials/hello/index`.


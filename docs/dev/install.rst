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
    bundled with Python 2, but it has become the de-facto
    standard. Here is how to install it on Debian::

      $ sudo apt-get install python-pip

#.  You will need to install git_ on your computer to get the source
    files::
      
      $ sudo apt-get install git

#.  Lino requires lxml_, which has some extra requirements before you
    can install it with pip_::

      $ sudo apt-get build-dep lxml

    Note: if you get an error message :message:`You must put some
    'source' URIs in your sources.list`, then (in Ubuntu) open
    :menuselection:`System Settings --> Software & Updates` and make
    sure that :guilabel:`Source code` is checked.

#.  Similar requirement for applications which use
    :mod:`lino.modlib.weasyprint`::

      $ sudo apt-get install libffi-dev



Set up a Python environment
===========================

Before you actually install Lino into your Python, we recommend to
create a new Python environment using virtualenv_.  On a Debian system
this means something like::

        $ sudo pip install virtualenv
        $ mkdir ~/virtualenvs
        $ virtualenv ~/virtualenvs/a

Note that we chose ``a`` as name for this environment. You might
prefer ``lino``, ``dev`` or ``my_first_environment``.

To activate this environment, you will type::

        $ . ~/virtualenvs/a/bin/activate

In a normal situation, all your Lino projects can use the same virtual
environment.  So you might add above line to your :xfile:`.bashrc`
file if you currently don't plan to work on any other project which
requires a different environment.

Get the sources
===============

You might theoretically install Lino using ``pip install lino``, but
this method isn't currently being tested very thoroughly. So in most
cases we currently recommend to use the development version because
you will probably want to use Lino's newest features before they get
released on PyPI.

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
a file :xfile:`setup.py` and a whole tree of other files and
directories.

One possible problem here is that the Lino repository has a big size.
If you just want to try out the latest version and will never submit
any pull request, then you can reduce this from 300MB to to 63MB by
adding ``--depth 1`` option (as explained in `this question on
stackoverflow
<http://stackoverflow.com/questions/1209999/using-git-to-get-just-the-latest-revision>`__
or Nicola Paolucci's blog entry `How to handle big repositories with
git
<http://blogs.atlassian.com/2014/05/handle-big-repositories-git/>`_).

.. _lino.dev.env:


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

Note that the `-e
<https://pip.pypa.io/en/latest/reference/pip_install.html#cmdoption-e>`_
command-line switch for :command:`pip` causes it to use the
"development" mode.  Development mode means that these modules run
"directly from source".  `pip` does not *copy* the sources to your
Python `site_packages`, but instead adds a link to them.  The first
argument after ``-e`` is not a *project name* but a *directory*.



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

To be honest, the Lino version number is not enough when using a
developer installation of Lino.  The Lino codebase repository changes
almost every day, while the version is incremented only when we do an
official release to PyPI.

So as a developer you will simply upgrade your copy of the code
repositories often.  Here is a quick series of commands for getting
the latest version::

  $ cd ~/repositories/lino ; git pull 
  $ cd ~/repositories/xl ; git pull 
  $ cd ~/repositories/book ; git pull 
  $ find ~/repositories -name '*.pyc' -delete

This process is fully described in :doc:`pull`.


Initialize the demo databases
=============================

The Lino Book contains a series of demo projects, each of which has
its own database. These databases need to be initialized before you
can use these projects.

The easiest way to do this is to run the :cmd:`inv initdb` command
from within your copy of the :ref:`book` repository::

    $ cd ~/repositories/book
    $ inv initdb

The ``inv`` command has been installed on your system (more precisely:
into your Python environment) by the invoke_ package, which itself has
been required by atelier_, which is another Python package developed
by Luc.

The ``inv`` command is a kind of make tool which works by looking for
a file named :xfile:`tasks.py`. The Lino repository contains such a
file, and this file uses :mod:`lino.invlib`, which (together with
:mod:`atelier.invlib` from which it inherits) defines a whole series
of commands like :cmd:`inv initdb` or :cmd:`inv test`.



Running your first Lino site
============================

You can now ``cd`` to any subdir of :mod:`lino_book.projects` and run
a development server::

  
    $ cd lino_book/projects/min1
    $ python manage.py runserver

Now start your browser, point it to http://127.0.0.1:8000/ and play
around.

Don't stay in :mod:`min1 <lino_book.projects.min1>`, also try the
other projects below :mod:`lino_book.projects`. None of them is a
"killer app", they are just little projects used for testing and
playing.



Where to go from here
=====================

As your next step, we now suggest to :doc:`/tutorials/hello/index`.


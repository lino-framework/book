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
.. _Debian: http://www.debian.org/

This document describes how to install Lino.  It is written for
Debian_ and derivated distributions, other Linuxes should be pretty
similar.

It assumes you are familiar with the Linux shell at least for basic
file operations like :cmd:`ls`, :cmd:`cp`, :cmd:`mkdir`, :cmd:`rmdir`,
file permissions, environment variables, bash scripts etc.  Otherwise
we suggest to learn about :ref:`Working in a UNIX shell
<learning.unix>`.


.. contents::
    :depth: 1
    :local:


System requirements
===================

#.  Lino theoretically works under **Python 3**, but we currently
    still recommend **Python 2**.  If you just want it to work, then
    choose Python 2. Otherwise consider giving it a try under Python 3
    and report your experiences.

#.  You need at least 500MB of RAM.  How to see how much memory you
    have::

        $ free -h

#.  We assume you have virtualenv_ and pip_ installed. See the next
    section.

#.  You will need to install git_ on your computer to get the source
    files::
      
      $ sudo apt-get install git

#.  There are Python C extensions among Lino's dependencies::

      $ sudo apt-get install python-dev

#.  Many Lino applications require lxml_, which has some extra
    requirements::

      $ sudo apt-get build-dep lxml

    Note: if you get an error message :message:`You must put some
    'source' URIs in your sources.list`, then (in Ubuntu) open
    :menuselection:`System Settings --> Software & Updates` and make
    sure that :guilabel:`Source code` is checked. Or (on the command
    line) edit your :file:`/etc/apt/sources.list` file::

        $ sudo nano /etc/apt/sources.list
        $ sudo apt-get update

#.  Similar requirement for applications which use
    :mod:`lino.modlib.weasyprint`::

      $ sudo apt-get build-dep cairocffi
      $ sudo apt-get install libffi-dev libssl-dev

#.  For applications which use :mod:`lino.utils.html2xhtml`::

      $ sudo apt-get install tidy


.. _lino.dev.env:

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
  $ git clone https://github.com/lino-framework/noi.git
  $ git clone https://github.com/lino-framework/book.git


Since June 2017 Lino requires a forked version of Django 1.11.
Once our patch is accepted by the Django Team we will switch back to
using the original sources::

  $ git clone --depth 1 -b ticket_20313 https://github.com/lsaffre/django.git


You should now have five directories called `~/repositories/lino`,
`~/repositories/xl`, `~/repositories/django`, `~/repositories/noi` and `~/repositories/book`,
each of which contains a file :xfile:`setup.py` and a whole tree of
other files and directories.

One possible problem here is that some repositories might have a big
size.  If you just want to get the latest version and don't plan to
submit any pull requests, then you can reduce download size by adding
``--depth 1`` and ``-b master`` options::

  $ git clone --depth 1 -b master https://...

(as explained in `this question on stackoverflow
<http://stackoverflow.com/questions/1209999/using-git-to-get-just-the-latest-revision>`__
or Nicola Paolucci's blog entry `How to handle big repositories with
git
<http://blogs.atlassian.com/2014/05/handle-big-repositories-git/>`_).


Set up a Python environment
===========================

Before you actually install the Lino sources into your system Python environment, we recommend to
create a new Python environment using virtualenv_.

If you have never used virtual environments before, then on a Debian
system you will do something like::

        $ sudo apt-get install virtualenv
        $ mkdir ~/virtualenvs
        $ # Here is how to create a new virgin python environment
        $ virtualenv --python=python2 ~/virtualenvs/a
        $ # To *activate* this environment, you will type::
        $ . ~/virtualenvs/a/bin/activate
        $ # Then update pip and setuptools to the latest version
        $ pip install -U pip
        $ pip install -U setuptools


The reason for creating a new environment is to separate Lino from your system install of python. The main advantages
are; if you are also developing other things with python you will require different packages then what lino-uses.
Also if you wish to remove Lino from your system you only need to remove the source files and the virtualenv. Rather
than trying to remove lino's dependencies from the system environment without breaking any other programs that use
python.


If you know that you are only going to be using python with lino.
You probably want to add above line to your :xfile:`.bashrc` file.
This will activate the lino environment whenever you open a bash shell::

    $ echo ". ~/virtualenvs/a/bin/activate" >> ~/.bashrc

Otherwise if you want a quick way to activate your lino python environment you can add an alias to your :xfile:`.bashrc` file::

    $ echo "alias lpy='.  ~/virtualenvs/a/bin/activate" >> ~/.bashrc
    $ . ~/.bashrc # To run the new alias
    $ lpy # Activates the environment
         
.. rubric:: Notes

We chose ``a`` as name for this environment. You might prefer
``lino``, ``dev`` or ``my_first_environment``.

If virtualenvs are new to you, then read Dan Poirier's post
`Managing multiple Python projects: Virtual environments
<https://www.caktusgroup.com/blog/2016/11/03/managing-multiple-python-projects-virtual-environments/>`__
where he explains what they are and why you want them.

The dot (``.``) is a synonym for the :cmd:`source` command. If you
didn't know it, read the `manpage
<http://ss64.com/bash/source.html>`__ and `What does 'source' do?
<http://superuser.com/questions/46139/what-does-source-do>`__

You can **deactivate** a virtual environment with the command
:cmd:`deactivate`. This switches you back to your machine's
system-wide environment.

You can **switch to another** virtualenv simply by activating it, you
don't need to deactivate the current one first.

You should never **rename** a virtualenv (they are not designed for
that), but you can easily create a new one and remove the old one.


Installation
============

Now you are ready to "install" Lino, i.e. to tell your Python
interpreter where the source file are, so that you can import them
from within any Python program.

Commands::

  $ cd ~/repositories
  $ pip install -e django/
  $ pip install -e lino/
  $ pip install -e xl/
  $ pip install -e noi/
  $ pip install -e book/

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


Upgrading the sources
=====================

Actually the Lino version number is not enough when using a developer
installation of Lino.  The Lino codebase repository changes almost
every day, while the version is incremented only when we do an
official release to PyPI.

So as a developer you will simply upgrade your copy of the code
repositories often.  Here is a quick series of commands for getting
the latest version::

  $ cd ~/repositories/lino ; git pull 
  $ cd ~/repositories/xl ; git pull 
  $ cd ~/repositories/noi ; git pull
  $ cd ~/repositories/book ; git pull 
  $ find ~/repositories -name '*.pyc' -delete

This process is fully described in :doc:`pull`.

Troubleshooting
===============

Using virtual environments seems to be one of the biggest challenges
for newbies. Here are some diagnostic tricks.

How to see which is your current virtualenv::

    $ echo $VIRTUAL_ENV
    /home/luc/virtualenvs/a

    $ which python
    /home/luc/virtualenvs/a/bin/python

How to see what's installed in your current virtualenv::

    $ pip freeze

The output will be about 60 lines of text, here is an excerpt::
  
    alabaster==0.7.9
    appy==0.9.4
    argh==0.26.2
    ...
    Django==1.9.10
    ...
    future==0.15.2
    ...
    -e git+git+ssh://git@github.com/lino-framework/lino.git@91c28245c970210474e2cc29ab2223fa4cf49c4d#egg=lino
    -e git+git+ssh://git@github.com/lino-framework/book.git@e1ce69aaa712956cf462498aa768d2a0c93ba5ec#egg=lino_book
    -e git+git+ssh://git@github.com/lino-framework/noi.git@2e56f2d07a940a42e563cfb8db4fa7444d073e7b#egg=lino_noi
    -e git+git@github.com:lino-framework/xl.git@db3875a6f7d449490537d68b08daf471a7f0e573#egg=lino_xl
    lxml==3.6.4
    ...
    Unipath==1.1
    WeasyPrint==0.31
    webencodings==0.5



Initialize the demo databases
=============================

The Lino Book contains a series of demo projects, each of which has
its own sqlite database. These databases need to be initialized before you
can use these projects.

The easiest way to do this is to run the :cmd:`inv prep` command
from within your copy of the :ref:`book` repository.
This will find all projects in :mod:`lino_book.projects` and initialise the database with demo data::

    $ cd ~/repositories/book
    $ inv prep

The ``inv`` command has been installed on your system (more precisely:
into your Python environment) by the invoke_ package, which itself has
been required by atelier_, which is another Python package developed
by Luc.

The ``inv`` command is a kind of make tool which works by looking for
a file named :xfile:`tasks.py`. The Lino repository contains such a
file, and this file uses :mod:`lino.invlib`, which (together with
:mod:`atelier.invlib` from which it inherits) defines a whole series
of commands like :cmd:`inv prep` or :cmd:`inv test`.

Note that this is the same as doing the following for each project::

    $ cd lino_book/projects/min1
    $ python manage.py prep

You can learn more about atelier_ in :doc:`projects`


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

If you are reading the **Developer's Guide**, we now suggest to
:doc:`/tutorials/hello/index`.

If you are reading the **Administrator's Guide**, then continue where
you left in :doc:`/admin/install`.

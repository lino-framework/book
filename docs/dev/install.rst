.. _lino.dev.install:
.. _dev.install:

===============
Installing Lino
===============

.. _fabric: http://www.fabfile.org/
.. _invoke: http://www.pyinvoke.org/
.. _pycrypto: https://pypi.python.org/pypi/pycrypto
.. _atelier: http://atelier.lino-framework.org/
.. _Debian: http://www.debian.org/

This document describes how to install a Lino development
environment. The first part is also used for production sites (for
which the full instruction are in :doc:`/admin/install`).

This document is written for Debian_ and derivated distributions,
other Linuxes should be pretty similar.

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

.. include:: /include/system_req.rst

.. _lino.dev.env:

Set up a Python environment
===========================

.. Before you actually install the Lino sources into your system Python.
   environment, we recommend to create a new Python environment using
   virtualenv_.

Rather than installing Lino into your site-wide Python installation,
you install it to a separate virtual Python environment using::

        $ virtualenv --python=python2 /path_to_project_dir/env

To *activate* this environment, you will type::

        $ . /path_to_project_dir/env/bin/activate

Afterwards update the new environment's pip and setuptools to the
latest version::

        $ pip install -U pip
        $ pip install -U setuptools

If you know that you are only going to be using Python with Lino, then
you probably want to add above line to your :xfile:`.bashrc` file.
This will activate the Lino environment whenever you open a bash
shell::

    $ echo ". /path_to_project_dir/env/bin/activate" >> ~/.bashrc

Otherwise if you want a quick way to activate your Lino python
environment you can add an alias to your :xfile:`.bashrc` file::

    $ echo "alias lpy='.  /path_to_project_dir/env/bin/activate" >> ~/.bashrc
    $ . ~/.bashrc # To run the new alias
    $ lpy # Activates the environment
         
.. rubric:: Notes

We chose ``env`` for our environment, however you are free to choose any
name for your new environment that suits. However when deploying
production version of a lino-site, the virtual environment **must** either,
be in the *site-folder* with the name *env* or, there must be a
*symbolic-link* of *env* pointing to the environment folder.


If virtualenvs are new to you; The reason for creating a new environment
is to separate Lino from your system install of python. The main
advantages are; if you are also developing other things with python you
will often require different packages then what lino-uses, and there is
the change of version or dependency conflicts.

Also if you wish to remove Lino from your system you only need to remove
the source files and the virtual environment. Rather than trying to
remove lino's dependencies from the system environment without breaking
any other programs that use python.

To learn more read Dan Poirier's post `Managing multiple Python projects: Virtual environments
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


Get the sources
===============

You might theoretically install Lino using ``pip install lino``, but
this method isn't currently being tested very thoroughly. So in most
cases we currently recommend to use the development version because
you will probably want to use Lino's newest features before they get
released on PyPI.

Create a directory (e.g. :file:`repositories`) meant to hold your
working copies of version-controlled software projects, `cd` to that
directory and and do::

  $ mkdir repositories
  $ cd repositories
  $ git clone https://github.com/lino-framework/lino.git; \
    git clone https://github.com/lino-framework/xl.git; \
    git clone https://github.com/lino-framework/noi.git; \
    git clone https://github.com/lino-framework/cosi.git; \
    git clone https://github.com/lino-framework/care.git; \
    git clone https://github.com/lino-framework/vilma.git; \
    git clone https://github.com/lino-framework/avanti.git; \
    git clone https://github.com/lino-framework/tera.git; \
    git clone https://github.com/lino-framework/book.git


You should now have nine directories called :file:`lino`, :file:`xl`,
:file:`noi`, ... and :file:`book` in your :file:`~/repositories`
directory each of which contains a file :xfile:`setup.py` and a whole
tree of other files and directories.

.. Note that if you just want a *simplified* development environment
   (for a specific application on a production site), then you don't
   need to download and install all Lino repositories mentioned
   above. For example, if you want an `avanti` site, you *only* need
   to install `xl`, `lino` and `avanti` but *not* `noi`, `vilma`,
   `cosi` etc. On a production site you will probably never need the
   `book` repository which is the only one which requires all other
   repositories.

One possible problem here is that some repositories might have a big
size.  If you just want to get the latest version and don't plan to
submit any pull requests, then you can reduce download size by adding
``--depth 1`` and ``-b master`` options at least for `lino` (which has
by far the biggest repository)::

  $ git clone --depth 1 -b master https://github.com/lino-framework/lino.git
  
(as explained in `this question on stackoverflow
<http://stackoverflow.com/questions/1209999/using-git-to-get-just-the-latest-revision>`__
or Nicola Paolucci's blog entry `How to handle big repositories with
git
<http://blogs.atlassian.com/2014/05/handle-big-repositories-git/>`_).


Installation
============

Now you are ready to "install" Lino, i.e. to tell your Python
interpreter where the source file are, so that you can import them
from within any Python program.

Commands::

  $ cd repositories
  $ pip install -e lino
  $ pip install -e xl
  $ pip install -e noi
  $ pip install -e cosi
  $ pip install -e care
  $ pip install -e vilma
  $ pip install -e avanti
  $ pip install -e tera
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


Upgrading the sources
=====================

Actually the Lino version number is not enough when using a developer
installation of Lino.  The Lino codebase repository changes almost
every day, while the version is incremented only when we do an
official release to PyPI.

So as a developer you will simply upgrade your copy of the code
repositories often.  Here is a quick series of commands for getting
the latest version::

  $ cd repositories/lino ; git pull
  $ cd repositories/xl ; git pull
  $ cd repositories/noi ; git pull
  $ cd repositories/care ; git pull
  $ cd repositories/care ; git pull
  $ cd repositories/vilma ; git pull
  $ cd repositories/avanti ; git pull
  $ cd repositories/tera ; git pull
  $ cd repositories/book ; git pull
  $ find repositories -name '*.pyc' -delete

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
    Django==1.11.2
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

    $ cd ~/repositories/book/lino_book/projects/min1
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

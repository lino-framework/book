.. _lino.dev.install:
.. _dev.install:

=========================================
Installing a Lino development environment
=========================================

.. _invoke: http://www.pyinvoke.org/
.. _atelier: http://atelier.lino-framework.org/
.. _pycrypto: https://pypi.python.org/pypi/pycrypto
.. _Debian: http://www.debian.org/

This document describes how to install a Lino **development
environment** in order to write your own Lino applications and
potentially contribute to the Lino project.  This differs from
:doc:`/dev/quick/install` in that it requires you to learn some extra
lessons about cloning repositories, installing development packages
and manging virtual environments.

This document is written for Debian_ and derivated distributions.
Other Linuxes should be pretty similar.  On proprietary operating
systems you might encounter problems that are not documented here
because some dependencies are more difficult to install on these
systems.  Lino itself has no specific OS requirements.

This document assumes you are familiar with the Linux shell at least
for basic file operations like :cmd:`ls`, :cmd:`cp`, :cmd:`mkdir`,
:cmd:`rmdir`, file permissions, environment variables, bash scripts
etc.  Otherwise we suggest to learn about :ref:`Working in a UNIX
shell <learning.unix>`.


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
you install it to a separate virtual Python environment.

If virtualenvs are new to you: the reason for creating a new
environment is to separate Lino from your system install of Python.
The main advantages are: if you are also developing other things with
Python you will often require different packages than what Lino uses,
and there is the chance of version or dependency conflicts.

Also if you wish to remove Lino from your system you only need to
remove the source files and the virtual environment (rather than
trying to remove Lino's dependencies from the system environment
without breaking any other programs that use python).

First you create a *virgin environment* using::

    $ virtualenv --python=python2 ~/pythonenvs/py2

You might prefer to install Python 3 here (as explained under `System
requirements`_).  Actually you can install both, in that case keep in
mind that they are separate environments and you must do the
installation for each of them.

To *activate* this environment, you type::

    $ . ~/pythonenvs/py2/bin/activate

The dot (``.``) is a synonym for the :cmd:`source` command. If you
didn't know it, read the `manpage
<http://ss64.com/bash/source.html>`__ and `What does 'source' do?
<http://superuser.com/questions/46139/what-does-source-do>`__

After creating a new environment, you should always update `pip` and
`setuptools` to the latest version::

        $ pip install -U pip
        $ pip install -U setuptools


If you want a quick way to activate your Lino python environment, you
can add an alias to your :xfile:`.bashrc` or :xfile:`.bash_aliases`
file::

    alias p2='. ~/pythonenvs/py2/bin/activate'
    alias p3='. ~/pythonenvs/py3/bin/activate'

  
.. rubric:: Notes

.. We chose ``env`` for our environment. You are free to choose any
   other name for your new environment, but we recommend this
   convention because it is being used also on production servers.
   Note that :xfile:`env` might be a *symbolic-link* pointing to some
   shared environment folder.

You can **deactivate** a virtual environment with the command
:cmd:`deactivate`.  This switches you back to your machine's
system-wide environment.

You can **switch to another** virtualenv simply by activating it, you
don't need to deactivate the current one first.

You should never **rename** a virtualenv (they are not designed for
that), but you can easily create a new one and remove the old one.

To learn more, read Dan Poirier's post `Managing multiple Python
projects: Virtual environments
<https://www.caktusgroup.com/blog/2016/11/03/managing-multiple-python-projects-virtual-environments/>`__
where he explains what they are and why you want them.

The appy package on Python 3
============================

The appy package is a bit special to install under Python 3 because the author
is special... (e.g. he still gives support to customers whose production sites
run on Python 2.4).  With ``pip install appy`` you would get a version that
installs without error under Python 3, but not much more. That's why we
recomment to get a clone of the appy-dev project and install it using ``pip
install -e``.  Or to be short ::

  $ cd ~/repositories
  $ svn checkout https://svn.forge.pallavi.be/appy-dev
  $ pip install -e appy-dev/dev1


Get the sources
===============

Create a directory (e.g. :file:`repositories`) meant to hold your
working copies of version-controlled software projects, `cd` to that
directory and and do::

  $ mkdir ~/repositories
  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/lino.git; \
    git clone https://github.com/lino-framework/xl.git; \
    git clone https://github.com/lino-framework/noi.git; \
    git clone https://github.com/lino-framework/cosi.git; \
    git clone https://github.com/lino-framework/care.git; \
    git clone https://github.com/lino-framework/vilma.git; \
    git clone https://github.com/lino-framework/avanti.git; \
    git clone https://github.com/lino-framework/tera.git; \
    git clone https://github.com/lino-framework/book.git
    
Yes, we have a whole little collection of repositories and
applications!  As a Lino developer you will sooner or later get in
touch with these.  You don't need to dive into each of them right now
(see :doc:`overview` if you are curious), but let's *install* them
already now so that your environment is complete.  They are part of
this book because it would be difficult to explain Lino without having
some serious examples.  They are part of the Lino SDK because we also
use them for running test suites.

You should now have nine directories called :file:`lino`, :file:`xl`,
:file:`noi`, ... and :file:`book` in your :file:`~/repositories`
directory each of which contains a file :xfile:`setup.py` and a whole
tree of other files and directories.

Note that even if you opted for having two environments (py2 and py3),
these environments will use the same source repositories.

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

  $ p2  # activate the environment
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

These commands take some time when you run them the first time on your
machine because they will download and install all Python packages
needed by Lino.  If you install them a second time into another
environment, the process will be quicker because the dependencies have
bin cached.

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


Troubleshooting
===============

Using virtual environments seems to be one of the biggest challenges
for newbies. Here are some diagnostic tricks.

How to see which is your current virtualenv::

    $ echo $VIRTUAL_ENV
    /home/luc/virtualenvs/py2

    $ which python
    /home/luc/virtualenvs/py2/bin/python

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



Running your first Lino site
============================

You can now ``cd`` to any subdir of :mod:`lino_book.projects` and run
a development server.  Before starting a web server on a project for
the first time, you must initialize its database using the
:manage:`prep` command::
  
    $ cd ~/repositories/book/lino_book/projects/min1
    $ python manage.py prep
    $ python manage.py runserver

Now start your browser, point it to http://127.0.0.1:8000/ and you
should see something like this:

.. image:: install/1.png

Congratulations! Enjoy the first Lino application running on your
machine!


Exercises
=========

#.  Sign in and play around.
    
#.  Create some persons and organizations. Don't enter lots of data
    because we are going to throw it away soon.




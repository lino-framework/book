.. _user.install:
.. _getlino.install.dev:
.. _lino.dev.install:
.. _dev.install:

=========================================
Installing a Lino developer environment
=========================================

.. _invoke: http://www.pyinvoke.org/
.. _atelier: http://atelier.lino-framework.org/
.. _pycrypto: https://pypi.python.org/pypi/pycrypto
.. _Debian: http://www.debian.org/

This document describes how to install a Lino :term:`developer environment` on
your computer.  This is the easiest way to get started. You might later evolve
into a *contributing* developer as described in :doc:`/team/install/index`. For
installing Lino on a :term:`production server` you should read
:doc:`/admin/install`.

This document is written for Debian_ and derived distributions. Other Linuxes
should be pretty similar.  On proprietary operating systems you might encounter
problems that are not documented here because some dependencies are more
difficult to install on these systems.  Lino itself has no specific OS
requirements.

This document assumes you are familiar with the Linux shell at least for basic
file operations like :cmd:`ls`, :cmd:`cp`, :cmd:`mkdir`, :cmd:`rmdir`, file
permissions, environment variables, bash scripts etc.  Otherwise we suggest to
learn about :ref:`Working in a UNIX shell <learning.unix>`.


.. contents::
    :depth: 1
    :local:


.. _lino.dev.env:

Set up a virtual Python environment
===================================

Rather than installing Lino into your site-wide Python installation, you install
it to a separate virtual Python environment, also known as a :term:`virtualenv`

If virtualenvs are new to you: the reason for creating a new environment is to
separate Lino from your system-wide Python. The main advantages are: if you are
also developing other things with Python you might require different packages
than what Lino uses, and there is the chance of version or dependency conflicts.

Also if you wish to remove Lino from your system you only need to remove the
virtual environment rather than trying to remove Lino's dependencies from the
system environment without breaking any other programs that use python.

Where to put your :term:`virtualenv`:

- In a :term:`developer environment` we suggest
  :file:`~/lino/env` as your *default environment*.

- On a :term:`production server` we suggest :file:`/usr/local/lino/shared/master` or
  :file:`/usr/local/lino/shared/stable`.

How to create a new virtual environment and activate it::

  $ sudo apt-get install python3-pip
  $ mkdir ~/lino
  $ cd ~/lino
  $ virtualenv -p python3 env
  $ . env/bin/activate

The dot (``.``) is a synonym for the :cmd:`source` command. If you
didn't know it, read the `manpage
<http://ss64.com/bash/source.html>`__ and `What does 'source' do?
<http://superuser.com/questions/46139/what-does-source-do>`__

After creating a new environment, you should always update `pip` and
`setuptools` to the latest version::

        $ pip install -U pip
        $ pip install -U setuptools

.. rubric:: Did you know?

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


Set your default virtualenv
===========================

As a developer you probably don't want to type ``. ~/env/bin/activate`` each
time you open a new terminal with :kbd:`Ctrl+Alt+T`.  So you should set your
default **default environment**  by adding the following line to your
:file:`~/.bashrc` file::

  . ~/lino/env/bin/activate

You will also instruct your favourite code editor to use this default
environment when doing syntax checks or finding definitions etc.  For example in
Atom you say :menuselection:`Edit --> Preferences --> Packages` select the
settings of the python-tools plugin and set the :guilabel:`Path to Python
directory` field to  :file:`~/lino/env/bin`


.. You want a quick way to activate your Lino python environment, you
  can add an alias to your :xfile:`.bashrc` or :xfile:`.bash_aliases`
  file::

    alias p2='. ~/pythonenvs/py2/bin/activate'
    alias p3='. ~/pythonenvs/py3/bin/activate'

Run getlino
===========

Make sure your default environment is activated and then install :ref:`getlino`
via pip::

  $ pip install getlino

Then run :cmd:`getlino configure`::

  $ getlino configure

It asks a lot of questions, but you can hit ENTER for each of them.

Warning :
when getlino asks a ``[y or n]`` question, you should read it and understand it before you hit :kbd:`y`.
getlino overwrites certain configuration files without making a backup copy.
Read twice before you hit :kbd:`y`!

For details about each question see the documentation about :ref:`getlino`.

Your first Lino site
====================

Run :cmd:`getlino startsite` to create a first site::

  $ getlino startsite noi first

Run :manage:`runserver`::

  $ cd ~/lino/sites/first
  $ python manage.py runserver


Now start your browser, point it to http://127.0.0.1:8000/ and you
should see something like this:

.. image:: 1.png

Congratulations! Enjoy the first Lino application running on your
machine!



.. This process takes some time. Yes, we have a whole little collection of
  repositories and applications!  You don't need to dive into each of them right
  now, but you must at least *install* them so that your environment is complete.
  They are part of the Lino SDK because we also use them for running test suites.
  They are part of the Lino book because it would be difficult to explain Lino
  without having some serious examples. As a Lino developer you will sooner or
  later get in touch with these. See :doc:`overview` if you are curious.


Troubleshooting
===============

Using virtual environments seems to be one of the biggest challenges
for newbies. Here are some diagnostic tricks.

How to see which is your current virtualenv::

    $ echo $VIRTUAL_ENV
    /home/joe/lino/env

    $ which python
    /home/joe/lino/env/bin/python

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



Behind the scenes
=================

The getlino script does a lot of work.

These commands take some time when you run them the first time on your machine
because they will download and install all Python packages needed by Lino.  If
you install them a second time into another environment, the process will be
quicker because the dependencies have been cached.

Note that the `-e
<https://pip.pypa.io/en/latest/reference/pip_install.html#cmdoption-e>`_
command-line switch for :command:`pip` causes it to use the "development" mode.
Development mode means that these modules run "directly from source".  `pip`
does not *copy* the sources to your Python `site_packages`, but instead adds a
link to them.  The first argument after ``-e`` is not a *project name* but a
*directory*.

A quick test when you want to see whether Lino is installed is to say
"hello" to Lino:

.. py2rst::

   self.shell_block(["python", "-m", "lino.hello"])

In case you didn't know: Python's `-m
<https://docs.python.org/2/using/cmdline.html#cmdoption-m>`_
command-line switch instructs it to just *import* the specified module
(here :mod:`lino.hello`) and then to return to the command line.


Concepts
========

.. glossary::

  virtualenv

    A virtual Python environment.

  Developer environment

    A set of tools configured on the desktop computer of a Lino developer who
    wants to develop their own :term:`Lino application`.

  Contributor environment

    An extended :term:`developer environment` suitable for developers who plan
    to potentially contribute to the :term:`Lino framework`.  A bit more work to
    install, but more future-proof.

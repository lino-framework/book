.. _dev.setup:
.. _dev.env:

================================
Setting up your work environment
================================

.. contents::
    :depth: 1
    :local:


What is a project?
==================

We use the word **project** for quite a lot of things. But for Lino
developers they all have one thing in common: each project is a
directory on your file system.  You "activate" a project by opening a
terminal and changing to its directory. That's all. Almost all. Read
on.

There are different types of "projects".  A **Django project** is
where you can invoke a :manage:`runserver`.  It contains at least a
:xfile:`settings.py` and usually a file :xfile:`manage.py`.  For
**Atelier**, a project must contain at least a file :xfile:`tasks.py`.
An *Atelier project* can contain one or more *Django projects*.

- An atelier project usually corresponds to a public code repository
  (using Git or Mercurial). But you can have unpublished projects
  which have no repo at all.
- An atelier project usually corresponds to a given Python package to
  be published on PyPI.
- An atelier project can have a number of Sphinx document trees
  (default is one tree named :file:`docs`).

You will have different **root directories** containing projects.
You don't want to have them all under a single top-level directory.
We suggest the following naming conventions.

.. xfile:: ~/repositories

    The :file:`~/repositories` directory is your collection of code
    repositories of projects for which you cloned a copy. We created
    this directory in :ref:`lino.dev.install`.

.. xfile:: ~/projects

    :xfile:`~/projects/` is the base directory for every new project of
    which you are the author. You created this directory in
    :doc:`/dev/hello/index`, and ``hello`` is your first local
    project.

.. xfile:: ~/repositories/book/lino_book/projects

    The Lino Book comes with a set of Django demo projects maintained
    by the Lino team.  For example, ``min1`` is one of the Django
    projects included in the ``book`` project.


Navigating between projects
===========================

We suggest that you create a shell function named ``go`` [#f1]_ in
your :xfile:`~/.bash_aliases` which looks like this::

    function go() {
        for BASE in ~/projects ~/repositories \
            ~/repositories/book/lino_book/projects
        do
          if [ -d $BASE/$1 ] ; then
            cd $BASE/$1;
            return;
          fi
        done
        echo Oops: no project $1
        return -1
    }

This adds a new shell command :cmd:`go` to your terminal:

.. command:: go

    Shortcut to :cmd:`cd` to one of your local project directories.

Now you should be able to do::

  $ go lino   # cd to ~/repositories/lino
  $ go hello  # cd to ~/projects/hello
  $ go min1   # cd to ~/repositories/book/lino_book/projects/min1


Configuring atelier
===================

To get a full Lino contributor environment, you must tell atelier the
list of your projects. That's done in your
:xfile:`~/.atelier/config.py` file. Create the directory and the file,
with the following content::

     add_project("/home/john/projects/hello")
     names = 'lino xl book noi voga presto welfare avanti vilma tera extjs6'
     for p in names.split():
         add_project("/home/john/repositories/" + p)

Note our use of a syntactical trick to avoid typing lots of
apostrophes: we put the names into a single string, separated just by
spaces. And then we call the :meth:`split` method on that string which
splits our string on every whitspace:

>>> 'foo bar  baz'.split()
['foo', 'bar', 'baz']

Letting :mod:`atelier` know where your projects are has the following
advantages:

- You can run the :cmd:`per_project` script (or its alias :cmd:`pp`)
  to run a given command over many projects.

- You can use :mod:`atelier.sphinxconf.interproject` to create
  Intersphinx links from one project's docs to the docs of another
  project.


Some more shell aliases
=======================

Here are some useful aliases and functions for your
:xfile:`~/.bash_aliases`::

    alias pp='per_project'
    alias runserver='python manage.py runserver'
    alias ci='inv ci'
    alias p3='. ~/pythonenvs/py3/bin/activate'
    alias p2='. ~/pythonenvs/py2/bin/activate'

    function pywhich() {
      python -c "import $1; print($1.__file__)"
    }

.. command:: pywhich

    Shortcut to quickly show where the source code of a Python module
    is coming from.

    This is useful e.g. when you are having troubles with your virtual
    environments.


.. We chose ``env`` for our environment. You are free to choose any
   other name for your new environment, but we recommend this
   convention because it is being used also on production servers.
   Note that :xfile:`env` might be a *symbolic-link* pointing to some
   shared environment folder.



Usage examples
==============

You can now play around in your development environment.

See a list of your atelier projects::

    $ pp -l
    ========= ========= ========================================== ========================
     Project   Status    URL                                        doctrees
    --------- --------- ------------------------------------------ ------------------------
     lino      master!   http://www.lino-framework.org              docs
     xl        master    http://www.lino-framework.org              docs
     noi       master    http://noi.lino-framework.org              docs
     cosi      master    http://cosi.lino-framework.org             docs
     avanti    master    http://avanti.lino-framework.org/          docs
     vilma     master    http://vilma.lino-framework.org            docs
     care      master    http://care.lino-framework.org             docs
     tera      master    http://tera.lino-framework.org             docs
     book      master!   http://www.lino-framework.org              docs
     voga      master    http://voga.lino-framework.org             docs
     welfare   master    http://welfare.lino-framework.org          docs, docs_de, docs_fr
     amici     master    http://amici.lino-framework.org            docs
    ========= ========= ========================================== ========================


Change to :file:`~/repositories/lino` and download the latest version
of Lino::

  $ go lino
  $ git pull

Run the full test suite in :ref:`book`::

  $ go book
  $ inv prep test

It happens that I type the following before leaving my computer for
getting a cup of coffee::

  $ pp -v inv prep test bd pd

Commit all my changes in all my projects before going to bed::

  $ pp inv ci

If that happens after midnight::

  $ pp inv ci --today 20161222





.. rubric:: Footnotes

.. [#f1] In case you also use the `Go <https://golang.org/>`_
         programming language on your computer, you should obviously
         pick another name than "go".


Have LibreOffice server running on your machine
===============================================

Some of the demo examples use :mod:`lino_xl.lib.appypod` for producing
printable pdf files.  To have this running, you should install the
LibreOffice server on your system as described in :doc:`/admin/oood`.



Quickly installing the Lino SDK into a new virtualenv
=====================================================


.. xfile:: install_dev_projects.sh

Not much tested. Read and follow at your own risk.

Here is how to quickly install the Lino SDK into a new virtualenv::

  $ cd ~/repositories
  $ sh book/docs/dev/install_dev_projects.sh

Automated way for cloning and installing the code repositories::

  $ cd ~/repositories
  $ wget https://raw.githubusercontent.com/lino-framework/book/master/docs/dev/install_dev_projects.sh
  $ sh install_dev_projects.sh


How to switch to the development version of Atelier
===================================================

Not much tested. Read and follow at your own risk.

The :mod:`atelier` package had been automatically installed together
with :mod:`lino`. That is, you are using the *PyPI* version of
Atelier.  That's usually okay because Atelier is more or less
stable. But one day we might decide that you should rather switch to
the *development* version.

Doing this is easy:

1. uninstall the PyPI version and then install the development
   version::

    $ pip uninstall atelier

    $ cd ~/repositories
    $ git clone https://github.com/lino-framework/atelier.git
    $ pip install -e atelier

2. Open your :xfile:`~/.atelier/config.py`
   file and insert ``atelier`` to the list of projects::

     ...
     names = 'atelier lino xl book noi voga presto welfare avanti extjs6'
     ...

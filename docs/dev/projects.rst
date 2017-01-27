==================
Project management
==================

This section introduces our minimalistic project management system
based on :mod:`atelier`.

What is a project?
==================

In :mod:`atelier`, a **project** is a directory on your file system
which contains at least a file :xfile:`tasks.py`.  That's the only
real *must* for being a project. Other parts of a project are
optional:

- A project usually corresponds to a public code repository (using Git
  or Mercurial). But you can have non-public projects which have no
  repo at all.
- A project usually corresponds to a given Python package to be
  published on PyPI.
- A project can have a number of Sphinx document trees (default is one
  tree named :file:`docs`).

You "activate" a project by opening a terminal and changing to its
directory. That's all.

Project root directories
========================

You don't need to have all your projects under a single top-level
directory.  You can have different **root directories** containing
projects.  We suggest the following naming conventions.

.. xfile:: ~/repositories

    The :file:`~/repositories` directory is your collection of
    repositories of projects for which you are not the author, but you
    cloned a read-only copy of the development repository, as explained in
    :ref:`lino.dev.install` or the installation instructions for
    :ref:`cosi`, :ref:`welfare`, :ref:`voga`.

.. xfile:: ~/projects

    :file:`~/projects/` is the base directory for every new project for
    which you are the author.


Configuring your atelier
========================

Create a :xfile:`~/.atelier/config.py` file which declares a list of
all your projects. If you have been following the tutorials so far,
then the content will be something like::
  
     add_project("/home/john/projects/mylets")
     add_project("/home/john/projects/hello")
     for p in ('lino', 'xl', 'cosi', 'book'):
         add_project("/home/john/repositories/" + p)

Letting :ref:`atelier` know where your projects are has the following
advantages:

- You can run the :cmd:`per_project` script (or its alias :cmd:`pp`)
  to run a command over each project.
- You can use :mod:`atelier.sphinxconf.interproject`


Navigating between projects
===========================

We suggest that you create a shell function named ``go`` [#f1]_ in
your :xfile:`~/.bash_aliases` which might look like this::

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


This adds a new shell command :command:`go` to your terminal:

.. command:: go

    Shortcut to :cmd:`cd` to one of your local project directories.


Some more shell aliases
=======================

Here are some useful aliases and functions for your
:xfile:`~/.bash_aliases`::

    alias pp='per_project'
    alias runserver='python manage.py runserver'
    alias ci='inv ci'
    alias p3='. ~/pythonenvs/py35/bin/activate'
    alias p2='. ~/pythonenvs/py27/bin/activate'

    function pywhich() { 
      python -c "import $1; print($1.__file__)"
    }
           
.. command:: pywhich

    Shortcut to quickly show where the source code of a Python module
    is coming from.

    This is useful e.g. when you are having troubles with your virtual
    environments.

Usage examples
==============

You can now play with these commands:

Change to :file:`~/repositories/lino` and download the latest version
of Lino::

  $ go lino
  $ git pull
  
Run :cmd:`inv prep` followed by :cmd:`inv test` in :ref:`book`::

  $ go book
  $ inv prep test
    
It happens that I type the following before leaving my computer::

  $ pp -v inv prep test bd pd

Commit all my changes in all my projects before going to bed::

  $ pp inv ci

If that happens after midnight::  
  
  $ pp inv ci --today 20161222
  

    
.. rubric:: Footnotes

.. [#f1] In case you also use the `Go <https://golang.org/>`_
         programming language on your computer, you should obviously
         pick another name than "go".


         

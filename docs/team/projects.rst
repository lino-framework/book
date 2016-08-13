==================
Project management
==================

This section introduces our minimalistic project management system
based on :mod:`atelier`.

What is a project?
==================

In :mod:`atelier`, a **project** is a directory on your file system
which contains at least a :xfile:`tasks.py`.  That's the only real
*must* for being a project. Other parts of a project are optional:

- A project usually corresponds to a public code repository (using Git
  or Mercurial). But you can have non-public projects which have no
  repo at all, e.g. your developer blog.
- A project usually corresponds to a given Python package to be
  published on PyPI.
- A project can have a number of Sphinx document trees (default is one
  tree named :file:`docs`).

You "activate" a project by opening a terminal and changing to its
directory. That's all.

That said, there are some tricks to make project management more
pleasant.


Going to a project
==================

We suggest that you create a shell function named ``go`` [#f1]_ in
your :xfile:`~/.bash_aliases` which might look like this::

    function go() { 
        for BASE in ~/projects ~/repositories \
            ~/repositories/lino/lino/projects
        do
          if [ -d $BASE/$1 ] 
          then
            cd $BASE/$1;
            return;
          fi
        done
        echo Oops: no $1 in $BASES
        return -1
    }


This adds a new shell command ``go`` to your terminal:

.. command:: go

    Shortcut to :cmd:`cd` to one of your local project directories.


If you installed :ref:`the development version of Lino
<lino.dev.install>` and :ref:`your developer blog <dblog>` as
instructed, you can now play with these commands:

  - :cmd:`go lino` changes to the main directory of your `lino` repository
  - :cmd:`git pull` downloads the latest version of Lino
  - :cmd:`inv initdb test` (i.e. :cmd:`inv initdb` followed by
    :cmd:`inv test`)

  - :cmd:`go myblog` changes to the main directory of your developer blog
  - :cmd:`inv blog` launches your editor on today's blog entry
  - :cmd:`inv bd pd` (i.e. :cmd:`inv bd` followed by :cmd:`inv pd`)


This way of working implies that you identify every project by a short
*internal project name*.


Project containers
==================

You don't need to keep all your projects under a single top-level
directory.  You can have different **base directories** containing
projects.  We suggest the following naming conventions (you don't need
to use these same conventions, but our examples are based on them).

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
all your projects. For example with this content::

     add_project("/home/john/projects/myblog")
     add_project("/home/john/projects/hello")
     for p in ('lino', 'xl', 'book'):
         add_project("/home/john/repositories/" + p)

Letting :ref:`atelier` know where your projects are has the following
advantages:

- You can run the :cmd:`per_project` script to run a command over each
  project
- You can use :mod:`atelier.sphinxconf.interproject`
- You can run :cmd:`inv ls` to display a summary about all your
  projects


See also :ref:`atelier.usage`.


Some bash aliases
=================

Here are some useful functions for your :xfile:`~/.bash_aliases`::

    alias ci='inv ci'
    alias runserver='python manage.py runserver'
    alias pp='per_project'

    function pywhich() { 
      python -c "import $1; print $1.__file__"
    }


.. command:: pp
             
.. command:: pywhich

    Shortcut to quickly see where the source code of a Python module
    is coming from.

    This is useful e.g. when you are having troubles with your virtual
    environments.


    
Looping over projects
=====================

For example::

  $ pp inv initdb test bd pd




.. rubric:: Footnotes

.. [#f1] In case you also use the `Go <https://golang.org/>`_
         programming language on your computer, you should obviously
         pick another name than "go".


         

.. doctest docs/dev/builddocs.rst
.. _lino.dev.bd:

======================
Building the Lino Book
======================

This page explains how to build the Lino Book, i.e. how to generate
the html pages you are reading right now.

The Lino Book is *static* html which is visible at different places,
e.g. at http://www.lino-framework.org\ , at `lino.readthedocs.io
<http://lino.readthedocs.io/en/latest/>`__ or (when you've built it)
locally on your computer.


Theoretically it's easy
=======================

When your development environment is correctly installed as explained
in :doc:`install`, then --theoretically-- it's easy to build the Lino
Book: you just run :cmd:`inv bd` in the root directory of your
``book`` repository::

  $ go book
  $ inv bd

This will tell Sphinx to read the `.rst` source files and to generate
:file:`.html` files into the :file:`docs/.build` directory.  Voilà.

If you get some error message, then you need to read the
Troubleshooting_ section.  Otherwise you can now start your browser on
the generated files::

  $ firefox docs/.build/html/index.html

Or jump directly to your local copy of this page:  

  $ firefox docs/.build/html/team/builddocs.html


Troubleshooting
===============

.../docs/api/xxx.yyy.foo.rst:21:failed to import Bar
----------------------------------------------------

This can occur when you have an earlier build of the book on your
computer, then pulled a new version of some Lino repository (or made
some local code changes) and then run :cmd:`inv bd` again.

The error should disappear either if you manually remove the specified
file :file:`docs/api/xxx.yyy.foo.rst`.  Or, most fool-proof solution,
you use the :cmd:`inv clean` command to automatically remove cached
and generated files::

    $ inv clean -b


[autosummary] failed to import u'lino_book.projects.team.tests.test_notify'
---------------------------------------------------------------------------

This means that `autosummary
<http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`__ (which
in turn needs `autodoc
<http://www.sphinx-doc.org/en/master/ext/autodoc.html>`__) has a
problem to import the module
:mod:`lino_book.projects.team.tests.test_notify`.

Indeed you can verify that importing this module in a normal Python
session will fail:


>>> import lino_book.projects.team.tests.test_notify  #doctest: +NORMALIZE_WHITESPACE +IGNORE_EXCEPTION_DETAIL +ELLIPSIS
Traceback (most recent call last):
...
ImproperlyConfigured: Requested setting SITE, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

As the error message tries to explain, the module refuses to import
because :envvar:`DJANGO_SETTINGS_MODULE` is not set.  That's related
to an oddness of Django (one of its well-known and widely accepted
oddnesses): you cannot simply import a module that imports
:mod:`django` when that environment variable is not set.
        
Note that the :file:`docs/conf.py` contains (among others) the
following lines::

    from lino.sphinxcontrib import configure
    configure(globals(), 'lino_book.projects.max.settings.doctests')

This calls the :func:`lino.sphinxcontrib.configure` function which
basically does exactly what we need here: it sets the
:envvar:`DJANGO_SETTINGS_MODULE` to
:mod:`lino_book.projects.max.settings.doctests`.
     
So Sphinx uses the :mod:`lino_book.projects.max` project when
generating the docs.

But your message says that something went wrong during all this.

Let's try this::

    $ # cd to ~/projects/book/lino_book/projects/max:
    $ go max
    $ python manage.py shell

And in *that* Python shell you try to import the module which Sphinx
was not able to import::

    import lino_book.projects.team.tests.test_notify

What happens now?





Introducing Sphinx
==================

Lino makes heavy usage of **Sphinx**, the dominant documentation
system in the Python world.  Sphinx is a tool that "makes it easy to
create intelligent and beautiful documentation" and that "actually
makes programmers **want** to write documentation!"
(`www.sphinx-doc.org <http://www.sphinx-doc.org>`__).

For example, the "source code" of the page your are reading right now
is in a file `docs/dev/builddocs.rst
<https://github.com/lino-framework/book/blob/master/docs/dev/actions.rst>`__.

Read more about the markup used by Sphinx in `reStructuredText Primer
<http://sphinx-doc.org/rest.html>`_.
Also `The build configuration file <http://sphinx-doc.org/config.html>`_.

  

Let's play
==========

Let's play a bit:  
  
Open the source file of this page::

  $  nano docs/team/builddocs.rst

Edit something in that file and save your changes. Then build the book
again::

  $ inv bd

Then hit :kbd:`Ctrl-R` in your browser and check whether the HTML
output changes as expected.

You can undo all your local changes using::

  $ git checkout docs/team/builddocs.rst

Or, if you agree to :doc:`contribute <contrib>` your changes to the
Lino project, you can :doc:`submit a pull request <request_pull>` as
you would do with code changes.

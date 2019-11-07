=========================================
Demo projects included with the Lino Book
=========================================

The Lino Book includes a collection of :term:`demo projects <demo project>`.

.. glossary::

  Demo project

    A Django project that can be run out of the box from a source repository
    after installing the :doc:`developer environment </dev/install/index>`).

An overview of all available demo projects is given in
:mod:`lino_book.projects`.

Each demo project has its own sqlite database which needs to be
initialized first.  For example, in order to try out
:mod:`lino_book.projects.polly` your can do::

    $ go polly
    $ django manage.py prep
    $ django manage.py runserver

You can initialize all demo projects in one operation by running the :cmd:`inv
prep` command from within the root directory of your ``book`` repository::

    $ cd ~/repositories/book
    $ inv prep

This will run :cmd:`inv prep` in all demo projects.

The list of demo projects included with a code repository is defined in the
:envvar:`demo_projects` setting of the :xfile:`tasks.py` file.

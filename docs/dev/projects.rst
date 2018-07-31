=========================================
Demo projects included with the Lino Book
=========================================

The Lino Book includes a collection of Django projects which you can
try out of the box (when your :doc:`work environment is set up
<env>`).

The overview of available projects is given in
:mod:`lino_book.projects`.

Each demo project has its own sqlite database which needs to be
initialized first.  For example, in order to try out
:mod:`lino_book.projects.polly` your can do::

    $ go polly
    $ django manage.py prep
    $ django manage.py runserver

You can initialize all demo projects in one operation by running the
:cmd:`inv prep` command from within the root directory of your
``book`` repository::

    $ cd ~/repositories/book
    $ inv prep

This will run :cmd:`inv prep` in all demo projects.

Note that the list of demo projects is defined in the
:xfile:`tasks.py` file (in :envvar:`demo_projects`).



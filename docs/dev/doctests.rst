.. _tested_docs:
.. _dev.doctest:

================
Doctests in Lino
================

**Tested documents** are pages that contain blocks of Python code marked by a
``>>>`` in the beginning of each line.
They are part of the Lino test suite and have been tested using Python's standard
doctest command.

You can re-play the instructions on
such pages in the demo project, either interactively in a Django
:manage:`shell` session or by writing a script and run it using :manage:`run`.

They run **on a cached demo database** and
not on a temporary test database as the Django test runner creates it.

The advantage of this is that they access the existing demo database and thus
don't need to populate it (load the demo fixtures) for each test run.

A limitation of these cases is of course that they may not modify the database.
That's why we sometimes call them static or passive. They just observe whether
everything looks as expected.

There is much more to say about this topic... meanwhile you must use the
source, Luke!

The doctest command extracts code snippets from any text file, runs
them in a subprocess and then checks whether their output is the same
as the one displayed in the document.

Lino comes with some tools and shortcuts to make it easier to write
such documents.


- Extended TestCase classes:

  - :mod:`atelier.test`
  - :mod:`lino.utils.pythontest` and :mod:`lino.utils.djangotest`
  - :mod:`lino.utils.test`


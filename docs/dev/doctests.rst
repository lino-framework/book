================
Doctests in Lino
================

**Tested documents** are a way of writing test cases. They are pages
of a document tree which are being tested using Python's standard
doctest command.

Examples of such documents are all pages below :doc:`/specs/index`.


Lino adds a new style of test cases: test cases that use a
:class:`django.test.Client`, but *on a cached demo database* and *not*
on a temporary test database as the Django test runner creates it.

The advantage is that they access the existing demo database and thus
don't need to populate it (load the demo fixtures) for each test run.

A limitation of these cases is of course that they may not modify the
database. That's why we sometimes call them static or passive. They
just observe whether everything looks as expected.

All these would deserve a whole chapter of documentation.  I'll do my
best to fill up this hole...  meanwhile you must use the source, Luke!


The doctest command extracts code snippets from any text file, runs
them in a subprocess and then checks whether their output is the same
as the one displayed in the document.

Lino comes with some tools and shortcuts to make it easier to write
such documents.




- Extended TestCase classes:

  - :mod:`atelier.test`
  - :mod:`lino.utils.pythontest` and :mod:`lino.utils.djangotest`
  - :mod:`lino.utils.test`


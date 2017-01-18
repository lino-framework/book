.. _dev.testing:


=========================
Testing Lino applications
=========================

You can write test suites for a Lino application like for any other
Django project. But Lino adds a set of tools, conventions, ideas and
suggestions for testing your applications.

Running classical Django tests
==============================

Any given *code repository* usually corresponds to one *Python
package* and has one *test suite*.


The test suite of a Python package is defined in
:xfile:`setup_info.py`.

In most of our projects this contains a single file
:file:`tests/__init__.py` which is if you want the "master file".


A Python package can contain multiple demo projects.  A typical test
is to run Django's :manage:`test` command in each of them. Something
like this (excerpt from the :file:`tests/__init__.py` of
:ref:`book`)::

    from lino.utils.pythontest import TestCase

    class ProjectsTests(TestCase):

        def test_min1(self):
            self.run_django_manage_test("lino_book/projects/min1")

You know that there is no way to test several Django applications in a
single Python process. Every piece of code which imports Django
requires the :envvar:`DJANGO_SETTINGS_MODULE` environment variable to
be set, and it is not allowed to change that variable at runtime. So
it is clear that every call to :meth:`run_django_manage_test
<lino.utils.pythontest.TestCase.run_django_manage_test>` is going to
spawn subprocess.


Running doctests
================

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


- Extended TestCase classes:

  - :mod:`atelier.test`
  - :mod:`lino.utils.pythontest` and :mod:`lino.utils.djangotest`
  - :mod:`lino.utils.test`


.. _travis:

Travis CI
=========

The Lino team has an `account at Travis CI
<https://travis-ci.org/lino-framework/>`__.

=============================
Django tests in demo projects
=============================

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


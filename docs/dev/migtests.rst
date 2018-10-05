===============
Migration tests
===============

Migration tests are a special test case in every demo project for
appölications for which we ofgfer migration suport. So that these
applications can be used for stable hosting.

Overview
========

- :manage:`makemigdump`
- :xfile:`test_restore.py`


Making migration dumps
======================


Testing migration dumps
=======================

.. xfile:: test_restore.py

A typical :xfile:`test_restore.py` file contains only something like
this::


    from lino.utils.djangotest import RestoreTestCase

    class TestCase(RestoreTestCase):
        tested_versions = ['18.8.0']

Note the :attr:`tested_versions
<lino.utils.djangotest.RestoreTestCase.tested_versions>` attribute.



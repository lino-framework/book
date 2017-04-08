.. _dev.setup_info:

====================================
How Lino applications use `setup.py`
====================================


.. How to test just this file:

   $ python setup.py test -s tests.DocsTests.test_setup

This document describes a trick which does not depend on
Lino and which we recommend to use for any Python project.

The problem
===========

Usually the setup information is directly contained in a file
:xfile:`setup.py` in the root directory of a project. The problem with
this layout is that this :xfile:`setup.py` file is always available at
runtime when the application was installed using PyPI.

Is there a way to have setup information both in a central place
**and** accessible at runtime.


The solution
============

To solve this problem, we store the setup information in a separate
file (which we usually name :xfile:`setup_info.py`) and which we
execute from both our :xfile:`setup.py` and our packages's main
:xfile:`__init__.py` file.



.. xfile:: setup_info.py

    The file which contains the information for Python's `setup.py`
    script, e.g. the Lino **version number** or the **dependencies**
    (i.e. which other Python packages must be installed when using
    Lino).

So that's why the :xfile:`setup.py` of a Lino application contains
just this::

    from setuptools import setup
    fn = 'lino/setup_info.py')
    exec(compile(open(fn, "rb").read(), fn, 'exec'))
    if __name__ == '__main__':
        setup(**SETUP_INFO)
    
And the :file:`__init__.py` file of the main module contains this::

    from os.path import join, dirname
    fn = join(dirname(__file__), 'setup_info.py')
    exec(compile(open(fn, "rb").read(), fn, 'exec'))
    __version__ = SETUP_INFO.get('version')


Note that ``exec(compile(open(fn, "rb").read(), fn, 'exec'))`` is
equivalent to ``execfile(fn)``, except that it works in both Python 2
and 3.
    


Usage example:

>>> import lino
>>> print lino.SETUP_INFO['description']
A framework for writing desktop-like web applications using Django and ExtJS

Setup information
=================

The :func:`setup` function has a lot of keyword parameters which are
documented elsewhere.

.. _install_requires:

install_requires
----------------

See http://python-packaging.readthedocs.io/en/latest/dependencies.html

.. _tests_require:

tests_require
-------------

See http://python-packaging.readthedocs.io/en/latest/dependencies.html


.. _long_description:

long_description
----------------

This being published on PyPI.

Lino usually inserts this in the :xfile:`api/index.rst` file of the
docs tree.

This is used by :command:`inv bd` as the source text for the projects
:xfile:`README.rst`.

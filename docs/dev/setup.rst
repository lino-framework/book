.. _dev.setup_info:

====================================
How Lino applications use `setup.py`
====================================


.. How to test just this file:

   $ python setup.py test -s tests.DocsTests.test_setup

The :xfile:`setup_info.py` file is a trick which does not depend on
Lino and which we recommend to use for any Python project.

Usually the setup information is directly contained in a file
:xfile:`setup.py` in the root directory of a project. The problem with
this layout is that this :xfile:`setup.py` file is always available at
runtime when the application was installed using PyPI.

To solve this problem, we store this information in a separate file
(which we usually name :xfile:`setup_info.py`) and which we execute
from both our :xfile:`setup.py` and our packages's main
:xfile:`__init__.py` file.  This trick makes it possible to have setup
information both in a central place **and** accessible at runtime.


.. xfile:: setup_info.py

    The file which contains the information for Python's `setup.py`
    script, e.g. the Lino **version number** or the **dependencies**
    (i.e. which other Python packages must be installed when using
    Lino).

So that's why the :xfile:`setup.py` of a Lino application contains
just this::

    from setuptools import setup
    from past.builtins import execfile
    execfile('lino/setup_info.py')
    if __name__ == '__main__':
        setup(**SETUP_INFO)
    
And the :file:`__init__.py` file of the main module contains this::

    from past.builtins import execfile
    from os.path import join, dirname
    execfile(join(dirname(__file__), 'setup_info.py'))
    __version__ = SETUP_INFO.get('version')


Usage example:

>>> import lino
>>> print lino.SETUP_INFO['description']
A framework for writing desktop-like web applications using Django and ExtJS


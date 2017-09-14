.. _dev.setup:
.. _dev.env:

================================
Setting up your work environment
================================

.. how to test just this document:

   $ python setup.py test -s tests.LibTests.test_runtests

As a Lino developer you are going to maintain and know a whole little
collection of repositories and applications. You don't need to dive
into each of them right now (see :doc:`overview` for details), but you
should install them before running test suites or building Sphinx
documentation trees.

.. contents::
    :depth: 1
    :local:

Installing the Lino SDK
=======================

Automated way for cloning and installing the code repositories::

  $ cd ~/repositories
  $ wget https://raw.githubusercontent.com/lino-framework/book/master/docs/dev/install_dev_projects.sh
  $ chmod +x install_dev_projects.sh
  $ ./install_dev_projects.sh

Then you must manually tell :ref:`atelier` about these new projects.
Open your :xfile:`~/.atelier/config.py` file which should contain::

     add_project("/home/john/projects/hello")
     for p in ('lino', 'xl', 'book'):
         add_project("/home/john/repositories/" + p)

Change that to::

     add_project("/home/john/projects/hello")
     names = 'lino xl book noi voga presto welfare avanti extjs6'
     for p in names.split():
         add_project("/home/john/repositories/" + p)

Note our use of a syntactical trick to avoid typing lots of
apostrophes: we put the names into a single string, separated just by
spaces. And then we call the :meth:`split` method on that string which
splits our string on every whitspace:

>>> 'foo bar  baz'.split()
['foo', 'bar', 'baz']

As a last step you must install the LibreOffice server on your system
as described in :doc:`/admin/oood`.


Showing your atelier projects
=============================

To see a list of your atelier projects, type::

    $ pp -l

The output should be something like::
  
    ========= ========================================== ========= ========================
     Project   URL                                        Version   doctrees
    --------- ------------------------------------------ --------- ------------------------
     atelier   http://atelier.lino-framework.org          1.0.2     docs
     lino      http://www.lino-framework.org              1.7.6     docs
     xl        http://www.lino-framework.org              1.7.5     docs
     noi       http://noi.lino-framework.org              0.0.3     docs
     cosi      http://cosi.lino-framework.org             0.0.3     docs
     welfare   http://welfare.lino-framework.org          1.1.26    docs, docs_de, docs_fr
     avanti    http://avanti.lino-framework.org/          2017.1.0  docs
     presto    http://presto.lino-framework.org           0.0.1     docs
     voga      http://voga.lino-framework.org             0.0.4     docs
     ext6      http://www.lino-framework.org              0.0.1     docs
     book      http://www.lino-framework.org              1.7.4     docs
    ========= ========================================== ========= ========================



How to switch to the development version of Atelier
===================================================

The :mod:`atelier` package had been automatically installed together
with :mod:`lino`. That is, you are using the *PyPI* version of
Atelier.  That's usually okay because Atelier is more or less
stable. But one day we might decide that you should rather switch to
the *development* version.

Doing this is easy:

1. uninstall the PyPI version and then install the development
   version::
  
    $ pip uninstall atelier

    $ cd ~/repositories
    $ git clone https://github.com/lino-framework/atelier.git
    $ pip install -e atelier

2. Open your :xfile:`~/.atelier/config.py`
   file and insert ``atelier`` to the list of projects::
  
     ...
     names = 'atelier lino xl book noi voga presto welfare avanti extjs6'
     ...



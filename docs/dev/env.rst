.. _dev.setup:
.. _dev.env:

================================
Setting up your work environment
================================

Work in progress. Read at your own risk.

.. how to test just this document:

   $ python setup.py test -s tests.LibTests.test_runtests

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

Then you must manually tell :ref:`atelier` about these new projects
in your :xfile:`~/.atelier/config.py` file.

As a last step you must install the LibreOffice server on your system
as described in :doc:`/admin/oood`.



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



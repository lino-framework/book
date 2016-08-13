.. _dev.runtests:

===========================
Running the Lino test suite
===========================


.. how to test just this document:

   $ python setup.py test -s tests.LibTests.test_runtests

This section explains how to run the test suite for the Lino
framework.

.. _dev.setup:

Setting up your work environment
================================

In :ref:`lino.dev.install` you did::

  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/atelier.git
  $ git clone https://github.com/lino-framework/lino.git
  $ git clone https://github.com/lino-framework/xl.git
  $ git clone https://github.com/lino-framework/book.git

As a member of the Lino core team you will also clone the other
repositories supported by our team::
  
  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/noi.git
  $ git clone https://github.com/lino-framework/cosi.git
  $ git clone https://github.com/lino-framework/voga.git
  $ git clone https://github.com/lino-framework/presto.git
  $ git clone https://github.com/lino-framework/welfare.git

And then you install them using pip (as editable using ``-e``
option)::

  $ pip install -e noi
  $ pip install -e cosi
  $ pip install -e voga
  $ pip install -e presto
  $ pip install -e welfare
  
Note that :ref:`atelier` had been automatically installed previously,
so you should uninstall it first::
  
  $ pip uninstall atelier   # uninstall PyPI version
  $ pip install -e atelier  # install development version
  
Now we'll tell :ref:`atelier` about these new projects.
Open your :xfile:`~/.atelier/config.py` file which should contain::
  
     add_project("/home/john/projects/mylets")
     add_project("/home/john/projects/hello")
     for p in ('lino', 'xl', 'book'):
         add_project("/home/john/repositories/" + p)

Change that to::

     add_project("/home/john/projects/mylets")
     add_project("/home/john/projects/hello")
     for p in 'lino xl book noi cosi voga presto welfare'.split():
         add_project("/home/john/repositories/" + p)

Note that the :meth:`split` method on a string splits that string on
every whitspace:

>>> 'lino xl book noi cosi voga presto welfare'.split()
['lino', 'xl', 'book', 'noi', 'cosi', 'voga', 'presto', 'welfare']


Looping over projects
=====================

Now you can do::

  $ pp inv initdb test

This loops over all your projects, initializes the demo databases of
that project and then runs the test suite. The whole process takes 20
minutes on my machine when there's no error.  If any error occurs,
then you need to find out the reason.

Possible reasons for failures are:

- :message:`PodError: An error occurred during the conversion. Could
  not connect to LibreOffice on port 8100. UNO (LibreOffice API) says:
  Connector : couldn't connect to socket (Success).`

  The means that you don't have the LibreOffice server running.
  See :ref:`admin.oood`

- Some dependency is not installed on your machine.

- Some test suite is broken.

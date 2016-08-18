.. _dev.setup:
.. _dev.env:

================================
Setting up your work environment
================================

.. how to test just this document:

   $ python setup.py test -s tests.LibTests.test_runtests

As a Lino developer you are going to maintain and know a whole little
collection of projects:
:ref:`noi`,
:ref:`cosi`,
:ref:`voga`,
:ref:`presto`,
:ref:`welfare`,
and :ref:`extjs6`.

You don't need to dive into each of them right now, but let's already
install them.




Remember that in :ref:`lino.dev.install` you did::

  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/lino.git
  $ git clone https://github.com/lino-framework/xl.git
  $ git clone https://github.com/lino-framework/book.git

Now clone the also the following other repositories in a similar way::
  
  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/noi.git
  $ git clone https://github.com/lino-framework/cosi.git
  $ git clone https://github.com/lino-framework/voga.git
  $ git clone https://github.com/lino-framework/presto.git
  $ git clone https://github.com/lino-framework/welfare.git
  $ git clone https://github.com/lino-framework/extjs6.git

And then you install them using pip (as editable using ``-e``
option)::

  $ pip install -e noi
  $ pip install -e cosi
  $ pip install -e voga
  $ pip install -e presto
  $ pip install -e welfare
  $ pip install -e extjs6
  
As a last step we must tell :ref:`atelier` about these new projects.
Open your :xfile:`~/.atelier/config.py` file which should contain::
  
     add_project("/home/john/projects/mylets")
     add_project("/home/john/projects/hello")
     for p in ('lino', 'xl', 'book'):
         add_project("/home/john/repositories/" + p)

Change that to::

     add_project("/home/john/projects/mylets")
     add_project("/home/john/projects/hello")
     for p in 'lino xl book noi cosi voga presto welfare extjs6'.split():
         add_project("/home/john/repositories/" + p)

Note that the :meth:`split` method on a string splits that string on
every whitspace:

>>> 'foo bar  baz'.split()
['foo', 'bar', 'baz']


How to switch to the development version of Atelier
===================================================

One day we might decide tht you should switch to the development
version of :ref:`atelier`.
     
The :ref:`atelier` package has been automatically installed as a
dependency of :mod:`lino`. That is, you are using the officially
released PyPI version. So you must uninstall it first::
  
  $ pip uninstall atelier

  $ cd ~/repositories
  $ git clone https://github.com/lsaffre/atelier.git  
  $ pip install -e atelier
  
Open your :xfile:`~/.atelier/config.py` file and insert ``atelier`` to
the list of projects::
  
     for p in 'atelier lino xl book noi cosi voga presto welfare extjs6'.split():

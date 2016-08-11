.. _dev.runtests:

===========================
Running the Lino test suite
===========================

This section explains how to run the test suite for the Lino
framework.

.. _dev.setup:

Setting up your work environment
================================

In :ref:`lino.dev.install` you did::

  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/lino.git
  $ git clone https://github.com/lino-framework/xl.git
  $ git clone https://github.com/lino-framework/book.git

As a member of the Lino core team you will also clone the other
repositories supported by our team.::
  
  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/noi.git
  $ git clone https://github.com/lino-framework/cosi.git
  $ git clone https://github.com/lino-framework/voga.git
  $ git clone https://github.com/lino-framework/presto.git
  $ git clone https://github.com/lino-framework/welfare.git  

  $ pip install -e noi
  $ pip install -e cosi
  $ pip install -e voga
  $ pip install -e presto
  $ pip install -e welfare
  
If you want a development version of :ref:`atelier`, then you can do::
  
  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/atelier.git
  $ pip uninstall atelier   # uninstall PyPI version
  $ pip install -e atelier  # install development version
  

  
:cmd:`go`
     

.. _dev.tours:

================
Screenshot tours
================

A **screenshot tour** is a page of documentation containing a series
of reusable screenshots generated and maintained by a script.

Screenshot tours could become an integral part of the Lino test suite
because generating them fails when something at the web interface is
broken.  They are not yet run automatically because we did not yet
find out how to automatically start and stop development servers on
different demo projects.  Until that problem is fixed, we must run
each tour manually as described below.

Screenshot tours are done using the :mod:`lino.api.selenium` module.

How to run a screenshot tour
============================

The ``XXX`` in the following instructions must be replaced by ``team``
because that's currently our first tour.  But we plan to extend the
system to other demo projects as well.
  
- Open a first terminal and run a devserver on a virgin XXX project::
    
    $ go book
    $ cd lino_book/projects/XXX
    $ python manage.py prep --noinput
    $ python manage.py runserver

  Leave that server running.

- Open a second terminal::  

    $ go book
    $ python docs/tours/XXX/maketour.py

This command will overwrite the :file:`index.rst` and :file:`*.png`
files in the :file:`docs/tours/XXX` directory.


The :xfile:`maketour.py` file
=============================

Every screenshot tour has its  :xfile:`maketour.py` file.

.. xfile:: maketour.py

The :xfile:`maketour.py` file for team currently generates only one
screenshot (:file:`login1.png`). It fails shortly after that first
one. The traceback of this failure shows that it happens somewhere
below `send_keys
<http://selenium-python.readthedocs.io/api.html#selenium.webdriver.common.action_chains.ActionChains.send_keys>`__. I
guess that the Selenium API has changed since I wrote that code.

The :xfile:`maketour.py` usually leaves a file :file:`geckodriver.log`
which might contain interesting information.



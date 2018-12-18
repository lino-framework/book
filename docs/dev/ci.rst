.. _lino.ci:

======================
Continuous integration
======================

A nice introduction to `Continuous integration <https://en.wikipedia.org/wiki/Continuous_integration>`_
is written by Kristijan Ivancic
on `RealPython <https://realpython.com/python-continuous-integration/>`__.

The Lino Team uses the TravisCI service for doing it.
Our home page there is https://travis-ci.org/lino-framework

It happens regularily that some build fails there, and we have a
sticky ticket (:ticket:`269`) just for this case: to analyze and
repair these failures.

Configuration
=============

The following files are important

.. xfile:: .travis.yml

    Most projects have a :xfile:`.travis.yml` file which specifies
    what TravisCI should do after each commit.

.. xfile:: requirements.txt

    Most projects have a :xfile:`requirements.txt` file which
    specifies additional requirements (to those specified in the
    project's :ref:`install_requires`.


Dependencies
============

cairocffi<0.7
-------------

html5lib==1.0b8
---------------

odfpy>1.3
---------

    
Notes
=====

Some notes which might be useful


- beautifulsoup4, html5lib, reportlab and pisa are actually needed
  only when you want to run the test suite, not for normal operation.
  Despite this they must be specified in :ref:`install_requires`, not
  in `tests_require`, because the doctests are run in the environment
  specified by `install_requires`.


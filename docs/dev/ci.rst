.. _lino.ci:

======================
Continuous integration
======================

A nice introduction to `Continuous integration
<https://en.wikipedia.org/wiki/Continuous_integration>`_ is written by Kristijan
Ivancic on `RealPython
<https://realpython.com/python-continuous-integration/>`__.

The Lino Team uses the TravisCI service for doing CI, but is moving to GitLab
little by little.

Our home page on Travis is https://travis-ci.org/lino-framework on GitLab it is
https://gitlab.com/lino-framework

It happens regularly that some build fails there, and we have a sticky ticket
(:ticket:`269`) just for this case: to analyze and repair these failures.

Configuration
=============

The following files are important

.. xfile:: .travis.yml

    A file in the root directory of a repository that specifies what TravisCI
    should do after each commit.

.. xfile:: .gitlab-ci.yml

    A file in the root directory of a repository that specifies what GitLab
    CI/CD should do after each commit.

.. xfile:: requirements.txt

    A file in the root directory of a repository that  specifies additional
    requirements (to those specified in the project's :ref:`install_requires`.

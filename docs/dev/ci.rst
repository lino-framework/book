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

    https://docs.gitlab.com/ee/ci/yaml/

.. xfile:: requirements.txt

    A file in the root directory of a repository that  specifies additional
    requirements (to those specified in the project's :ref:`install_requires`.





.. glossary::

  job artifact

    In a :xfile:`.gitlab-ci.yml` file, the artifacts of a job are the files and
    directories to "attach" to a job . When the job has finished, the specified
    files and directories are uploaded to the production server from where they
    are available for download as a single archive via web UI or API.  They are
    kept for 1 week be default.

    A job artifact can have properties like `when` (whether to upload them only
    on success, only when it fails, or in both cases) or `expire_in` (how long
    to keep the artifacts).

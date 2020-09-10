====================================
The :cmd:`getlino startsite` command
====================================

.. command:: getlino startsite

.. program:: getlino startsite

The script will ask you some questions:

.. rubric:: Run-time behaviour options:

.. option:: --batch

  Whether to run in batch mode, i.e. without asking any questions.  Assume
  yes to all questions. Don't use this on a machine that is already being
  used.

.. rubric:: Settings for the new site

.. option:: --dev-repos

    A space-separated list of repositories for which this site uses the
    development version (i.e. not the PyPI release).

    Usage example::

        $ getlino startsite avanti mysite --dev-repos "lino xl"

    Not that the sort order is important. The following would not work::

        $ getlino startsite avanti mysite --dev-repos "xl lino"

.. option:: --shared-env

    Full path to the shared virtualenv to use for this site.
    Default value is the value specified during :option:`getlino configure --shared-env`
    If this is empty, the new site will get its own virgin environment.

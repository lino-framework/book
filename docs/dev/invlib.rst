.. _lino.invlib:

======================================
``inv`` tasks defined by Lino
======================================

The ``inv`` command has been installed into your Python environment by
the invoke_ package, which itself has been required by the atelier_
package.

.. _invoke: http://www.pyinvoke.org/
.. _atelier: http://atelier.lino-framework.org/

The ``inv`` command is a kind of make tool which works by looking for
a file named :xfile:`tasks.py`. The Lino repository contains such a
file, and this file uses :mod:`lino.invlib`, which defines a whole
series of subcommands ("tasks") like :cmd:`inv prep` or :cmd:`inv
test`.

Most of these tasks are documented in the ateler docs
:ref:`atelier.invlib`.

Lino adds one task and one configuration settings to those defined by
atelier.

Tasks
=====

.. command:: inv prep

    Prepare a test run. This currently runs :manage:`prep` on every
    demo project defined by :envvar:`demo_projects`.


Configuration settings
======================

This lists the Lino-specific settings available in your
:xfile:`tasks.py` when it uses :mod:`lino.invlib`.  See also
:class:`atelier.invlib`.

.. envvar:: demo_projects

    The list of *Django demo projects* included in this project.

    Django demo projects are used by the test suite and the Sphinx
    documentation.  Before running :command:`inv test` or
    :command:`inv bd`, they must have been initialized.  To initialize
    them, run :command:`inv initdb`.

    It is not launched automatically by :command:`inv test` or
    :command:`inv bd` because it can take some time and is not always
    necessary.



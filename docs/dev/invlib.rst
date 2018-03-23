.. _lino.invlib:

====================
What means ``inv`` ?
====================

The :cmd:`inv` command has been installed into your Python environment
by the invoke_ package, which itself has been required by the atelier_
package.

.. _invoke: http://www.pyinvoke.org/
.. _atelier: http://atelier.lino-framework.org/

The :cmd:`inv` command is a kind of make tool which works by looking
for a file named :xfile:`tasks.py`.  Every repository of the Lino
framework contains such a file, and they all import a whole series of
subcommands ("tasks") like :cmd:`inv prep` or :cmd:`inv test`.  These
tasks are defined in :mod:`atelier.invlib` and documented in the docs
of the atelier_ package: :ref:`atelier.invlib`.



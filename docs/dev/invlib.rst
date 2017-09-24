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
for a file named :xfile:`tasks.py`. The Lino repository contains such
a file, and this file uses :mod:`atelier.invlib`, which defines a
whole series of subcommands ("tasks") like :cmd:`inv prep` or
:cmd:`inv test`.  These tasks are documented in the ateler docs
:ref:`atelier.invlib`.



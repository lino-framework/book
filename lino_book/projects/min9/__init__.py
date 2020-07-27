"""A minimal application used by a number of tests and tutorials. It
is not meant to be actually useful in the real world.

The basic idea of min9 is to have most plugins installed. So it is the least
minimal of this series.

This is also a **usage example** of :ref:`plugin_inheritance` because if
overrides the :mod:`lino_xl.lib.contacts` plugin by its own version
``lino.projects.min9.modlib.contacts`` (which is not included in this
documentation tree for technical reasons, and anyway you should
inspect the source code if you want to go futher).

The package has a unit test suite for testing some of the plugins it uses:

.. autosummary::
   :toctree:

   tests.test_addresses
   tests.test_birth_date
   tests.test_min2
   tests.test_cal

"""

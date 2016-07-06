"""A minimal application used by a number of tests and tutorials. It
is not meant to be actually useful in the real world.

It is a little bit less minimal than :mod:`lino.projects.min1` in that
it adds some more modlib plugins:

- :mod:`lino.modlib.changes`
- :mod:`lino_xl.lib.excerpts`
- :mod:`lino_xl.lib.addresses`
- :mod:`lino_xl.lib.reception`
- :mod:`lino.modlib.sepa`
- :mod:`lino_xl.lib.notes`
- :mod:`lino_xl.lib.projects`
- :mod:`lino_xl.lib.humanlinks`
- :mod:`lino_xl.lib.households`
- :mod:`lino_xl.lib.pages`

This is also a **usage example** of :ref:`app_inheritance` because if
overrides the :mod:`lino_xl.lib.contacts` plugin by its own version
``lino.projects.min2.modlib.contacts`` (which is not included in this
documentation tree for technical reasons, and anyway you should
inspect the source code if you want to go futher).

The package has a **test suite** for testing some of the plugins it
uses:

.. autosummary::
   :toctree:

   tests.test_addresses
   tests.test_birth_date
   tests.test_min2
   tests.test_cal

"""

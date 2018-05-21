"""
A fictive application used to satisfy Sphinx autodoc when
generating the API documentation for :ref:`book`.

It contains a settings module to be used as
:envvar:`DJANGO_SETTINGS_MODULE` when Sphinx generates the Lino docs.
See :ref:`lino.dev.bd`.

It installs (almost) all plugins, which makes no sense in practice and
would maybe raise errors if you try to initialize a database or
validate the models, but it is enough to have autodocs do its job.
And that's all we want.


.. autosummary::
   :toctree:


    settings
"""

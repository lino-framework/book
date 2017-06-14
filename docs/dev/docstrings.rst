.. _dev.docstrings:

============================
Where to put your docstrings
============================

This document describes our recommended way for organizing the
docstrings for your API docs.

The autosummary Sphinx extension is not really suitable for
documenting plugins because

- you can load only one Django application per Python process.
- the model definitions and certain functionalities of a Lino plugin
  may change depending on which other plugins are installed in a given
  application.
- the class definitions of a plugin may be spread over different
  modules (:xfile:`models.py`, :xfile:`desktop.py`,
  :xfile:`choicelists.py`, :xfile:`roles.py`...), but this is an
  implementation detail because Django anyway groups them into a
  common namespace (their :attr:`app_label`).
  
Our solution to these problems is to not use autosummary but to create
one (or several) specs pages. Usage example is
:mod:`lino.modlib.users` where all the docstrings have been moved to
the :ref:`specs`. I believe that this is now finally our prefererred
way for structuring the documentation of a plugin. I created
:ticket:`1708` for this and started this document.

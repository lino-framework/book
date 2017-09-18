========================
The runtime API (``rt``)
========================

The :mod:`lino.api.rt` module is a shortcut to miscellaneous functions
and classes which are often used "at runtime", i.e. when the Django
machine has been initialized.

You may *import* it at the global namespace of a :xfile:`models.py`
file, but you can *use* most of it only when the :func:`startup`
function has been called.


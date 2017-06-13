=================================
The :func:`inject_field` function
=================================

Lino has a feature which is when one plugin adds a field on a model in
another plugin using the :func:`dd.inject_field
<lino.core.inject.inject_field>` function.


Here is a list of the plugins which use :doc:`inject_field`.


- :mod:`lino.modlib.notify` injects two fields into auth.User
  
- :mod:`lino.modlib.uploads` (if you define shortcut fields
  (:class:`lino.modlib.uploads.choicelists.Shortcuts`)
  
- :mod:`lino_xl.lib.coachings`
- :mod:`lino_xl.lib.reception`
- :mod:`lino_xl.lib.cal`
- :mod:`lino_xl.lib.notes`
- :mod:`lino_xl.lib.teams`
- :mod:`lino_xl.lib.excerpts`




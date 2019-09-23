===================================
Multiple front ends for a same site
===================================

You can configure two different "web sites" which serve a same :term:`Lino site`.

Create the Lino site as usual using :cmd:`getlino startsite`.

In the project directory of the site, create a file named
:file:`settings_react.py` with this content::

  from .settings import *

  class Site(Site):
      default_ui = "lino_react.react"

  x = DATABASES, SECRET_KEY

  SITE = Site(globals())  # this will set new values for DATABASES and SECRET_KEY

  DATABASES, SECRET_KEY = x

Create a :file:`manage_react.py` file as a copy of :xfile:`manage.py`.  Modify
the copy to point to  the :file:`settings_react.py` file.

Create a file :xfile:`wsgi_react.py` as a copy of  :xfile:`wsgi.py`. Modify also
this copy to point to  the :file:`settings_react.py` file.

Manually copy the supervisor and nginx or apache config files.

No need to run a second linod.

Perhaps you must install the alternative front end into the virtualenv::

  $ . env/bin/activate
  $ pip install lino_react

  

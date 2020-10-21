.. _hosting.multiple_frontends:

===================================
Multiple front ends for a same site
===================================

You can configure two different Django projects (web sites) to serve a same
:term:`Lino site`. They will have different domain names and nginx
configurations, but share the same application code and database. The
:xfile:`settings.py` file of one of them will import the settings of the other
one, and will basically just change the :attr:`default_ui
<lino.core.site.Site.default_ui>` setting.

Create the Lino site as usual using :cmd:`getlino startsite` and selecting extjs
as front end.

In the project directory of the site, create a file named
:file:`settings_react.py` with this content::

  from .settings import *

  class Site(Site):
      default_ui = "lino_react.react"

  x = DATABASES, SECRET_KEY

  # the following will set new values for DATABASES and SECRET_KEY, which we are
  # going to restore from those we imported previously.

  SITE = Site(globals())

  DATABASES, SECRET_KEY = x

Create a :file:`manage_react.py` file as a copy of :xfile:`manage.py`.  Modify
the copy to point to  the :file:`settings_react.py` file.

Create a file :xfile:`wsgi_react.py` as a copy of  :xfile:`wsgi.py`. Modify also
this copy to point to  the :file:`settings_react.py` file.

Manually copy the supervisor and nginx or apache config files.

No need to run a second linod.

Install the alternative front end into the virtualenv::

  $ . env/bin/activate
  $ pip install lino_react

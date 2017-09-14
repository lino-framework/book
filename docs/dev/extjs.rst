.. _lino.dev.extjs:

Debugging generated ExtJS Javascript code
=========================================

.. xfile:: lino_XXX_yy.js
.. xfile:: linoweb.js

At server startup the :mod:`lino.modlib.extjs` (or
:mod:`lino_extjs6.extjs`) user interface generates a series of files
named :xfile:`lino_XXX_yy.js` which contain the client side
application logic.  The first part of this file comes from a file
:srcref:`lino/modlib/extjs/linoweb.js`, the second part is generated
from your models, tables, layouts and actions.

When you modified your copy of :xfile:`linoweb.js` in order to debug
it, there are some pitfalls:

A **first pitfall** is that when you modify :xfile:`linoweb.js`, your
development server does not automatically restart. This is because it
watches only the `.py` files for changes.  A development server
constantly watches the timestamps of all Python source files and
reloads itself automatically if something has changed. This is a
convenient feature of Django which BTW works only in a developement
server, not e.g. when serving your site on a production server.
Actually Django's :manage:`runserver` command also detects changes in
Django templates, but :xfile:`linoweb.js` is not a Django template.

A quick workaround is to `touch` the timestamp of a Python file::

    $ touch manage.py
    
A **second pitfall** is that when the process restarted, Lino does not
yet create the :xfile:`lino_XXX_yy.js` file. You must first hit
:kbd:`Ctrl-R` in your browser and watch for a next message in the
Python console::

  INFO Building /lino_cache/team/media/cache/js/lino_000_en.js ...

This is because Lino by default generates the Javascript cache file
*lazily*, i.e. only when there is an incoming request. You can change
this behaviour by setting :attr:`build_js_cache_on_startup
<lino.core.site.Site.build_js_cache_on_startup>` to `True`. But when
debugging this is not convenient because it causes Lino to generate
*all* Javascript files (one file per user type and language), which
can take quite some time.


And then there is **a third pitfall!** Lino does not correctly detect
*every* code source change. This is probably a bug. Lino seems to
watch only the source of those modules which were loaded when the
kernel started to startup. Observe the `code_mtime` attribute of
:class:`lino.core.kernel.Kernel` for details.  But that bug is not
important to explore since it occurs only on a development server.

In case of doubt, just watch whether the message :message:`INFO
Building /lino_cache/.../media/cache/js/lino_000_en.js` comes when you
hit :kbd:`Ctrl-R`. If it doesn't, then touch another code file.



.. xfile:: lino.css

The ExtJS 

.. _djangomig:

===========================
Django migrations with Lino
===========================

With Lino version 19.8 and later, you can do Django migrations with Lino.

Each Lino production site which defines their own :attr:`languages
<lino.core.site.Site.languages>` setting  must have its own migrations package
and run their local :manage:`makemigrations` before actually running
:manage:`migrate`.

With :attr:`languages <lino.core.site.Site.languages>` and babelfields, the
developer cannot make migrations for you, they must be build for every
production site.


Migrating from a pre Lino 19.8 site
===================================

(TODO) 

.. _djangomig:

===========================
Django migrations with Lino
===========================

With Lino version 19.8 and later, you can do Django migrations with Lino.

TODO: is the old system (:doc:`datamig`) still possible at all?

Each :term:`Lino production site` which defines their own :attr:`languages
<lino.core.site.Site.languages>` setting (and ATM they all do it) must have its
own migrations package and run their local :manage:`makemigrations` before
actually running :manage:`migrate`.

With :attr:`languages <lino.core.site.Site.languages>` and babelfields, the
developer cannot make migrations for you, they must be build for every
production site.



Migrating from a pre Lino 19.8 site
===================================

Converting existing

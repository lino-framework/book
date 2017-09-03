.. _lino.about:

==========
About Lino
==========

**Lino** is a high-level framework for writing customized database
applications based on `Django <https://www.djangoproject.com/>`_ and
and `Sencha ExtJS <http://www.sencha.com/products/extjs/>`_.

A **database application** is a computer program whose primary purpose
is entering and retrieving information from a database (`Wikipedia
<https://en.wikipedia.org/wiki/Database_application>`__).  A
**customized** database application is one which is taylored to your
needs.  A **framework** means that Lino is designed to be **used by
professional** developers who write and maintain applications for
their employer or their customers.

Primary **target users** of Lino applications are organizations who
need a customized database application "better than MS-Access for
cheaper than SAP".

From the system administrator's point of view, Lino applications are
**just Django** projects.  People who know how to host a Django
project can also host a Lino application.  The **advantages** of Lino
versus plain Django are visible for the developer (technical details
in :doc:`lino_and_django`), but these advantages are indirectly
tangible to their customers because certain parts of the **development
process become easier** and cheaper: analysis, writing a prototype,
adapting your application to changed needs and long-term maintenance.

Typical Lino applications have a rather **complex database
structure**.  For example Lino Welfare has 155 models in 65 plugins.
Even Lino Noi (the smallest Lino application which is being used on a
production site) has 44 models in 32 plugins.

The growing collection of :ref:`lino.projects` can be used by
**service providers** who offer professional hosting of one of these
applications.


.. toctree::
   :maxdepth: 1

   why
   name
   more
   

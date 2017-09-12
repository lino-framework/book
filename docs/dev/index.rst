.. _lino.dev:

=================
Developer's Guide
=================

This is the central meeting place for :doc:`Lino developers
</community/developers>`.


.. _lino.dev.start:

Getting started
===============


.. toctree::
   :maxdepth: 1
   :hidden:

   install
   /tutorials/hello/index
   polls/index
   projects
   env

1.  :doc:`/dev/install` : System requirements. Set up a Python
    environment. Run your first Lino applications.

2.  :doc:`/tutorials/hello/index` : The first Lino application running
    on your machine. It's easier than with Django. A ``settings.py``
    and a ``manage.py``.

3.  :doc:`polls/index` : Convert the "Polls"
    application from Django’s tutorial into a Lino application. This
    will illustrate some differences between Lino and Django.

4. :doc:`projects` introduces our minimalistic project
   management system based on :mod:`atelier`.
   
5. :doc:`env` : install other projects maintained by the Lino team.
   If you want to join our team and help us to make Lino better, then
   you will sooner or later get in touch with these
   applications. Let's install them already now so that your
   environment is complete.

   
.. _lino.dev.first:

Your first application
======================

.. toctree::
   :hidden:

   /tutorials/dumpy/index
   tables
   layouts
   initdb


10.  :doc:`/tutorials/dumpy/index` : Playing with Python fixtures.
     Writing your own Python fixtures.

#.  :doc:`tables` : Models, tables and views. What is a
    table? Designing your tables. Using tables without a web server.

#.  :doc:`layouts` : About layouts, detail windows, data elements and
    panels.

#.  :doc:`initdb` : More about the ``initdb`` and ``prep``
    commands.



The Lino design choices
=======================

Now we think it is time to explain some fundamental differences
between Lino and other frameworks.

.. toctree::
   :hidden:
              
   /about/faq
   /about/ui
   /about/lino_and_django
   /about/features
   /about/not_easy
   /about/think_python
   ui
    
20. :doc:`/about/faq`
#.  :doc:`/about/ui`
#.  :doc:`/about/features`
#.  :doc:`/about/lino_and_django`
#.  :doc:`/about/not_easy`
#.  :doc:`/about/think_python`
#.  :doc:`ui`
     


.. _lino.dev.team:

Working with others
===================

30. :doc:`pull`
#.  :doc:`runtests`
#.  :doc:`contrib`
#.  :doc:`patch`
#.  :doc:`request_pull`
#.  :doc:`ci`
#.  :doc:`versioning`


.. toctree::
   :hidden:

   pull
   runtests
   contrib
   patch
   request_pull
   ci
   versioning
   
   
Writing documentation
=====================

50. :doc:`/team/builddocs`
#. :doc:`/team/devblog`
#. :doc:`docstrings`
#. :doc:`doctests`

   
.. toctree::
   :hidden:

   /team/builddocs
   /team/devblog
   doctests
   docstrings


Getting acquaintained
=====================


60. Read Hamza's tutorial `Discovering Lino using your debugger
    <https://github.com/lino-framework/book/raw/master/docs/dev/discovering_lino_using_your_debugger.pdf>`__.
#.  :doc:`datamig`
#.  :doc:`perms`
#.  :doc:`settings` : The Django settings module. How Lino integrates
    into Django settings. Inheriting settings.
#.  :doc:`application` : An app is not an application.
#.  :doc:`summaries` : Introduction to table summaries.
#.  :doc:`plugins` : Why we need plugins. Configuring plugins.
#.  :doc:`users` : Why do we replace Django's user management. Passwords.
#.  :doc:`site` : Instantiating a `Site`.  Specifying the
    `INSTALLED_APPS`. Additional local apps.
#.  :doc:`dump2py` : Python dumps
#.  :doc:`site_config` : The SiteConfig used to store "global" site-wide
    parameters in the database.
#.  :doc:`languages` : if you write applications for users who don't
    speak English.
#.  :doc:`i18n` : About "internationalization" and "translatable strings".
#.  :doc:`menu` : Standard items of a main menu
#.  :doc:`actors`
#.  :doc:`choicelists`
#.  :doc:`parameters`
#.  :doc:`virtualfields`
#.  :doc:`ar` : Using action requests
#.  :doc:`html` : Generating HTML
#.  :doc:`custom_actions` : Writing custom actions
#.  :doc:`action_parameters` :
#.  :doc:`gfks` : Lino and `GenericForeignKey` fields
#.  :doc:`lets` : Write a new Lino application from scratch, in the
    hope that this helps you with writing your own Lino application.
#.  :doc:`/tutorials/layouts` :
#.  :doc:`actions` :
#.  :doc:`mldbc/index` :
#.  :doc:`plugin_inheritance` : Plugin inheritance
#.  :doc:`plugin_cooperation` : Plugin cooperation
#.  :doc:`printing` : (TODO)
#.  :doc:`cache` : telling Lino where to store temporari files.
#.  :doc:`rendering` : 
#.  :doc:`mti` : 

.. toctree::
   :maxdepth: 1
   :hidden:

   settings
   datamig
   perms
   application
   summaries
   plugins
   site
   dump2py
   site_config
   users
   languages
   i18n
   menu
   actors
   choicelists
   parameters
   ar
   virtualfields
   html
   custom_actions
   action_parameters
   gfks
   lets
   /tutorials/layouts
   actions
   mldbc/index
   plugin_inheritance
   plugin_cooperation
   printing
   cache
   rendering
   mti
   

Special topics
==============

.. toctree::
   :maxdepth: 1

   /specs/projects/mti
   /specs/projects/nomti
   watch
   /tutorials/workflows_tutorial/index
   /tutorials/matrix_tutorial/index

   /tutorials/input_mask/index

   setup

Drafts
======
   
.. toctree::
   :maxdepth: 1

   /tutorials/tested_docs/index
   startup
   workflows
   translate/index
   
   demo_projects
   testing
   help_texts
   userdocs
   signals
   intro
   style
   extjs
   overview
   inject_field


Other
-----

.. toctree::
   :maxdepth: 1

   /changes
   /todo
   /tested/index
   newbies/index
   git
   /ref/index
   py3
   logging
   linod
   design
   testing
   /team/deploy
   /team/noi_intro
   memo
   analysis
   bash_aliases
   diamond


.. toctree::
   :hidden:

   tables
   fields
   ad
   dd
   rt
   mixins
   /tutorials/index
   ml/index
   /team/index
   interview

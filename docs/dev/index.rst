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

   install
   hello/index
   env
   pull
   projects

..    
    #.  :doc:`/dev/install` : System requirements. Set up a Python
        environment. Run your first Lino applications.

    #.  :doc:`hello/index` : The first Lino project on your machine.

    #.  :doc:`env` : set up your Lino development environment.

    #.  :doc:`pull`

    #.  :doc:`projects` : play with the demo projects

   
Diving into Lino
================

In the first section we deliberately remained outside of the real code
because first things first.  Now you hopefully feel self-confident
about your work environment and running demo projects.  We are ready
to dive *into* Lino.

.. toctree::
   :maxdepth: 1

   polls/index
   warning
   django
   models
   mixins
   /about/lino_and_django
   initdb
   dumpy/index
   tables
   layouts/index
   choicelists
   perms
   users
   settings

..    
    10. :doc:`dive`

    #.  :doc:`polls/index` : In this tutorial we convert the "Polls"
        application from Django’s tutorial into a Lino application. This
        will illustrate some differences between Lino and Django.

    #.  :doc:`django`

    #.  :doc:`models`

    #.  :doc:`mixins`

    #.  :doc:`/about/lino_and_django`

    #.  :doc:`initdb` : More about the ``initdb`` and ``prep``
        commands.

    #.  :doc:`dumpy/index` : Playing with Python fixtures.
        Writing your own Python fixtures.

    #.  :doc:`tables` : Models, tables and views. What is a
        table? Designing your tables. Using tables without a web server.

    #.  :doc:`layouts/index` : About layouts, detail windows, data elements and
        panels.

    #.  :doc:`choicelists`

    #.  :doc:`users`

    #.  :doc:`perms`

    #.  :doc:`settings` : The Django settings module. How Lino integrates
        into Django settings. Inheriting settings.


Application development using Lino
==================================

Lino is for writing **customized** database applications. That means
that a development project starts when the customer explains to the
analyst their needs.

20. :doc:`analysis` : 
#.  :doc:`lets/index` : In this tutorial we write a new Lino application
    from scratch, with focus on some techniques for doing analysis.

.. toctree::
   :hidden:
              
   analysis
   lets/index
   

Lino design goals
=================
   
#.  :doc:`/about/faq`
#.  :doc:`/about/ui`
#.  :doc:`/about/features`
#.  :doc:`/about/not_easy`
#.  :doc:`/about/think_python`
#.  :doc:`ui`

.. toctree::
   :hidden:
              
   /about/faq
   /about/ui
   /about/features
   /about/not_easy
   /about/think_python
   ui
    
     


.. _lino.dev.team:

Working with others
===================

30. :doc:`runtests`
#.  :doc:`contrib`
#.  :doc:`patch`
#.  :doc:`request_pull`
#.  :doc:`ci`
#.  :doc:`versioning`


.. toctree::
   :hidden:

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


60. :doc:`datamig`
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
#.  :doc:`parameters`
#.  :doc:`virtualfields`
#.  :doc:`ar` : Using action requests
#.  :doc:`html` : Generating HTML
#.  :doc:`custom_actions` : Writing custom actions
#.  :doc:`action_parameters` :
#.  :doc:`gfks` : Lino and `GenericForeignKey` fields
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

   datamig
   application
   summaries
   plugins
   site
   dump2py
   site_config
   online
   languages
   i18n
   menu
   actors
   parameters
   ar
   virtualfields
   html
   custom_actions
   action_parameters
   gfks
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
   invlib

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
   bash_aliases
   diamond


.. toctree::
   :hidden:

   tables
   fields
   ad
   dd
   rt
   /tutorials/index
   ml/index
   /team/index
   interview

  

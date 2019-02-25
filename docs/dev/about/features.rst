========
Features
========
    
.. _lino.features:

Because Lino applications are Django projects, the following features
(copied from the `Django website <https://www.djangoproject.com/>`_)
also apply to Lino:

- **Object-relational mapper** :
  Define your data models entirely in Python. 
  You get a rich, dynamic database-access API for free -- 
  but you can still write SQL if needed.
  
- **Internationalization** :
  Django has full support for multi-language applications, 
  letting you specify translation strings and providing 
  hooks for language-specific functionality.  

- **Cache system** :
  Hook into memcached or other cache frameworks for super performance 
  -- caching is as granular as you need.
  
Lino then adds its own features to the above:

- An out-of-the-box front end.  We believe that application
  developers should *develop applications*, not waste their time
  writing html templates or css.  It is one of Lino's design goals to
  :doc:`separate business logic and front end <ui>`.

- :ref:`Layouts <layouts>`:
  Lino applications use the Python language not only
  for designing your *models* but also your *forms*.
  
- Lino adds enterprise-level concepts for definining 
  :ref:`permissions` and :ref:`workflows`.
  
- Lino  applications have a good support for managing
  :ref:`multilingual database content <mldbc>`.
  
- Lino provides tools for generating :ref:`userdocs`.
  
- Lino includes :ref:`dpy`, a great alternative to `Django's built-in
  migration system
  <https://docs.djangoproject.com/en/1.11/topics/migrations/>`_ to
  manage your :ref:`database migrations <datamig>`.
  
- Lino comes with a nice way for handling :ref:`polymorphism`.
  
- Lino includes :ref:`xl`, a collection of reusable plugins for all
  kinds of Lino applications.



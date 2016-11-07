=========================
Features and design goals
=========================
    
Design goals
------------

- Lino applications are intuitive and easy to understand for the end user.
  (see :doc:`values`)
- Lino applications are easy to maintain because Lino encourages
  sustainable application development.
- agile programming
- rapid prototyping 
- libraries of reusable code
- short release cycles
- stable 

.. _lino.features:

Features
--------

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

- An out-of-the-box :doc:`user interface <ui>`.  Lino application
  developers don't waste their time writing html templates or css.

- :ref:`Layouts <layouts>`:
  Lino applications use the Python language not only
  for designing your *models* but also your *forms*.
  
- Lino adds enterprise-level concepts for definining 
  :ref:`permissions` and :ref:`workflows`.
  
- :ref:`mldbc` : 
  Use Lino's rich experience with applications that manage 
  multilingual database content.
  
- Lino provides tools for generating :ref:`userdocs`.
  
- Lino includes :ref:`dpy`, a great alternative to `Django's built-in
  migration system
  <https://docs.djangoproject.com/en/dev/topics/migrations/>`_ to
  manage your :ref:`database migrations <datamig>`.
  
- Other features include extensions to handle :ref:`polymorphism`.
  
- And last but not least, Lino includes :ref:`xl`, a collection of
  reusable plugins for all kinds of Lino applications.

See also :doc:`think_python`.  



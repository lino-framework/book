.. _lino.tutorial.polls:

The Lino Polls tutorial 
=======================


.. how to test:
    $ python setup.py test -s tests.DocsTests.test_polls

In this tutorial we are going to convert the “Polls” application from
Django’s tutorial into a Lino application. This will illustrate some
differences between Lino and Django.

The result of this tutorial is available as a public live demo at
http://demo1.lino-framework.org


.. currentmodule:: lino.core.site

.. contents:: Table of Contents
 :local:
 :depth: 2


Create a local Django project
-----------------------------

Lino is a set of extensions for a Django project, so there is a lot of
Django know-how which applies to Lino applications as well.  So before
reading on, please follow parts 1 and 2 of the *Django* tutorial (just
parts 1 & 2, not the whole tutorial):

- `Writing your first Django app, part 1
  <https://docs.djangoproject.com/en/1.9/intro/tutorial01/>`__.  
- `Writing your first Django app, part 2
  <https://docs.djangoproject.com/en/1.9/intro/tutorial02/>`__.  

Done? You should now have a set of files in your "project directory"::

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py
        polls/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py


Two remarks about the Django tutorial:

- Don't worry if you found the `Write your first view
  <https://docs.djangoproject.com/en/1.9/intro/tutorial01/#write-your-first-view>`__
  section difficult, in Lino you don't need to write views.

- The `Explore the free admin functionality
  <https://docs.djangoproject.com/en/1.9/intro/tutorial02/#explore-the-free-admin-functionality>`__
  section was important only so you know what you are going to leave.
  Lino is an alternative to Django's Admin interface.

We now leave the Django philosophy and continue "the Lino way" of
writing web applications.  Some files remain unchanged:
:xfile:`__init__.py`, :xfile:`manage.py` and :xfile:`wsgi.py`.

You can *delete* the following files::

  $ rm mysite/urls.py
  $ rm polls/views.py
  $ rm polls/admin.py

And then we are now going to modify the files
:file:`mysite/settings.py` and :file:`polls/models.py`.

The :file:`settings.py` file
-----------------------------

Please change the contents of your :xfile:`settings.py` to the
following:

.. literalinclude:: settings.py

A few explanations:

#.  A Lino :xfile:`settings.py` file always defines (or imports) a
    **class** named ``Site`` which is a direct or indirect descendant of
    :class:`lino.core.site.Site`.  Our example also **overrides** that
    class before instantiating it.

#.  In the line ``SITE = Site(globals())`` we **instantiate** our
    class into a variable named ``SITE``. Note that we pass our
    :func:`globals` `dict` to Lino. Lino needs this to insert all
    those Django settings into the global namespace of our settings
    module.

#.  One of the Django settings managed by Lino is
    :setting:`INSTALLED_APPS`. In Lino you don't code this setting
    directly into your :xfile:`settings.py` file, you override your
    Site's :meth:`get_installed_apps
    <lino.core.site.Site.get_installed_apps>` method.  Our example
    does the equivalent of ``INSTALLED_APPS = ['polls']``, except for
    the fact that Lino automagically adds some more apps.
    
#.  The **main menu** of a Lino application is defined in the
    :meth:`setup_menu <lino.core.site.Site.setup_menu>` method.
    
Lino uses some tricks to make Django settings modules more pleasant to
work with, especially if you maintain Lino sites for several
customers. We will come back to this later.  More about all this in
:doc:`/dev/settings` and :doc:`/dev/site`

..
    >>> from pprint import pprint
    >>> from django.conf import settings
    >>> from atelier.utils import tuple_py2
    >>> pprint(tuple_py2(settings.INSTALLED_APPS))
    ('lino.modlib.lino_startup',
     'django.contrib.staticfiles',
     'lino.modlib.about',
     'lino.modlib.jinja',
     'lino.modlib.bootstrap3',
     'lino.modlib.extjs',
     'polls')


The :file:`models.py` file
--------------------------

Please change the contents of your :file:`polls/models.py` to the
following:

.. literalinclude:: ../polls/models.py

A few explanations while looking at that file:

- The :mod:`lino.api.dd` module is a shortcut to most Lino extensions
  used by application programmers in their :xfile:`models.py` modules.
  `dd` stands for "data design".
  
- :class:`dd.Model <lino.core.model.Model>` is an optional (but
  recommended) wrapper around Django's Model class.  For this tutorial
  you could use Django's `models.Model` as well, but in general we
  recommend to use :class:`dd.Model <lino.core.model.Model>`.

- There's one **custom action** in our application, defined as the
  `vote` method on the `Choice` model, using the :func:`dd.action
  <lino.core.actions.action>` decorator. More about actions in the
  Actions_ section.


The :file:`desktop.py` file
---------------------------

Now please create (in the same directory as your :xfile:`models.py`) a
file named :file:`desktop.py` with the following content.

.. literalinclude:: ../polls/desktop.py

This file defines three **tables** for our application.  Tables are an
important new concept in Lino.  We will learn more about them in
another tutorial :ref:`lino.tutorial.tables`.  For now just note that

- we defined one table per model (`Questions` for the `Question` model
  and `Choices` for the `Choice` model)

- we defined one additional table `ChoicesByQuestion` which inherits
  from `Choices`. This table shows the choices *for a given question*.
  We call it a *slave table* because it *depends* on its "master"
  which (in this case) must be a question instance.

  
Changing the database structure
-------------------------------

One more thing before seeing a result.  We made at least one change in
our :xfile:`models.py` file after the Django tutorial: we added the
`hidden` field of a Question::

    hidden = models.BooleanField(
        "Hidden",
        help_text="Whether this poll should not be shown in the main window.",
        default=False)

To be more precise: Django and Lino "know" that we added a field named
`hidden` in the `Questions` table of our database, **but** the database
doesn't yet know it.  If you would run your application now, then you
would get some "operational" database error because Lino would ask the
database to read or update this field, and the database would answer
that there is no field named "hidden".  We must tell our database that
the structure has changed.

For the moment we are just going to *reinitialize* our database,
i.e. *delete* any data you may have manually entered during the Django
Polls tutorial and turn the database into a virgin state::

    $ python manage.py initdb_demo

The output should be::

    Operations to perform:
      Synchronize unmigrated apps: about, jinja, staticfiles, polls, lino_startup, extjs, bootstrap3
      Apply all migrations: (none)
    Synchronizing apps without migrations:
      Creating tables...
        Running deferred SQL...
    Running migrations:
      No migrations to apply.
    Installed 13 object(s) from 1 fixture(s)

..
    >>> from django.core.management import call_command
    >>> call_command('initdb_demo', interactive=False, verbosity=0) 


Adding a demo fixture
---------------------

This section is optional and recommended in case you were frustrated
when we deleted the data you had manually entered during the Django
Polls tutorial.

When you are developing and maintaining a database application, it
happens very often that you need to change the database structure.

Instead of manually filling your demo data again and again after every
database change, you write it once as a *fixture*.

With Lino it is easy and fun to write demo fixtures because you can
write them in Python.  Read more about them in
:ref:`lino.tutorial.dpy`, or simply stay here and learn by doing.

We are now going to add a **demo fixture**.

- Create a directory named :file:`fixtures` in your :file:`polls`
  directory.

- Create an empty file named :xfile:`__init__.py` in that directory.

- Still in the same directory, create another file named ``demo.py``
  with the following content:

  .. literalinclude:: ../polls/fixtures/demo1.py

- If you prefer, the following code does exactly the same but has the
  advantage of being more easy to maintain:

  .. literalinclude:: ../polls/fixtures/demo.py

- Run the following command (from your project directory) 
  to install these fixtures::

    $ python manage.py initdb demo

  The output should be::

    Operations to perform:
      Synchronize unmigrated apps: about, jinja, staticfiles, polls, lino_startup, extjs, bootstrap3
      Apply all migrations: (none)
    Synchronizing apps without migrations:
      Creating tables...
        Running deferred SQL...
    Running migrations:
      No migrations to apply.
    Installed 13 object(s) from 1 fixture(s)

..
    >>> from lino.api.doctest import *
    >>> from atelier.sheller import Sheller
    >>> shell = Sheller()
    >>> shell("python manage.py initdb demo --noinput -v 0")
    <BLANKLINE>   
    
    >>> rt.show('polls.Questions')  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    ==== ================================ ===================== ========
     ID   Question text                    Date published        Hidden
    ---- -------------------------------- --------------------- --------
     1    What is your preferred colour?   ...        00:00:00   No
     2    Do you like Django?              ...        00:00:00   No
     3    Do you like ExtJS?               ...        00:00:00   No
    ==== ================================ ===================== ========
    <BLANKLINE>   
    
    >>> shell("python manage.py initdb demo1 -v 0 --noinput")  #doctest: +ELLIPSIS
    <BLANKLINE>   
    
    >>> rt.show('polls.Questions')  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    ==== ================================ ===================== ========
     ID   Question text                    Date published        Hidden
    ---- -------------------------------- --------------------- --------
     1    What is your preferred colour?   ...        00:00:00   No
     2    Do you like Django?              ...        00:00:00   No
     3    Do you like ExtJS?               ...        00:00:00   No
    ==== ================================ ===================== ========
    <BLANKLINE>   
    
    >>> shell("python manage.py initdb_demo --noinput -v 0")
    <BLANKLINE>   
    
    >>> rt.show('polls.Questions')  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    ==== ================================ ===================== ========
     ID   Question text                    Date published        Hidden
    ---- -------------------------------- --------------------- --------
     1    What is your preferred colour?   ...        00:00:00   No
     2    Do you like Django?              ...        00:00:00   No
     3    Do you like ExtJS?               ...        00:00:00   No
    ==== ================================ ===================== ========
    <BLANKLINE>   
    
    
  
Starting the web interface
--------------------------

Now we are ready to start the development web server on our project::

  $ cd ~/mypy/mysite
  $ python manage.py runserver
  
or (on Windows)::

  c:\mypy\mysite> python manage.py runserver
  
and point your browser to http://127.0.0.1:8000/ 
to see your first Lino application running.

- Please play around and create some polls before reading on.



The main index
--------------
  
The following template is used to build the HTML to be displayed in
our Main Window.

Create a directory named :file:`mysite/config`, and in that directory
create a file named :xfile:`admin_main.html` with the following
content:

.. literalinclude:: config/admin_main.html

Explanations:

- :attr:`rt.models <lino.core.site.Site.models>` : is a shortcut to access the models and tables of the application.
  Usually it is better to write
  
  ::

    Question = rt.models.polls.Question

  instead of
  
  ::

    from polls.models import Question
  
  because the latter hard-wires the location of the `polls` plugin.
    
- If `objects`, `filter()` and `order_by()` are new to you, 
  then please read the `Making queries 
  <https://docs.djangoproject.com/en/1.9/topics/db/queries>`__
  chapter of Django's documentation. 
  Lino is based on Django, and Django is known for its good documentation. Use it!

- If `joiner` and `sep` are a riddle to you, you'll find the 
  solution in Jinja's `Template Designer 
  Documentation <http://jinja.pocoo.org/docs/templates/#joiner>`__.
  Lino applications by default replace Django's template engine by Jinja.

- ``obj.vote`` is an :class:`InstanceAction <lino.core.actions.InstanceAction>`,
  and we call its 
  :meth:`as_button <lino.core.actions.InstanceAction.as_button>`
  method
  which returns a HTML fragment that displays a button-like 
  link which will run the action when clicked.
  More about this in Actions_.



Screenshots
-----------

Make sure that you understand and can reproduce the concepts explained
in this section.


The **Main Window** is the top-level window of your application:

.. image:: polls1.jpg
    :scale: 50
    
Your application specifies what to put there, and there are several 
methods to do this:

- define a custom :xfile:`admin_main.html` template (as we did in this
  tutorial)

- use the default :xfile:`admin_main.html` template and override the
  :meth:`get_admin_main_items
  <lino.core.site.Site.get_admin_main_items>` and
  :meth:`setup_quicklinks <lino.core.site.Site.setup_quicklinks>`
  methods.

- override the :meth:`get_main_html
  <lino.core.site.Site.get_main_html>` method to return your own chunk
  of html.
    
After clicking on a vote, here is the `vote` method 
of our `Choice` model in action:

.. image:: polls2.jpg
    :scale: 50
    
    
After selecting :menuselection:`Polls --> Questions` in the main menu, 
Lino opens that table in a **grid window**:
    
.. image:: polls3.jpg
    :scale: 50
    
Every table can be displayed in a **grid window**, a tabular 
representation with common functionality such as sorting, 
setting column filters, editing individual cells, 
and a context menu.
  
After double-clicking on a row in the previous screen, Lino shows the
**detail window** on that Question:

.. image:: polls4.jpg
    :scale: 50
    
This window has been designed by the following code in 
your :file:`desktop.py` file::

    detail_layout = """
    id question_text
    hidden pub_date
    ChoicesByQuestion
    """

To add a detail window to a table, you simply add a
:attr:`detail_layout <lino.core.actors.Actor.detail_layout>` attribute
to the Table's class definition.
    
Not all tables have a detail window.  In our case the `Questions`
table has one, but the `Choices` and `ChoicesByQuestion` tables don't.
Double-clicking on a cell of a Question will open the Detail Window,
but double-clicking on a cell of a Choice will start cell editing.
Note that can still edit an individual cell of a Question in a Grid
Window by pressing the :kbd:`F2` key.

  **Exercise**: comment out above lines in your code and observe how
  the application changes its behaviour.


  
After clicking the :guilabel:`New` button, you can admire an **Insert
Window**:

.. image:: polls5.jpg
    :scale: 50
    
This window layout is defined by the following :attr:`insert_layout
<lino.core.actors.Actor.insert_layout>` attribute::

    insert_layout = """
    question
    hidden
    """
    
(Again: see :doc:`/tutorials/layouts` for more explanations.)

After clicking the :guilabel:`[html]` button:

.. image:: polls6.jpg
    :scale: 50
    

Actions
-------

Lino has a class :class:`Action <lino.core.actions.Action>` 
which represents the methods who have a clickable button 
or menu item in the user interface. 

Each :class:`Action <lino.core.actions.Action>` instance holds a few important pieces
of information:

- label : the text to place on the button or menu item
- help_text : the text to appear as tooltip when the mouse is over that button
- permission requirements : specify for whom and under which
  conditions this action is available (a complex subject, we'll talk
  about it in a later tutorial)
- handler function : the function to execute when the action is invoked

Many actions are created automatically by Lino. For example:

- each table has a "default action" which is to open a window which
  displays this table as a grid.  That's why (in the :meth:`setup_menu
  <lino.core.plugin.Site.setup_menu>` function of your
  :file:`polls/models.py`) you can say::

    def setup_menu(site, ui, profile, main):
        m = main.add_menu("polls", "Polls")
        m.add_action('polls.Questions')
        m.add_action('polls.Choices')


  The :meth:`add_action <lino.core.menus.Menu.add_action>` method of
  Lino's :class:`lino.core.menus.Menu` is smart enough to understand
  that if you specify a Table, you mean in fact that table's default
  action.

- The :guilabel:`Save`, :guilabel:`Delete` and :guilabel:`New` buttons
  in the bottom toolbar of the Detail window have their own
  :class:`Action <lino.core.actions.Action>` instance.
  
Custom actions are the actions defined by the application developer.
Our tutorial has one of them:

.. code-block:: python

    @dd.action(help_text="Click here to vote this.")
    def vote(self, ar):
        def yes(ar):
            self.votes += 1
            self.save()
            return ar.success(
                "Thank you for voting %s" % self,
                "Voted!", refresh=True)
        if self.votes > 0:
            msg = "%s has already %d votes!" % (self, self.votes)
            msg += "\nDo you still want to vote for it?"
            return ar.confirm(yes, msg)
        return yes(ar)

The :func:`@dd.action <dd.action>` decorator can have keyword
parameters to specify information about the action. In practice these
may be :attr:`label <lino.core.actions.Action.label>`, :attr:`help_text
<lino.core.actions.Action.help_text>` and :attr:`required <lino.core.actions.Action.required>`.

The action method itself should have the following signature::

    def vote(self, ar, **kw):
        ...
        return ar.success(kw)
        
Where ``ar`` is an :class:`ActionRequest
<lino.core.requests.ActionRequest>` instance that holds information
about the web request which called the action.

- :meth:`callback <lino.core.requests.BaseRequest.callback>` 
  and :meth:`confirm <lino.core.requests.BaseRequest.callback>`
  lets you define a dialog with the user using callbacks.

- :meth:`success <lino.core.requests.BaseRequest.success>` and
  :meth:`error <lino.core.requests.BaseRequest.error>` are possible
  return values where you can ask the client to do certain things.



Summary
-------

In this tutorial we followed the first two chapters of the Django
Tutorial, then continued the Lino way and introduced two concepts
which Lino adds to Django: Tables and Actions





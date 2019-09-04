=====================
Django admin commands
=====================

Lino applications are Django projects. Here is some more Django
know-how you should know as a Lino developer.

The :xfile:`manage.py` file in every demo project is the standard
Django interface for running a so-called **administrative task**, also
known as **admin command** or **management command**. If you did't
know that, please read `django-admin.py and manage.py
<https://docs.djangoproject.com/en/2.2/ref/django-admin/>`_.

Here are some standard Django admin commands that you should know.


.. management_command:: shell

    Start an interactive Python session on the application defined by
    the :xfile:`settings.py` file.  See the `Django documentation
    <https://docs.djangoproject.com/en/2.2/ref/django-admin/#shell>`__

.. management_command:: runserver
                        
    Start a web server which "runs" the application defined by the
    :xfile:`settings.py`.  See the `Django documentation
    <https://docs.djangoproject.com/en/2.2/ref/django-admin/#runserver>`__
                        

.. management_command:: dumpdata

    Output all data in the database (or some tables) to a serialized
    stream.  Serialization formats include *json* or *xml*.  The
    default will write to `stdout`, but you usually redirect this into
    a file.  See the `Django documentation
    <https://docs.djangoproject.com/en/2.2/ref/django-admin/#dumpdata>`__
    
    With a Lino application you will probably prefer
    :manage:`dump2py`.

.. management_command:: flush

    Removes all data from the database and re-executes any
    post-synchronization handlers. The migrations history is not
    cleared.  If you would rather start from an empty database and
    re-run all migrations, you should drop and recreate the database
    and then run :manage:`migrate` instead.  See the `Django
    documentation
    <https://docs.djangoproject.com/en/2.2/ref/django-admin/#flush>`__
    
    With a Lino application you will probably prefer :manage:`initdb`
    or :manage:`prep`.

    
.. management_command:: loaddata

    Loads the contents of the named fixtures into the database.
    See the `Django documentation
    <https://docs.djangoproject.com/en/2.2/ref/django-admin/#loaddata>`__.
    
    With a Lino application you will probably prefer :manage:`initdb`
    or :manage:`prep`.


.. management_command:: migrate

    Updates the database schema.
                        
    With a Lino application you will probably prefer :manage:`dump2py`
    as explained in :doc:`datamig`.



======================
Useful Django know-how
======================

Lino applications are Django projects. There is a lot of Django
know-how you should know as a Lino developer.

Standard Django admin commands
==============================

Here are some standard Django admin commands that you should know.

.. management_command:: shell

    Start an interactive Python session using your project settings.
    See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#shell>`__

.. management_command:: dumpdata

    Output all data in the database (or some tables) to a serialized
    stream. The default will write to `stdout`, but you usually
    redirect this into a file.  See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#dumpdata>`__
    
    You might theoretically use :manage:`dumpdata` for writing a
    Python fixture, but Lino's preferred equivalent is
    :manage:`dump2py`.

.. management_command:: flush

    Removes all data from the database and re-executes any
    post-synchronization handlers. The table of which migrations have
    been applied is not cleared.  See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#flush>`__
    
.. management_command:: loaddata

    Loads the contents of the named fixtures into the database.
    See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#loaddata>`__.
    
    Both :manage:`loaddata` and :manage:`initdb` can be used to load
    fixtures into a database.  The difference is that :manage:`loaddata`
    *adds* data to your database while :manage:`initdb` first clears
    (initializes) your database.




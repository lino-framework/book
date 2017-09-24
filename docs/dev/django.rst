==========================
Django management commands
==========================

Lino applications are Django projects. Here is some more Django
know-how you should know as a Lino developer.

The :xfile:`manage.py` file in every demo project is the standard
Django interface for running a so-called **administrative task** (if
you did't know that, please read `django-admin.py and manage.py
<https://docs.djangoproject.com/en/1.11/ref/django-admin/>`_).

.. management_command:: shell

    Start an interactive Python session on the application defined by
    the :xfile:`settings.py` file.  See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#shell>`__

.. management_command:: runserver
                        
    Start a web server which "runs" the application defined by the
    :xfile:`settings.py`.  See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#runserver>`__

                        

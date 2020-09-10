==========================
Frequently Asked Questions
==========================


**Is Lino an accounting software?**

Accounting is just one functionality covered by Lino. And actually it isn't
even yet in production anywhere. We are testing it. People usually prefer to use
some "established" software for their accounting.

**What's the main function of Lino?**

It's a framework to write applications. Comparable to SAP. Or imagine a very
generic ERP software.  Here are some functions that are currently being used on
Lino :term:`production sites <production site>`:

- Office functionality (contact management, group calendar, notes, tasks, ...)
- Recording contracts and agreements and print them out
- Record and maintain customized data about people and business partners
- Generate pdf or odt documents based on database content.
- Upload files and manage them


**As an application developer, why should I invest time to learn yet
another framework?**

Because our team  is so `hygge <https://en.wikipedia.org/wiki/Hygge>`__.
Because Lino is so great.
With Lino you understand what your users want you to do.
With Lino you can concentrate on doing what your users want.
With Lino you become a magician.


**Why can't we use plain Django do develop our application?**

Nobody uses *plain* Django.
Django application developers
always use Django *together with*
their "portfolio" of "add-ons".
For example
`Jinja <http://jinja.pocoo.org/>`_,
`South <http://south.aeracode.org/>`_,
`bootstrap <http://getbootstrap.com/>`_,
`jQuery <http://jquery.com/>`_,
`ExtJS <https://www.sencha.com/products/extjs/>`_,
`Memcached <http://memcached.org/>`_
...
There are many add-ons to Django, and Lino is just one of them.

Django is not designed to provide out-of-the-box solutions.
Developing a Django application means that you are going
to either write a set of html templates and css files from scratch,
or copy and paste them from some other project.

Lino applications are much more out-of-the-box.
For example you don't need to write a single html template
and you don't need to `design your URLs
<https://docs.djangoproject.com/en/3.1/topics/http/urls/>`_
because we've done this work for you.
Of course you are less flexible. Letting others do some work
always means that you trust them to make certain decisions.

Read more in :doc:`lino_and_django`

**Can I use Lino together with my existing Django add-on?**

It depends. Some Django add-ons are directly usable from within a Lino
applications, others not.  The fact that :doc:`Lino has its own user
management and permissions system<auth>` makes us enter a new world.

You can use plain Django models that were not written for Lino
and add a Lino-style user interface for them to integrate them
into a Lino application.
You can then gradually convert your Django models to make
them more "Lino-like".
You can override Lino's default URL schema,
adding it to an existing Django site.

.. You can run Lino together with a Django admin.

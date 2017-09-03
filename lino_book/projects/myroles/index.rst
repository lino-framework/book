.. _lino.tutorials.myroles:

============================================
Local customizations to the user permissions
============================================

.. How to test only this document:

    $ python setup.py test -s tests.DocsTests.test_myroles
    
    doctest init:

    >>> from lino.api.doctest import *

This tutorial explains how to locally override a user types module.

.. contents::
   :depth: 1
   :local:


The example
===========

For example the default permission system of Lino Polly says that only
a site administrator can see the global list of all polls. This list
is visible through :menuselection:`Explorer --> Polls --> Polls`.  A
normal user does not see that menu command.

We are going to apply a local customization. In our variant of a Lino
Polly application, *every* authenticated user (not only site admins)
can see that table.

Here is the :xfile:`settings.py` file used by this tutorial:

.. literalinclude:: settings.py

And here is the :file:`myroles.py` file used by this tutorial:

.. literalinclude:: myroles.py



Explanations
============

The standard user types module of a Lino Polly is
:mod:`lino_xl.lib.xl.user_types`:

>>> from lino_book.projects.polly.settings import Site
>>> print(Site.user_types_module)
lino_xl.lib.xl.user_types

On this site we created a local user types module whose first line
imports everything from the standard module::

    from lino_xl.lib.xl.user_types import *

In our :xfile:`settings.py` file, we set :attr:`user_types_module
<lino.core.site.Site.user_types_module>` to the Python path of
above file::
    
    user_types_module = 'mysite.myroles'

This first step should have no visible effect at all. We've just
prepared a hook for defining local customizations.  The only
difference is that our local :file:`myroles.py` module is being
imported at startup:

>>> print(settings.SITE.user_types_module)
lino_book.projects.myroles.myroles

Second step is to add customizations to that :file:`myroles.py` file.

An example
==========

The following code snippets are to test whether a normal user now
really can see all polls (i.e. has the :menuselection:`Explorer -->
Polls --> Polls` menu command):

>>> u = users.User(username="user", user_type="100")
>>> u.full_clean()
>>> u.save()
>>> rt.login('user').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Polls : My Polls, My Responses
- Explorer :
  - Polls : Polls
- Site : About

.. _dev.watch:

=========================
Watching database changes
=========================

.. How to test only this module:

    $ python setup.py test -s tests.DocsTests.test_watch


This tutorial explains how to use the :mod:`lino.modlib.changes`
plugin for logging changes to individual rows of database tables and
implementing a kind of `audit trail
<https://en.wikipedia.org/wiki/Audit_trail>`_.

This tutorial is a tested document and part of the Lino test suite. It
uses the :mod:`lino_book.projects.watch` sample application:

>>> from lino import startup
>>> startup('lino_book.projects.watch.settings')
   
To enable database change watching, you add :mod:`lino.modlib.changes`
to your :meth:`get_installed_apps
<lino.core.site.Site.get_installed_apps>` and then register "change
watchers" for every type of change you want to watch.

You will also want to make your changes visible for users by adding
the :class:`changes.ChangesByMaster
<lino.modlib.changes.models.ChangesByMaster>` slave table to some of
your detail layouts.

The example in this tutorial uses the :mod:`lino_xl.lib.contacts`
module.  It also adds a model `Entry` as an example of a watched
model.  Imagine some journal entry to be audited.

The "master" of a change watcher is the object to which every change
should be attributed.  In this example the master is *Partner*: every
change to *Entry*, *Partner* **or** *Company* will be logged and
attributed to their *Partner* record.

We define our own subclass of `Site` for this tutorial (which is the
recommended way except for very simple examples).  Here is the
:xfile:`settings.py` file:

.. literalinclude:: ../../lino_book/projects/watch/settings.py

We need to redefine the default list of user profiles by overriding
:meth:`Site.setup_choicelists` because `contacts` adds a user group
"office", required to see most commands.

Here is our :xfile:`models.py` module which defines the `Entry` model
and some few startup event listeners:

.. literalinclude:: ../../lino_book/projects/watch/entries/models.py


You can play with this application by cloning the latest development 
version of Lino, then doing::

    $ go watch
    $ python manage.py prep
    $ python manage.py runserver



TODO: write a demo fixture which reproduces what we are doing in
the temporary database during djangotests.

>>> from lino.api.doctest import *

>>> rt.show('changes.Changes')
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP
==== ============= ===================== ===================== =============================================================
 ID   Change Type   Master                Object                Changes
---- ------------- --------------------- --------------------- -------------------------------------------------------------
 1    Create        `My pub <Detail>`__   `My pub <Detail>`__   Company(id=181,language='en',name='My pub',partner_ptr=181)
==== ============= ===================== ===================== =============================================================
<BLANKLINE>


>>> rt.show('gfks.BrokenGFKs')
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP
===================== ================= =============================================================== ========
 Database model        Database object   Message                                                         Action
--------------------- ----------------- --------------------------------------------------------------- --------
 `Change <Detail>`__   `#1 <Detail>`__   Invalid primary key 181 for contacts.Company in `object_id`     clear
 `Change <Detail>`__   `#2 <Detail>`__   Invalid primary key 181 for contacts.Company in `object_id`     clear
 `Change <Detail>`__   `#3 <Detail>`__   Invalid primary key 1 for watch_tutorial.Entry in `object_id`   clear
 `Change <Detail>`__   `#4 <Detail>`__   Invalid primary key 1 for watch_tutorial.Entry in `object_id`   clear
 `Change <Detail>`__   `#5 <Detail>`__   Invalid primary key 181 for contacts.Company in `object_id`     clear
 `Change <Detail>`__   `#1 <Detail>`__   Invalid primary key 181 for contacts.Partner in `master_id`     clear
 `Change <Detail>`__   `#2 <Detail>`__   Invalid primary key 181 for contacts.Partner in `master_id`     clear
 `Change <Detail>`__   `#3 <Detail>`__   Invalid primary key 181 for contacts.Partner in `master_id`     clear
 `Change <Detail>`__   `#4 <Detail>`__   Invalid primary key 181 for contacts.Partner in `master_id`     clear
 `Change <Detail>`__   `#5 <Detail>`__   Invalid primary key 181 for contacts.Partner in `master_id`     clear
===================== ================= =============================================================== ========
<BLANKLINE>

There open questions regarding these change records:

- Do we really never want to remove them? Do we really want a nullable
  master field? Should this option be configurable?
- How to tell :class:`lino.modlib.gfks.models.BrokenGFKs` to
  differentiate them from ?
- Should :meth:`get_broken_generic_related
  <lino.core.kernel.Kernel.get_broken_generic_related>` suggest to
  "clear" nullable GFK fields?


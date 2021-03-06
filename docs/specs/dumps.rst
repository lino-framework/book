.. doctest docs/specs/dumps.rst
.. _book.specs.dumps:

==========================
The ``dumps`` demo project
==========================

.. If this test fails because something has changed in the expected
   dump, then you can update these dumps by running::

     $ go dumps
     $ ./init.sh


This document shows a series of usage examples for :ref:`Python dumps <dpy>`.
It verifies whether :ticket:`2204` (AmbiguousTimeError) is fixed, it
demonstrates three methods of writing demo multilingual data for babel
fields, and it demonstrates behaviour of choicelists in Python dumps.

See also :doc:`/dev/datamig` and :doc:`/dev/dump2py`.


This document uses the :mod:`lino_book.projects.dumps` demo project.

>>> from atelier.sheller import Sheller
>>> shell = Sheller("lino_book/projects/dumps")




Database structure
==================

Here is our :xfile:`models.py` file:

.. literalinclude:: /../../book/lino_book/projects/dumps/models.py

We also have a choicelist:

.. literalinclude:: /../../book/lino_book/projects/dumps/choicelists.py

And we have a Python fixture in file :xfile:`fixtures/demo.py`, which adds three
records:

.. literalinclude:: /../../book/lino_book/projects/dumps/fixtures/demo.py


First site : without time zone
==============================

In a first example we have :setting:`USE_TZ` set to False.  This is
defined by the :file:`settings/a.py` file:

.. literalinclude:: /../../book/lino_book/projects/dumps/settings/a.py

We initialize our database from the demo fixture:

>>> shell("python manage_a.py prep --noinput")
... #doctest: +ELLIPSIS
`initdb demo` started on database .../default.db.
Operations to perform:
  Synchronize unmigrated apps: about, bootstrap3, dumps, extjs, jinja, lino, staticfiles
  Apply all migrations: (none)
Synchronizing apps without migrations:
  Creating tables...
    Creating table dumps_foo
    Running deferred SQL...
Running migrations:
  No migrations to apply.
Loading data from ...
Installed 3 object(s) from 1 fixture(s)

And here is the result:

>>> shell("python manage_a.py show dumps.Foos")
... #doctest: +ELLIPSIS
==== ============= ================== ================== ===================== ======
 ID   Designation   Designation (de)   Designation (fr)   Last visit            Bar
---- ------------- ------------------ ------------------ --------------------- ------
 1    First         Erster             Premier            2016-07-02 23:55:12   Sale
 2    January       Januar             janvier            2016-07-03 00:10:23   Sale
 3    Three         Drei               Trois              2017-10-29 03:16:06   Sale
==== ============= ================== ================== ===================== ======

Note that our demo data contains an ambigous time stamp.  When
somebody living in Brussels tells you "it was at on 2017-10-29 at
01:16:06", then you don't know whether they mean summer or winter
time.  Because their clock showed that particular time twice during
that night.  Every year on the last Sunday of October, all clocks in
Europe are turned back at 2am by one hour to 1am again.  The timestamp
"2017-10-29 01:16:06" is ambigous.  Thanks to Ilian Iliev for
publishing his blog post `Django, pytz, NonExistentTimeError and
AmbiguousTimeError
<http://www.ilian.io/django-pytz-nonexistenttimeerror-and-ambiguoustimeerror/>`__.

Now we run :manage:`dum2py` to create a dump:

>>> shell("python manage_a.py dump2py tmp/a --overwrite")
... #doctest: +ELLIPSIS
Writing .../lino_book/projects/dumps/tmp/a/restore.py...
Wrote 3 objects to .../lino_book/projects/dumps/tmp/a/restore.py and siblings.

The dump generated by :manage:`dump2py` consists of two files. First
:xfile:`restore.py`:

.. literalinclude:: /../../book/lino_book/projects/dumps/a/restore.py

and the second is :file:`dumps_foo.py` (app label and model name)

.. literalinclude:: /../../book/lino_book/projects/dumps/a/dumps_foo.py


Verify that the newly created dump is as expected:

>>> shell("diff a tmp/a")
... #doctest: +ELLIPSIS
<BLANKLINE>

Load the dump, dump again and verify that both dumps are the same:

>>> shell("python manage_a.py run a/restore.py --noinput")
... #doctest: +ELLIPSIS
Unversioned Site instance : no database migration
`initdb ` started on database .../default.db.
Operations to perform:
  Synchronize unmigrated apps: about, bootstrap3, dumps, extjs, jinja, lino, staticfiles
  Apply all migrations: (none)
Synchronizing apps without migrations:
  Creating tables...
    Creating table dumps_foo
    Running deferred SQL...
Running migrations:
  No migrations to apply.
Execute file dumps_foo.py ...
Loading 3 objects to table dumps_foo...


>>> shell("python manage_a.py dump2py tmp/a --overwrite")
... #doctest: +ELLIPSIS
Writing .../lino_book/projects/dumps/tmp/a/restore.py...
Wrote 3 objects to .../lino_book/projects/dumps/tmp/a/restore.py and siblings.

>>> shell("diff a tmp/a")
... #doctest: +ELLIPSIS
<BLANKLINE>



Second suite
============

Now the same with `b`, i.e. with :setting:`USE_TZ` enabled.

The :file:`settings/b.py` file:

.. literalinclude:: /../../book/lino_book/projects/dumps/settings/b.py


We load our demo data:

>>> shell("python manage_b.py prep --noinput")
... #doctest: +ELLIPSIS
`initdb demo` started on database .../default.db.
Operations to perform:
  Synchronize unmigrated apps: about, bootstrap3, dumps, extjs, jinja, lino, staticfiles
  Apply all migrations: (none)
Synchronizing apps without migrations:
  Creating tables...
    Creating table dumps_foo
    Running deferred SQL...
Running migrations:
  No migrations to apply.
Loading data from ...
Installed 3 object(s) from 1 fixture(s)

The result as seen by the user is the same as in a.

>>> shell("python manage_b.py show dumps.Foos")
... #doctest: +ELLIPSIS
==== ============= ================== ================== =========================== ======
 ID   Designation   Designation (de)   Designation (fr)   Last visit                  Bar
---- ------------- ------------------ ------------------ --------------------------- ------
 1    First         Erster             Premier            2016-07-02 23:55:12+00:00   Sale
 2    January       Januar             janvier            2016-07-03 00:10:23+00:00   Sale
 3    Three         Drei               Trois              2017-10-29 03:16:06+00:00   Sale
==== ============= ================== ================== =========================== ======


>>> shell("python manage_b.py dump2py tmp/b --overwrite")
... #doctest: +ELLIPSIS
Writing .../lino_book/projects/dumps/tmp/b/restore.py...
Wrote 3 objects to .../lino_book/projects/dumps/tmp/b/restore.py and siblings.

Verify that the newly created dump is as expected:

>>> shell("diff b tmp/b")
... #doctest: +ELLIPSIS
<BLANKLINE>

Load the dump, dump again and verify that both dumps are the same:

>>> shell("python manage_b.py run b/restore.py --noinput")
... #doctest: +ELLIPSIS
Unversioned Site instance : no database migration
`initdb ` started on database .../default.db.
Operations to perform:
  Synchronize unmigrated apps: about, bootstrap3, dumps, extjs, jinja, lino, staticfiles
  Apply all migrations: (none)
Synchronizing apps without migrations:
  Creating tables...
    Creating table dumps_foo
    Running deferred SQL...
Running migrations:
  No migrations to apply.
Execute file dumps_foo.py ...
Loading 3 objects to table dumps_foo...


>>> shell("python manage_b.py dump2py tmp/b --overwrite")
... #doctest: +ELLIPSIS
Writing .../lino_book/projects/dumps/tmp/b/restore.py...
Wrote 3 objects to .../lino_book/projects/dumps/tmp/b/restore.py and siblings.

>>> shell("diff b tmp/b")
... #doctest: +ELLIPSIS
<BLANKLINE>


Third suite
===========

Here we test the `--max-row-count` option.  Since we have only three
rows, we change the value from its default 50000 to 2 in order to
trigger the situation:

>>> shell("python manage_b.py dump2py tmp/c --overwrite -m 2")
... #doctest: +ELLIPSIS
Writing .../lino_book/projects/dumps/tmp/c/restore.py...
Wrote 3 objects to .../lino_book/projects/dumps/tmp/c/restore.py and siblings.

Verify that the newly created dump is as expected:

>>> shell("diff c tmp/c")
... #doctest: +ELLIPSIS
<BLANKLINE>


Error messages
==============

Here we try to call :manage:`dump2y` in some invalid ways, just to
demonstrate the possible error messages.

>>> shell("python manage_a.py dump2py")
... #doctest: +ELLIPSIS
usage: manage_a.py dump2py [-h] ...
manage_a.py dump2py: error: ...


>>> shell("python manage_a.py dump2py a")
... #doctest: +ELLIPSIS
CommandError: Specified output_dir ...lino_book/projects/dumps/a already exists. Delete it yourself if you dare!


Bibliography
============

Thanks to Ilian Iliev `Django, pytz, NonExistentTimeError and
AmbiguousTimeError
<http://www.ilian.io/django-pytz-nonexistenttimeerror-and-ambiguoustimeerror/>`__

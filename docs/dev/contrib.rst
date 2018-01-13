.. _dev.contrib:

=================
Contributing code
=================

So you want to benefit other people by publishing your changes and
integrating them into the related source code repository.  That's
nice. Thank you.  At this point it is time to speak about code
contributions.


General workflow
================

The general workflow for a code contribution is

- Make sure that you have have the latest version (a "clean working
  directory" for all your repositories)::

    $ pp git pull
  
- :doc:`Run the test suite <runtests>` in order to verify that your
  environment is correctly set up.
  
- Make your changes. That is, you change one or several files in your
  local copy of one or several repositories.
  
- :doc:`Run the test suite again <runtests>` to verify that your
  change didn't break anything.
  
- Communicate your changes to the others by submitting a :doc:`pull
  request <request_pull>`.

 

.. _lino.copyright:

Copyright considerations
========================

Every free software project has a copyright holder.

Currently most Lino source files are *(c) Luc Saffre*, and we consider
Luc as the official copyright holder of the Lino framework.  This
doesn't reflect reality perfectly, but it seems the most reasonable
formulation at the moment.  As long as there is no legal entity to act
as copyright holder, everybody just trusts that Luc will manage these
things one day before he dies...

So if you contribute some code to some repository of the Lino project,
we ask you to assign your copyright to *Luc Saffre* because we want to
avoid legal problems in case we want to change the license in the
future.  And because we do not want to add every individual
contributor to every copyright statement.

We are still working on the details.

We plan to change the copyright holder to "The Lino Team" or something
similar in the future.  One challenge is that we currently don't have
any legal person called "Lino Team".  And if some day we would create
a legal entity for Lino, then its name would probably not be "Lino
Team" because there are other projects called "Lino", and they
probably also have a "team" around them.  See :ref:`lino.name`.
Possible other names for that future entity are *Lino Framework
project* or *Lino Software Foundation*.

Rumma & Ko OÜ might act as the copyright holder because they are
currently the community motor.  This name has some disadvantages: it
contains an ``&`` and an ``Ü`` which both can cause problems when
rendering them to different media.

Contributor License Agreement
=============================

When you contribute a change to Lino, then basically you are the
copyright holder of your work and you agree to publish your work under
the same license as Lino and you ask us to integrate your
contribution.

We did not (yet) formulate and sign any Contributor License Agreement
as e.g. `Django <https://www.djangoproject.com/foundation/cla/>`__
does it.  Every contributor is liable for their work: if one of us
would (accidentally) publish a file with sensitive confidential data
or copyrighted content, only that particular person (or their
employer) would be liable.



Types of code contributions
===========================

Bugfix
------

- Find a bug in Lino (report it to the others, discuss about how to
  fix it)
  
- Note that you are in a kind of priveleged situation: the test suite
  passed, claiming that Lino is perfect and everything works well, but
  *you* know it better, you know that there is a bug! The best thing
  to do in this situation is to first write a new test case which
  reproduces your bug. This new test case will of course break the
  test suite. You then fix the bug. 

Documentation change
--------------------


Translations
------------

Test case
---------

New feature
-----------

Optimization
------------



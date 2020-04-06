.. _dev.contrib:

=================
Contributing code
=================

So you want to share your changes in code or docs and let other people benefit
from your skills. That's nice! Thank you.  Now is the time to speak about code
contributions.

This sections explains technical aspects. See also :ref:`legal stuff <lino.copyright>`.


General workflow
================

The general workflow for a code contribution is

- Make sure that you have have the latest version (a "clean working directory"
  for all your repositories), e.g. by running :cmd:`pp git pull` (see :cmd:`pp`).

- :doc:`Run the test suite <runtests>` in order to verify that your
  environment is correctly set up.

- Make your changes. That is, you change one or several files in your
  local copy of one or several repositories.

- :doc:`Run the test suite again <runtests>` to verify that your
  change didn't break anything.

- Communicate your changes to the others by submitting a :doc:`pull
  request <request_pull>`.




Types of code contributions
===========================

Bugfix
------

- Find a bug in Lino (report it to the others, discuss about how to
  fix it)

- A good thing to do in this situation is to first write a new test
  case which reproduces your bug. This new test case will of course
  break the test suite. You then fix the bug.

Documentation change
--------------------

- You stumbled into some pitfall because Lino's documentation is not perfect.
  Now we should review the docs: how can we avoid that other newbies have this
  pitfall which caused you frustration.


Translations
------------

Test case
---------

New feature
-----------

Optimization
------------

.. _dev.contrib:

=================
Contributing code
=================

When you reached here, it is time to speak about code contributions.

General workflow
================

The general workflow for a code contribution is

- Make sure that you have have the latest version (a "clean working
  directory" for all your repositories)::

    $ pp git status
  
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



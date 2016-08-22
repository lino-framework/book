=================
Contributing code
=================

When you reached here, it is time to speak about code contributions.

The general workflow for a code contribution is

- Find a bug in Lino (report it to the others, discuss about how to
  fix it)
  
- Make sure that you have have the latest version (a "clean working
  directory" for all your repositories)::

    $ pp git st
  
- Run the test suite in order to verify that your environment is
  correctly set up.

- Note that you are in a kind of priveleged situation: the test suite
  passed, claiming that Lino is perfect and everything works well, but
  *you* know it better, you know that there is a bug! The best thing
  to do in this situation is to first write a new test case which
  reproduces your bug. This is called *coverage*. This new test case
  will of course break the test suite. If you never worried about
  these things, you might leave this step for later or to a more
  experienced contributor.

- Change one or several files in one or several repositories in order
  to fix the bug.
  
- Run the test suite again to verify that your change didn't break
  anything.
  
- Submit a pull request


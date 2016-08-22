.. _dev.runtests:

===========================
Running the Lino test suite
===========================

Once your :doc:`environment <env>` is correctly set up you can run the
test suite for the Lino framework as follows::

  $ pp inv initdb test

This loops over all your projects, initializes their demo databases
and then runs the test suite. The whole process takes 20 minutes on my
machine when there's no error. It produces a lot of output of this
style::

    ==== lino ====
    no previously-included directories found matching 'docs'
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.013s
    OK
  
    (...)

    ==== noi ====
    --------------------------------------------------------------------------------
    In demo project lino_noi.projects.team.settings.demo:
    `initdb std demo demo2` started on database .../default.db.
    Operations to perform:
    ...
    Installed 148 object(s) from 11 fixture(s)
    ...................
    ----------------------------------------------------------------------
    Ran 19 tests in 34.440s

    OK

    (...)

If any error occurs, then you need to find out the reason.  Possible
reasons for failures are:

- :message:`PodError: An error occurred during the conversion. Could
  not connect to LibreOffice on port 8100. UNO (LibreOffice API) says:
  Connector : couldn't connect to socket (Success).`

  This means that you don't have the LibreOffice server running.  See
  :ref:`admin.oood`.

- Some dependency is not installed on your machine.

- Some test suite is broken.


Tips & tricks
=============
  
You can split the process into two::

  $ pp inv initdb
  $ pp inv test

This can save you time if there is some problem. Once :manage:`inv
initdb` has run successfully for all projects, you can focus on
:manage:`inv test`.

You can run the test suite for one project at a time by doing::

  $ go <prjname>
  $ inv initdb test

You can prepend the standard Unix `time
<http://linux.die.net/man/1/time>`__ command if you want to know how
much time it took on your machine::

  $ time pp inv initdb test

You can use the `-v` option of :cmd:`pp` so that you can peacefully
leave your computer, go to the kitchen and make yourself a cup of tea,
knowing that your computer will pronounce the result through its
speakers when the process has finished::

  $ time pp -v inv initdb test

You can try this without actually needing to wait by issuing::  

  $ pp -v ls
  
Your computer should then say the words "Successfully terminated 'ls'
for all projects" with a more or less clear male voice.

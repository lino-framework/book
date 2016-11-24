.. _dev.runtests:

===========================
Running the Lino test suite
===========================

Once your :doc:`environment <env>` is correctly set up you can run the
test suite for the Lino framework as follows::
  
  $ oood
  $ pp inv prep test


Where :cmd:`oood` starts up the LibreOffice server, required by
several tests.  See :doc:`/admin/oood`.  You don't need to do this
here if you installed LO as a service on your machine.

The :cmd:`pp inv prep test` command then loops over all your
projects (:cmd:`pp`), initializes their demo databases (:cmd:`inv
initdb`) and then runs the test suite (:cmd:`inv test`. The whole
process takes 20 minutes on my machine when there's no error. It
produces a lot of output of this style::

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

In order to check whether everything worked well, we are now going to
run the test suite.

Make sure that your demo databases are initialized and that you did
not do any manual changes therein.  Because the test suite has many
test cases which would fail if these demo databases were missing or
not in their virgin state.  In case you *did* write into some database
during the previous section, just run :cmd:`inv prep` once more.


Tips & tricks
=============
  
#.  You can split the process into two::

      $ pp inv prep
      $ pp inv test

    This can save you time if there is some problem. Once :manage:`inv
    initdb` has run successfully for all projects, you can focus on
    :manage:`inv test`.

#.  You can run the test suite for one project at a time by doing::

      $ go <prjname>
      $ inv prep test

#.  You can prepend the standard Unix `time
    <http://linux.die.net/man/1/time>`__ command if you want to know
    how much time it took on your machine::

      $ time pp inv prep test

#.  You can use the `-v` option of :cmd:`pp` so that you can
    peacefully go to the kitchen and make yourself a cup of tea,
    knowing that your computer will announce the result through its
    speakers when the process has finished::

      $ time pp -v inv prep test

    You can try this by issuing::

      $ pp -v ls

    Your computer should then say the words "Successfully terminated 'ls'
    for all projects" with a more or less clear male voice.

    Note that this requires the `espeak
    <http://espeak.sourceforge.net/>`__ package to be installed on
    your machine::

      $ sudo apt-get install espeak

  

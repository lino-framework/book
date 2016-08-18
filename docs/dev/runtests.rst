.. _dev.runtests:

===========================
Running the Lino test suite
===========================

Once your :doc:`environment <env>` is correctly set up you can easily
run the test suite for the Lino framework::


  $ pp inv initdb test

This loops over all your projects, initializes their demo databases
and then runs the test suite. The whole process takes 20 minutes on my
machine when there's no error.  If any error occurs, then you need to
find out the reason.

Possible reasons for failures are:

- :message:`PodError: An error occurred during the conversion. Could
  not connect to LibreOffice on port 8100. UNO (LibreOffice API) says:
  Connector : couldn't connect to socket (Success).`

  This means that you don't have the LibreOffice server running.  See
  :ref:`admin.oood`.

- Some dependency is not installed on your machine.

- Some test suite is broken.

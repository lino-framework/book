.. _dev.sdist:

============================
Simulating a release on PyPI
============================


Before actually publishing a new version of Lino on PyPI, we want to
test whether the process of packaging and installing causes issues
which do not exist when using a clone of the source repositories.
Because once a package has been published on http://pypi.python.org,
you cannot update it any more without increasing the version number.

Here is how to test a Lino installation using your unofficial local
copy of PyPI.

Check whether your :envvar:`sdist_dir` is correctly set in your
:xfile:`.invoke.py`. It should be some value like::

     sdist_dir = '/home/joe/mypackages/{prj}'

Use the :cmd:`inv sdist` command (and :cmd:`pp`) to generate
distribution packages for all our projects::


        $ pp inv sdist

The package files will be created in your :envvar:`sdist_dir`.

Now start a local pypi server who will simulate the public pypi::

    $ pip install pypiserver
    $ pypi-server -p 8080 /home/joe/mypackages

Where :file:`/home/joe/mypackages` is what you specified in your
:envvar:`sdist_dir`.  This will run the server which waits for
incoming requests.  Leave it waiting.

Open another terminal create a new virgin virtualenv and activate it::
  
    $ virtualenv env
    $ . env/bin/activate

Install :mod:`lino_cosi` as described in :ref:`user.install`, but with
the difference that we specify :option:`--index-url` (tell pip to use
our local pypi server) :option:`--extra-index-url` (tell pip to use
the official pypi server for packages that don't exist on the local
server)::
    
    $ pip install --index-url http://localhost:8080/simple --extra-index-url https://pypi.org/simple lino_cosi

Note: the word "simple" comes from :pep:`503`.

Note how dependencies are resolved: :mod:`lino_xl` and :mod:`lino` are
downloaded from localhost while packages like Django, Sphinx etc. are
downloaded from `python.org`.

If the installation worked, continue as described in
:ref:`user.install`::

    $ cd ~/tmp
    $ mkdir mylino
    $ touch mylino/__init__.py
    $ echo "from lino_cosi.lib.cosi.settings import *" > mylino/settings.py
    $ echo "SITE = Site(globals())" >> mylino/settings.py
    $ echo "DEBUG = True" >> mylino/settings.py

Then we initialize and populate the demo database::
  
    $ export DJANGO_SETTINGS_MODULE=mylino.settings
    $ export PYTHONPATH=.
    $ django-admin prep

And finally we launch a development server::
  
    $ django-admin runserver

Sign in as some user and play around in the application in order to
check whether this is what a new Lino user should see.

If everything is okay, you can continue and publish

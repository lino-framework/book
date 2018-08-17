.. _dev.sdist:

================================
Publishing a new version of Lino
================================

Before releasing a new version of Lino on PyPI, we want to test
whether the process of packagine and installing causes issues which
did not exist when using a clone of the source repositories.

Check whether you :envvar:`sdist_dir` is correctly set in your
:xfile:`.invoke.py`. It should be some value like::

     sdist_dir = '/home/joe/mypackages/{prj}'

To generate packages for all our projects, we use the :cmd:`inv sdist`
command (and :cmd:`pp`)::

        $ pp inv sdist

This will create all the files below my :envvar:`sdist_dir`.
Then in one terminal::

    $ pip install pypiserver
    $ pypi-server -p 8080 /home/joe/mypackages

Where :file:`/home/joe/mypackages` is what you specified in your
:envvar:`sdist_dir`.  This will run a server which waits for incoming
requests.

And then in another terminal::

    $ virtualenv env
    $ . env/bin/activate
    $ pip install --index-url http://localhost:8080/simple --extra-index-url https://pypi.org/simple lino_cosi

Note: the word "simple" comes from :pep:`503`.

If the installation worked, continue as described in
:ref:`user.install`::

    $ cd ~/tmp
    $ mkdir mylino
    $ touch mylino/__init__.py
    $ echo "from lino_cosi.lib.cosi.settings import *" > mylino/settings.py
    $ echo "SITE = Site(globals())" >> mylino/settings.py

Then we initialize and populate the demo database::
  
    $ export DJANGO_SETTINGS_MODULE=mylino.settings
    $ export PYTHONPATH=.
    $ django-admin prep

And finally we launch a development server::
  
    $ django-admin runserver
    



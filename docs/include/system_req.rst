.. this is included by admin/install.rst and dev/install.rst

.. _lxml: http://lxml.de/
.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _git: http://git-scm.com/downloads

#.  At this point you should retrieve new lists of packages.::

      $ sudo apt update

#.  You will need virtualenv_ and pip_ installed::

        $ sudo apt install virtualenv

#.  You need to install git_ on your computer to get the source
    files::

      $ sudo apt install git

#.  There are Python C extensions among Lino's dependencies::

      $ sudo apt install python-dev

#.  Many Lino applications require lxml_, which has some extra
    requirements::

      $ sudo apt-get build-dep lxml

    Note: if you get an error message :message:`You must put some
    'source' URIs in your sources.list`, then (in Ubuntu) open
    :menuselection:`System Settings --> Software & Updates` and make
    sure that :guilabel:`Source code` is checked. Or (on the command
    line) edit your :file:`/etc/apt/sources.list` file::

      $ sudo nano /etc/apt/sources.list
      $ sudo apt update

#.  Similar requirement for applications which use
    :mod:`lino.modlib.weasyprint`::

      $ sudo apt-get build-dep cairocffi
      $ sudo apt install libffi-dev libssl-dev

#.  For applications which use :mod:`lino.utils.html2xhtml`::

      $ sudo apt install tidy

#.  For applications which use :mod:`lino_xl.lib.appy`::

      $ sudo apt install libreoffice libreoffice-script-provider-python uno-libs3 python3-uno python3

    See also :doc:`/admin/oood` because you might want to have the
    LibreOffice server listening.



The appy package on Python 3
============================

The appy package is a bit special to install under Python 3 because its author
is special... (e.g. he still gives support to customers whose production sites
run on Python 2.4).  With ``pip install appy`` you would get a version that
installs without error under Python 3, but not much more. That's why we
recommend to get a clone of the appy-dev project and install it using ``pip
install -e``.  Or to be short ::

  $ cd ~/repositories
  $ svn checkout https://svn.forge.pallavi.be/appy-dev
  $ pip install -e appy-dev/dev1




Get the sources
===============

Create a directory (e.g. :file:`repositories`) meant to hold your
working copies of version-controlled software projects, `cd` to that
directory and and do::

  $ mkdir ~/repositories
  $ cd ~/repositories
  $ git clone https://github.com/lino-framework/book.git
  $ . book/docs/dev/install_dev_projects.sh

..
  $ git clone https://github.com/lino-framework/lino.git; \
    git clone https://github.com/lino-framework/xl.git; \
    git clone https://github.com/lino-framework/noi.git; \
    git clone https://github.com/lino-framework/cosi.git; \
    git clone https://github.com/lino-framework/care.git; \
    git clone https://github.com/lino-framework/vilma.git; \
    git clone https://github.com/lino-framework/avanti.git; \
    git clone https://github.com/lino-framework/tera.git




You should now have nine directories called :file:`lino`, :file:`xl`,
:file:`noi`, ... and :file:`book` in your :file:`~/repositories`
directory each of which contains a file :xfile:`setup.py` and a whole
tree of other files and directories.

Note that even if you opted for having two environments (py2 and py3),
these environments will use the same source repositories.

.. Note that if you just want a *simplified* development environment
   (for a specific application on a production site), then you don't
   need to download and install all Lino repositories mentioned
   above. For example, if you want an `avanti` site, you *only* need
   to install `xl`, `lino` and `avanti` but *not* `noi`, `vilma`,
   `cosi` etc. On a production site you will probably never need the
   `book` repository which is the only one which requires all other
   repositories.

One possible problem here is that some repositories might have a big
size.  If you just want to get the latest version and don't plan to
submit any pull requests, then you can reduce download size by adding
``--depth 1`` and ``-b master`` options at least for `lino` (which has
by far the biggest repository)::

  $ git clone --depth 1 -b master https://github.com/lino-framework/lino.git

(as explained in `this question on stackoverflow
<http://stackoverflow.com/questions/1209999/using-git-to-get-just-the-latest-revision>`__
or Nicola Paolucci's blog entry `How to handle big repositories with
git
<http://blogs.atlassian.com/2014/05/handle-big-repositories-git/>`_).



Installation
============

Now you are ready to "install" Lino, i.e. to tell your Python
interpreter where the source file are, so that you can import them
from within any Python program.

Commands::

  $ p2  # activate the environment
  $ cd repositories
  $ pip install -e lino
  $ pip install -e xl
  $ pip install -e noi
  $ pip install -e cosi
  $ pip install -e care
  $ pip install -e vilma
  $ pip install -e avanti
  $ pip install -e tera
  $ pip install -e book

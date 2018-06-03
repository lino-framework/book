.. this is included by admin/install.rst and dev/install.rst

.. _lxml: http://lxml.de/
.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _git: http://git-scm.com/downloads

#.  Lino theoretically works under **Python 3**, but we currently
    still recommend **Python 2**.  If you just want it to work, then
    choose Python 2. Otherwise consider giving it a try under Python 3
    and report your experiences.

#.  You need at least 500MB of RAM.  How to see how much memory you
    have::

        $ free -h

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



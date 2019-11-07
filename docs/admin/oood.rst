.. _admin.oood:

============================
Running a LibreOffice server
============================

Read :doc:`appy` before reading this page.

This page is probably useless because getlino does these things automatically.

The :mod:`lino_xl.lib.appypod` plugin uses `appy.pod
<http://appyframework.org/pod.html>`_ which in turn uses `python3-uno
<https://packages.debian.org/de/sid/python3-uno>`__ to connect to a
`LibreOffice` server.

`appy.pod` is part of the ``appy`` Python package and was
automatically installed together with Lino into your Python
environment.

But appy requires two system packages `libreoffice` and `python3-uno` which must
be installed using something like this::

  $ sudo apt-get install libreoffice python3-uno

If this fails, you might try with adding the `LibreOffice Fresh
<https://launchpad.net/~libreoffice/+archive/ubuntu/ppa>`__ PPA::

  $ sudo add-apt-repository ppa:libreoffice/ppa
  $ sudo apt update
  $ sudo apt upgrade

Then you need to run a LO server. For **occasional or experimental
usage** you can fire it up manually using something like this::

  $ libreoffice '--accept=socket,host=127.0.0.1,port=8100;urp;' &

You might create an executable bash script named :cmd:`oood` in your
``PATH`` with above line.

But for **regular usage** and especially on a production server you
will want to use a startup script. We recommend supervisor (which is
also used for :doc:`linod`):

- Install the `Supervisor <http://www.supervisord.org/index.html>`_
  package::

      $ sudo apt-get install supervisor

  Note that the supervisor package is being installed system-wide, it
  is not related to any specific project.

- Create a file :file:`libreoffice.conf` in
  :file:`/etc/supervisor/conf.d/` with this content::

    [program:libreoffice]
    command=libreoffice --accept="socket,host=127.0.0.1,port=8100;urp;" --nologo --headless --nofirststartwizard
    user = root

- Restart :program:`supervisord`::

    $ sudo service supervisor restart

- Have a look at the log files in :file:`/var/log/supervisor` and
  check the status::

    $ sudo service supervisor status

- When everything works, then add supervisor as a service so that it
  gets automatically started after a system restart::

    $ sudo systemctl enable supervisor


..
    Vic Vijayakumar has written such a
    script, and for convenience the Lino repository contains a copy of it
    :file:`/bash/openoffice-headless`.

    - Make your local copy of the startup script::

        $ sudo cp ~/repositories/lino/bash/openoffice-headless /etc/init.d

    - Edit your copy::

        $ sudo nano /etc/init.d/openoffice-headless

      Check the value of the `OFFICE_PATH` variable in that script::

        OFFICE_PATH=/usr/lib/libreoffice

    - Make it executable::

        $ sudo chmod 755 /etc/init.d/openoffice-headless

    - Finally, run ``update-rc.d`` to have the daemon
      automatically start when the server boots::

        $ sudo update-rc.d openoffice-headless defaults

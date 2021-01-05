================
The Qt front end
================

Lino comes with a admin command :manage:`qtclient` that runs a Qt client for any
:term:`Lino site`.

In that case the :term:`front end` is not a web application but a desktop GUI
application. It can be combined with one or several web front ends.

At the moment this is just a proof of concept that is looking for a volunteer to
evolve.

To see it in action, install a  `Lino contributor environment
<lino.dev.install>`__, manually install `PyQt5
<https://en.wikipedia.org/wiki/PyQt>`__ and then run it in any of the Lino demo
projects. For example::

    $ pip install pyqt5
    $ go min2
    $ python manage.py qtclient

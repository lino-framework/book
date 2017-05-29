.. _specs.noi.github:

================
The github module
================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_github

    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


The :mod:`lino_xl.lib.github` module is a plugin to help with tracking what was
committed by who on what ticket.

It uses git-hub's v3 api to request all commits on the Master branch of any repository.
It is recommended to create a o-auth token for larger repositories beacuse without it there is a limit
of 60 requests per hour.

After the plugin has requested the list of commits it matches the commits to users and tickets by the following logic.

If the commit has a github username associated with it it will try to match the name to a user user
via their Github Username that is set in their My Settings page.
Failing that it will try to match the First name of the Commiter name and User name.
That might change in the future for larger teams.

To match to a ticket it first looks at the description of the ticket,
if there is a ticket number listed in the format of::

    #[0-9]

The commit will be matched to the ticket with that number.

Otherwise it will try to match to a ticket via the associated user's working time by looking for
sessions that were active during the time of committing.


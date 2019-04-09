.. doctest docs/specs/noi/general.rst
.. _noi.specs.general:

=================
Lino Noi Overview
=================

The goal of Lino Noi is managing **tickets** (problems reported by
customers or other users) and registering the **time** needed by
developers or other users to work on these tickets.
It is then possible to publish **service reports**.
It is also used for managing agile development projects.



.. contents::
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *



Ticket management is not Worktime tracking
==========================================

Lino Noi uses both :mod:`lino_xl.lib.tickets` (Ticket management) and
:mod:`lino_xl.lib.working` (Worktime tracking).

But :mod:`lino_xl.lib.tickets` is an independent plugin which might be
reused by other applicaton that have no worktime tracking.  Lino Noi
uses them both and extends the "library" version of tickets:

- :mod:`lino_noi.lib.tickets` 

>>> dd.plugins.working
lino_xl.lib.working

>>> dd.plugins.tickets
lino_noi.lib.tickets (extends_models=['Ticket', 'Site'])

>>> dd.plugins.working.needs_plugins
['lino_noi.lib.noi', 'lino_noi.lib.tickets', 'lino.modlib.summaries', 'lino.modlib.checkdata']

>>> dd.plugins.tickets.needs_plugins
['lino_xl.lib.excerpts', 'lino.modlib.comments', 'lino.modlib.changes', 'lino_noi.lib.noi']



User types
==========

A default Lino Noi site has the following user types:

>>> rt.show(users.UserTypes)
======= ============ ==================
 value   name         text
------- ------------ ------------------
 000     anonymous    Anonymous
 100     user         User
 200     consultant   Consultant
 300     hoster       Hoster
 400     developer    Developer
 490     senior       Senior developer
 900     admin        Administrator
======= ============ ==================
<BLANKLINE>


A **user** is somebody who uses some part of the software being
developed by the team. This is usually the contact person of a
customer.

A **consultant** is an intermediate agent between end-users and the
team.

A **hoster** is a special kind of customer who installs and maintains
servers where Lino applications run.

A **developer** is somebody who works on tickets by doing code
changes.

A **senior** is a developer who additionaly can triage tickets.

Here is a list of user types of those who can work on tickets:

>>> from lino_xl.lib.working.roles import Worker
>>> UserTypes = rt.models.users.UserTypes
>>> [p.name for p in UserTypes.items()
...     if p.has_required_roles([Worker])]
['consultant', 'hoster', 'developer', 'senior', 'admin']

And here are those who don't work:

>>> [p.name for p in UserTypes.items()
...    if not p.has_required_roles([Worker])]
['anonymous', 'user']


Users
=====

>>> rt.show('users.UsersOverview')
========== ======================== ==========
 Username   User type                Language
---------- ------------------------ ----------
 jean       490 (Senior developer)   en
 luc        400 (Developer)          en
 marc       100 (User)               en
 mathieu    200 (Consultant)         en
 robin      900 (Administrator)      en
 rolf       900 (Administrator)      de
 romain     900 (Administrator)      fr
========== ======================== ==========
<BLANKLINE>


Countries
=========

>>> rt.show(countries.Countries)
============================= ================================ ================================= ==========
 Designation                   Designation (de)                 Designation (fr)                  ISO code
----------------------------- -------------------------------- --------------------------------- ----------
 Belgium                       Belgien                          Belgique                          BE
 Congo (Democratic Republic)   Kongo (Demokratische Republik)   Congo (République democratique)   CD
 Estonia                       Estland                          Estonie                           EE
 France                        Frankreich                       France                            FR
 Germany                       Deutschland                      Allemagne                         DE
 Maroc                         Marokko                          Maroc                             MA
 Netherlands                   Niederlande                      Pays-Bas                          NL
 Russia                        Russland                         Russie                            RU
============================= ================================ ================================= ==========
<BLANKLINE>


.. just another test:

    >>> json_fields = 'count rows title success no_data_text'
    >>> kwargs = dict(fmt='json', limit=10, start=0)
    >>> demo_get('robin', 'api/countries/Countries', json_fields, 9, **kwargs)



Lino Noi and Scrum
==================

- Every sprint is registered as a site
- Usually there is at least one ticket per site for planning and
  discussion.
- Every backlog item is registered as a ticket on that site
- The detail view of a site is the equivalent of a backlog  

>>> show_fields(system.SiteConfig)
... #doctest: +REPORT_UDIFF
+----------------------+----------------------+---------------------------------------------------------------------+
| Internal name        | Verbose name         | Help text                                                           |
+======================+======================+=====================================================================+
| default_build_method | Default build method | The default build method to use when rendering printable documents. |
+----------------------+----------------------+---------------------------------------------------------------------+
| simulate_today       | Simulated date       | A constant user-defined date to be substituted as current           |
|                      |                      | system date.                                                        |
+----------------------+----------------------+---------------------------------------------------------------------+
| site_company         | Site owner           | The organisation who runs this site.  This is used e.g. when        |
|                      |                      | printing your address in certain documents or reports.  Or          |
|                      |                      | newly created partners inherit the country of the site owner.       |
+----------------------+----------------------+---------------------------------------------------------------------+
| next_partner_id      | Next partner id      | The next automatic id for any new partner.                          |
+----------------------+----------------------+---------------------------------------------------------------------+
| default_event_type   | Default Event Type   | The default type of events on this site.                            |
+----------------------+----------------------+---------------------------------------------------------------------+
| site_calendar        | Site Calendar        | The default calendar of this site.                                  |
+----------------------+----------------------+---------------------------------------------------------------------+
| max_auto_events      | Max automatic events | Maximum number of automatic events to be generated.                 |
+----------------------+----------------------+---------------------------------------------------------------------+
| hide_events_before   | Hide events before   | If this is not empty, any calendar events before that date are      |
|                      |                      | being hidden in certain places.                                     |
+----------------------+----------------------+---------------------------------------------------------------------+

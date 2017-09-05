.. _noi.specs.general:

=================
Lino Noi Overview
=================

.. How to test just this document:

    $ doctest docs/specs/noi/general.rst
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *



.. contents::
  :local:

     
The goal of Lino Noi is managing **tickets** (problems reported by
customers or other users) and registering the **time** needed by
developers or other users to work on these tickets.
It is then possible to publish **service reports**.
It is also used for managing agile development projects.


Ticket management is not Worktime tracking
==========================================

Lino Noi uses both :mod:`lino_xl.lib.tickets` (Ticket management) and
:mod:`lino_xl.lib.clocking` (Worktime tracking).

Note that :mod:`lino_xl.lib.clocking` and :mod:`lino_xl.lib.tickets`
are independent modules which might be reused by other applicaton.
Lino Noi uses them both and extends the "library" versions:

- :mod:`lino_noi.lib.clocking` 
- :mod:`lino_noi.lib.tickets` 

>>> dd.plugins.clocking
lino_noi.lib.clocking

>>> dd.plugins.tickets
lino_noi.lib.tickets (extends_models=['Ticket'])

For example, a service report is part of the clocking plugin, but the
current implementation is defined in :mod:`lino_noi.lib.clocking` (not
in :mod:`lino_xl.lib.clocking`) because it makes sense only if you
have both clocking and tickets.


>>> dd.plugins.clocking.needs_plugins
['lino_noi.lib.tickets']

>>> dd.plugins.tickets.needs_plugins
['lino_xl.lib.excerpts', 'lino_xl.lib.topics', 'lino.modlib.comments', 'lino.modlib.changes', 'lino_noi.lib.noi']

See also :attr:`needs_plugins <lino.core.plugin.Plugin.needs_plugins>`.


User types
==========

A default Lino Noi site has the following user types:

>>> rt.show(users.UserTypes)
======= ============ ================== ========================================
 value   name         text               User role
------- ------------ ------------------ ----------------------------------------
 000     anonymous    Anonymous          lino_noi.lib.noi.user_types.Anonymous
 100     user         User               lino_noi.lib.noi.user_types.EndUser
 200     consultant   Consultant         lino_noi.lib.noi.user_types.Consultant
 300     hoster       Hoster             lino_noi.lib.noi.user_types.Consultant
 400     developer    Developer          lino_noi.lib.noi.user_types.Developer
 490     senior       Senior developer   lino_noi.lib.noi.user_types.Senior
 900     admin        Administrator      lino_noi.lib.noi.user_types.SiteAdmin
======= ============ ================== ========================================
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

>>> from lino_xl.lib.clocking.roles import Worker
>>> UserTypes = rt.modules.users.UserTypes
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
========== ================== ==========
 Username   User type          Language
---------- ------------------ ----------
 jean       Senior developer   en
 luc        Developer          en
 mathieu    Consultant         en
 robin      Administrator      en
 rolf       Administrator      de
 romain     Administrator      fr
========== ================== ==========
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
    >>> demo_get('robin', 'api/countries/Countries', json_fields, 8, **kwargs)



Lino Noi and Scrum
==================

- Every sprint is registered as a subproject of a development project
- Every backlog item is registered as a subproject of a sprint
- IOW backlog items are projects without children
- Usually there is at least one ticket per project for planning and
  discussion.



>>> show_fields(system.SiteConfig)
... #doctest: -REPORT_UDIFF
+----------------------+----------------------+---------------------------------------------------------------------+
| Internal name        | Verbose name         | Help text                                                           |
+======================+======================+=====================================================================+
| id                   | ID                   |                                                                     |
+----------------------+----------------------+---------------------------------------------------------------------+
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
| hide_events_before   | Hide events before   | If this is specified, certain tables show only                      |
|                      |                      | events after the given date.                                        |
+----------------------+----------------------+---------------------------------------------------------------------+
| mobile_item          | Description          |                                                                     |
+----------------------+----------------------+---------------------------------------------------------------------+
| overview             | Description          |                                                                     |
+----------------------+----------------------+---------------------------------------------------------------------+
| workflow_buttons     | Workflow             |                                                                     |
+----------------------+----------------------+---------------------------------------------------------------------+

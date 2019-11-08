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

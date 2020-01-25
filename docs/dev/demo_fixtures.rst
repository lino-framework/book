.. _demo_fixtures:

=============
Demo fixtures
=============

A **fixture**, in Django, is a portion of data (a collection of data
records in one or several tables) which can be loaded into a database.

.. xfile:: fixtures

Fixtures are defined by the files in so-called :xfile:`fixtures` directories.
When a plugin has a subpackage named :xfile:`fixtures`, Django will discover
this package when you run the :manage:`loaddata` command. This is standard
Django knowledge. Read more about it in the `Django documentation
<https://docs.djangoproject.com/en/1.9/howto/initial-data/>`_.

Lino uses this to define the concept of **demo fixtures**. These are a
predefined set of fixture names to be specified by the application developer in
the :attr:`demo_fixtures <lino.core.site.Site.demo_fixtures>` attribute. The
`min1` application has the following value for this attribute:

>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.demo')
>>> from django.conf import settings
>>> settings.SITE.demo_fixtures
'std demo demo2'

This means that the :manage:`prep` command (in a
:mod:`lino_book.projects.min1` application) is equivalent to::

  $ python manage.py initdb std demo demo2

The difference between :manage:`initdb` and :manage:`prep` is that with
:manage:`prep`, you don't need to know the list of demo fixtures when invoking
the command. The default list of demo fixtures to load for initializing a
"clean" standard demo database can be long and difficult to remember, and (more
importantly) which can change when an application evolves.  System
administrators usually don't *want* to know such details. As a future
application developer you can learn more about them in
:ref:`lino.tutorial.writing_fixtures`.

Note that in Lino we usually don't write fixtures in XML or JSON but
:doc:`write them in Python </dev/pyfixtures/index>`.

The loading phases of demo fixtures
===================================

We suggest to see each fixture name as a **loading phase**. It is up to the
application developer to specify a meaningful set of loading phases in the
:attr:`demo_fixtures <lino.core.site.Site.demo_fixtures>` setting.

Our convention is to define the following loading phases::

    std minimal_ledger demo demo_bookings payments demo2 checkdata

:fixture:`std`
:fixture:`minimal_ledger`
:fixture:`demo`
:fixture:`demo_bookings`
:fixture:`payments`
:fixture:`demo2`
:fixture:`checkdata`


The loading order of demo data is important because the fixtures of the
:ref:`xl` are inter-dependent.  They create users, cities, journals, contacts,
invoices, payments, reports, notifications, ...  you cannot write invoices if
you have no customers, and an accounting report makes no sense if bank
statements haven't been entered.

Lino basically uses Django's approach of finding demo fixtures: When Django
gets a series of fixture names to load, it will load them in the specified
order, and for each fixture will ask each plugin to load that fixture.  If a
plugin doesn't define a fixture of that name, it simply does nothing.

The :attr:`demo_fixtures <lino.core.site.Site.demo_fixtures>` setting is a
string with a space-separated list of fixture names to be loaded by
:manage:`prep`.

.. fixture:: std

The :fixture:`std` fixtures should add default database content expected to be
in a virgin database even when no "demo data" is requested. This should always
be the first fixture of your :attr:`demo_fixtures
<lino.core.site.Site.demo_fixtures>` setting.  It is provided by the following
plugins:

- :mod:`lino.modlib.users`
  Create an excerpt type "Welcome letter" (when appypod and excerpts are installed)

- :mod:`lino.modlib.tinymce`
- :mod:`lino.modlib.gfks`
- :mod:`lino_xl.lib.cv`
- :mod:`lino_xl.lib.coachings`
- :mod:`lino_xl.lib.bevat` creates an excerpt type for the VAT declaration.
- :mod:`lino_xl.lib.bevats` does nothing
- :mod:`lino_xl.lib.eevat` does nothing
- :mod:`lino_xl.lib.contacts` adds a series of default company types.

- :mod:`lino_xl.lib.deploy`
- :mod:`lino_xl.lib.pages`

- :mod:`lino_xl.lib.ledger` creates some *payment terms*.
  Creates an *account* for every item of
  :class:`CommonAccounts <lino_xl.lib.ledger.CommonAccounts>`, which results in a minimal
  accounts chart.

- :mod:`lino_xl.lib.sheets`
  creates common sheet items and assigns them to their accounts.

- :mod:`lino_xl.lib.households` adds some household member roles.

- :mod:`lino_xl.lib.cal` installs standard calendar entry types, including a
  set of holidays.  (TODO: make them more configurable.)
  The default value of
  :attr:`lino.modlib.system.SiteConfig.hide_events_before` is set to
  January 1st (of the current year when demo_date is after April and of
  the previous year when demo_date is before April).
  See also :ref:`xl.specs.holidays`.

- :mod:`lino_xl.lib.sales` creates some common paper types.

- :mod:`lino_xl.lib.working`
- :mod:`lino_xl.lib.polls`
- :mod:`lino_xl.lib.notes`
- :mod:`lino_xl.lib.excerpts`



.. fixture:: minimal_ledger

Add minimal config data.
Should come after :fixture:`std` and before :fixture:`demo`.

- :mod:`lino_xl.lib.vat` sets VAT column for common accounts

- :mod:`lino_xl.lib.ledger` adds a minimal set of journals and match rules.

- :mod:`lino_xl.lib.ana` creates analytic accounts and
  assigns one of them to each general account with :attr:`needs_ana` True


.. fixture:: demo

Adds master demo data.

- :mod:`lino.modlib.users`
  adds fictive root users (administrators), one for
  each language.  These names are being used by the online demo
  sites.
  We are trying to sound realistic without actually hitting any real
  person.

- :mod:`lino_xl.lib.humanlinks` creates two fictive families (Hubert & Gaby
  Frisch-Frogemuth with their children and grand-children).


- :mod:`lino_xl.lib.sepa` adds some commonly known companies and their bank
  accounts. These are real data collected from Internet.

- :mod:`lino_xl.lib.countries` adds
  :mod:`few_countries <lino_xl.lib.countries.fixtures.few_countries>`
  and
  :mod:`few_cities <lino_xl.lib.countries.fixtures.few_cities>`.

- :mod:`lino_xl.lib.contacts`
  adds a series of fictive persons and companies.

- :mod:`lino_xl.lib.mailbox`
  Adds a mailbox named "team".

- :mod:`lino_xl.lib.ledger`
  sets :attr:`lino_xl.lib.contacts.Partner.payment_term` of all partners.

- :mod:`lino_xl.lib.vat`
  Sets fictive VAT id for all companies and then a VAT regime for all partners.

- :mod:`lino_xl.lib.sheets`
  adds an excerpt type to print a sheets.Report

- :mod:`lino_xl.lib.households`
  creates some households by marrying a few Persons.
  Every third household gets divorced: we put an `end_date` to that
  membership and create another membership for the same person with
  another person.

- :mod:`lino_xl.lib.lists`

- :mod:`lino_xl.lib.groups`
  creates some user groups and users Andy, Bert and Chloé.

- :mod:`lino_xl.lib.notes`


.. fixture:: demo_bookings

Adds more demo data (originally "bookings").
Should come after :fixture:`demo`.

- :mod:`lino_xl.lib.invoicing`
  creates monthly invoicing plans and executes them.
  Starts a January 1st of :attr:`lino_xl.lib.ledger.Plugin.start_year`.
  Stops 2 months before today (we "forgot" to run invoicing the last two months)
  because we want to have something in our invoicing plan.

- :mod:`lino_xl.lib.ledger`
  Creates fictive monthly purchase invoices.

- :mod:`lino_xl.lib.sales` creates fictive monthly sales.


.. fixture:: payments

Adds even more demo data (originally "payments").
Should come after :fixture:`demo_bookings`.

- :mod:`lino_xl.lib.bevat`
  creates a Belgian VAT office and some VAT declarations.

- :mod:`lino_xl.lib.bevats`
  creates a Belgian VAT office and some VAT declarations.

- :mod:`lino_xl.lib.eevat`
  creates an Estonian VAT office and some VAT declarations.

- :mod:`lino_xl.lib.finan` creates automatic monthly payment orders and bank
  statements.  Bank statements of last month are not yet entered into database


.. fixture:: demo2

Add final demo data.

- :mod:`lino.modlib.users` sets password 1234 for all users.

- :mod:`lino.modlib.comments` adds some fictive comments.

- :mod:`lino.modlib.notify`
  sends a notification "The database has been initialized" to every user.

- :mod:`lino_xl.lib.addresses`
  adds some additional non-primary addresses to some partners.

- :mod:`lino_xl.lib.sheets`
  creates some accounting reports (one per year).

- :mod:`lino_xl.lib.cal`
  generates 60 fictive appointments and 10 absences "for private reasons".

- :mod:`lino_xl.lib.phones`
  runs :meth:`propagate_contact_details` for each partner.

- :mod:`lino_xl.lib.groups`
  creates a membership for every user in one or two groups and a welcome comment
  for each membership.

- :mod:`lino_xl.lib.polls`
  creates a response for every poll.

- :mod:`lino_xl.lib.votes.fixtures.demo2`
- :mod:`lino_xl.lib.dupable_partners.fixtures.demo2`
- :mod:`lino_xl.lib.excerpts.fixtures.demo2`


.. fixture:: checkdata

Should come after :fixture:`demo2`.

This fixture should always be the last in your :attr:`demo_fixtures
<lino.core.site.Site.demo_fixtures>` setting.

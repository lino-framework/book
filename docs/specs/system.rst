.. doctest docs/specs/system.rst
.. _specs.system:

=================================
``system`` : some system features
=================================

.. currentmodule:: lino.modlib.system

The :mod:`lino.modlib.system` plugin defines some system features that are
automatically installed with every Lino application.

It especially provides the :class:`SiteConfig` model.


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

Code snippets in this document are tested using the
:mod:`lino_book.projects.noi1e` demo project.

>>> import lino
>>> lino.startup('lino_book.projects.noi1e.settings.doctests')
>>> from lino.api.doctest import *


Editable site parameters
========================

Lino provides a standard method for defining persistent site parameters that are
editable by :term:`end users <end user>` (at least for those who have access
permission).

.. class:: SiteConfig

    A singleton database object used to store persistent site parameters.

    This model has exactly one instance, which is accessible as the
    :attr:`settings.SITE.site_config <lino.core.site.Site.site_config>`
    property.

    .. attribute:: default_build_method

        The default build method to use when rendering printable documents.

        If this field is empty, Lino uses the value found in
        :attr:`lino.core.site.Site.default_build_method`.

    .. attribute:: simulate_today

        A constant user-defined date to be substituted as current
        system date.

        This should be empty except in situations such as *a
        posteriori* data entry in a prototype.

    .. attribute:: site_company

        The :term:`site operator`, i.e. the legal person that operates this
        :term:`Lino site`.

        This can be used e.g. when printing your address in documents or
        reports.  Or newly created partners inherit the country of the site
        operator.

        If no plugin named 'contacts' is installed, then this is a
        dummy field and always contains `None`.

    .. attribute:: hide_events_before

        If this is not empty, any calendar events before that date are
        being hidden in certain places.

        For example OverdueEvents, EntriesByController, ...

        Injected by :mod:`lino_xl.lib.cal`.

.. class:: SiteConfigManager

    Always return the cached instance which holds the one and only
    database instance.

    This is to avoid the following situation:

    - User 1 opens the :menuselection:`Configure --> System--> System
      Parameters` dialog
    - User 2 creates a new Person (which increases `next_partner_id`)
    - User 1 clicks on `Save`.

    `next_partner_id` may not get overwritten by its old value when
    User 1 clicks "Save".

.. class:: Lockable

    Mixin to add row-level edit locking to any model.

    Models with row-level edit locking are not editable in detail view
    by default.  All form fields are disabled. The user must click
    :guilabel:`Edit` in order to request an edit lock for that row.
    This will enable all fields (except those which are disabled for
    some other reason).

    Caveats: locking a row and then navigating away without changing
    anything will leave the row locked.


.. class:: BuildSiteCache

    Rebuild the site cache.
    This action is available on :class:`About`.


.. class:: SiteConfigs

    The table used to present the :class:`SiteConfig` row in a Detail form.

    See also :meth:`lino.core.site.Site.get_site_config`.



.. class:: BleachChecker

    A data checker used to find unbleached html content.


.. class:: Genders

    Defines the two possible choices "male" and "female"
    for the gender of a person.

    See :ref:`lino.tutorial.human` for examples.
    See :doc:`/dev/choicelists`.


.. class:: YesNo

    A choicelist with two values "Yes" and "No".

    Used e.g. to define parameter panel fields for BooleanFields::

      foo = dd.YesNo.field(_("Foo"), blank=True)

.. class:: ObservedEvent

    Base class for choices of "observed event"-style choicelists.

    .. method:: add_filter(self, qs, pv)

        Add a filter to the given Django queryset. The given `obj` must be
        either a `datetime.date` object or must have two attributes
        `start_date` and `end_date`. The easiest way is to have it an
        instance of :class:`DateRange
        <lino.mixins.periods.DateRange>` or :class:`DateRangeValue
        <lino.utils.dates.DateRangeValue>`.




.. class:: PeriodEvents

    The list of things you can observe on a
    :class:`lino.mixins.periods.DateRange`.

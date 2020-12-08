.. doctest docs/specs/about.rst
.. _specs.about:

====================================
``about`` : Information about a site
====================================

.. currentmodule:: lino.modlib.about

The :mod:`lino.modlib.about` plugin is always installed.  It defines some
virtual tables and choicelists, but no database models. See also :doc:`search`


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.noi1e.settings.doctests')
>>> from lino.api.doctest import *

Which means that code snippets in this document are tested using the
:mod:`lino_book.projects.noi1e` demo project.

Information about the site
==========================

.. class:: About

    A dialog window which displays some information about the site.

    Versions of used third-party libraries.

    Time stamps of source code.

    **Complexity factors:** Some numbers which express the complexity of this
    site.  These numbers can be used for computing the membership fee.
    See http://community.lino-framework.org/membership.html


Time zones
==========

Every Lino site can define its own list of time zones.

>>> rt.show('about.TimeZones')
======= ========= =================
 value   name      text
------- --------- -----------------
 01      default   UTC
 02                Europe/Tallinn
 03                Europe/Brussels
 04                Africa/Tunis
======= ========= =================
<BLANKLINE>



This list is usually populated in the local :attr:`workflows_module
<lino.core.site.Site.workflows_module>` of a project.  For example::

    # don't forget to import the default workflows:
    from lino_noi.lib.noi.workflows import *

    from lino.modlib.about import TimeZones
    TimeZones.clear()
    add = TimeZones.add_item
    add('01', settings.TIME_ZONE or 'UTC', 'default')
    add('02', "Europe/Tallinn")
    add('03', "Europe/Brussels")
    add('04', "Africa/Tunis")


.. class:: TimeZones

    The list of time zones available on this site.

    This choicelist always contains at least one choice named
    :attr:`default`.

    You can redefine this choicelist in your local
    :attr:`workflows_module <lino.core.site.Site.workflows_module>`.

    .. attribute:: default

        The default time zone on this server, corresponding to
        :setting:`TIME_ZONE`.  Unlike :setting:`TIME_ZONE` (which is a
        string), :attr:`default` is a choice object whose :attr:`text`
        is the same as the string and which has an attribute
        :attr:`tzinfo` which contains the time zone info object.

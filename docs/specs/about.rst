.. doctest docs/specs/about.rst
.. _specs.about:

The ``lino.modlib.about`` plugin
================================

..  doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *


The :mod:`lino.modlib.about` plugin is always installed.  It defines
some virtual tables and choicelists, but no database models.

See also :doc:`/specs/search`

.. currentmodule:: lino.modlib.about

                   
.. class:: SiteSearch

    Search across all tables of the application.
           
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
        
    

The :mod:`lino_book.projects.team` is an example of a site which
defines a list of time zones:

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
              
This list is populated in the local :attr:`workflows_module
<lino.core.site.Site.workflows_module>` of that project::

    # don't forget to import the default workflows:
    from lino_noi.lib.noi.workflows import *
    
    from lino.modlib.about import TimeZones
    TimeZones.clear()
    add = TimeZones.add_item
    add('01', settings.TIME_ZONE or 'UTC', 'default')
    add('02', "Europe/Tallinn")
    add('03', "Europe/Brussels")
    add('04', "Africa/Tunis")


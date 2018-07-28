.. _dev.xl:

================================
The Lino Extensions Library (XL)
================================

The :ref:`Lino Extensions Library <xl>` is a collection of plugins
used by many Lino projects.

It is in a separate repository because not everybody might want it.
If you just want to write a quick database application from scratch,
you maybe won't want to dive into all these concepts right now.  It is
*a big library*.  On the other hand it is *not big enough* : it is
still just *one* possible view of the world, and even an uncomplete
one.  For example :ref:`welfare` is a plugin library based on the XL
but adding new concepts that are specific to the work of Belgian
social centers.

Where is the borderline between a "core" plugin and an "XL" plugin
(:mod:`lino_xl.lib`)?  The theoretical answer is that
:mod:`lino.modlib` contains functionality which is remains useful for
people who don't want the XL.

But for example we have two plugins :mod:`printing` and
:mod:`excerpts`.  The :mod:`printing` plugin is in the core
(:mod:`lino.modlib`) while :mod:`excerpts` is in :mod:`lino_xl.lib`.
Yes, it remains arbitrary choice.

TODO: move :mod:`languages` and :mod:`office` to the XL?  And what
about :mod:`vocbook`?  Move :mod:`excerpts` to the core?

  

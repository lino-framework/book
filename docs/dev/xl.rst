.. _dev.xl:

======================================
Introduction to the Extensions Library
======================================

The :ref:`Lino Extensions Library <xl>` is a collection of plugins
used by many --but not all-- Lino projects.

It is in a separate repository because not everybody might want it:

- It is *a big library*. If you just want to write a quick database
  application from scratch, you maybe won't not want to dive into all
  these concepts right now.
  
- It is *not big enough* : it is still just *one* possible view of the
  world, and even an uncomplete one.

Where is the borderline between a "core" plugin and an "XL" plugin
(:mod:`lino_xl.lib`)?

The theoretical answer is: :mod:`lino.modlib` contains functionality
which is still useful for people who don't want the XL.

We have two plugins :mod:`printing` :mod:`excerpts`. The
:mod:`printing` plugin is in the core (:mod:`lino.modlib`) while
:mod:`excerpts` is in :mod:`lino_xl.lib`.  Why?

Todo: move :mod:`languages` and :mod:`office` to the XL?
And :mod:`vocbook`?

  

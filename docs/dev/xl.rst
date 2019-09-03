.. _dev.xl:

==================
Extensions Library
==================

The :term:`Extensions Library` or **XL** (stored in the :mod:`lino_xl` package)
is a :term:`plugin library` considered  part of the :term:`Lino framework` but
not of the :doc:`/specs/modlib`. It is used by many Lino applications. 

It is separate from the :doc:`/specs/modlib` because not everybody might want
these features. It is *a big library*: newbies maybe won't want to dive into all
these concepts right now. On the other hand it is *not big enough* : it is still
just *one* possible view of the world, and even an incomplete one.

Where is the borderline between the  and an "XL" plugin?  The
theoretical answer is that the :doc:`/specs/modlib` contains
"basic features".
functionality which is
remains useful for people who don't want the XL.

But for example we have two plugins :mod:`printing` and
:mod:`excerpts`.  The :mod:`printing` plugin is in the core
(:mod:`lino.modlib`) while :mod:`excerpts` is in :mod:`lino_xl.lib`.
Yes, it remains arbitrary choice.

TODO: move :mod:`languages` and :mod:`office` to the XL?  And what
about :mod:`vocbook`?  Move :mod:`excerpts` to the core?

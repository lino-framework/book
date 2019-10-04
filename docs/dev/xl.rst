.. _dev.xl:

============================
About the Extensions Library
============================

The :term:`Extensions Library` or **XL** is a :term:`plugin library` considered
part of the :term:`Lino framework` and used by many Lino applications.

It is stored in the :mod:`lino_xl` package. See :ref:`specs.xl` for the list of
plugins.

It is separate from the :doc:`/specs/modlib` because not everybody might want
it. It is *a big library*, so beginners might not want to dive into all these
concepts right now. And despite our efforts of making it very reusable, it is
still just *one* possible view of the world which you might not want to share.

Where is the borderline between the  and an "XL" plugin?  The theoretical answer
is that the :doc:`/specs/modlib` contains "basic features" which remain useful
also for people who don't want the XL.

The borderline is neither very clear nor definitive. For example we have two
plugins :mod:`printing <lino.modlib.printing>` and :mod:`excerpts
<lino_xl.lib.excerpts>`.  The former in the core (:mod:`lino.modlib`) while the
latter is in :mod:`lino_xl.lib`. Yes, it remains arbitrary choice.

TODO: move :mod:`languages` and :mod:`office` to the XL?  Move :mod:`excerpts`
to the core? And what about :mod:`vocbook`?

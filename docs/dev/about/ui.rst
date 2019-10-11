.. _about.ui:
.. _lino.ui:

==========================================
Separate business logic and front end
==========================================

People tend to judge a framework by its front-end because this is the only
"visible" part of an application.

But Lino's beauty lies beyond the front end.  Lino is designed to have *many
possible* front ends.  Lino comes with an extensible collection of
*out-of-the-box* front ends.  You can write a Lino application once and then
deploy it via different web interfaces.

So it is difficult to answer the question "how does Lino look like"?

There are currently two realistic choices for the front end:
:mod:`lino.modlib.extjs` (the classic front end based on ExtJS) and the
:ref:`React front end <react>` (the new front end that will replace ExtJS step
by step). The `Demo sites <http://www.lino-framework.org/demos.html>`__ page
shows both front ends for some applications.

The quality of these front ends is *admittedly less user-friendly* than what
people are used to get on big web applications where hundreds of developers have
been working hard to make it a perfect ergonomic experience.

But it is *good enough*.  More than hundred users use it every day, and most of
them love it.  Which doesn't mean that they never complain about certain known
oddnesses.  Don't forget that complaining is an integral part of loving.

Lino has currently only this one choice because because writing and maintaining
a front end is a big task, because our resources are limited, and because there
are many other, more interesting tasks to be done.

There are several proofs of concept for alternative front ends. An overview of
these research projects in :doc:`/dev/ui`.

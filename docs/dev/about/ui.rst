.. _about.ui:
.. _lino.ui:

==========================================
Separate business logic and user interface
==========================================

People tend to judge a framework by its user interface or front-end
because this is the only "visible" part of an application.

So it is difficult to answer the question "how does Lino look like"?

But Lino's beauty lies beyond the user interface.  Lino is designed to
have *many possible* user interfaces.  Lino comes with an extensible
collection of *out-of-the-box* user interfaces.  You can write a Lino
application once and then deploy it via different interfaces.

That said, there is currently indeed only one realistic choice for the user
interface, the one based on ExtJS.  Lino applications "look like" those you can
see at the `Demo sites <http://www.lino-framework.org/demos.html>`__ page.

The qualitiy of this user interface is *admittedly less* than what
people are used to get on big web applications where hundreds of
developers have been working hard to make it a perfect ergonomic
experience.

But it is *good enough*.  Its only serious limitation is that it is
not very usable on mobile devices.  But more than hundred users use it
every day, and most of them love it.  Which doesn't mean that they
never complain about certain known oddnesses.  Don't forget that
complaining is an integral part of loving.

Lino has currently only this one choice because because writing and
maintaining a user interface is a big task, because our resources are
limited, and because there are many other, more interesting tasks to
be done.

There are several proofs of concept for alternative user interfaces.
An overview of these research projects in :doc:`/dev/ui`.



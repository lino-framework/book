.. _about.ui:
.. _lino.ui:

==========================================
Separate business logic and user interface
==========================================

People tend to judge a framework by its user interface or front-end,
because this is the first and almost only "visible" part of an
application.

But Lino is designed to have **many possible** user interfaces.  Lino
comes with an extensible collection of *out-of-the-box* user
interfaces.  You can write a Lino application once and then deploy it
via different interfaces.

That said, the only realistic choice is currently indeed the ExtJS UI.
Lino applications "look like" those you can see at :doc:`/demos`.

The qualitiy of Lino's user interface is just *good enough* and
admittedly less than what people are used to get on big web
applications where hundreds of developers have been working hard to
make it a perfect ergonomic experience.  Lino's beauty lies beyond the
user interface.

Lino has currently only this one choice because because writing and
optimizing a user interface is a rather boring task, and there are
many other, more interesting tasks that are waiting to be done, and,
last but not least, because the ExtJS UI is actually quite usable,
once you accept a few known oddnesses.

There are several proofs of concept for alternative user interfaces.
We discuss them in the :doc:`Developer's Guide </dev/ui>`.



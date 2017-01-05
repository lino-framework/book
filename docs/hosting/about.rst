=============================
Being a Lino hosting provider
=============================

As a qualified *Lino hosting provider* you assume the following
**responsibilities**:

- You set up a virtual machine running some Linux, usually Debian,
  where a maintainer will have SSH access.

- You care about registering a domain name and SSH certificates if the
  customer needs it.

- you care about security and protect the system against hackers
  
- you make backups of the data to make sure it doesn't get lost in
  case of a serious accident.
  
- you care about scaling. When a customer's site grows, then they
  might want to move to a bigger machine.

- you care about reliability and make sure that the Lino site is
  always available to respond when your customer needs it.

- you help end-users with certain problems.

Development hosting
===================
  
In case of **development hosting** (the easiest case for you) the
customer has two contracts: one with a developer and one with you.
You are not reponsible for maintaining the system software on that
server, nor answering end-user questions about how to use or configure
the software. That's the job of the developer.

Your contract with the customer will have the form of an `SLA
<https://en.wikipedia.org/wiki/Service-level_agreement>`__.

You should have at least one employee who is able to act as
**emergency maintainer**.  An emergency maintainer knows how a Lino
application works (as described in :doc:`/admin/index`) and how to
react in certain situations:

- connection problems caused by the end-user's machine
- diagnose and fix server-side problems like performance
- get the server back to work after a technical problem

It is also your emergency maintainer who will decide whether and when
you are able to offer **stable hosting** for one or several Lino
applications.

.. _stable_hosting:

Stable hosting
==============

The difference between development and stable hosting is that your
emergency maintainer has grown into an independent maintainer who can
maintain the system software, give limited end-user support and
install new versions of the application when the customer asks you to
do so.  In stable mode, the customer pays more money to you because
you provide additional services and because they don't need support by
a developer.  With stable hosting, no external developer has access to
your customer's server.

.. The Lino team suggests a **price** around 100€ per month per site
   for development hosting. The prices for stable hosting are higher,
   and they depend on the application and your tarification system.


================
Types of hosting
================

There are three types of Lino hosting:
  
- in case of **basic hosting** the hoster is *not reponsible* for
  *end-user support* and *regular maintenance*.  The site owner needs a
  second agreement with a :doc:`developer </community/developers>` for
  these.
       
- in case of **stable hosting** the hoster also offers these services,
  i.e. they answer end-user questions about how to use or configure the
  software, and they are able upgrade the site when new versions of the
  software are available. They may or may not forward any reported
  problems to a developer.

- in case of **development hosting** the hoster additionally provides
  end-user support and maintenance of a Lino application.


Basic hosting
=============
  
In case of **basic hosting** the customer has two contracts: one with
a developer and one with you.  

Your job is to provide and manage the server where the developer will
install and maintain Lino. You make sure that the server is available
and secure. You collaborate with the developer for certain tasks like
mail server setup.

You are *not* reponsible for maintaining the system software on that
server, nor answering end-user questions about how to use or configure
the software. That's the job of the developer.

You are able to act as **emergency maintainer**.  An emergency
maintainer knows how Lino is installed on the server (usually as
described in :doc:`/admin/index`) and how to react in certain
situations:

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

Development hosting
===================
  
In case of **development hosting** you offer both the hosting and the
development.


..
    A **master machine** is a virtual machine which hosts one or several
    demo sites on different Lino versions.

    customized for you by a
    developer

    You can set up and maintain a docker server and serve one of the
    dockerfiles maintained by the Lino team.  See e.g.
    https://docs.docker.com/engine/installation/linux/ubuntulinux/

    With Docker hosting the customer is always in stable mode and cannot
    switch to development mode.

    The Lino team plans to start this type of hosting as soon as there is
    a first pilot user.

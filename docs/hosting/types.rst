================
Types of hosting
================

As a hosting provider you may offer different types of hosting, we
call them "development", "stable" and "docker".

Development hosting
===================

You set up and maintain a virtual private server with a stable
Debian, a domain name and SSH access to be used by a Lino
developer with sudo permissions.

The customer has two contracts: one with the developer and one with
you.

The customer gets support from the developer, and the developer gets
support from you (e.g. in case of technical problems).

Stable hosting
==============

At any moment a customer can ask you to go into stable mode. In this
mode, the customer has no support by the developer and pays more money
to you because you provide two additional services: limited end-user
support and upgrades.

  
Docker hosting
==============

You set up and maintain a docker server and 
serve one of the dockerfiles maintained by the Lino team.
See e.g.
https://docs.docker.com/engine/installation/linux/ubuntulinux/

With Docker hosting the customer is always in stable mode and cannot
switch to development mode.

The Lino team plans to start this type of hosting as soon as there is
a first pilot user.

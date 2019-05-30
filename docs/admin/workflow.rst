.. _team.workflow:

Operations modes of a Lino production site
==========================================

Stable
======

The normal state of a production site. The primary goal of a site in this state
is that it just works: the server is always available, no changes in behaviour
which would confuse users.

Any issues reported by the site operator are collected as change requests

The developer works on the reported issues.

The developer publishes and maintains **release notes** for the coming version.

This document describes the issues that will be fixed by the coming version.

The release notes also explains any **non-requested changes** which will come
with the new version.  These can be caused by changes in dependencies, by
technology choices, changes in external services, ...

Users can ask at any moment to start a release. They decided that the advantage
of having these issues fixed is worth the work and risks caused by a release.


Preview testing
===============

The site administrator may run a preview site

We installed the latest version on their preview environment.  Users are now
invited to test that preview and to report their observations.

After some time of preview, the users declare that the preview is
okay and that they want it to go into production.

After release
=============

We upgrade their production environment to use
the version which has been in preview so far. During some time we
concentrate on removing any side effects and keep ready to react to
potential regression reports which might occur (because our test
suite ha not 100% coverage and because end-users didn't test
perfectly).

There can be additional updates during the next days which are
added to that same deployment in Noi.

After some time there are no more regressions and side effects reported: we
return to the Stable_ operation mode.

This is the moment to decide whether an official release (on PyPI) of the
involved projects makes sense.


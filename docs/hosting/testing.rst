.. _hosting.testing:

=========================
The `testing` environment
=========================

For certain customers it can be useful to provide a separate "testing"
site of their application.

A testing site contains a copy of their production site as it would
look if they were running the newest version.

A testing site is implemented as a subdomain with its own Python
environment and database.

It can be used for end-user driven tests before a release.  End-user
tests usually don't reveil important regressions (though that might
happen).  The primary goal of such a setup is more social than
technical: it encourages the local Lino community to develop a sane
communication culture for discussing about new features, and
priorities.


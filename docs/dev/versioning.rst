.. _dev.versioning:

==============================
Versioning and release process
==============================

Date-based versioning
=====================

The different projects maintained by the Lino Team depend quite
strongly on each other. This is why we adopted a date-based versioning
system.

Date-based versioning is similar to what Ubuntu uses: "Ubuntu releases
on a time based cycle, rather than a feature driven one. Sometimes
this can generate confusion, especially when people ask for a new
feature to be added."  (`ubuntu.com
<https://wiki.ubuntu.com/TimeBasedReleases>`__)

For us, "Version 16.10" means "The version we started to release in
October 2016". If a particular project decides that a bugfix release
is needed, then they would call it 16.10.1 (and so on) even if this
happens two months later.

Which projects

- :ref:`atelier`
  :ref:`lino`
  :ref:`xl`
  :ref:`book`
  :ref:`extjs6`
  :ref:`noi`
  :ref:`cosi`
  :ref:`welfare`
  :ref:`voga`
  :ref:`presto`
       


The release process
===================

- Check you have a clean working copy of all projects maintained by
  the Lino Team.

- Check that all test suites are passing and all doc trees are
  building.

- Update the `version` and `install_requires` in the
  :xfile:`setup_info.py` files of each project.

- Run :cmd:`pp inv ci`
  
- Run :cmd:`pp inv release`         

- Update the release notes.

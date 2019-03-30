.. _dev.specs:

========================
Technical specifications
========================

A **technical specification** page ("specs") is a page which contains prosa
documentation about a plugin.  It may also be a :ref:`tested document
<tested_docs>`.

The :doc:`/specs/index` section is an example of a collection of specs pages.

A specs page is meant for application developers, trainers and technical
analysts, not for end users. It should describe what that plugin is being used
for, and serve as a reference documentation.

For application developers it provides an important introduction into
what a given plugin does or is expected to do.

It is also an integral
part of our test suite since all code examples are automatically being
verified before each release.

There should be at least one specs page for every plugin. Every page ideally
explains all technical and functional aspects about a given plugin or topic.
If some functionality is covered by another specs page, it refers to these.

Specs template
==============

Here is an example about how a specs file should ideally be structures::

    .. doctest docs/specs/foo/bar.rst
    .. _nickname.specs.bar:

    ======================================
    ``bar`` :
    ======================================

    The :mod:`lino_nickname.lib.bar` plugin adds support for managing foos and
    bars.

    .. currentmodule:: lino_nickname.lib.bar

    .. contents::
       :depth: 2
       :local:

    .. include:: /../docs/shared/include/tested.rst

    >>> from lino import startup
    >>> startup('lino_nickname.projects.foo.settings.doctests')
    >>> from lino.api.doctest import *




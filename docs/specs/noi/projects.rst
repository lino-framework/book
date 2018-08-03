.. doctest docs/specs/noi/projects.rst
.. _noi.specs.projects:

==================
Project management
==================


.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *


This document specifies the project management functions of Lino Noi,
implemented in :mod:`lino_xl.lib.tickets`.

.. contents::
  :local:


What is a project?
==================

.. currentmodule:: lino_xl.lib.tickets.models

.. class:: Project

    A **project** is something on which several users work together.

    A Project is something into which somebody (the `partner`) invests
    time, energy and money.  The partner can be either external or the
    runner of the site.

    Projects form a hierarchical tree: each Project can have a
    `parent` (another Project for which it is a sub-project).

    A project in Noi is called a *product backlog item* (PBI) or a
    *Sprint* in Scrum. (At least for the moment we don't see why Lino
    should introduce a new database model for differentiating them. We
    have the ProjectType

    .. attribute:: name

    .. attribute:: parent

    .. attribute:: assign_to

        The user to whom new tickets will be assigned.
        See :attr:`Ticket.assigned_to`.


Ticket versus project
=====================

The difference between "ticket" and "project" might not be obvious.
For example something that started as a seemingly meaningless "ticket"
can grow into a whole "project". But if this happens in reality, then
you simply do it in the database.

The most visible difference is that projects are handled by their
*name* while tickets just have a *number*.  Another rule of thumb is
that tickets are atomic tasks while projects are a way for grouping
tickets into a common goal. Tickets are short term while projects are
medium or long term. Tickets are individual and have a single author
while projects are group work. The only goal of a ticket is to get
resolved while a project has a more complex definition of goals and
requirements.



Project types
=============

.. class:: ProjectType

    The type of a :class:`Project`.
           


.. class:: TimeInvestment
           
    Model mixin for things which represent a time investment.  This
    currently just defines a group of three fields:

    .. attribute:: closed

        Whether this investment is closed, i.e. certain things should
        not change anymore.

    .. attribute:: private

        Whether this investment is private, i.e. should not be
        publicly visible anywhere.
        
        The default value is True.  Tickets on public projects cannot
        be private, but tickets on private projects may be manually
        set to public.

    .. attribute:: planned_time

        The time (in hours) we plan to work on this project or ticket.

           

    

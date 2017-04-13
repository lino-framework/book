.. _specs.noi.deploy:

=================================
Deployment management in Lino Noi
=================================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_noi_deploy
    Or:
    $ python -m atelier.doctest_utf8 docs/specs/noi/deploy.rst
    
    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


This document specifies the ticket management functions implemented in
:mod:`lino_xl.lib.tickets` (as used by Lino Noi).

.. contents::
  :local:


.. currentmodule:: lino_xl.lib.deploy

     


What is a milestone
===================

What is a wish?
=================


.. class:: Deployment

    A **wish** (formerly "deployment") is the fact that a given ticket
    is being fixed (or installed or activated) by a given milestone
    (to a given site).
    
    A wish is when a given ticket occurs as item in a given milestone.

    .. attribute:: milestone

       The milestone (activity) containing this wish.

    .. attribute:: ticket
    .. attribute:: wish_type
    .. attribute:: remark

.. class:: WishTypes

    When a ticket occurs in a milestone, then we might want to qualify
    how or why it occured. We call it the "type" of that "wish".
    
    Internally this is done in the :attr:`Deployment.wish_type` field
    of the :class:`Deployment` model.
    
    Lino Noi knows the following types of wishes:

    >>> rt.show("deploy.WishTypes")
    ======= ============== ==============
     value   name           text
    ------- -------------- --------------
     10      talk           Agenda item
     20      new_feature    New feature
     22      optimization   Optimization
     25      bugfix         Bugfix
     30      gimmick        Gimmick
     40      side_effect    Side effect
     50      todo           Resolution
     60      aftermath      Aftermath
    ======= ============== ==============
    <BLANKLINE>
           

    .. attribute:: resolution

        a new ticket was created as the result of this milestone

           
.. class:: Deployments
.. class:: DeploymentsByMilestone

           
.. class:: DeploymentsByTicket

    Show the milestones where this ticket occurs as a wish.
           




For example, ticket #17 occurs as agenda item in milestone
20150513@welsch:

>>> obj = rt.models.tickets.Ticket.objects.get(pk=17)
>>> rt.show("deploy.DeploymentsByTicket", obj)
<ul><li><em>Gimmick</em> in <em>20150513@welsch</em> : </li></ul>
>>> rt.show("deploy.DeploymentsByTicket", obj, nosummary=True)
================= =========== ========
 Activity          Wish type   Remark
----------------- ----------- --------
 20150513@welsch   Gimmick
================= =========== ========
<BLANKLINE>



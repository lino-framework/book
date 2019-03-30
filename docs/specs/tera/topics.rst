.. doctest docs/specs/tera/topics.rst
.. _specs.tera.topics:

====================================
The ``topics`` plugin in :ref:`tera`
====================================

.. currentmodule:: lino_xl.lib.topics
                   
                   
:ref:`tera` uses the :mod:`lino_xl.lib.topics` plugin.  See
:doc:`/specs/topics` for a general description of this module.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst
             
>>> import lino
>>> lino.startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q


Overview
========

In :ref:`tera` the "partners" who can be interested in a topic are not
partners but therapies.  Users define topic interests *per therapy*,
not e.g. *per patient*.

>>> print(dd.plugins.topics.partner_model)
courses.Course


Interests
=========

Therapists assign interests per dossier.  In the detail window of a
dossier they have a panel "Interests" (:class:`InterestsByPartner`).

For example let's take some dossier and look at the interests it has
been assigned to:

>>> c = courses.Course.objects.all().first()
>>> c
Course #1 ('Arens Andreas')

>>> rt.show(topics.InterestsByPartner, c)
*(A) Alcoholism*
*(P) Phobia*

A site administrator can configure the list of topics.

>>> show_menu_path(topics.AllTopics)
Configure --> Topics --> Topics

The detail window of a topic has a panel "Interests"
(:class:`InterestsByTopic`) which shows the dossiers for which this
topic ios interesting.

>>> t = topics.Topic.objects.all().first()
>>> t
Topic #1 ('(A) Alcoholism')

>>> rt.show(topics.InterestsByTopic, t)
======================= ===============
 Dossier                 Controlled by
----------------------- ---------------
 Arens Andreas
 Arens Annette
 Bastiaensen Laurent
 Collard Charlotte
 Demeulenaere Dorothée
 Dericum Daniel
 Eierschal Emil
 Emonts Daniel
 Emontspool Erwin
 Evers Eberhart
 Evertz Bernd
 Groteclaes Gregory
 Ingels Irene
 Jacobs Jacqueline
 Johnen Johann
 Kaivers Karl
 Keller Karl
 Laschet Laura
 Malmendier Marc
 Martelaer Mark
 Mießen Michael
 Radermacher Christian
 Radermacher Daniela
 Radermacher Guido
 Radermacher Inge
 Radermacher Jean
 da Vinci David
 Ärgerlich Erna
 Õunapuu Õie
======================= ===============
<BLANKLINE>


A site administrator can see a global list of all interests.
This might be useful e.g. for exporting the data.
           
>>> show_menu_path(topics.AllInterests)
Explorer --> Topics --> Interests



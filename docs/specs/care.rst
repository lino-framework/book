.. _noi.specs.care:

=======================================
Lino Care, a network of people who care
=======================================

.. How to test only this document:

    $ doctest docs/specs/care.rst
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.anna.settings.demo')
    >>> from lino.api.doctest import *

.. contents::
  :local:



Overview
========

**Lino Care** is for organizations who help people caring for each
other.


A Lino Care site maintains a catalog of **skills**.  This is a
classification of "services or things" that are offered by the
persons and organisations registered as contacts.


Demo users
==========

As an **administrator** you can (additionally to the above) also
create new users, change the catalog of faculties, ...

The demo database has a set of **fictive users**. Let's introduce
them:

>>> rt.show('users.Users')
========== =============== ============ ===========
 Username   User type       First name   Last name
---------- --------------- ------------ -----------
 robin      Administrator   Robin        Rood
 rolf       Administrator   Rolf         Rompen
 romain     Administrator   Romain       Raffault
========== =============== ============ ===========
<BLANKLINE>



Skills
======


>>> rt.show(faculties.AllSkills)
... #doctest: +REPORT_UDIFF
========================== ============================= ============================ =============== ============ =========
 Designation                Designation (de)              Designation (fr)             Parent skill    Skill type   Remarks
-------------------------- ----------------------------- ---------------------------- --------------- ------------ ---------
 Babysitting                Babysitting                   Garde enfant
 Car driving                Fahrdienst                    Voiture
 French lessons             Französischunterricht         Cours de francais            Teaching
 Garden works               Gartenarbeiten                Travaux de jardin            Home & Garden
 German lessons             Deutschunterricht             Cours d'allemand             Teaching
 Go out with dogs           Hunde spazierenführen         Chiens
 Guitar lessons             Gitarrenunterricht            Cours de guitare             Music
 Hair cutting               Friseur                       Coiffure
 Home & Garden              Haus und Garten               Maison et jardin
 Maths lessons              Matheunterricht               Cours de maths               Teaching
 Mentoring elderly people   Gesellschafter für Senioren   Rencontres personnes agées
 Music                      Musik                         Musique
 Piano lessons              Klavierunterricht             Cours de piano               Music
 Renovation                 Renovierung                   Rénovation                   Home & Garden
 Repair works               Reparaturarbeiten             Travaux de réparation        Home & Garden
 Repairing clothes          Kleider reparieren            Réparer des vètements        Home & Garden
 Shopping                   Botengänge                    Commissions
 Teaching                   Unterricht                    Cours
 Translations               Übersetzungsarbeiten          Traductions
 Write letters              Briefe schreiben              Écrire des lettres
========================== ============================= ============================ =============== ============ =========
<BLANKLINE>


>>> rt.show(faculties.TopLevelSkills)
... #doctest: +REPORT_UDIFF
============================ ========= =================================================================== ==============
 overview                     Remarks   Children                                                            Parent skill
---------------------------- --------- ------------------------------------------------------------------- --------------
 *Babysitting*
 *Car driving*
 *Go out with dogs*
 *Hair cutting*
 *Home & Garden*                        *Garden works*, *Renovation*, *Repair works*, *Repairing clothes*
 *Mentoring elderly people*
 *Music*                                *Guitar lessons*, *Piano lessons*
 *Shopping*
 *Teaching*                             *French lessons*, *German lessons*, *Maths lessons*
 *Translations*
 *Write letters*
============================ ========= =================================================================== ==============
<BLANKLINE>



Miscellaneous
=============

>>> c = rt.models.plausibility.Checkers.get_by_value('phones.ContactDetailsOwnerChecker')
>>> list(c.get_checkable_models())
[<class 'lino_xl.lib.contacts.models.Partner'>]


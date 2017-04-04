.. _lino.specs.households:

=====================
The Households module
=====================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_households
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.max.settings.demo')
    >>> from lino.api.doctest import *

The :mod:`lino_xl.lib.households` module adds functionality for
managing households (i.e. groups of humans who live together in a same
house).

.. contents:: 
   :local:
   :depth: 2
           

Configuration
=============

>>> rt.show(rt.modules.households.Types)  #doctest: +REPORT_UDIFF
==== ==================== ========================= ====================== ==================== ==================== ===================== ====================
 ID   Designation          Designation (de)          Designation (fr)       Designation (et)     Designation (nl)     Designation (pt-br)   Designation (es)
---- -------------------- ------------------------- ---------------------- -------------------- -------------------- --------------------- --------------------
 1    Married couple       Ehepaar                   Couple marié           Married couple       Married couple       Married couple        Married couple
 2    Divorced couple      Geschiedenes Paar         Couple divorcé         Divorced couple      Divorced couple      Divorced couple       Divorced couple
 3    Factual household    Faktischer Haushalt       Cohabitation de fait   Factual household    Factual household    Factual household     Factual household
 4    Legal cohabitation   Legale Wohngemeinschaft   Cohabitation légale    Legal cohabitation   Legal cohabitation   Legal cohabitation    Legal cohabitation
 5    Isolated             Getrennt                  Isolé                  Isolated             Isolated             Isolated              Isolated
 6    Other                Sonstige                  Autre                  Other                Other                Other                 Other
==== ==================== ========================= ====================== ==================== ==================== ===================== ====================
<BLANKLINE>

>>> rt.show('households.MemberRoles')
======= ============ ===================
 value   name         text
------- ------------ -------------------
 01      head         Head of household
 02      spouse       Spouse
 03      partner      Partner
 04      cohabitant   Cohabitant
 05      child        Child
 06      relative     Relative
 07      adopted      Adopted child
 10      other        Other
======= ============ ===================
<BLANKLINE>


SiblingsByPerson
================

>>> SiblingsByPerson = rt.modules.households.SiblingsByPerson

The :class:`SiblingsByPerson
<lino_xl.lib.households.models.SiblingsByPerson>` table shows the
family composition of a person.  More precisely it shows all members
of the current household of that person.

This works of course only when Lino can determine the "one and only"
current household.  If the person has only one membership (at a given
date), then there is no question.

When there are several memberships, then theoretically one of them
should be marked as `primary`.

But even when a person has multiple household memberships and none of
them is primary, Lino can look at the `end_date`.

Let's get a list of the candidates to inspect:

>>> Link = rt.models.humanlinks.Link
>>> Person = rt.models.contacts.Person
>>> Member = rt.models.households.Member
>>> MemberRoles = rt.models.households.MemberRoles
>>> heads = Person.objects.filter(household_members__role=MemberRoles.head).distinct()
>>> for m in heads.order_by('id'):
...     qs = Member.objects.filter(role=MemberRoles.head, person=m.person)
...     all = qs.count()
...     primary = qs.filter(primary=True).count()
...     if all > 1 and not primary:
...         print(u"{} ({}) is head of {} households".format(
...             m.person, m.person.pk, all))
Mr Karl Keller (177) is head of 2 households
Mr Jérôme Jeanémart (180) is head of 2 households
Mr Albert Adam (201) is head of 3 households
Mr Bruno Braun (202) is head of 2 households

The most interesting is 177:

>>> p = Person.objects.get(pk=177)
>>> rt.show('households.MembersByPerson', master_instance=p)
Mr Karl Keller is
`☐  <javascript:Lino.households.Members.set_primary(null,70,{  })>`__Head of household in *Karl & Erna Keller-Emonts-Gast (Factual household)*
`☐  <javascript:Lino.households.Members.set_primary(null,52,{  })>`__Head of household in *Karl & Õie Keller-Õunapuu (Legal cohabitation)*
<BLANKLINE>
Create a household : **Married couple** / **Divorced couple** / **Factual household** / **Legal cohabitation** / **Isolated** / **Other**

>>> rt.show('households.MembersByPerson', p, nosummary=True)
==================================================== =================== ========= ============ ============
 Household                                            Role                Primary   Start date   End date
---------------------------------------------------- ------------------- --------- ------------ ------------
 Karl & Erna Keller-Emonts-Gast (Factual household)   Head of household   No
 Karl & Õie Keller-Õunapuu (Legal cohabitation)       Head of household   No                     04/03/2002
==================================================== =================== ========= ============ ============
<BLANKLINE>

>>> rt.show(SiblingsByPerson, p)
========= =================== =============== ====================== ============ ============= ============ ========
 Age       Role                Dependency      Person                 First name   Last name     Birth date   Gender
--------- ------------------- --------------- ---------------------- ------------ ------------- ------------ --------
 unknown   Head of household   Not at charge   Mr Karl Keller         Karl         Keller                     Male
 unknown   Partner             Not at charge   Mrs Erna Emonts-Gast   Erna         Emonts-Gast                Female
========= =================== =============== ====================== ============ ============= ============ ========
<BLANKLINE>

Same case for 180:

>>> rt.show(SiblingsByPerson, Person.objects.get(pk=180))
========= =================== =============== ======================= ============ ============= ============ ========
 Age       Role                Dependency      Person                  First name   Last name     Birth date   Gender
--------- ------------------- --------------- ----------------------- ------------ ------------- ------------ --------
 unknown   Head of household   Not at charge   Mr Jérôme Jeanémart     Jérôme       Jeanémart                  Male
 unknown   Partner             Not at charge   Mrs Berta Radermacher   Berta        Radermacher                Female
========= =================== =============== ======================= ============ ============= ============ ========
<BLANKLINE>

For the other candidates, Lino cannot determine a current household:

>>> rt.show(SiblingsByPerson, Person.objects.get(pk=201))
Mr Albert Adam is member of multiple households

>>> rt.show(SiblingsByPerson, Person.objects.get(pk=202))
Mr Bruno Braun is member of multiple households

>>> rt.show(SiblingsByPerson, Person.objects.get(pk=170))
Jean Dupont is not member of any household


Lars
====

Lars Braun is the natural son of Bruno Braun and Eveline Evrard who
both maried another partner. These new households automatically
created foster parent links between Lars and the new partners of his
natural parents. Here is what Lars would say about them:

>>> lars = Person.objects.get(first_name="Lars", last_name="Braun")
>>> for lnk in Link.objects.filter(child=lars):
...    print(u"{} is my {}".format(lnk.parent,
...         lnk.type.as_parent(lnk.parent)))
Mr Bruno Braun is my Father
Mrs Eveline Evrard is my Mother
Mr Albert Adam is my Foster father
Mrs Françoise Freisen is my Foster mother
Mrs Daniela Radermacher is my Foster mother

>>> rt.show('households.MembersByPerson', master_instance=lars)
... #doctest: +ELLIPSIS
Mr Lars Braun is
`☐  <javascript:Lino.households.Members.set_primary(null,21,{  })>`__Child in *Albert & Eveline Adam-Evrard (Married couple)*
`☐  <javascript:Lino.households.Members.set_primary(null,28,{  })>`__Child in *Albert & Françoise Adam-Freisen (Divorced couple)*
`☐  <javascript:Lino.households.Members.set_primary(null,33,{  })>`__Child in *Bruno & Eveline Braun-Evrard (Divorced couple)*
`☐  <javascript:Lino.households.Members.set_primary(null,41,{  })>`__Child in *Bruno & Françoise Braun-Freisen (Married couple)*
`☐  <javascript:Lino.households.Members.set_primary(null,66,{  })>`__Child in *Albert & Daniela Adam-Radermacher (Married couple)*
<BLANKLINE>
Create a household : **Married couple** / **Divorced couple** / **Factual household** / **Legal cohabitation** / **Isolated** / **Other**

>>> rt.show(SiblingsByPerson, lars)
Mr Lars Braun is member of multiple households

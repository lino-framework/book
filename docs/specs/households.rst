.. doctest docs/specs/households.rst
.. _lino.specs.households:

======================================================
``households`` : handling households and their members
======================================================

.. currentmodule:: lino_xl.lib.households

The :mod:`lino_xl.lib.households` plugin adds functionality for
managing households (i.e. groups of humans who live together in a same
house).

.. contents::
   :depth: 1
   :local:


.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.adg.settings.demo')
>>> from lino.api.doctest import *


Overview
=========

A **household** is a group of humans who live together in a same house.

A **household membership** is the fact that a given person is (or has been)
part of a given household.




Related plugins
===============

This plugin collaborates with :mod:`lino_xl.lib.humanlinks`.

This plugin is extended by :ref:`welfare` in
:mod:`lino_welfare.modlib.households`.



Households
==========


A household is a subclass of :class:`lino_xl.lib.contacts.Partner`.


.. class:: Household

    Django model to represent a household.

    .. attribute:: type

        The type of this household.  See `household types`_

    .. method:: create_household(cls, ar, head, partner, type)

        Create a household with the given head, partner and type.

Household types
===============

There are different types of households.

.. class:: Type

    Django model to represent the type of a household.

    http://www.belgium.be/fr/famille/couple/cohabitation/


>>> rt.show(households.Types)  #doctest: +REPORT_UDIFF
==== ==================== ========================= ======================
 ID   Designation          Designation (de)          Designation (fr)
---- -------------------- ------------------------- ----------------------
 1    Married couple       Ehepaar                   Couple marié
 2    Divorced couple      Geschiedenes Paar         Couple divorcé
 3    Factual household    Faktischer Haushalt       Cohabitation de fait
 4    Legal cohabitation   Legale Wohngemeinschaft   Cohabitation légale
 5    Isolated             Getrennt                  Isolé
 6    Other                Sonstige                  Autre
==== ==================== ========================= ======================
<BLANKLINE>


Memberships
===========


.. class:: Member

    Django model to represent a household membership.


    .. attribute:: household
    .. attribute:: person
    .. attribute:: role
    .. attribute:: dependency
    .. attribute:: primary

        Whether this is the primary household of this person.
        Checking this field will automatically disable any other primary memberships.


    .. attribute:: start_date

        Since when this membership exists. This is usually empty.

    .. attribute:: end_date

        Until when this membership exists.

.. class:: Members
.. class:: MembersByHousehold


.. class:: PopulateMembers

    Populate household members from data in human links.

Configuration
=============


.. class:: MemberRoles

    The list of allowed choices for the role of a household member.

    See :attr:`role <Member.role>`.




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
 08      foster       Foster-child
 10      other        Other
======= ============ ===================
<BLANKLINE>


SiblingsByPerson
================

>>> SiblingsByPerson = rt.models.households.SiblingsByPerson

The :class:`SiblingsByPerson` table shows the family composition of a person,
i.e. all members of the current household of that person.

This works of course only when Lino can determine the "one and only"
current household.  If the person has only one membership (at a given
date), then there is no question.

When there are several memberships, then theoretically one of them
should be marked as `primary`.

But even when a person has multiple household memberships and none of
them is primary, Lino can look at the `end_date`.

The active household is determined as follows:

  - If the person has only one household, use this.
  - Otherwise, if one household is marked as primary, use this.
  - Otherwise, if there is exactly one membership whose end_date is
    either empty or in the future, take this.

If no active household can be determined, the panel just displays an
appropriate message.

Let's get a list of the candidates to inspect:

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
Mr Aleksándr Alvang (178) is head of 2 households

The most interesting is 178:

>>> ses = rt.login('robin')
>>> p = Person.objects.get(pk=178)
>>> ses.show('households.MembersByPerson', master_instance=p)
Mr Aleksándr Alvang is
`☐  <javascript:Lino.households.Members.set_primary(null,false,11,{  })>`__Head of household in `Aleksándr & Agápiiá Alvang-Bek-Murzin (Other) <Detail>`__
`☐  <javascript:Lino.households.Members.set_primary(null,false,5,{  })>`__Head of household in `Aleksándr & Cátává Alvang-Maalouf (Factual household) <Detail>`__
<BLANKLINE>
**Join an existing household** or **create a new one**.

>>> ses.show('households.MembersByPerson', p, nosummary=True)
======================================================= =================== ========= ============ ============
 Household                                               Role                Primary   Start date   End date
------------------------------------------------------- ------------------- --------- ------------ ------------
 Aleksándr & Agápiiá Alvang-Bek-Murzin (Other)           Head of household   No
 Aleksándr & Cátává Alvang-Maalouf (Factual household)   Head of household   No                     04/03/2002
======================================================= =================== ========= ============ ============
<BLANKLINE>

>>> rt.show(SiblingsByPerson, p)
========== =================== ======================== ============ ============ ======== ============ ============= ========
 Age        Role                Person                   First name   Last name    Gender   Birth date   Nationality   School
---------- ------------------- ------------------------ ------------ ------------ -------- ------------ ------------- --------
 43 years   Partner             Mrs Agápiiá Bek-Murzin   Agápiiá      Bek-Murzin   Female   1973-09-04
 23 years   Head of household   Mr Aleksándr Alvang      Aleksándr    Alvang       Male     1993-09-09
========== =================== ======================== ============ ============ ======== ============ ============= ========
<BLANKLINE>



Don't read on
=============

The following covers a problem that occured 20181023 and was detected
by welfare but not yet by book.

>>> print(p.id)
178
>>> test_client.force_login(ses.user)

>>> def check(uri, fieldname):
...     url = '/api/%s?fmt=json&an=detail' % uri
...     res = test_client.get(url, REMOTE_USER=ses.user.username)
...     assert res.status_code == 200
...     d = json.loads(res.content)
...     if not fieldname in d['data']:
...         raise Exception("20181023 '{}' not in {}".format(
...             fieldname, d['data'].keys()))
...     return d['data'][fieldname]

>>> uri = 'avanti/Clients/{}'.format(p.id)
>>> html = check(uri, 'households_MembersByPerson')
>>> soup = BeautifulSoup(html, 'lxml')
>>> links = soup.find_all('a')
>>> len(links)
6

.. class:: MemberDependencies

    The list of allowed choices for the `charge` of a household member.


Table reference
===============1

.. class:: Households
.. class:: HouseholdsByType
.. class:: Types

.. doctest docs/specs/voga/roger.rst
.. _voga.specs.roger:

=================================
Specific for Lino Voga à la Roger
=================================

..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *


A customized management of membership fees
==========================================

In :mod:`lino_book.projects.roger` they have the following rules for
handling memberships:

- Membership costs 15€  per year.
- Members get a discount on enrolments to courses.
- Customers can freely decide whether they want to be members or not.
- They become member by paying the membership fee.

To handle these rules, we have an additional field :attr:`member_until
<lino_voga.lib.roger.courses.models.Pupil.member_until>` on
each pupil.

There is a custom data checker
:class:`lino_voga.lib.roger.courses.models.MemberChecker`
    
    
>>> dd.demo_date()
datetime.date(2015, 5, 22)


>>> rt.show(courses.Pupils)
... #doctest: +ELLIPSIS
======================================== ================================= ================== ============ ===== ===== ======== ==============
 Name                                     Address                           Participant Type   Section      LFV   CKK   Raviva   Mitglied bis
---------------------------------------- --------------------------------- ------------------ ------------ ----- ----- -------- --------------
 Hans Altenberg (MEL)                     Aachener Straße, 4700 Eupen       Member                          Yes   No    No       31/12/2015
 Annette Arens (MEC)                      Alter Malmedyer Weg, 4700 Eupen   Helper                          No    Yes   No       31/12/2015
 Laurent Bastiaensen (ME)                 Am Berg, 4700 Eupen               Non-member                      No    No    No       31/12/2015
 Bernd Brecht (ME)                        Germany                           Member                          No    No    No       31/12/2015
 Ulrike Charlier (ME)                     Auenweg, 4700 Eupen               Helper                          No    No    No       31/12/2015
 Dorothée Demeulenaere (ME)               Auf'm Rain, 4700 Eupen            Non-member                      No    No    No       31/12/2016
 ...
 Hedi Radermacher (ME)                    4730 Raeren                       Non-member                      No    No    No       31/12/2015
 Jean Radermacher (ME)                    4730 Raeren                       Member                          No    No    No       31/12/2015
 Marie-Louise Vandenmeulenbos (MEC)       Amsterdam, Netherlands            Helper                          No    Yes   No       31/12/2015
 Didier di Rupo (MS)                      4730 Raeren                       Non-member         Herresbach   No    No    No
 Erna Ärgerlich (ME)                      4730 Raeren                       Member                          No    No    No       31/12/2015
 Otto Östges (MCS)                        4730 Raeren                       Helper             Eynatten     No    Yes   No
======================================== ================================= ================== ============ ===== ===== ======== ==============
<BLANKLINE>


>>> print(dd.plugins.ledger.force_cleared_until)
None

>>> rt.show(checkdata.ProblemsByChecker, 'courses.MemberChecker')
============= ====================================== ==========================================
 Responsible   Database object                        Message
------------- -------------------------------------- ------------------------------------------
 Robin Rood    *Karl Kaivers (ME)*                    Member until 2015-12-31, but no payment.
 Robin Rood    *Laura Laschet (ME)*                   Member until 2015-12-31, but no payment.
 Robin Rood    *Josefine Leffin (MEL)*                Member until 2015-12-31, but no payment.
 Robin Rood    *Marie-Louise Meier (ME)*              Member until 2015-12-31, but no payment.
 Robin Rood    *Alfons Radermacher (ME)*              Member until 2015-12-31, but no payment.
 Robin Rood    *Christian Radermacher (MEL)*          Member until 2015-12-31, but no payment.
 Robin Rood    *Edgard Radermacher (ME)*              Member until 2015-12-31, but no payment.
 Robin Rood    *Guido Radermacher (ME)*               Member until 2015-12-31, but no payment.
 Robin Rood    *Hedi Radermacher (ME)*                Member until 2015-12-31, but no payment.
 Robin Rood    *Jean Radermacher (ME)*                Member until 2015-12-31, but no payment.
 Robin Rood    *Erna Ärgerlich (ME)*                  Member until 2015-12-31, but no payment.
 Robin Rood    *Jean Dupont (ME)*                     Member until 2015-12-31, but no payment.
 Robin Rood    *Marie-Louise Vandenmeulenbos (MEC)*   Member until 2015-12-31, but no payment.
 Robin Rood    *Bernd Brecht (ME)*                    Member until 2015-12-31, but no payment.
 Robin Rood    *Jérôme Jeanémart (ME)*                Member until 2015-12-31, but no payment.
============= ====================================== ==========================================
<BLANKLINE>

>>> acc = rt.models.accounts.CommonAccounts.membership_fees.get_object()
>>> print(acc)
(7310) Membership fees

>>> rt.show(ledger.MovementsByAccount, acc)
============ ========= ===================================== ============ ======== =============
 Value date   Voucher   Description                           Debit        Credit   Match
------------ --------- ------------------------------------- ------------ -------- -------------
 22/12/2015   *CSH 5*   *Faymonville Luc*                     15,00                 **CSH 5:1**
 22/12/2015   *CSH 5*   *Groteclaes Gregory*                  15,00                 **CSH 5:2**
 22/12/2015   *CSH 5*   *Hilgers Hildegard*                   15,00                 **CSH 5:3**
 22/12/2015   *CSH 5*   *Jacobs Jacqueline*                   15,00                 **CSH 5:4**
 22/12/2015   *CSH 5*   *Jonas Josef*                         15,00                 **CSH 5:5**
 22/11/2015   *CSH 4*   *Dobbelstein-Demeulenaere Dorothée*   15,00                 **CSH 4:1**
 22/11/2015   *CSH 4*   *Emonts Daniel*                       15,00                 **CSH 4:3**
 22/11/2015   *CSH 4*   *Engels Edgar*                        15,00                 **CSH 4:4**
 22/11/2015   *CSH 4*   *Evers Eberhart*                      15,00                 **CSH 4:2**
 22/10/2015   *CSH 3*   *Demeulenaere Dorothée*               15,00                 **CSH 3:2**
 22/10/2015   *CSH 3*   *Dericum Daniel*                      15,00                 **CSH 3:1**
 22/02/2015   *CSH 2*   *Charlier Ulrike*                     15,00                 **CSH 2:1**
 22/01/2015   *CSH 1*   *Altenberg Hans*                      15,00                 **CSH 1:2**
 22/01/2015   *CSH 1*   *Arens Annette*                       15,00                 **CSH 1:1**
 22/01/2015   *CSH 1*   *Bastiaensen Laurent*                 15,00                 **CSH 1:3**
                        **Balance 225.00 (15 movements)**     **225,00**
============ ========= ===================================== ============ ======== =============
<BLANKLINE>



.. Here is the output of :func:`walk_menu_items
   <lino.api.doctests.walk_menu_items>` for this database.

    >>> walk_menu_items('rolf', severe=False)
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP

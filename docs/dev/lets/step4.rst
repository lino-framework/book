.. doctest docs/dev/lets/step4.rst
.. include:: /../docs/shared/include/defs.rst
.. _dev.lets.step4:

===================
Step 4 : User types
===================

- We start differentiating between a "system administrator" and "normal members"
- We review the detail layout of a member
- We start using doctests
- We add a detail view for offer and for demand

To activate the code of this step in your contributor environment::

  $ go lets
  $ git checkout step4

To see what we changed since the previous step::

  $ git diff step3

Some explanations.

Going multi-user
================

.. currentmodule:: lino.modlib.users

In step 4 we start to think multi-user. During the first three steps we just
assumed that every member behaves responsibly and has permission to do
everything.
Now we realized that we need to introduce some rules:

- Normal members can *see*, but may not *edit* the offers or demands of other
  members

- Normal members may not see a list of all members. This is for privacy reasons.

- Normal members may not configure new places and product categories because
  that task is reserved to experts.

A question coming up as a side effect: Should normal users be allowed to see
*all* offers and *all* demands? These things are to be decided by our customer
(the :term:`application carrier`). Let's say that the customer decided : all
offers, but not all demands. When you create an offer, you want to go public. We
also added a new description field per offer.

Multi-user functionality has been there from the beginning in the background.
We just didn't care. And we didn't *need* to care.  We used only one :term:`user
type`, the system administrator, who can do everything.

Until now there we saw only one user named "robin" as suggested demo user in the
web interface. But the "normal" members already existed.  You know them: Argo,
Fred, Peter, Anne, Jaanika, Mari, Katrin and so on.   We created them in the
demo fixture (file `lino_lets/projects/letsdemo/settings/fixtures/demo.py
<https://gitlab.com/lino-framework/lets/-/blob/master/lino_lets/projects/letsdemo/settings/fixtures/demo.py>`__).

Until now these members were inactive users.  Because they had an empty
:attr:`User.user_type` field.  But now our demo fixture now sets it to
:attr:`UserTypes.user`.

Now you can sign in using some other username than "robin".

The :class:`UserTypes <UserTypes>` choicelist is part of the standard users
plugin (:mod:`lino.modlib.users`) and

We remove the :menuselection:`Contacts --> Members` menu command. Anyway it was
a duplicate of :menuselection:`Configuration --> System --> Members`.  We
imagine that the customer, who initially wanted this list of members in the
Master menu, now changed their mind: since that list is not visible to normal
users, it makes sense to have it only under the Configuration menu.  This is
just an example of how easily customers can change their mind when developing
has already started, simply because some new aspect emerged. This is a normal
phenomenon.  It is not a reason to blame the customer.

Introduction to doctests
========================

To explain our changes in a more "professional" way, let's use a few doctest
snippets.

Doctest snippets have two advantages: (1) they show code examples, which is
sometimes to easiest way to explain things, and (2) you can test them, which is
sometimes the most efficient way to implement them. Besides the obvious
advantage of providing test coverage for your appliciation.

Every user (member) has a :term:`user type`, and every user type has its
specific set of user roles.  Every actor has a set of required user roles.

>>> from lino import startup
>>> startup('lino_lets.projects.letsdemo.settings.demo')
>>> from lino.api.doctest import *

>>> settings.SITE.user_types_module
'lino.core.user_types'

>>> rt.show(users.UserTypes)
======= =========== ===============
 value   name        text
------- ----------- ---------------
 000     anonymous   Anonymous
 100     user        User
 900     admin       Administrator
======= =========== ===============
<BLANKLINE>

>>> rt.show(users.UserRoles)
================ ===== ===== =====
 Name             000   100   900
---------------- ----- ----- -----
 core.SiteAdmin               ☑
 core.SiteUser          ☑     ☑
================ ===== ===== =====
<BLANKLINE>


The :class:`AllUsers` table (the actor that shows all users) requires the
SiteAdmin role.

>>> users.AllUsers.required_roles
{<class 'lino.core.roles.SiteAdmin'>}

That's what makes the  :menuselection:`Configuration --> System --> Members`
menu command (which is nothing else than the :class:`AllUsers` table) visible
for site administrators and invisible for normal users.


In :mod:`lino_lets.lib.market` we no import the user role :class:`SiteStaff`.
This role is what differentiates site administrators from normal users.  We set
this as a required role for the Categories and Places tables::

    required_roles = dd.login_required(SiteStaff)

>>> market.Places.required_roles
{<class 'lino.core.roles.SiteStaff'>}

>>> market.Categories.required_roles
{<class 'lino.core.roles.SiteStaff'>}

This was a quick crash course about permissions.
More details in :ref:`dev.permissions`.

A detail view for offers and demands
====================================

We added two new tables :class:`OffersByDemand` and :class:`DemandsByOffer`.
:class:`DemandsByOffer` is used in the detail view of an offer and shows all
demands on the same product as this offer.

That's similar to :class:`DemandsByProduct`, but we need to tell Lino where to
find the product of this offer::

  class DemandsByOffer(DemandsByProduct):

      required_roles = dd.login_required(SiteUser)

      @classmethod
      def get_master_instance(cls, ar, model, pk):
          assert model is rt.models.market.Product
          offer = rt.models.market.Offer.objects.get(pk=pk)
          return offer.product

We also must set :attr:`required_roles` to tell Lino that every site user may
see this table. Otherwise this table would be as hidden as the DemandsByProduct
and the Demands tables, which are not visible to normal users.

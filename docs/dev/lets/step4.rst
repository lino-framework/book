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
offers, but not all demands. When you create an offer, then you want to go
public. We also added a new `description` field per offer.

Multi-user functionality has been there from the beginning in the background. We
just didn't care. And we didn't *need* to care (that's a feature): we used only
one :term:`user type`, the :term:`site administrator`, who can do everything.

Until now we saw only one user named "robin" as suggested demo user in the web
interface. But the "normal" members already existed.  You know them: Argo, Fred,
Peter, Anne, Jaanika, Mari, Katrin and so on.   We created them in our demo
fixture (file `lino_lets/projects/letsdemo/settings/fixtures/demo.py
<https://gitlab.com/lino-framework/lets/-/blob/master/lino_lets/projects/letsdemo/settings/fixtures/demo.py>`__).

.. highlight:: diff

Until now these members were "inactive" users because their :attr:`user_type
<lino.modlib.users.User.user_type>` field was empty.  But in step 4 we modified
our demo fixture to set it to :attr:`UserTypes.user`::

  diff --git a/lino_lets/projects/letsdemo/settings/fixtures/demo.py b/lino_lets/projects/letsdemo/settings/fixtures/demo.py
  index b1de442..b410f34 100644
  --- a/lino_lets/projects/letsdemo/settings/fixtures/demo.py
  +++ b/lino_lets/projects/letsdemo/settings/fixtures/demo.py

  @@ -44,6 +44,7 @@ def objects():
       def member(name, place, email=''):
           return User(
               username=name.lower(), first_name=name, email=email,
  +            user_type=rt.models.users.UserTypes.user,
               place=findbyname(Place, place))

The user type named "user" was already defined in the :class:`UserTypes
<UserTypes>` choicelist, which is part of the standard users plugin
(:mod:`lino.modlib.users`).  We just didn't use it until now.

Because of this change you can now sign in using some other username than
"robin".  For example, log in as `argo` and note that now you have a much
smaller menu than when you are `robin`.

We also remove the :menuselection:`Contacts --> Members` menu command by
removing the custom :meth:`setup_menu` method::

  diff --git a/lino_lets/lib/lets/settings.py b/lino_lets/lib/lets/settings.py
  index bf738b3..14db0d1 100644
  --- a/lino_lets/lib/lets/settings.py
  +++ b/lino_lets/lib/lets/settings.py
  @@ -23,8 +23,3 @@ class Site(Site):
           # gadgets:
           yield 'lino.modlib.export_excel'
           yield 'lino_xl.lib.appypod'
  -
  -    def setup_menu(self, profile, main):
  -        m = main.add_menu("master", _("Master"))
  -        m.add_action('users.AllUsers')
  -        super(Site, self).setup_menu(profile, main)

Why did we do this? One reason is that anyway this list of all members (users)
was already available via the :menuselection:`Configuration --> System -->
Members` command, which is defined as a standard functionality in
:mod:`lino.modlib.users`.  So we actually had two menu commands for the same
thing.  Such a redundancy of having two commands leading to the same result can
make sense, but for now we imagine that the customer, who initially wanted this
list of members in the Master menu, now changed their mind: since that list is
not visible to normal users, it makes sense to have it only under the
Configuration menu.  This is just an example of how easily customers can change
their mind when developing has already started, simply because some new aspect
emerged. This is a normal phenomenon.  It is not a reason to blame the customer.

Because of this change in our menu, we need to adapt the doctest in
:file:`docs/specs/roles.rst`, which tests this menu.  In that file we also add a
second section, which tests the menu of a normal member::

  diff --git a/docs/specs/roles.rst b/docs/specs/roles.rst
  index dc6e838..7829e24 100644
  --- a/docs/specs/roles.rst
  +++ b/docs/specs/roles.rst
  @@ -23,7 +23,7 @@ Rolf is a :term:`site administrator`, he has a complete menu:

   >>> show_menu('robin')
   ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
  -- Master : Members, Products
  +- Master : Products
   - Market : Offers, Demands
   - Configure :
     - System : Members, Site Parameters
  @@ -31,3 +31,18 @@ Rolf is a :term:`site administrator`, he has a complete menu:
   - Explorer :
     - System : Authorities, User types, User roles
   - Site : About
  +
  +Normal members
  +--------------
  +
  +Fred is a normal user, he has a limited main menu.
  +
  +>>> ses = rt.login('fred')
  +>>> ses.user.user_type
  +<users.UserTypes.user:100>
  +
  +>>> show_menu(ses.user.username)
  +... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
  +- Master : Products
  +- Market : Offers
  +- Site : About


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

The :class:`AllUsers` table (the actor that shows all users) requires the
:class:`lino.core.roles.SiteAdmin` role. That's what makes the
:menuselection:`Configuration --> System --> Members` menu command (which opens
the :class:`AllUsers` table) visible for site administrators and invisible for
normal users.

In :mod:`lino_lets.lib.market` we now import the user role :class:`SiteStaff`
and set it as a required role for the Categories and Places tables::

    required_roles = dd.login_required(SiteStaff)

:class:`SiteStaff` gives a bit less rights than :class:`SiteAdmin`. The
difference is not important at the moment (it might become important when we
would introduce a third user type for site administrators who should not have
permission to create new users).

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

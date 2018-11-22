# -*- coding: utf-8 -*-
# Copyright 2016-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Runs some tests about the disable-delete handler and cascading deletes.

You can run only these tests by issuing::

  $ go anna
  $ python manage.py test tests.test_cascaded_delete

This tests for :ticket:`1177`, :ticket:`1180`, :ticket:`1181`

"""

from __future__ import unicode_literals
from __future__ import print_function
import six

from django.core.exceptions import ValidationError
from lino.utils.djangotest import RemoteAuthTestCase
from lino.api import rt


def create(m, **kwargs):
    obj = m(**kwargs)
    obj.full_clean()
    obj.save()
    return obj
    

class Tests(RemoteAuthTestCase):
    maxDiff = None

    def test01(self):
        from lino.modlib.users.choicelists import UserTypes
        User = rt.models.users.User
        Person = rt.models.contacts.Person
        # Note = rt.models.notes.Note
        Skill = rt.models.skills.Skill
        Demand = rt.models.skills.Demand
        Competence = rt.models.skills.Competence

        general = create(Skill, name="General work")
        special = create(Skill, name="Special work", parent=general)

        alex = create(User, username='alex',
                      first_name="Alex",
                      user_type=UserTypes.user,
                      language="en")
        
        bruno = create(User, username='bruno',
                       first_name="Bruno",
                       user_type=UserTypes.user,
                       language="en")
        
        berta = create(User, username='berta',
                       first_name="Berta",
                       user_type=UserTypes.user,
                       language="en")
        
        claude = create(Person, first_name="Claude", language="en")
        
        # note1 = create(Note, user=berta, short_text="test 1")
        # note2 = create(Note, user=berta, short_text="test 2")
        note1 = create(Person, first_name="Dirk")
        note2 = create(Person, first_name="Eric")
        
        create(Competence, user=bruno, faculty=special)
        create(Competence, user=alex, faculty=general)
        
        create(Demand, demander=note1, skill=general)
        create(Demand, demander=note2, skill=special)

        ar = rt.models.skills.AssignableWorkersByTicket.request(note1)
        s = ar.to_rst()
        # print(s)
        self.assertEquivalent("""
==========
 Username
----------
 alex
==========
""", s)


        ar = rt.models.skills.AssignableWorkersByTicket.request(note2)
        s = ar.to_rst()
        # print(s)
        self.assertEquivalent("""
==========
 Username
----------
 alex
 bruno
==========
""", s)


        # cannot delete a faculty when there are competences referring
        # to it:
        try:
            special.delete()
            self.fail("Expected veto")
        except Warning as e:
            self.assertEqual(
                six.text_type(e), "Cannot delete Skill Special work "
                "because 1 Skill offers refer to it.")

        # you cannot delete a skill when it is the parent of other
        # skills
        try:
            general.delete()
            self.fail("Expected veto")
        except Warning as e:
            self.assertEqual(
                six.text_type(e), "Cannot delete Skill General work "
                "because 1 Skill offers refer to it.")
            
        # deleting a user will automatically delete all their
        # offers:
        
        bruno.delete()
        alex.delete()

        # make sure that database state is as expected:

        self.assertEqual(Skill.objects.count(), 2)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Person.objects.count(), 3)
        self.assertEqual(Competence.objects.count(), 0)
        
        

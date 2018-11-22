# -*- coding: utf-8 -*-
# Copyright 2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""Test some functionalities-

This module is part of the Lino test suite. You can test only this
module by issuing either::

  $ go mti
  $ python manage.py test
  $ python manage.py test tests.test_misc.QuickTest

or::

  $ go book
  $ python setup.py test -s tests.ProjectsTests.test_mti

"""

from __future__ import unicode_literals
from __future__ import print_function

from django.core.exceptions import ValidationError

from lino.api import dd, rt

from lino.utils.djangotest import RemoteAuthTestCase
from lino.utils.mti import insert_child

class QuickTest(RemoteAuthTestCase):

    # fixtures = ['std', 'demo_users']

    def test_create_entry(self):
        ses = rt.login()

        Person = rt.models.app.Person
        Restaurant = rt.models.app.Restaurant
        Place = rt.models.app.Place
        Visit = rt.models.app.Visit
        Meal = rt.models.app.Meal

        # Create some initial data:

        Person(name="Alfred").save()
        Person(name="Bert").save()
        Person(name="Claude").save()
        Person(name="Dirk").save()
        r = Restaurant(id=1, name="First")
        r.save()
        for i in 1, 2:
            r.owners.add(Person.objects.get(pk=i))
        for i in 3, 4:
            r.cooks.add(Person.objects.get(pk=i))

        # Here is our data:

        lst = list(Person.objects.all())
        self.assertEqual(str(lst), "[<Person: Alfred>, <Person: Bert>, <Person: Claude>, <Person: Dirk>]")

        lst = list(Restaurant.objects.all())
        self.assertEqual(
            str(lst),
            "[Restaurant #1 ('First (owners=Alfred, Bert, cooks=Claude, Dirk)')]")
        
        x = list(Place.objects.all())
        self.assertEqual(
            str(x),
            "[Place #1 ('First (owners=Alfred, Bert)')]")


        """
        The :func:`delete_child` function
        ---------------------------------

        Imagine that a user of our application discovers that Restaurant #1
        isn't actually a `Restaurant`, it's just a `Place`.  They would like
        to "remove it's Restaurant data" from the database, but keep the
        `Place` data.  Especially the primary key (#1) and the related objects
        (the owners) should remain unchanged. But the cooks must be deleted
        since they exist only for restaurants.

        It seems that this is not trivial in Django (`How do you delete child
        class object without deleting parent class object?
        <http://stackoverflow.com/questions/9439730>`__).  That's why we wrote
        the :func:`delete_child` function.
        Here is how to "reduce" a Restaurant to a `Place` by 
        calling the :func:`delete_child` function:

        """

        from lino.utils.mti import delete_child

        p = Place.objects.get(id=1)
        delete_child(p, Restaurant)

        # The Place still exists, but no longer as a Restaurant:

        x = Place.objects.get(pk=1)
        self.assertEqual(
            str(x),
            "First (owners=Alfred, Bert)")

        try:
            list(Restaurant.objects.get(pk=1))
            self.fail("Expected DoesNotExist")
        except Restaurant.DoesNotExist:
            pass
            # Traceback (most recent call last):
        # ...
        # DoesNotExist: Restaurant matching query does not exist.

        """

        The :func:`insert_child` function
        ----------------------------------

        The opposite operation, "promoting a simple Place to a Restaurant", 
        is done using :func:`insert_child`.

        from lino.utils.mti import insert_child

        Let's first create a simple Place #2 with a single owner.
        """

        obj = Place(id=2, name="Second")
        obj.save()
        obj.owners.add(Person.objects.get(pk=2))
        obj.save()
        self.assertEqual(
            str(obj),
            "Second (owners=Bert)")

        # Now this Place becomes a Restaurant and hires 2 cooks:

        obj = insert_child(obj, Restaurant)
        for i in 3, 4:
            obj.cooks.add(Person.objects.get(pk=i))
        self.assertEqual(
            str(obj),
            "Second (owners=Bert, cooks=Claude, Dirk)")

        # If you try to promote a Person to a Restaurant, you'll get an exception:

        person = Person.objects.get(pk=2)
        try:
            insert_child(person, Restaurant).save()
            self.fail("Expected ValidationError")
        except ValidationError as e:
            self.assertEqual(
                str(e), "['A Person cannot be parent for a Restaurant']")

        """
        The :class:`EnableChild` virtual field 
        --------------------------------------

        This section shows how the :class:`EnableChild` virtual field is being 
        used by Lino, and thus is Lino-specific.


        After the above examples our database looks like this:

        """
         
        x = list(Person.objects.all())
        self.assertEqual(
            str(x),
            "[<Person: Alfred>, <Person: Bert>, <Person: Claude>, <Person: Dirk>]")
        x = list(Place.objects.all())
        self.assertEqual(
            str(x),
            "[Place #1 ('First (owners=Alfred, Bert)'), Place #2 ('Second (owners=Bert)')]")
        x = list(Restaurant.objects.all())
        self.assertEqual(
            str(x),
            "[Restaurant #2 ('Second (owners=Bert, cooks=Claude, Dirk)')]")

        # Let's take Place #1 and look at it.

        obj = Place.objects.get(pk=1)
        self.assertEqual(
            str(obj), "First (owners=Alfred, Bert)")

        # How to see whether a given Place is a Restaurant?

        x  = ""
        for i in Place.objects.all():
            x += "{0} -> {1}\n".format(i, i.get_mti_child('restaurant'))
        self.assertEqual(
            x, """\
First (owners=Alfred, Bert) -> None
Second (owners=Bert) -> Second (owners=Bert, cooks=Claude, Dirk)
""")

        # Let's promote First (currently a simple Place) to a Restaurant:

        x = insert_child(obj, Restaurant)
        # Restaurant #1 ('#1 (name=First, owners=Alfred, Bert, cooks=)')


        # And Second stops being a Restaurant:

        second = Place.objects.get(pk=2)
        delete_child(second, Restaurant)

        # This operation has removed the related Restaurant instance:

        try:
            Restaurant.objects.get(pk=2)
            self.fail("Expected DoesNotExist")
        except Restaurant.DoesNotExist:
            pass

        # And finally, rather to explain why Restaurants sometimes 
        # close and later reopen:

        bert = Person.objects.get(pk=2)
        second = Place.objects.get(pk=2)
        insert_child(second, Restaurant)
        # Restaurant #2 ('#2 (name=Second, owners=Bert, cooks=)')

        # Now we can see this place again as a Restaurant

        second = Restaurant.objects.get(pk=2)

        # And engage for example a new cook:

        second.cooks.add(bert)
        # second
        # Restaurant #2 ('#2 (name=Second, owners=Bert, cooks=Bert)')



        # Related objects
        # ---------------

        # Now let's have a more detailed look at what happens to the related 
        # objects (Person, Visit and Meal).

        # Bert, the owner of Restaurant #2 does two visits:

        second = Restaurant.objects.get(pk=2)
        Visit(purpose="Say hello", person=bert, place=second).save()
        Visit(purpose="Hang around", person=bert, place=second).save()
        x = list(second.visit_set.all())
        self.assertEqual(
            str(x),
            "[<Visit: Say hello visit by Bert at Second>, <Visit: Hang around visit by Bert at Second>]")

        # Claude and Dirk, now workless, still go to eat in restaurants:

        Meal(what="Fish",person=Person.objects.get(pk=3),restaurant=second).save()
        Meal(what="Meat",person=Person.objects.get(pk=4),restaurant=second).save()
        x = list(second.meal_set.all())
        self.assertEqual(
            str(x),
            "[<Meal: Claude eats Fish at Second>, <Meal: Dirk eats Meat at Second>]")

        # Now we reduce Second to a Place:

        second = Place.objects.get(pk=2)
        delete_child(second, Restaurant)

        # Restaurant #2 no longer exists:

        try:
            Restaurant.objects.get(pk=2)
            self.fail("Expected DoesNotExist")
        except Restaurant.DoesNotExist:
            pass
        
        # Note that `Meal` has :attr:`allow_cascaded_delete
        # <lino.core.model.Model.allow_cascaded_delete>` set to
        # `['restaurant']`, otherwise the above code would have raised a
        # ValidationError :message:`Cannot delete #2
        # (name=Second,owners=Bert,cooks=Bert) because 2 meals refer to it.` But
        # the meals have been deleted:

        self.assertEqual(Meal.objects.count(), 0)

        # Of course, #2 remains as a Place
        # The owner and visits have been taken over:

        second = Place.objects.get(pk=2)
        x = list(second.visit_set.all())
        self.assertEqual(
            str(x),
            "[<Visit: Say hello visit by Bert at Second>, <Visit: Hang around visit by Bert at Second>]")


        # The :func:`create_mti_child` function
        # -------------------------------------

        # This function is for rather internal use.  :ref:`Python dumps <dpy>`
        # generated by :class:`lino.utils.dpy.Serializer` use this function for
        # creating MTI children instances without having to lookup their parent.

        # .. currentmodule:: lino.utils.dpy

        # In a Python dump we are in a special situation: All Place instances
        # are being generated first, and in another step we are going to create
        # all the Restaurant instances.  So how can we create a Restaurant whose
        # Place already exists *without first having to do a lookup of the Place
        # record*?  That's why :func:`create_mti_child` was written for.

        obj = Place(id=3, name="Third")
        obj.save()
        obj.owners.add(Person.objects.get(pk=2))
        obj.save()
        self.assertEqual(
            str(obj),
            "Third (owners=Bert)")

        from lino.utils.dpy import create_mti_child
        obj = create_mti_child(Place, 3, Restaurant)

        # The return value is technically a normal model instance,
        # but whose `save` and `full_clean` methods have been 
        # patched: `full_clean` is overridden to do nothing, 
        # and `save` will call a "raw" save to avoid the 
        # need of a proper Place instance for that Restaurant.
        # The only thing you can do with it is to save it:

        obj.save()

        # The `save` and `full_clean` methods are the only methods that 
        # will be called by 
        # :class:`lino.utils.dpy.Deserializer`.

        # To test whether :func:`create_mti_child` did her job, 
        # we must re-read an instance:

        obj = Restaurant.objects.get(pk=3)
        self.assertEqual(
            str(obj),
            "Third (owners=Bert, cooks=)")

        # Note that :func:`create_mti_child` supports changing the
        # `name` although that field is defined in the Place model,
        # not in Restaurant. This feature was added 20170626 (#1926,
        # #1923). Before that date Lino raised an exception when you
        # specified a field of the parent model.  And before *that*
        # (until 20120930) this case was silently ignored for
        # backwards compatibility (`/blog/2011/1210`).

        obj = Place(id=4, name="Fourth")
        obj.save()
        ow = create_mti_child(Place, 4, Restaurant, name="A new name")
        ow.full_clean()
        ow.save()
        obj = Restaurant.objects.get(id=4)
        self.assertEqual(obj.name, "A new name")







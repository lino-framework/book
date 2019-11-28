# Copyright 2010-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals
from builtins import str
from lino.api import dd
from django.db import models
from lino.mixins.polymorphic import Polymorphic


class Person(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Place(Polymorphic):

    name = models.CharField(max_length=50)
    owners = models.ManyToManyField(Person)

    def __str__(self):
        return "%s (owners=%s)" % (
            self.name,
            ', '.join([str(o) for o in self.owners.all()]))



class Restaurant(Place):

    serves_hot_dogs = models.BooleanField(default=False)
    cooks = models.ManyToManyField(Person)

    def __str__(self):
        return "%s (owners=%s, cooks=%s)" % (
            self.name,
            ', '.join([str(o) for o in self.owners.all()]),
            ', '.join([str(o) for o in self.cooks.all()]))



class Visit(models.Model):

    allow_cascaded_delete = ['place']
    person = dd.ForeignKey(Person)
    place = dd.ForeignKey(Place)
    purpose = models.CharField(max_length=50)

    def __str__(self):
        return "%s visit by %s at %s" % (
            self.purpose, self.person, self.place.name)



class Meal(models.Model):

    allow_cascaded_delete = ['restaurant']
    person = dd.ForeignKey(Person)
    restaurant = dd.ForeignKey(Restaurant)
    what = models.CharField(max_length=50)

    def __str__(self):
        return "%s eats %s at %s" % (
            self.person, self.what, self.restaurant.name)

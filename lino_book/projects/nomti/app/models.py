# -*- coding: UTF-8 -*-
# Copyright 2015-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals
from builtins import str
from django.db import models
from lino.api import dd



class Person(dd.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Place(dd.Model):
        
    name = models.CharField(max_length=50)
    owners = models.ManyToManyField(Person, related_name="owned_places")
    ceo = dd.ForeignKey(Person, related_name="managed_places")

    def __str__(self):
        if self.get_restaurant():
            if self.get_bar():
                what = "Restaurant & Bar "
            else:
                what = "Restaurant "
        elif self.get_bar():
            what = "Bar "
        else:
            what = ''
        return "%s %s(ceo=%s,owners=%s)" % (
            self.name, what, self.ceo,
            ','.join([str(o) for o in self.owners.all()]))

    def get_restaurant(self):
        try:
            return self.restaurant
        except Restaurant.DoesNotExist:
            return None

    def get_bar(self):
        try:
            return self.bar
        except Bar.DoesNotExist:
            return None



class Bar(dd.Model):
    
    place = dd.OneToOneField(Place)
    serves_alcohol = models.BooleanField(default=True)

    def __str__(self):
        if self.serves_alcohol:
            return self.place.name
        return "%s (no alcohol)" % self.place.name



class Restaurant(dd.Model):
        
    place = dd.OneToOneField(Place)
    serves_hot_dogs = models.BooleanField(default=False)
    cooks = models.ManyToManyField(Person)

    def __str__(self):
        return "%s (cooks=%s)" % (
            self.place.name,
            ','.join([str(o) for o in self.cooks.all()]))
    

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



# -*- coding: UTF-8 -*-
# Copyright 2015-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)


class Bar(Restaurant):
    bar_restaurant = models.OneToOneField(
        Restaurant, parent_link=True, on_delete=models.CASCADE)
    min_age = models.IntegerField()


class Pizzeria(Restaurant):
    pizzeria_restaurant = models.OneToOneField(
        Restaurant, parent_link=True, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)


class PizzeriaBar(Bar, Pizzeria):
    pizza_bar_specific_field = models.CharField(max_length=255)

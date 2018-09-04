from django.db import models
from lino.api import dd

class Restaurant(models.Model):
    name = models.CharField(max_length=255)


class Bar(Restaurant):
    bar_restaurant = dd.OneToOneField(
        Restaurant, parent_link=True, on_delete=models.CASCADE)
    min_age = models.IntegerField()


class Pizzeria(Restaurant):
    pizzeria_restaurant = dd.OneToOneField(
        Restaurant, parent_link=True, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)


class PizzeriaBar(Bar, Pizzeria):
    pizza_bar_specific_field = models.CharField(max_length=255)

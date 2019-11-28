
from django.db import models
from lino.api import dd, _

from lino_book.projects.chooser.food import year_in_school, food_choices, food



class Country(dd.Model):
    class Meta(object):
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class City(dd.Model):
    class Meta(object):
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    name = models.CharField(max_length=20)
    country = dd.ForeignKey(Country)

    def __str__(self):
        return self.name



class Contact(dd.Model):
    class Meta(object):
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    name = models.CharField(max_length=20)
    country = dd.ForeignKey(Country, blank=True, null=True)
    city = dd.ForeignKey(City, blank=True, null=True)
    year_in_school = year_in_school
    food = food

    def __str__(self):
        return self.name

    @dd.chooser()
    def city_choices(cls, country):
        if country is not None:
            return country.city_set.order_by('name')
        return cls.city.field.remote_field.model.objects.order_by('name')

    food_choices = food_choices



class Contacts(dd.Table):
    model = Contact


class Countries(dd.Table):
    model = Country
    detail_layout = """name id
    CitiesByCountry
    """

class Cities(dd.Table):
    model = City
    detail_layout = """name country id
    ContactsByCity
    """


class CitiesByCountry(Cities):
    master_key = "country"


class ContactsByCity(Contacts):
    master_key = "city"
    column_names = "name year_in_school food *"

from django.db import models
from django.core.exceptions import ValidationError
from lino.api import dd, rt

class Country(dd.Model):
    
    class Meta(object):
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(dd.Model):
    
    class Meta(object):
        verbose_name_plural = "Cities"
        
    country = dd.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Person(dd.Model):
    
    class Meta(object):
        verbose_name_plural = "Persons"
        
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = dd.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = dd.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    @dd.chooser()
    def city_choices(cls, country):
        return City.objects.filter(country=country)

    def create_city_choice(self, text):
        """
        Called when an unknown city name was given.
        """
        if self.country is None:
            raise ValidationError(
                "Cannot auto-create city %r if country is empty", text)
        return City.lookup_or_create(
            'name', text, country=self.country)

    def __str__(self):
        return self.name
    

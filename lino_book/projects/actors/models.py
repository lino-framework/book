from django.db import models
from lino.api import dd


class PartnerType(dd.Model):
    name = models.CharField("Name", max_length=20)
    
    def __str__(self):
        return self.name


class Partner(dd.Model):

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    type = dd.ForeignKey(PartnerType)
    name = models.CharField("Name", max_length=30)


class Person(Partner):
    first_name = models.CharField("First name", max_length=20)
    last_name = models.CharField("Last name", max_length=20)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"



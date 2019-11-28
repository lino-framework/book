from django.db import models

from lino_xl.lib.countries.mixins import AddressLocation


class Company(AddressLocation):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name


from .ui import *

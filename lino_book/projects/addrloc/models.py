from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from lino_xl.lib.countries.mixins import AddressLocation


@python_2_unicode_compatible
class Company(AddressLocation):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name


from .ui import *

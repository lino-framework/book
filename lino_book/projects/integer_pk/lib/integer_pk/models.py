from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

   
@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AutoPerson(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=_("ID"))
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class IntegerPerson(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name=_("ID"))
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CharPerson(models.Model):
    id = models.CharField(_("ID"), primary_key=True, max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


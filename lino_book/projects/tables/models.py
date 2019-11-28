from __future__ import unicode_literals
from lino.api import dd
from django.db import models
from django.core.exceptions import ValidationError



class Author(dd.Model):
    first_name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last name", max_length=50)
    country = models.CharField("Country", max_length=50, blank=True)
    
    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Book(dd.Model):
    author = dd.ForeignKey(Author, blank=True, null=True)
    title = models.CharField("Title", max_length=200)
    published = models.IntegerField(
        "Published",
        help_text="The year of publication")
    price = models.DecimalField("Price", decimal_places=2, max_digits=10)


    def full_clean(self):
        super(Book, self).full_clean()
        if self.published > 2000 and self.price < 5:
            price = dd.format_currency(self.price)
            msg = "A book from {} for only {}!".format(
                self.published, price)
            raise ValidationError(msg)
                

        

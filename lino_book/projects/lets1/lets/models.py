from django.db import models
from lino.api import dd
from lino.utils import join_elems
from etgen.html import E
from lino.core.actors import qs2summary



class Place(dd.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Member(dd.Model):
    name = models.CharField(max_length=200)
    place = dd.ForeignKey(Place, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True)

    def __str__(self):
        return self.name



class Product(dd.Model):
    name = models.CharField(max_length=200)

    providers = models.ManyToManyField(
        'lets.Member', verbose_name="Offered by",
        through='lets.Offer', related_name='offered_products')
    customers = models.ManyToManyField(
        'lets.Member', verbose_name="Wanted by",
        through='lets.Demand', related_name='wanted_products')

    def __str__(self):
        return self.name

    @dd.displayfield("Offered by")
    def offered_by(self, ar):
        if ar is None:
            return ''
        return qs2summary(ar, self.providers.all())

    @dd.displayfield("Wanted by")
    def wanted_by(self, ar):
        if ar is None:
            return ''
        return qs2summary(ar, self.customers.all())



class Offer(dd.Model):
    provider = dd.ForeignKey(Member)
    product = dd.ForeignKey(Product)
    valid_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return "%s offered by %s" % (self.product, self.provider)



class Demand(dd.Model):
    customer = dd.ForeignKey(Member)
    product = dd.ForeignKey(Product)

    def __str__(self):
        return "%s (%s)" % (self.product, self.customer)



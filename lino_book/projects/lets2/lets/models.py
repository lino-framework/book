from django.db import models

from lino.api import dd
from lino.utils import join_elems
from etgen.html import E
from lino.mixins.polymorphic import Polymorphic


class Place(dd.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Member(Polymorphic):
    name = models.CharField(max_length=200)
    place = dd.ForeignKey(Place, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Customer(Member):
    customer_remark = models.CharField(max_length=200, blank=True)

    
class Supplier(Member):

    supplier_remark = models.CharField(max_length=200, blank=True)
    


class Product(dd.Model):
    name = models.CharField(max_length=200)

    suppliers = models.ManyToManyField(
        'Supplier', through='Offer',
        related_name='offered_products')
    customers = models.ManyToManyField(
        'Customer', through='Demand',
        related_name='wanted_products')

    def __str__(self):
        return self.name

    @dd.displayfield("Offered by")
    def offered_by(self, ar):
        if ar is None:
            return ''
        items = [ar.obj2html(o) for o in self.suppliers.all()]
        items = join_elems(items, sep=', ')
        return E.p(*items)

    @dd.displayfield("Wanted by")
    def demanded_by(self, ar):
        if ar is None:
            return ''
        items = [ar.obj2html(o) for o in self.customers.all()]
        items = join_elems(items, sep=', ')
        return E.p(*items)



class Offer(dd.Model):
    supplier = dd.ForeignKey(Supplier)
    product = dd.ForeignKey(Product)
    valid_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return "%s offered by %s" % (self.product, self.supplier)



class Demand(dd.Model):
    customer = dd.ForeignKey(Customer)
    product = dd.ForeignKey(Product)

    def __str__(self):
        return "%s (%s)" % (self.product, self.customer)



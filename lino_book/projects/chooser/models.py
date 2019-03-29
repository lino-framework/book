
from django.db import models
from lino.api import dd, _

YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)

MENU = [
    # name reserved_for
    ('Potato', None),
    ('Vegetable', 'SO JR SR GR'),
    ('Meat', 'JR SR GR'),
    ('Fish', 'SR GR'),
]


@dd.python_2_unicode_compatible
class Country(dd.Model):
    class Meta(object):
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


@dd.python_2_unicode_compatible
class City(dd.Model):
    class Meta(object):
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    name = models.CharField(max_length=20)
    country = dd.ForeignKey(Country)

    def __str__(self):
        return self.name


@dd.python_2_unicode_compatible
class Contact(dd.Model):
    class Meta(object):
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    name = models.CharField(max_length=20)
    country = dd.ForeignKey(Country, blank=True, null=True)
    city = dd.ForeignKey(City, blank=True, null=True)
    year_in_school = models.CharField(
        max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, blank=True)
    food = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    @dd.chooser()
    def city_choices(cls, country):
        if country is not None:
            return country.city_set.order_by('name')
        return cls.city.field.remote_field.model.objects.order_by('name')

    @dd.chooser(simple_values=True)
    def food_choices(cls, year_in_school):
        food = []
        for name, reserved_for in MENU:
            if (year_in_school is None) or (reserved_for is None) or year_in_school in reserved_for:
                food.append(name)
        return food


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

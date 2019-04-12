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

year_in_school = models.CharField(
        max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, blank=True)
food = models.CharField(max_length=20, blank=True)

@dd.chooser(simple_values=True)
def food_choices(cls, year_in_school):
    food = []
    for name, reserved_for in MENU:
        if (year_in_school is None) or (reserved_for is None) or year_in_school in reserved_for:
            food.append(name)
    return food
from lino.api import dd
from .models import Person, City, Country

class Persons(dd.Table):
    model = Person
    detail_layout = dd.DetailLayout("""
    name
    country
    city
    """, window_size=(50, 'auto'))

    insert_layout = """
    name
    country
    city
    """


class Cities(dd.Table):
    model = City

class Countries(dd.Table):
    model = Country

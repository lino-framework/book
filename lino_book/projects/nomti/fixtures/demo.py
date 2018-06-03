from lino.api import rt
from lino.utils.cycler import Cycler

# thanks to http://fantasynamegenerators.com/restaurant-names.php#.VM1yRWNgtx0
RESTAURANT_NAMES = """
The Chopping Shack
The Abacus Well
The Olive Lounge
The Autumn Bite
The Private Mission
Nova
Babylon
Blossoms
Whisperwind
Catch
"""


def objects():
    Person = rt.models.app.Person
    Restaurant = rt.models.app.Restaurant
    Place = rt.models.app.Place

    anne = Person(name="Anne")
    yield anne

    bert = Person(name="Bert")
    yield bert

    claude = Person(name="Claude")
    yield claude

    dirk = Person(name="Dirk")
    yield dirk

    ernie = Person(name="Ernie")
    yield ernie

    fred = Person(name="Fred")
    yield fred

    PERSONS = Cycler(Person.objects.all())

    p = Place(name="Bert's pub", ceo=PERSONS.pop())
    yield p
    p.owners.add(anne)
    p.owners.add(bert)

    for name in RESTAURANT_NAMES.strip().splitlines():
        p = Place(name=name, ceo=PERSONS.pop())
        yield p
        r = Restaurant(place=p)
        yield r
        p.owners.add(PERSONS.pop())
        r.cooks.add(PERSONS.pop())


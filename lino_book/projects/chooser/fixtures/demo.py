from lino.api import rt

def objects():
    Country = rt.models.chooser.Country
    City = rt.models.chooser.City

    be = Country(name="Belgium")
    yield be
    yield City(name="Brussels", country=be)
    yield City(name="Eupen", country=be)
    yield City(name="Gent", country=be)

    fr = Country(name="France")
    yield fr
    yield City(name="Paris", country=fr)
    yield City(name="Bordeaux", country=fr)

    ee = Country(name="Estonia")
    yield ee
    yield City(name="Tallinn", country=ee)
    yield City(name="Tartu", country=ee)
    yield City(name="Narva", country=ee)

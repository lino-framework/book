from lino.api import rt


def objects():
    Country = rt.models.combo.Country
    City = rt.models.combo.City
    
    be = Country(name="Belgium")
    yield be
    ee = Country(name="Estonia")
    yield ee
    
    yield City(name="Eupen", country=be)
    yield City(name="Brussels", country=be)
    yield City(name="Gent", country=be)
    yield City(name="Raeren", country=be)
    yield City(name="Namur", country=be)
    
    yield City(name="Tallinn", country=ee)
    yield City(name="Tartu", country=ee)
    yield City(name="Vigala", country=ee)

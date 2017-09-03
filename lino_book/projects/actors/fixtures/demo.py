from lino.api import rt

def objects():
    PartnerType = rt.models.actors.PartnerType
    Customers = rt.models.actors.Customers
    Providers = rt.models.actors.Providers
    
    yield PartnerType(
        id=rt.models.actors.Customers.partner_type_pk,
        name="Our customers")
    yield PartnerType(
        id=rt.models.actors.Providers.partner_type_pk,
        name="Our providers")

    yield Customers.make_instance(name="Adams")
    yield Customers.make_instance(name="Bowman")
    yield Providers.make_instance(name="Carlsson")
    yield Customers.make_instance(name="Dickens")

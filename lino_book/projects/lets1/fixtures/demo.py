from lino.api import rt


def findbyname(model, name):
    """
    Utility function.
    """
    return model.objects.get(name=name)


def objects():
    """This will be called by the :ref:`dpy` deserializer during
    :manage:`prep` and must yield a list of object instances to
    be saved.

    """
    Place = rt.models.lets.Place
    Member = rt.models.lets.Member
    Product = rt.models.lets.Product

    def offer(what, who):
        return rt.models.lets.Offer(
            product=findbyname(Product, what),
            provider=findbyname(Member, who))

    def demand(what, who):
        return rt.models.lets.Demand(
            product=findbyname(Product, what),
            customer=findbyname(Member, who))

    def member(name, place, email=''):
        return rt.models.lets.Member(
            name=name, email=email,
            place=findbyname(Place, place))

    yield Place(name="Tallinn")
    yield Place(name="Tartu")
    yield Place(name="Vigala")
    yield Place(name="Haapsalu")

    yield Product(name="Bread")
    yield Product(name="Buckwheat")
    yield Product(name="Eggs")
    yield Product(name="Sanitary repair work")
    yield Product(name="Building repair work")
    yield Product(name="Electricity repair work")

    yield member("Fred", "Tallinn", 'fred@example.com')
    yield member("Argo", "Haapsalu", 'argo@example.com')
    yield member("Peter", "Vigala", 'peter@example.com')
    yield member("Anne", "Tallinn", 'anne@example.com')
    yield member("Jaanika", "Tallinn", 'jaanika@example.com')

    yield member("Henri", "Tallinn", 'henri@example.com')
    yield member("Mari", "Tartu", 'mari@example.com')
    yield member("Katrin", "Vigala", 'katrin@example.com')

    yield offer("Bread", "Fred")
    yield offer("Buckwheat", "Fred")
    yield offer("Buckwheat", "Anne")
    yield offer("Electricity repair work", "Henri")
    yield offer("Electricity repair work", "Argo")

    yield demand("Buckwheat", "Henri")
    yield demand("Eggs", "Henri")
    yield demand("Eggs", "Mari")


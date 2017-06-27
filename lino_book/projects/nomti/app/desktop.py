from lino.api import dd


class Persons(dd.Table):
    model = 'app.Person'
    column_names = 'name *'
    detail_layout = """
    id name
    owned_places managed_places
    VisitsByPerson
    MealsByPerson
    """


class Places(dd.Table):
    model = 'app.Place'
    detail_layout = """
    id name ceo
    owners
    VisitsByPlace
    """


class Restaurants(dd.Table):
    model = 'app.Restaurant'
    detail_layout = """
    id place serves_hot_dogs 
    cooks
    MealsByRestaurant
    """


class VisitsByPlace(dd.Table):
    model = 'app.Visit'
    master_key = 'place'
    column_names = 'person purpose'


class VisitsByPerson(dd.Table):
    model = 'app.Visit'
    master_key = 'person'
    column_names = 'place purpose'


class MealsByRestaurant(dd.Table):
    model = 'app.Meal'
    master_key = 'restaurant'
    column_names = 'person what'


class MealsByPerson(dd.Table):
    model = 'app.Meal'
    master_key = 'person'
    column_names = 'restaurant what'



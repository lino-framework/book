from lino.api import dd


class Persons(dd.Table):
    model = 'app.Person'
    column_names = 'name *'
    detail_layout = """
    id name
    VisitsByPerson
    MealsByPerson
    """


class Places(dd.Table):
    model = 'app.Place'
    detail_layout = """
    id name mti_navigator
    owners
    VisitsByPlace
    """


class Restaurants(dd.Table):
    model = 'app.Restaurant'
    detail_layout = """
    id name serves_hot_dogs mti_navigator
    owners cooks
    VisitsByPlace
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



@dd.chooser()
def food_choices(cls, ar):
    year_in_school = ar.get_user().year_in_school if ar is not None else None
    food = []
    for name, reserved_for in MENU:
        if (year_in_school is None) or (reserved_for is None) or year_in_school in reserved_for:
            food.append(name)
    return food
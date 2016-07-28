from lino.api import dd, rt


def objects():
    User = rt.models.users.User
    yield User(
        username='pbommel',
        first_name='Piet', last_name='Bommel',
        email='piet@bommel.be')

    yield User(
        username='jdupond',
        first_name='Jean', last_name='Dupond',
        email='jean@bommel.be')
      

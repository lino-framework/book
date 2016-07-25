from lino.utils.instantiator import Instantiator

User = Instantiator(
    'users.User',
    'username first_name last_name email').build


def objects():
    yield User('pbommel', 'Piet', 'Bommel', 'piet@bommel.be')
    yield User('jdupond', 'Jean', 'Dupond', 'jean@bommel.be')
      

from lino.api.shell import *
from lino.utils.instantiator import Instantiator


def objects():
    author = Instantiator(
        'contacts.Person', 'first_name last_name').build
    yield author("Douglas", "Adams")
    yield author("Albert", "Camus")
    yield author("Hannes", "Huttner")

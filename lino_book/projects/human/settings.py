from lino.projects.std.settings import *
SITE = Site(
    globals(),
    ['lino_book.projects.human', 'lino.modlib.system'],
    languages='en de fr')

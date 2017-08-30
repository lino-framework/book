from lino.api import dd, _
from lino.utils.mldbc.mixins import BabelDesignated


class Expression(BabelDesignated):

    class Meta:
        verbose_name = _('Expression')
        verbose_name_plural = _('Expressions')


class Expressions(dd.Table):
    model = Expression
    column_names = 'id designation *'



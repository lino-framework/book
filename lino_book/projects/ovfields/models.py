from lino.api import dd, _
from lino.mixins.ref import Referrable


class MyMixin(dd.Model):

    class Meta:
        abstract = True

    @dd.displayfield(_("Foo"))
    def foo(self, ar):
        return str(self) + "!"


class MyModel(MyMixin):

    foo = dd.CharField(
        _("Foo"), max_length=200, blank=True)


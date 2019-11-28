from lino.api import dd


class Tag(dd.Model):

    name = dd.CharField(max_length=100)

    def __str__(self):
        return self.name

@dd.receiver(dd.auto_create)
def my_auto_create_handler(sender, **kw):
    print("My handler was called with {}".format(sender))

==================
Lino in a nutshell
==================

Models describe how the data is structured in the database.  Tables and layouts
describe how it is structured on the screen or paper.  Actions describe what the
end user can do with the data besides editing it.  User types are
a way to classify end users in order to grant them different sets of
permissions.

A "model" is the Django word for a database table.  A model is a Python class
that defines a collection of "fields". For each Python data type (integer,
float, string, date, ...) there is a corresponding database field type.  Each
database object is an instance of a model.

Example::

  class Country(dd.Model):
    name = CharField()

  class Author(dd.Model):
    name = CharField()
    country = ForeignKey(Country)

  class Book(dd.Model):
    title = CharField()
    country = ForeignKey(Country)
    year = IntegerField()
    author = ForeignKey(Author)

A "table" describes a set of tabular data together with any information needed
for a front end to produce a satisfying result on any medium. There is at least
one table per model. Usually there are several tables per model.  In a Lino
application you write Tables instead of writing Admin classes for your models.

A "layout" describes how the fields of a table are laid out in an entry form. We
differentiate detail layouts and insert layouts.

::

  class Countries(dd.Table):
    model = Country

  class Authors(dd.Table):
    model = Author
    column_names = "name country *"

    detail_layout = """
    name country id
    BooksByAuthor
    """

    insert_layout = """
    name
    country
    """

  class Books(dd.Table):
    model = Author
    column_names = "title author year *"

  class BooksByAuthor(Books):
    master_key = "author"
    column_names = "title year *"

An Action describes a button (or some equivalent UI element) that can be clicked
(executed) by a user.  We differentiate between row actions and list actions.
Many actions are defined automatically, but you can write custom actions.  Example::

  class Book(Model):
    ...
    @dd.action(_("Publish"), icon_name="arrow")
    def publish_book(self):
        # do something

The Menu describes describes how the tables of your application are presented to
the end user.  Instead of letting each plugin register its models to the admin
site, you let it register tables to the main menu.

Example code::

  class Plugin(dd.Plugin)

    def setup_config_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('contacts.CompanyTypes')
        m.add_action('contacts.RoleTypes')

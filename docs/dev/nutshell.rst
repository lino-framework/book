==================
Lino in a nutshell
==================

Let's look back at what we have learned so far.

:term:`Database models <database model>` and :term:`database fields <database
field>`  describe how data is structured for getting stored in the database.
:term:`tables <table>` and :term:`layouts <layout>` describe how data is
structured on the screen or paper. :term:`actions <action>` describe what
:term:`end users <end user>` can do with the data. Every incoming HTTP request
in a Lino application requests execution of a given :term:`action` on a given
:term:`actor`.  We call this an :term:`action request`.


.. glossary::

  database model

    The Django word for what most database management systems call a "table".
    Each row of a database table is represented in Django as an instance of a
    database model. It is a Python class that defines a collection of
    :term:`database fields <database field>`. See :ref:`dev.models`.

  database field

    An attribute of a database model.

    For each Python data type (integer, float, string, date, ...) Django
    defines is a corresponding Python class.

  actor

    A globally known class object that provides *actions*.

    An alternative name for "actor" might have been "resource" or "view", but
    these words are already being used very often, so in Lino we called them
    *actors*.

  action

    Something a user can request to do.  Actions are visible to the :term:`end
    users <end user>` as menu items, toolbar buttons or clickable chunks of text
    at arbitrary places. Actions can also get called programmatically.

  layout

    A textual description of how to visually arrange the fields and other data
    elements in an entry form or a table.

  model instance

    Django word for what we use to call a :term:`database object`.

  database object

    The Python object representing a row in a database table.
    Also known as :term:`model instance` in Django.

  action request

    A volatile object representing the fact that a user "clicked on a button",
    i.e. requested to run a given action on a given actor (and potentially a
    given set of selected database rows).

    Action requests are instances of the :class:`BaseRequest
    <lino.core.requests.BaseRequest>` class or one of its subclasses
    (:class:`ActorRequest <lino.core.requests.ActorRequest>`
    :class:`ActionRequest <lino.core.requests.ActionRequest>`
    :class:`TableRequest <lino.core.tablerequest.TableRequest>`.

  window action

    An :term:`action` that does nothing but opening a new window. See
    :ref:`window_actions`.





Example of database models::

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
for a :term:`front end` to produce a meaningful result on any medium. There is
at least one table per model. Usually there are several tables per model.  In a
Lino application you write tables instead of writing Admin classes for your
models.

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

The **application menu** describes how the tables of your application are
presented to the end user.

Example code::

  class Plugin(dd.Plugin)

    def setup_config_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('contacts.CompanyTypes')
        m.add_action('contacts.RoleTypes')

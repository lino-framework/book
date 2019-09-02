.. doctest docs/specs/migrate.rst
.. _book.specs.migrate:

=========================
Django migrations in Lino
=========================

..  doctest init:
    >>> from atelier.sheller import Sheller
    >>> shell = Sheller("lino_book/projects/migs")
    >>> shell("./clean.sh")
    <BLANKLINE>

This verifies whether Lino is able to make and use migrations created by Django admin commands.


>>> shell("python manage.py makemigrations")
... #doctest: +ELLIPSIS
Migrations for ...

>>> shell("python manage.py migrate")
... #doctest: +ELLIPSIS
Operations to perform:
  Apply all migrations: ...
Running migrations:
  Applying ...

>>> shell("./clean.sh")
<BLANKLINE>
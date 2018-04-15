.. doctest docs/tested/test_i18n.rst
.. _lino.tested.i18n:

===================================================
Code snippets for testing Lino's i18n
===================================================

.. to run (almost) only this test:

    $ 

    Doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.docs.settings.demo')
    >>> from lino.api.shell import *
    

Users Overview in different languages
=====================================

We use the `users.UsersOverview` table for testing some 
basic i18n functionality.
Since we are interested only in the column headers and not to see 
all users, we add a filter:

>>> kw = dict(known_values=dict(username='robin'))

The non-translated result is:

>>> ses = settings.SITE.login('robin')
>>> ses.show('users.UsersOverview', language='en', **kw)
========== ===================== ==========
 Username   User type             Language
---------- --------------------- ----------
 robin      900 (Administrator)   en
========== ===================== ==========
<BLANKLINE>

Now we look at this table in different languages:

>>> ses.show('users.UsersOverview', language='de', **kw)
============== ================= =========
 Benutzername   Benutzerart       Sprache
-------------- ----------------- ---------
 robin          900 (Verwalter)   en
============== ================= =========
<BLANKLINE>


>>> ses.show('users.UsersOverview', language='fr', **kw)
=================== ====================== ========
 Nom d'utilisateur   Type d'utilisateur     Langue
------------------- ---------------------- --------
 robin               900 (Administrateur)   en
=================== ====================== ========
<BLANKLINE>

>>> ses.show('users.UsersOverview', language='et', **kw)
============== ====================== ======
 Kasutajanimi   Kasutajaliik           Keel
-------------- ---------------------- ------
 robin          900 (Administraator)   en
============== ====================== ======
<BLANKLINE>


>>> ses.show('users.UsersOverview', language='pt', **kw)
================= ===================== ========
 Nome de usuário   User type             Idioma
----------------- --------------------- --------
 robin             900 (Administrador)   en
================= ===================== ========
<BLANKLINE>

>>> ses.show('users.UsersOverview', language='pt-br', **kw)
================= ===================== ========
 Nome de usuário   User type             Idioma
----------------- --------------------- --------
 robin             900 (Administrador)   en
================= ===================== ========
<BLANKLINE>


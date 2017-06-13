.. _lino.tested.i18n:

===================================================
Code snippets for testing Lino's i18n
===================================================

.. to run (almost) only this test:

    $ python setup.py test -s tests.DocsTests.test_docs

    Doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.docs.settings.demo')
    >>> from lino.api.shell import *
    

Users Overview in different languages
=====================================

We use the `auth.UsersOverview` table for testing some 
basic i18n functionality.
Since we are interested only in the column headers and not to see 
all users, we add a filter:

>>> kw = dict(known_values=dict(username='robin'))

The non-translated result is:

>>> ses = settings.SITE.login('robin')
>>> ses.show('auth.UsersOverview', language='en', **kw)
========== =============== ==========
 Username   User type       Language
---------- --------------- ----------
 robin      Administrator   en
========== =============== ==========
<BLANKLINE>

Now we look at this table in different languages:

>>> ses.show('auth.UsersOverview', language='de', **kw)
============== ============= =========
 Benutzername   Benutzerart   Sprache
-------------- ------------- ---------
 robin          Verwalter     en
============== ============= =========
<BLANKLINE>


>>> ses.show('auth.UsersOverview', language='fr', **kw)
=================== ==================== ========
 Nom d'utilisateur   Type d'utilisateur   Langue
------------------- -------------------- --------
 robin               Administrateur       en
=================== ==================== ========
<BLANKLINE>

>>> ses.show('auth.UsersOverview', language='et', **kw)
============== ================ ======
 Kasutajanimi   Kasutajaliik     Keel
-------------- ---------------- ------
 robin          Administraator   en
============== ================ ======
<BLANKLINE>


>>> ses.show('auth.UsersOverview', language='pt', **kw)
================= =============== ========
 Nome de usuário   User type       Idioma
----------------- --------------- --------
 robin             Administrador   en
================= =============== ========
<BLANKLINE>

>>> ses.show('auth.UsersOverview', language='pt-br', **kw)
================= =============== ========
 Nome de usuário   User type       Idioma
----------------- --------------- --------
 robin             Administrador   en
================= =============== ========
<BLANKLINE>


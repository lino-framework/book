.. doctest docs/dev/languages.rst

===========================
The languages of a ``Site``
===========================

.. This document is part of the Lino test suite.

The :attr:`languages <lino.core.site.Site.languages>` attribute of a
:class:`Site <lino.core.site.Site>` specifies the language
distribution used on this site.

- the user interface languages available on this site
- if your application uses :ref:`mldbc`, the languages for
  multi-lingual database content

Changing this setting affects your database structure if your
application uses :ref:`mldbc`, and thus might require a :ref:`data
migration <datamig>`.

This must be either `None` or an iterable of language codes, or a
string containing a space-separated series of language codes.

Examples::

  languages = "en de fr nl et".split()
  languages = ['en', 'fr']
  languages = 'en fr'

The first language in this list will be the site's default
language.




.. currentmodule:: lino.core.site

>>> from django.utils import translation
>>> from lino.core.site import TestSite as Site
>>> import json


Application code usually specifies :attr:`Site.languages` as a single
string with a space-separated list of language codes.  The
:class:`Site` will analyze this string during instantiation and
convert it into a tuple of :data:`LanguageInfo` objects.

The following examples use the :class:`TestSite` class just to show
certain things which apply also to "real" Sites.

>>> SITE = Site(languages="en fr de")
>>> print(SITE.languages)  #doctest: +NORMALIZE_WHITESPACE
(LanguageInfo(django_code='en', name='en', index=0, suffix=''),
 LanguageInfo(django_code='fr', name='fr', index=1, suffix='_fr'),
 LanguageInfo(django_code='de', name='de', index=2, suffix='_de'))

>>> SITE = Site(languages="de-ch de-be")
>>> print(SITE.languages)  #doctest: +NORMALIZE_WHITESPACE
(LanguageInfo(django_code='de-ch', name='de_CH', index=0, suffix=''), LanguageInfo(django_code='de-be', name='de_BE', index=1, suffix='_de_BE'))

If we have more than one locale of a same language *on a same Site*
(e.g. 'en-us' and 'en-gb') then it is not allowed to specify just
'en'.  But otherwise it is allowed to just say "en", which will mean
"the English variant used on this Site".

>>> site = Site(languages="en-us fr de-be de")
>>> print(site.languages)  #doctest: +NORMALIZE_WHITESPACE
(LanguageInfo(django_code='en-us', name='en_US', index=0, suffix=''),
 LanguageInfo(django_code='fr', name='fr', index=1, suffix='_fr'),
 LanguageInfo(django_code='de-be', name='de_BE', index=2, suffix='_de_BE'),
 LanguageInfo(django_code='de', name='de', index=3, suffix='_de'))

>>> from pprint import pprint
>>> pprint(site.language_dict)
{'de': LanguageInfo(django_code='de', name='de', index=3, suffix='_de'),
 'de_BE': LanguageInfo(django_code='de-be', name='de_BE', index=2, suffix='_de_BE'),
 'en': LanguageInfo(django_code='en-us', name='en_US', index=0, suffix=''),
 'en_US': LanguageInfo(django_code='en-us', name='en_US', index=0, suffix=''),
 'fr': LanguageInfo(django_code='fr', name='fr', index=1, suffix='_fr')}

>>> site.language_dict['de']
LanguageInfo(django_code='de', name='de', index=3, suffix='_de')

>>> site.language_dict['de_BE']
LanguageInfo(django_code='de-be', name='de_BE', index=2, suffix='_de_BE')

>>> site.language_dict['de'] == site.language_dict['de_BE']
False

>>> site.language_dict['en'] == site.language_dict['en_US']
True

>>> site.language_dict['en']
LanguageInfo(django_code='en-us', name='en_US', index=0, suffix='')
>>> site.language_dict['en']
LanguageInfo(django_code='en-us', name='en_US', index=0, suffix='')

>>> site.language_dict['fr']
LanguageInfo(django_code='fr', name='fr', index=1, suffix='_fr')

>>> pprint(site.django_settings['LANGUAGES'])  #doctest: +ELLIPSIS
[('de', 'German'), ('fr', 'French')]

Note that Lino automatically sets :setting:`USE_L10N` to `True` when you specify
:attr:`languages <lino.core.site.Site.languages>`.

>>> site.django_settings['USE_L10N']
True
>>> pprint(site.django_settings['LANGUAGE_CODE'])
'en-us'

When you leave :attr:`languages <lino.core.site.Site.languages>` at its default
value `None`, Lino will set the default language "en" at startup. But there is a
difference between `None` and "en": `None` will cause :setting:`USE_L10N` to be
False because this is what we want when we don't worry about languages.

Lino's default language is "en" and not "en-us" because Django has no entry in
:setting:`LANGUAGES` for this language code, and because we also reduce the
:setting:`LANGUAGES` setting to the languages that are needed. Django 3.0.3
system check complained with "(translation.E004) You have provided a value for
the LANGUAGE_CODE setting that is not in the LANGUAGES setting."

>>> site = Site()
>>> print(site.languages)
(LanguageInfo(django_code='en', name='en', index=0, suffix=''),)
>>> pprint(site.django_settings['LANGUAGES'])
[('en', 'English')]

>>> 'USE_L10N' in site.django_settings
False

>>> 'LANGUAGE_CODE' in site.django_settings
False

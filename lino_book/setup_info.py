# -*- coding: UTF-8 -*-
# Copyright 2009-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

# python setup.py test -s tests.test_misc.PackagesTests

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

install_requires = [
    'Sphinx', 'getlino',
    'lino_xl', 'selenium', 'mock',
    'pisa', 'django-wkhtmltopdf',
    'django-iban', 'metafone',
    'djangorestframework',
    # 'bleach',  installed by inv prep
    # 'radicale==1.1.2',
    'radicale',
    'icalendar',
    'vobject',
    'eidreader',   # required to build the book.
    'social-auth-app-django',
    'lino_cosi',
    'lino_noi',
    'lino_voga',
    'lino_welfare',
    'requests_mock',
    'lino_care',
    'lino_vilma',
    'lino_avanti',
    'lino_tera',
    'lino_amici',
    'commondata', 'commondata.be', 'commondata.ee', 'commondata.eg',
    'mock', 'sqlparse',
    'django-mailbox@git+https://github.com/cylonoven/django-mailbox',
]

SETUP_INFO = dict(
    name='lino_book',
    version='20.1.0',
    install_requires=install_requires,
    # dependency_links=[
    #     'git+https://github.com/cylonoven/django-mailbox.git#egg=django_mailbox'],
    description="Lino documentation and demo projects",
    license='BSD-2-Clause',
    include_package_data=True,
    zip_safe=False,
    author='Luc Saffre',
    author_email='luc@lino-framework.org',
    url="http://www.lino-framework.org",
    # ~ test_suite = 'lino_book.projects',
    # test_suite='tests',
    classifiers="""\
  Programming Language :: Python
  Programming Language :: Python :: 2
  Programming Language :: Python :: 3
  Development Status :: 5 - Production/Stable
  Environment :: Web Environment
  Framework :: Django
  Intended Audience :: Developers
  Intended Audience :: System Administrators
  License :: OSI Approved :: BSD License
  Natural Language :: English
  Natural Language :: French
  Natural Language :: German
  Operating System :: OS Independent
  Topic :: Database :: Front-Ends
  Topic :: Home Automation
  Topic :: Office/Business
  Topic :: Software Development :: Libraries :: Application Frameworks""".splitlines())

SETUP_INFO.update(long_description="""

.. image:: https://readthedocs.org/projects/lino/badge/?version=latest
   :target: http://lino.readthedocs.io/en/latest/?badge=latest
.. image:: https://coveralls.io/repos/github/lino-framework/book/badge.svg?branch=master
   :target: https://coveralls.io/github/lino-framework/book?branch=master
.. image:: https://travis-ci.org/lino-framework/book.svg?branch=stable
   :target: https://travis-ci.org/lino-framework/book?branch=stable
.. image:: https://img.shields.io/pypi/v/lino.svg
   :target: https://pypi.python.org/pypi/lino/
.. image:: https://img.shields.io/pypi/l/lino.svg
   :target: https://pypi.python.org/pypi/lino/

This is the code repository that contains (1) the Sphinx source files
of the Lino Book, (2) the ``lino_book`` Python package and (3) a test
suite with doctest-based tests for the Lino framework.

The **Lino Book** is the central documentation tree of the Lino
framework.  It is visible on `www.lino-framework.org
<http://www.lino-framework.org>`__ and on `lino.readthedocs.io
<http://lino.readthedocs.io>`__.

The ``lino_book`` Python package is a collection of small example Lino
applications used for educational and testing purposes.

The code repositories for the ``lino`` and ``lino_xl`` Python packages
have no documentation tree on their own and almost no unit tests, they
are tested and documented here.

Your feedback is welcome.  Our `community page
<http://www.lino-framework.org/community>`__ explains how to contact us.


""")

SETUP_INFO.update(packages=[str(n) for n in """
lino_book
lino_book.projects
lino_book.projects.babel_tutorial
lino_book.projects.babel_tutorial.fixtures
lino_book.projects.dumps
lino_book.projects.dumps.fixtures
lino_book.projects.dumps.settings
lino_book.projects.belref
lino_book.projects.belref.fixtures
lino_book.projects.belref.settings
lino_book.projects.combo
lino_book.projects.combo.fixtures
lino_book.projects.docs
lino_book.projects.docs.settings
lino_book.projects.estref
lino_book.projects.estref.settings
lino_book.projects.estref.tests
lino_book.projects.events
lino_book.projects.events.tests
lino_book.projects.polls
lino_book.projects.polls.polls
lino_book.projects.polls.polls.fixtures
lino_book.projects.polls.mysite
lino_book.projects.polls2
lino_book.projects.polls2.polls
lino_book.projects.polls2.polls.fixtures
lino_book.projects.polls2.mysite
lino_book.projects.polly
lino_book.projects.polly.settings
lino_book.projects.polly.tests
lino_book.projects.20090714
lino_book.projects.20090717
lino_book.projects.20100126
lino_book.projects.20100127
lino_book.projects.20100206
lino_book.projects.20100212
lino_book.projects.20121124
lino_book.projects.chooser
lino_book.projects.chooser.fixtures
lino_book.projects.example
lino_book.projects.properties
lino_book.projects.quantityfield
lino_book.projects.cms
lino_book.projects.cms.settings
lino_book.projects.crl
lino_book.projects.crl.fixtures
lino_book.projects.eric
lino_book.projects.eric.settings
lino_book.projects.eric.settings.fixtures
lino_book.projects.eric.tests
lino_book.projects.homeworkschool
lino_book.projects.homeworkschool.fixtures
lino_book.projects.homeworkschool.settings
lino_book.projects.i18n
lino_book.projects.igen
lino_book.projects.igen.tests
lino_book.projects.max
lino_book.projects.max.settings
lino_book.projects.chatter
lino_book.projects.chatter.settings
lino_book.projects.chatter.tests
lino_book.projects.migs
lino_book.projects.migs.settings
lino_book.projects.migs.settings.fixtures
lino_book.projects.min1
lino_book.projects.min1.settings
lino_book.projects.min1.migrations
lino_book.projects.min1.migrations.about
lino_book.projects.min1.migrations.bootstrap3
lino_book.projects.min1.migrations.contacts
lino_book.projects.min1.migrations.countries
lino_book.projects.min1.migrations.extjs
lino_book.projects.min1.migrations.jinja
lino_book.projects.min1.migrations.lino
lino_book.projects.min1.migrations.office
lino_book.projects.min1.migrations.printing
lino_book.projects.min1.migrations.system
lino_book.projects.min1.migrations.users
lino_book.projects.min1.migrations.xl
lino_book.projects.min2
lino_book.projects.min2.settings
lino_book.projects.min2.tests
lino_book.projects.min3
lino_book.projects.min3.lib
lino_book.projects.min3.lib.contacts
lino_book.projects.min3.lib.contacts.fixtures
lino_book.projects.min3.settings
lino_book.projects.min3.tests
lino_book.projects.min9
lino_book.projects.min9.modlib
lino_book.projects.min9.modlib.contacts
lino_book.projects.min9.modlib.contacts.fixtures
lino_book.projects.min9.modlib.contacts.management
lino_book.projects.min9.modlib.contacts.management.commands
lino_book.projects.min9.settings
lino_book.projects.min9.tests
lino_book.projects.apc
lino_book.projects.apc.settings
lino_book.projects.apc.tests
lino_book.projects.avanti1
lino_book.projects.avanti1.settings
lino_book.projects.avanti1.settings.fixtures
lino_book.projects.avanti1.tests
lino_book.projects.cosi_ee
lino_book.projects.cosi_ee.settings
lino_book.projects.pierre
lino_book.projects.pierre.settings
lino_book.projects.bs3
lino_book.projects.bs3.settings
lino_book.projects.bs3.tests
lino_book.projects.team
lino_book.projects.team.tests
lino_book.projects.team.settings
lino_book.projects.team.settings.fixtures
lino_book.projects.liina
lino_book.projects.liina.tests
lino_book.projects.liina.settings
lino_book.projects.liina.settings.fixtures
lino_book.projects.lydia
lino_book.projects.lydia.tests
lino_book.projects.lydia.settings
lino_book.projects.lydia.settings.fixtures
lino_book.projects.public
lino_book.projects.anna
lino_book.projects.anna.settings
lino_book.projects.anna.tests
lino_book.projects.anna.lib
lino_book.projects.anna.lib.tickets
lino_book.projects.public.settings
lino_book.projects.public.tests
lino_book.projects.lets1
lino_book.projects.lets1.lets
lino_book.projects.lets1.fixtures
lino_book.projects.lets2
lino_book.projects.lets2.lets
lino_book.projects.lets2.fixtures
lino_book.projects.mti
lino_book.projects.mti.app
lino_book.projects.mti.fixtures
lino_book.projects.mti.tests
lino_book.projects.nomti
lino_book.projects.nomti.app
lino_book.projects.nomti.fixtures
lino_book.projects.watch
lino_book.projects.watch.entries
lino_book.projects.watch.fixtures
lino_book.projects.watch.tests
lino_book.projects.watch2
lino_book.projects.watch2.fixtures
lino_book.projects.mldbc
lino_book.projects.mldbc.fixtures
lino_book.projects.actions
lino_book.projects.actors
lino_book.projects.actors.fixtures
lino_book.projects.addrloc
lino_book.projects.addrloc.fixtures
lino_book.projects.myroles
lino_book.projects.auto_create
lino_book.projects.de_BE
lino_book.projects.de_BE.fixtures
lino_book.projects.diamond
lino_book.projects.diamond.main
lino_book.projects.diamond2
lino_book.projects.diamond2.main
lino_book.projects.float2decimal
lino_book.projects.float2decimal.lib
lino_book.projects.float2decimal.lib.float2decimal
lino_book.projects.integer_pk
lino_book.projects.integer_pk.lib
lino_book.projects.integer_pk.lib.integer_pk
lino_book.projects.human
lino_book.projects.gfktest
lino_book.projects.gfktest.settings
lino_book.projects.gfktest.lib
lino_book.projects.gfktest.lib.gfktest
lino_book.projects.pisa
lino_book.projects.sendchanges
lino_book.projects.tables
lino_book.projects.tables.fixtures
lino_book.projects.vtables
lino_book.projects.ovfields
lino_book.projects.edmund
lino_book.projects.edmund.settings
lino_book.projects.edmund.settings.fixtures
lino_book.projects.roger
lino_book.projects.roger.settings
lino_book.projects.roger.settings.fixtures
lino_book.projects.roger.tests
lino_book.projects.workflows
lino_book.projects.workflows.entries
""".splitlines() if n])


SETUP_INFO.update(message_extractors={
    'lino': [
        ('**/sandbox/**',        'ignore', None),
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**/linoweb.js',        'jinja2', None),
        #~ ('**.js',                'javascript', None),
        ('**/config/**.html', 'jinja2', None),
        # ~ ('**/templates/**.txt',  'genshi', {
        # ~ 'template_class': 'genshi.template:TextTemplate'
        # ~ })
    ],
})

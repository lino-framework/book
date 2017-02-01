# -*- coding: UTF-8 -*-
# Copyright 2009-2017 Luc Saffre
# License: BSD (see file COPYING for details)

# python setup.py test -s tests.PackagesTests

from __future__ import unicode_literals
import sys
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3



SETUP_INFO = dict(
    name='lino_book',
    # version='1.7.4',
    version='2016.12.0',
    install_requires=[
        'lino', 'selenium',
        'django-iban', 'metafone', 'channels',
        'lino-cosi',
        'commondata', 'commondata.ee', 'commondata.be'],
    tests_require=['pytest'],

    description="The documentation for Lino",
    license='BSD License',
    include_package_data=True,
    zip_safe=False,
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://www.lino-framework.org",
    #~ test_suite = 'lino_book.projects',
    test_suite='tests',
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

if PY2:
    SETUP_INFO['install_requires'].append('reportlab<2.7')
else:
    SETUP_INFO['install_requires'].append('reportlab')

SETUP_INFO.update(long_description="""

.. image:: https://readthedocs.org/projects/lino/badge/?version=latest
   :target: http://lino.readthedocs.io/en/latest/?badge=latest
.. image:: https://coveralls.io/repos/github/lino-framework/book/badge.svg?branch=master
   :target: https://coveralls.io/github/lino-framework/book?branch=master
.. image:: https://travis-ci.org/lino-framework/book.svg?branch=master
   :target: https://travis-ci.org/lino-framework/book?branch=master
.. image:: https://img.shields.io/pypi/v/lino.svg
   :target: https://pypi.python.org/pypi/lino/
.. image:: https://img.shields.io/pypi/l/lino.svg
   :target: https://pypi.python.org/pypi/lino/

The Lino Book is a code repository used for educational and testing
purposes.  It contains the big Sphinx documentation tree about the
Lino framework published on http://www.lino-framework.org/.

It also contains the ``lino_book`` Python package, a collection of
small example Lino applications.

The code repositories for the ``lino`` and ``lino_xl`` Python packages
have no documentation tree on their own, their documentation is here.

It also contains a big test suite which runs doctest-based tests for
all these packages.

""")

SETUP_INFO.update(packages=[str(n) for n in """
lino_book
lino_book.projects
lino_book.projects.babel_tutorial
lino_book.projects.babel_tutorial.fixtures
lino_book.projects.dumps
lino_book.projects.dumps.fixtures
lino_book.projects.dumps.settings
lino_book.projects.watch
lino_book.projects.watch.entries
lino_book.projects.watch.fixtures
lino_book.projects.watch.tests
lino_book.projects.belref
lino_book.projects.belref.fixtures
lino_book.projects.belref.settings
lino_book.projects.docs
lino_book.projects.docs.settings
lino_book.projects.estref
lino_book.projects.estref.settings
lino_book.projects.estref.tests
lino_book.projects.events
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
lino_book.projects.example
lino_book.projects.nomti
lino_book.projects.properties
lino_book.projects.quantityfield
lino_book.projects.cms
lino_book.projects.cms.settings
lino_book.projects.crl
lino_book.projects.crl.fixtures
lino_book.projects.homeworkschool
lino_book.projects.homeworkschool.fixtures
lino_book.projects.homeworkschool.settings
lino_book.projects.i18n
lino_book.projects.igen
lino_book.projects.igen.tests
lino_book.projects.max
lino_book.projects.max.settings
lino_book.projects.min1
lino_book.projects.min1.settings
lino_book.projects.min2
lino_book.projects.min2.modlib
lino_book.projects.min2.modlib.contacts
lino_book.projects.min2.modlib.contacts.fixtures
lino_book.projects.min2.modlib.contacts.management
lino_book.projects.min2.modlib.contacts.management.commands
lino_book.projects.min2.settings
lino_book.projects.min2.tests
lino_book.projects.apc
lino_book.projects.apc.settings
lino_book.projects.cosi_ee
lino_book.projects.cosi_ee.settings
lino_book.projects.pierre
lino_book.projects.pierre.settings
""".splitlines() if n])

SETUP_INFO.update(message_extractors={
    'lino': [
        ('**/sandbox/**',        'ignore', None),
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**/linoweb.js',        'jinja2', None),
        #~ ('**.js',                'javascript', None),
        ('**/config/**.html', 'jinja2', None),
        #~ ('**/templates/**.txt',  'genshi', {
        #~ 'template_class': 'genshi.template:TextTemplate'
        #~ })
    ],
})


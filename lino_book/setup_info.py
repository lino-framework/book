# -*- coding: UTF-8 -*-
# Copyright 2009-2016 Luc Saffre
# License: BSD (see file COPYING for details)

#~ Note that this module may not have a docstring because any
#~ global variable defined here will override the global
#~ namespace of lino/__init__.py who includes it with execfile.

# This module is part of the Lino test suite.
# To test only this module:
#
#   $ python setup.py test -s tests.PackagesTests

from __future__ import unicode_literals
import sys
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

SETUP_INFO = dict(
    name='lino_book',
    version='1.7.3',
    install_requires=['lino'],
    tests_require=[],
    # pisa has a bug which makes it complain that "Reportlab Version
    # 2.1+ is needed!" when reportlab 3 is installed.
    # So we install reportlab 2.7 (the latest 2.x version)

    # beautifulsoup4, html5lib, reportlab and pisa are actually needed
    # only when you want to run the test suite, not for normal
    # operation.  Despite this they must be specified in
    # `install_requires`, not in `tests_require`, because the doctests
    # are run in the environment specified by `install_requires`.

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

SETUP_INFO.update(long_description="""\

This is the main documentation tree about the Lino framework.  It
covers three software packages and contains example code to be used
for educational and testing purposes.

Central documentation is published at http://www.lino-framework.org

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
lino_book.projects.cms.fixtures
lino_book.projects.cms.tests
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
lino_book.projects.min2.settings
lino_book.projects.min2.tests
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


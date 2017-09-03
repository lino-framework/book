import sys

from unipath import Path

from django import VERSION

from lino.utils.pythontest import TestCase
from lino import PYAFTER26
from lino_book import SETUP_INFO
from lino.utils.html2xhtml import HAS_TIDYLIB
import lino
LINO_SRC = Path(lino.__file__).parent.parent + '/'
# LINO_SRC = '../lino/'



class LinoTestCase(TestCase):
    django_settings_module = "lino_book.projects.max.settings.demo"
    project_root = Path(__file__).parent.parent

# LinoTestCase = TestCase

class PackagesTests(LinoTestCase):
    def test_01(self):
        self.run_packages_test(SETUP_INFO['packages'])


class TestAppsTests(LinoTestCase):
    
    def test_20100212(self):
        self.run_django_admin_test_cd("lino_book/projects/20100212")

    def test_quantityfield(self):
        self.run_django_admin_test_cd("lino_book/projects/quantityfield")


class DumpTests(LinoTestCase):
    def test_dump2py(self):
        for prj in ["lino_book/projects/belref"]:
            p = Path(prj)
            tmp = p.child('tmp').absolute()
            tmp.rmtree()
            self.run_django_admin_command_cd(p, 'dump2py', tmp)
            self.assertEqual(tmp.child('restore.py').exists(), True)


class CoreTests(TestCase):

    def test_site(self):

        # note that run_simple_doctests (i.e. python -m doctest
        # lino/core/site.py) does NOT run any tests in Python 2.7.6
        # because it imports the `site` module of the standard
        # library.

        # self.run_simple_doctests('lino/core/site.py')
        args = [sys.executable]
        args += [LINO_SRC+'lino/core/site.py']
        self.run_subprocess(args)

    # TODO: implement pseudo tests for QuantityField
    # def test_fields(self):
    #     self.run_simple_doctests('lino/core/fields.py')



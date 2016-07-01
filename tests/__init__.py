from unipath import Path

from lino.utils.pythontest import TestCase
from lino import PYAFTER26
from lino_book import SETUP_INFO


class LinoTestCase(TestCase):
    django_settings_module = "lino_book.projects.max.settings.demo"
    project_root = Path(__file__).parent.parent


class PackagesTests(LinoTestCase):
    def test_01(self):
        self.run_packages_test(SETUP_INFO['packages'])


class LibTests(LinoTestCase):

    def test_users(self):
        self.run_simple_doctests("docs/dev/users.rst")

    # def test_cal_utils(self):
    #     self.run_simple_doctests('lino_xl.lib.cal/utils.py')


class DocsAdminTests(TestCase):
    def test_printing(self):
        self.run_simple_doctests('docs/admin/printing.rst')


class DocsTests(LinoTestCase):

    # python setup.py test -s tests.DocsTests.test_docs
    def test_docs(self):
        self.run_simple_doctests("""
        docs/dev/ml/contacts.rst
        docs/dev/mixins.rst
        docs/user/templates_api.rst
        docs/tested/test_i18n.rst
        """)

    def test_i18n(self):
        self.run_simple_doctests('docs/dev/i18n.rst')

    def test_setup(self):
        self.run_simple_doctests('docs/dev/setup.rst')

    #

    def test_gfks(self):
        self.run_simple_doctests('docs/tested/gfks.rst')

    def test_dynamic(self):
        self.run_simple_doctests('docs/tested/dynamic.rst')

    def test_initdb(self):
        self.run_simple_doctests("docs/dev/initdb.rst")

    def test_polly(self):
        self.run_simple_doctests("docs/tested/polly.rst")

    def test_core_utils(self):
        self.run_simple_doctests("docs/tested/core_utils.rst")

    def test_choicelists(self):
        self.run_simple_doctests("docs/dev/choicelists.rst")

    def test_languages(self):
        self.run_simple_doctests("docs/dev/languages.rst")

    def test_site(self):
        self.run_simple_doctests("docs/dev/site.rst")

    # def test_min1(self):
    #     self.run_simple_doctests("docs/tested/min1.rst")

    def test_e006(self):
        self.run_simple_doctests("docs/tested/e006.rst")

    def test_ddh(self):
        self.run_simple_doctests("docs/tested/ddh.rst")

    def test_settings(self):
        self.run_simple_doctests('docs/dev/ad.rst')

    def test_translate(self):
        self.run_django_manage_test('docs/dev/translate')

    def test_de_BE(self):
        self.run_django_manage_test('docs/tutorials/de_BE')

    def test_sendchanges(self):
        self.run_django_manage_test('docs/tutorials/sendchanges')

    def test_myroles(self):
        self.run_django_manage_test('docs/tutorials/myroles')

    def test_mti(self):
        self.run_django_manage_test('docs/tutorials/mti')

    def test_auto_create(self):
        self.run_django_manage_test('docs/tutorials/auto_create')
    
    def test_human(self):
        self.run_django_manage_test('docs/tutorials/human')

    def test_actions(self):
        self.run_django_manage_test('docs/tutorials/actions')

    def test_actors(self):
        self.run_django_manage_test('docs/tutorials/actors')

    def test_watch(self):
        self.run_django_manage_test('docs/tutorials/watch_tutorial')
    
    def test_vtables(self):
        self.run_django_manage_test('docs/tutorials/vtables')
    
    def test_tables(self):
        self.run_django_manage_test('docs/tutorials/tables')
    
    def test_diamond(self):
        self.run_django_manage_test('docs/tested/diamond')

    def test_diamond2(self):
        self.run_django_manage_test('docs/tested/diamond2')

    def test_addrloc(self):
        self.run_django_manage_test('docs/tutorials/addrloc')
    
    def test_pisa(self):
        self.run_django_manage_test('docs/tutorials/pisa')
    
    def test_polls(self):
        self.run_django_manage_test('docs/tutorials/polls')

    def test_hello(self):
        self.run_django_manage_test('docs/tutorials/hello')

    def test_lets(self):
        self.run_django_manage_test('docs/tutorials/lets')

    def test_letsmti(self):
        self.run_django_manage_test('docs/tutorials/letsmti')

    def test_gfktest(self):
        self.run_django_manage_test('docs/tutorials/gfktest')

    def test_mldbc(self):
        self.run_django_manage_test('docs/tutorials/mldbc')

    def test_belref(self):
        self.run_django_manage_test("docs/tutorials/belref")

    def test_float2decimal(self):
        if PYAFTER26:
            self.run_django_manage_test("docs/tested/float2decimal")

    def test_integer_pk(self):
        self.run_django_manage_test("docs/tested/integer_pk")


class SpecsTests(TestCase):

    def test_gfks(self):
        self.run_simple_doctests('docs/specs/gfks.rst')

    def test_printing(self):
        self.run_simple_doctests('docs/specs/printing.rst')

    def test_holidays(self):
        self.run_simple_doctests('docs/specs/holidays.rst')

    def test_cal(self):
        self.run_simple_doctests('docs/specs/cal.rst')

    def test_checkdata(self):
        self.run_simple_doctests('docs/specs/checkdata.rst')

    def test_cv(self):
        self.run_simple_doctests('docs/specs/cv.rst')

    def test_households(self):
        self.run_simple_doctests('docs/specs/households.rst')

    def test_tinymce(self):
        self.run_simple_doctests("docs/specs/tinymce.rst")

    def test_export_excel(self):
        self.run_simple_doctests("docs/specs/export_excel.rst")

    def test_invalid_requests(self):
        self.run_simple_doctests("docs/specs/invalid_requests.rst")

    def test_html(self):
        self.run_simple_doctests('docs/specs/html.rst')

    def test_countries(self):
        self.run_simple_doctests('docs/specs/countries.rst')


class ProjectsTests(LinoTestCase):
    
    # def test_all(self):
    #     from atelier.fablib import run_in_demo_projects
    #     run_in_demo_projects('test')

    def test_events(self):
        self.run_django_manage_test("lino_book/projects/events")

    def test_belref(self):
        self.run_django_manage_test("lino_book/projects/belref")

    def test_babel_tutorial(self):
        self.run_django_manage_test("lino_book/projects/babel_tutorial")

    def test_min1(self):
        self.run_django_manage_test("lino_book/projects/min1")

    def test_min2(self):
        self.run_django_manage_test("lino_book/projects/min2")


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

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


class LibTests(LinoTestCase):

    def test_users(self):
        self.run_simple_doctests("docs/dev/users.rst")
        
    def test_runtests(self):
        self.run_simple_doctests("docs/dev/runtests.rst")

    def test_env(self):
        self.run_simple_doctests("docs/dev/env.rst")

    # def test_cal_utils(self):
    #     self.run_simple_doctests('lino_xl.lib.cal/utils.py')


class DocsAdminTests(TestCase):
    def test_printing(self):
        self.run_simple_doctests('docs/admin/printing.rst')
    def test_linod(self):
        self.run_simple_doctests('docs/admin/linod.rst')


class DocsTests(LinoTestCase):

    # python setup.py test -s tests.DocsTests.test_docs
    def test_docs(self):
        self.run_simple_doctests("""
        docs/dev/ml/contacts.rst
        docs/dev/mixins.rst
        docs/user/templates_api.rst
        docs/tested/test_i18n.rst
        """)

    def test_memo(self):
        self.run_simple_doctests("docs/dev/memo.rst")

    def test_ar(self):
        self.run_simple_doctests("docs/dev/ar.rst")

    def test_watch(self):
        self.run_simple_doctests("docs/dev/watch.rst")

    def test_perms(self):
        self.run_simple_doctests('docs/dev/perms.rst')

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
        # self.run_simple_doctests('docs/tutorials/de_BE/index.rst')
        # self.run_django_admin_command_cd('docs/tutorials/de_BE', 'test')
        self.run_django_manage_test('docs/tutorials/de_BE')

    # def test_sendchanges(self):
    #     self.run_django_manage_test('docs/tutorials/sendchanges')

    def test_myroles(self):
        self.run_django_manage_test('docs/tutorials/myroles')

    def test_mti(self):
        self.run_django_manage_test('lino_book/projects/mti')

    def test_auto_create(self):
        self.run_django_manage_test('docs/tutorials/auto_create')
    
    def test_human(self):
        self.run_django_manage_test('docs/tutorials/human')

    def test_actions(self):
        self.run_django_manage_test('docs/tutorials/actions')

    def test_actors(self):
        self.run_django_manage_test('docs/tutorials/actors')

    # def test_watch(self):
    #     self.run_django_manage_test('docs/tutorials/watch_tutorial')
    
    def test_vtables(self):
        self.run_django_manage_test('docs/tutorials/vtables')
    
    def test_tables(self):
        self.run_django_manage_test('docs/tutorials/tables')
    
    def test_diamond(self):
        # TODO: reactivate when #28332 is fixed.
        # https://code.djangoproject.com/ticket/28332
        if VERSION[0] == 1 and VERSION[1] < 11:
            self.run_django_manage_test('docs/tested/diamond')

    def test_diamond2(self):
        # TODO: reactivate when #28332 is fixed.
        # https://code.djangoproject.com/ticket/28332
        if VERSION[0] == 1 and VERSION[1] < 11:
            self.run_django_manage_test('docs/tested/diamond2')

    def test_addrloc(self):
        self.run_django_manage_test('docs/tutorials/addrloc')
    
    # def test_pisa(self):
    #     self.run_django_manage_test('docs/tutorials/pisa')
    
    def test_polls(self):
        self.run_django_manage_test('docs/tutorials/polls')
        
    def test_polls2(self):
        self.run_django_manage_test('docs/tutorials/polls2')

    def test_hello(self):
        self.run_django_manage_test('docs/tutorials/hello')

    def test_dumpy(self):
        self.run_django_manage_test('docs/tutorials/dumpy')

    # def test_lets(self):
    #     self.run_django_manage_test('docs/tutorials/lets')

    # def test_letsmti(self):
    #     self.run_django_manage_test('docs/tutorials/letsmti')

    def test_gfktest(self):
        self.run_django_manage_test('docs/tutorials/gfktest')

    def test_mldbc(self):
        self.run_django_manage_test('docs/tutorials/mldbc')

    # def test_belref(self):
    #     self.run_django_manage_test("docs/tutorials/belref")

    def test_float2decimal(self):
        if PYAFTER26:
            self.run_django_manage_test("docs/tested/float2decimal")

    def test_integer_pk(self):
        self.run_django_manage_test("docs/tested/integer_pk")


class SpecsTests(TestCase):


    def test_notify(self):
        self.run_simple_doctests('docs/specs/notify.rst')

    def test_dumps(self):
        self.run_simple_doctests('docs/specs/dumps.rst')

    def test_i18n(self):
        self.run_simple_doctests('docs/specs/i18n.rst')

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

    def test_users(self):
        self.run_simple_doctests('docs/specs/users.rst')

    def test_households(self):
        self.run_simple_doctests('docs/specs/households.rst')

    def test_tinymce(self):
        self.run_simple_doctests("docs/specs/tinymce.rst")

    def test_export_excel(self):
        self.run_simple_doctests("docs/specs/export_excel.rst")

    def test_noi_export_excel(self):
        self.run_simple_doctests("docs/specs/noi/export_excel.rst")

    def test_invalid_requests(self):
        self.run_simple_doctests("docs/specs/invalid_requests.rst")

    def test_html(self):
        self.run_simple_doctests('docs/specs/html.rst')

    def test_countries(self):
        self.run_simple_doctests('docs/specs/countries.rst')

    def test_help_texts(self):
        self.run_simple_doctests('docs/specs/help_texts.rst')

    def test_polly(self):
        self.run_simple_doctests('docs/specs/polly.rst')
        
    def test_ajax(self):
        self.run_simple_doctests('docs/specs/ajax.rst')

    def test_contacts(self):
        return self.run_simple_doctests('docs/specs/contacts.rst')

    def test_ssin(self):
        self.run_simple_doctests('docs/specs/ssin.rst')

    def test_faculties(self):
        self.run_simple_doctests('docs/specs/noi/faculties.rst')

    def test_tickets(self):
        self.run_simple_doctests('docs/specs/noi/tickets.rst')

    def test_projects(self):
        self.run_simple_doctests('docs/specs/noi/projects.rst')

    def test_votes(self):
        self.run_simple_doctests('docs/specs/noi/votes.rst')

    def test_clocking(self):
        self.run_simple_doctests('docs/specs/noi/clocking.rst')

    def test_noi_export_excel(self):
        self.run_simple_doctests('docs/specs/noi/export_excel.rst')

    def test_memo(self):
        self.run_simple_doctests('docs/specs/noi/memo.rst')

    def test_care(self):
        self.run_simple_doctests('docs/specs/noi/care.rst')

    def test_care_de(self):
        self.run_simple_doctests('docs/specs/noi/care_de.rst')

    def test_std(self):
        self.run_simple_doctests('docs/specs/noi/std.rst')

    def test_stars(self):
        self.run_simple_doctests('docs/specs/noi/stars.rst')

    def test_smtpd(self):
        self.run_simple_doctests('docs/specs/noi/smtpd.rst')

    def test_ddh(self):
        self.run_simple_doctests('docs/specs/noi/ddh.rst')

    def test_hosts(self):
        self.run_simple_doctests('docs/specs/noi/hosts.rst')

    def test_topics(self):
        self.run_simple_doctests('docs/specs/noi/topics.rst')
        
    def test_noi_public(self):
        self.run_simple_doctests('docs/specs/noi/public.rst')

    def test_bs3(self):
        self.run_simple_doctests('docs/specs/noi/bs3.rst')

    def test_general(self):
        self.run_simple_doctests('docs/specs/noi/general.rst')

    def test_mailbox(self):
        self.run_simple_doctests('docs/specs/noi/mailbox.rst')

    def test_github(self):
        self.run_simple_doctests('docs/specs/noi/github.rst')

    def test_as_pdf(self):
        self.run_simple_doctests('docs/specs/noi/as_pdf.rst')

    def test_noi_db(self):
        self.run_simple_doctests('docs/specs/noi/db.rst')

    def test_noi_deploy(self):
        self.run_simple_doctests('docs/specs/noi/deploy.rst')

        
    def test_cosi_ee(self):
        self.run_simple_doctests('docs/specs/cosi/cosi_ee.rst')
        
    def test_accounting(self):
        self.run_simple_doctests('docs/specs/cosi/accounting.rst')

    def test_finan(self):
        self.run_simple_doctests('docs/specs/cosi/finan.rst')

    def test_invoicing(self):
        self.run_simple_doctests('docs/specs/cosi/invoicing.rst')

    def test_ledger(self):
        self.run_simple_doctests('docs/specs/cosi/ledger.rst')

    def test_sales(self):
        self.run_simple_doctests('docs/specs/cosi/sales.rst')

    def test_tim2lino(self):
        return self.run_simple_doctests('docs/specs/cosi/tim2lino.rst')

    def test_apc(self):
        self.run_simple_doctests('docs/specs/cosi/apc.rst')
        
    def test_iban(self):
        self.run_simple_doctests('docs/specs/cosi/iban.rst')

    def test_b2c(self):
        self.run_simple_doctests('docs/specs/cosi/b2c.rst')


    def test_avanti_courses(self):
        self.run_simple_doctests('docs/specs/avanti/courses.rst')

    def test_avanti_general(self):
        self.run_simple_doctests('docs/specs/avanti/general.rst')

    def test_avanti_db(self):
        self.run_simple_doctests('docs/specs/avanti/db.rst')

    def test_avanti_cal(self):
        self.run_simple_doctests('docs/specs/avanti/cal.rst')

    def test_avanti_roles(self):
        self.run_simple_doctests('docs/specs/avanti/roles.rst')

    def test_tera(self):
        self.run_simple_doctests('docs/specs/tera.rst')


    def test_projects_mti(self):
        self.run_simple_doctests('docs/specs/projects/mti.rst')

    def test_projects_nomti(self):
        self.run_simple_doctests('docs/specs/projects/nomti.rst')

    def test_projects_lets1(self):
        self.run_simple_doctests('docs/specs/projects/lets1.rst')

    def test_projects_lets2(self):
        self.run_simple_doctests('docs/specs/projects/lets2.rst')

        


        
class ProjectsTests(TestCase):
    
    # def test_all(self):
    #     from atelier.fablib import run_in_demo_projects
    #     run_in_demo_projects('test')

    def test_events(self):
        self.run_django_manage_test("lino_book/projects/events")

    def test_watch(self):
        self.run_django_manage_test("lino_book/projects/watch")

    def test_belref(self):
        self.run_django_manage_test("lino_book/projects/belref")

    def test_babel_tutorial(self):
        self.run_django_manage_test("lino_book/projects/babel_tutorial")

    def test_min1(self):
        self.run_django_manage_test("lino_book/projects/min1")

    def test_min2(self):
        self.run_django_manage_test("lino_book/projects/min2")

    def test_apc(self):
        self.run_django_manage_test('lino_book/projects/apc')

    def test_cosi_ee(self):
        self.run_django_manage_test('lino_book/projects/cosi_ee')

    def test_team(self):
        self.run_django_manage_test('lino_book/projects/team')

    def test_bs3(self):
        self.run_django_manage_test('lino_book/projects/bs3')
        
    # def test_care(self):
    #     self.run_django_manage_test('lino_book/projects/care')

    def test_liina(self):
        self.run_django_manage_test('lino_book/projects/liina')

    def test_adg(self):
        self.run_django_manage_test('lino_book/projects/adg')

    def test_lydia(self):
        self.run_django_manage_test('lino_book/projects/lydia')
        
    def test_mti(self):
        self.run_django_manage_test('lino_book/projects/mti')
        
    def test_nomti(self):
        self.run_django_manage_test('lino_book/projects/nomti')
        
    def test_lets1(self):
        self.run_django_manage_test('lino_book/projects/lets1')
        
    def test_lets2(self):
        self.run_django_manage_test('lino_book/projects/lets2')
        

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

    def test_utils(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/__init__.py')

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


class UtilsTests(LinoTestCase):

    def test_instantiator(self):
        self.run_simple_doctests(LINO_SRC+"lino/utils/instantiator.py")

    def test_dates(self):
        self.run_simple_doctests(LINO_SRC+"lino/utils/dates.py")

    def test_soup(self):
        self.run_simple_doctests(LINO_SRC+"lino/utils/soup.py")

    def test_html2odf(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/html2odf.py')

    def test_jinja(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/jinja.py')

    def test_xmlgen_html(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/xmlgen/html.py')

    def test_html2rst(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/html2rst.py')

    def test_xmlgen_sepa(self):
        if PYAFTER26:
            self.run_simple_doctests(LINO_SRC+'lino/utils/xmlgen/sepa/__init__.py')

    def test_memo(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/memo.py')

    def test_tidy(self):
        if HAS_TIDYLIB:
            self.run_simple_doctests(LINO_SRC+'lino/utils/html2xhtml.py')

    def test_demonames(self):
        self.run_simple_doctests(LINO_SRC+"lino/utils/demonames/bel.py")
        self.run_simple_doctests(LINO_SRC+"lino/utils/demonames/est.py")

    def test_odsreader(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/odsreader.py')
    
    # def test_choicelists(self):
    #     self.run_simple_doctests(LINO_SRC+'lino/core/choicelists.py')

    def test_jsgen(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/jsgen.py')

    def test_format_date(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/format_date.py')

    def test_ranges(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/ranges.py')

    def test_addressable(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/addressable.py')

    def test_cycler(self):
        self.run_simple_doctests(LINO_SRC+'lino/utils/cycler.py')



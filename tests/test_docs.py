# import os, sys
# from os.path import join, dirname
# import unittest
# import doctest
# import subprocess
from atelier.test import make_docs_suite
# THIS = dirname(__file__)

# doc_files = []

def load_tests(loader, standard_tests, pattern):
    return make_docs_suite("docs", exclude="docs/specs/printing.rst")

# test_suite = make_docs_suite("docs")

# print(len(doc_files))
# raise Exception("20170829")

# docs = doctest.DocFileSuite(
#     *doc_files,
#     optionflags=doctest.REPORT_ONLY_FIRST_FAILURE,
#     module_relative=False, encoding='utf-8')


# def load_tests(loader, standard_tests, pattern):
#     # top level directory cached on loader instance
#     # package_tests = loader.discover(start_dir=THIS, pattern=pattern)
#     # standard_tests.addTests(package_tests)
#     # standard_tests.addTests(docs)
#     # return standard_tests
#     return docs



# from lino.utils.pythontest import TestCase

# class Tests(TestCase):

#     def test_all(self):
#         for root, dirs, files in os.walk("docs/specs/cosi"):
#             for file in files:
#                 if file.endswith(".rst"):
#                      # print(os.path.join(root, file))
#                      fn = join(root, file)
#                      self.run_simple_doctests(fn)
        
# class LibTests(TestCase):

#     def test_users(self):
#         self.run_simple_doctests("docs/dev/users.rst")
        
#     def test_runtests(self):
#         self.run_simple_doctests("docs/dev/runtests.rst")

#     def test_env(self):
#         self.run_simple_doctests("docs/dev/env.rst")

#     # def test_cal_utils(self):
#     #     self.run_simple_doctests('lino_xl.lib.cal/utils.py')


# class DocsAdminTests(TestCase):
#     def test_printing(self):
#         self.run_simple_doctests('docs/admin/printing.rst')
#     def test_linod(self):
#         self.run_simple_doctests('docs/admin/linod.rst')


# class DocsTests(TestCase):

#     # python setup.py test -s tests.DocsTests.test_docs
#     def test_docs(self):
#         self.run_simple_doctests("""
#         docs/dev/ml/contacts.rst
#         docs/dev/mixins.rst
#         docs/user/templates_api.rst
#         docs/tested/test_i18n.rst
#         """)

#     def test_memo(self):
#         self.run_simple_doctests("docs/dev/memo.rst")

#     def test_ar(self):
#         self.run_simple_doctests("docs/dev/ar.rst")

#     def test_watch(self):
#         self.run_simple_doctests("docs/dev/watch.rst")

#     def test_perms(self):
#         self.run_simple_doctests('docs/dev/perms.rst')

#     def test_i18n(self):
#         self.run_simple_doctests('docs/dev/i18n.rst')

#     def test_setup(self):
#         self.run_simple_doctests('docs/dev/setup.rst')

#     #

#     def test_gfks(self):
#         self.run_simple_doctests('docs/tested/gfks.rst')

#     def test_dynamic(self):
#         self.run_simple_doctests('docs/tested/dynamic.rst')

#     def test_initdb(self):
#         self.run_simple_doctests("docs/dev/initdb.rst")

#     def test_polly(self):
#         self.run_simple_doctests("docs/tested/polly.rst")

#     def test_core_utils(self):
#         self.run_simple_doctests("docs/tested/core_utils.rst")

#     def test_choicelists(self):
#         self.run_simple_doctests("docs/dev/choicelists.rst")

#     def test_languages(self):
#         self.run_simple_doctests("docs/dev/languages.rst")

#     def test_site(self):
#         self.run_simple_doctests("docs/dev/site.rst")

#     # def test_min1(self):
#     #     self.run_simple_doctests("docs/tested/min1.rst")

#     def test_e006(self):
#         self.run_simple_doctests("docs/tested/e006.rst")

#     def test_ddh(self):
#         self.run_simple_doctests("docs/tested/ddh.rst")

#     def test_settings(self):
#         self.run_simple_doctests('docs/dev/ad.rst')

# class SpecsTests(TestCase):


#     def test_notify(self):
#         self.run_simple_doctests('docs/specs/notify.rst')

#     def test_phones(self):
#         self.run_simple_doctests('docs/specs/phones.rst')

#     def test_dumps(self):
#         self.run_simple_doctests('docs/specs/dumps.rst')

#     def test_i18n(self):
#         self.run_simple_doctests('docs/specs/i18n.rst')

#     def test_gfks(self):
#         self.run_simple_doctests('docs/specs/gfks.rst')

#     def test_printing(self):
#         self.run_simple_doctests('docs/specs/printing.rst')

#     def test_holidays(self):
#         self.run_simple_doctests('docs/specs/holidays.rst')

#     def test_cal(self):
#         self.run_simple_doctests('docs/specs/cal.rst')

#     def test_checkdata(self):
#         self.run_simple_doctests('docs/specs/checkdata.rst')

#     def test_cv(self):
#         self.run_simple_doctests('docs/specs/cv.rst')

#     def test_users(self):
#         self.run_simple_doctests('docs/specs/users.rst')

#     def test_households(self):
#         self.run_simple_doctests('docs/specs/households.rst')

#     def test_tinymce(self):
#         self.run_simple_doctests("docs/specs/tinymce.rst")

#     def test_export_excel(self):
#         self.run_simple_doctests("docs/specs/export_excel.rst")

#     def test_noi_export_excel(self):
#         self.run_simple_doctests("docs/specs/noi/export_excel.rst")

#     def test_invalid_requests(self):
#         self.run_simple_doctests("docs/specs/invalid_requests.rst")

#     def test_html(self):
#         self.run_simple_doctests('docs/specs/html.rst')

#     def test_countries(self):
#         self.run_simple_doctests('docs/specs/countries.rst')

#     def test_help_texts(self):
#         self.run_simple_doctests('docs/specs/help_texts.rst')

#     def test_polly(self):
#         self.run_simple_doctests('docs/specs/polly.rst')
        
#     def test_ajax(self):
#         self.run_simple_doctests('docs/specs/ajax.rst')

#     def test_jsgen(self):
#         self.run_simple_doctests('docs/specs/jsgen.rst')

#     def test_contacts(self):
#         return self.run_simple_doctests('docs/specs/contacts.rst')

#     def test_ssin(self):
#         self.run_simple_doctests('docs/specs/ssin.rst')

#     def test_faculties(self):
#         self.run_simple_doctests('docs/specs/noi/faculties.rst')

#     def test_tickets(self):
#         self.run_simple_doctests('docs/specs/noi/tickets.rst')

#     def test_projects(self):
#         self.run_simple_doctests('docs/specs/noi/projects.rst')

#     def test_votes(self):
#         self.run_simple_doctests('docs/specs/noi/votes.rst')

#     def test_clocking(self):
#         self.run_simple_doctests('docs/specs/noi/clocking.rst')

#     def test_noi_export_excel(self):
#         self.run_simple_doctests('docs/specs/noi/export_excel.rst')

#     def test_memo(self):
#         self.run_simple_doctests('docs/specs/noi/memo.rst')

#     def test_care(self):
#         self.run_simple_doctests('docs/specs/noi/care.rst')

#     def test_care_de(self):
#         self.run_simple_doctests('docs/specs/noi/care_de.rst')

#     def test_std(self):
#         self.run_simple_doctests('docs/specs/noi/std.rst')

#     def test_stars(self):
#         self.run_simple_doctests('docs/specs/noi/stars.rst')

#     def test_smtpd(self):
#         self.run_simple_doctests('docs/specs/noi/smtpd.rst')

#     def test_ddh(self):
#         self.run_simple_doctests('docs/specs/noi/ddh.rst')

#     def test_hosts(self):
#         self.run_simple_doctests('docs/specs/noi/hosts.rst')

#     def test_topics(self):
#         self.run_simple_doctests('docs/specs/noi/topics.rst')
        
#     def test_noi_public(self):
#         self.run_simple_doctests('docs/specs/noi/public.rst')

#     def test_bs3(self):
#         self.run_simple_doctests('docs/specs/noi/bs3.rst')

#     def test_general(self):
#         self.run_simple_doctests('docs/specs/noi/general.rst')

#     def test_mailbox(self):
#         self.run_simple_doctests('docs/specs/noi/mailbox.rst')

#     def test_github(self):
#         self.run_simple_doctests('docs/specs/noi/github.rst')

#     def test_as_pdf(self):
#         self.run_simple_doctests('docs/specs/noi/as_pdf.rst')

#     def test_noi_db(self):
#         self.run_simple_doctests('docs/specs/noi/db.rst')

#     def test_noi_deploy(self):
#         self.run_simple_doctests('docs/specs/noi/deploy.rst')

        
#     def test_cosi_ee(self):
#         self.run_simple_doctests('docs/specs/cosi/cosi_ee.rst')
        
#     def test_accounting(self):
#         self.run_simple_doctests('docs/specs/cosi/accounting.rst')

#     def test_finan(self):
#         self.run_simple_doctests('docs/specs/cosi/finan.rst')

#     def test_invoicing(self):
#         self.run_simple_doctests('docs/specs/cosi/invoicing.rst')

#     def test_ledger(self):
#         self.run_simple_doctests('docs/specs/cosi/ledger.rst')

#     def test_sales(self):
#         self.run_simple_doctests('docs/specs/cosi/sales.rst')

#     def test_tim2lino(self):
#         return self.run_simple_doctests('docs/specs/cosi/tim2lino.rst')

#     def test_apc(self):
#         self.run_simple_doctests('docs/specs/cosi/apc.rst')
        
#     def test_iban(self):
#         self.run_simple_doctests('docs/specs/cosi/iban.rst')

#     def test_b2c(self):
#         self.run_simple_doctests('docs/specs/cosi/b2c.rst')


#     def test_avanti_courses(self):
#         self.run_simple_doctests('docs/specs/avanti/courses.rst')

#     def test_avanti_general(self):
#         self.run_simple_doctests('docs/specs/avanti/general.rst')

#     def test_avanti_db(self):
#         self.run_simple_doctests('docs/specs/avanti/db.rst')

#     def test_avanti_cal(self):
#         self.run_simple_doctests('docs/specs/avanti/cal.rst')

#     def test_avanti_avanti(self):
#         self.run_simple_doctests('docs/specs/avanti/avanti.rst')

#     def test_avanti_roles(self):
#         self.run_simple_doctests('docs/specs/avanti/roles.rst')

#     def test_tera(self):
#         self.run_simple_doctests('docs/specs/tera/misc.rst')

#     def test_tera_tim2lino(self):
#         self.run_simple_doctests('docs/specs/tera/tim2lino.rst')

#     def test_ana(self):
#         self.run_simple_doctests('docs/specs/ana.rst')

#     def test_vat(self):
#         self.run_simple_doctests('docs/specs/vat.rst')
#     def test_bevat(self):
#         self.run_simple_doctests('docs/specs/bevat.rst')
#     def test_bevats(self):
#         self.run_simple_doctests('docs/specs/bevats.rst')


#     def test_projects_mti(self):
#         self.run_simple_doctests('docs/specs/projects/mti.rst')

#     def test_projects_nomti(self):
#         self.run_simple_doctests('docs/specs/projects/nomti.rst')

#     def test_projects_lets1(self):
#         self.run_simple_doctests('docs/specs/projects/lets1.rst')

#     def test_projects_lets2(self):
#         self.run_simple_doctests('docs/specs/projects/lets2.rst')

        

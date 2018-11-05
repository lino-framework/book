from django import VERSION

from lino.utils.pythontest import TestCase
from lino import PYAFTER26

class TestCase(TestCase):
    
    def test_translate(self):
        self.run_django_manage_test('docs/dev/translate')

    # def test_hello(self):
    #     self.run_django_manage_test('docs/tutorials/hello')

    # def test_dumpy(self):
    #     self.run_django_manage_test('docs/tutorials/dumpy')

    # def test_lets(self):
    #     self.run_django_manage_test('docs/tutorials/lets')

    # def test_letsmti(self):
    #     self.run_django_manage_test('docs/tutorials/letsmti')

    # def test_pisa(self):
    #     self.run_django_manage_test('lino_book/projects/pisa')
    
    # def test_de_BE(self):
    #     self.run_django_manage_test('lino_book/projects/de_BE')

    # def test_myroles(self):
    #     self.run_django_manage_test('lino_book/projects/myroles')

    def test_mti(self):
        self.run_django_manage_test('lino_book/projects/mti')

    def test_auto_create(self):
        self.run_django_manage_test('lino_book/projects/auto_create')
    
    def test_human(self):
        self.run_django_manage_test('lino_book/projects/human')

    def test_actions(self):
        self.run_django_manage_test('lino_book/projects/actions')

    def test_actors(self):
        self.run_django_manage_test('lino_book/projects/actors')

    # def test_watch(self):
    #     self.run_django_manage_test('lino_book/projects/watch_tutorial')
    
    def test_vtables(self):
        self.run_django_manage_test('lino_book/projects/vtables')
    
    def test_tables(self):
        self.run_django_manage_test('lino_book/projects/tables')
    
    def test_diamond(self):
        self.run_django_manage_test('lino_book/projects/diamond')

    def test_diamond2(self):
        # TODO: Even when using method described in
        # https://code.djangoproject.com/ticket/28332
        # we still have the problem of Django saying
        # django.core.exceptions.FieldError: Local field u'street' in class
        # 'PizzeriaBar' clashes with field of the same name from base class
        # 'Pizzeria'.
        if VERSION[0] == 1 and VERSION[1] < 11:
            self.run_django_manage_test('lino_book/projects/diamond2')

    def test_addrloc(self):
        self.run_django_manage_test('lino_book/projects/addrloc')
    
    def test_polls(self):
        self.run_django_manage_test('lino_book/projects/polls')
        
    def test_polls2(self):
        self.run_django_manage_test('lino_book/projects/polls2')

    def test_gfktest(self):
        self.run_django_manage_test('lino_book/projects/gfktest')

    def test_mldbc(self):
        self.run_django_manage_test('lino_book/projects/mldbc')

    # def test_belref(self):
    #     self.run_django_manage_test("docs/tutorials/belref")

    def test_float2decimal(self):
        if PYAFTER26:
            self.run_django_manage_test("lino_book/projects/float2decimal")

    def test_integer_pk(self):
        self.run_django_manage_test("lino_book/projects/integer_pk")

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
        
    def test_anna(self):
        self.run_django_manage_test('lino_book/projects/anna')

    def test_liina(self):
        self.run_django_manage_test('lino_book/projects/liina')

    def test_adg(self):
        self.run_django_manage_test('lino_book/projects/adg')

    def test_lydia(self):
        self.run_django_manage_test('lino_book/projects/lydia')
        
    def test_nomti(self):
        self.run_django_manage_test('lino_book/projects/nomti')
        
    def test_lets1(self):
        self.run_django_manage_test('lino_book/projects/lets1')
        
    def test_lets2(self):
        self.run_django_manage_test('lino_book/projects/lets2')
        
    def test_gerd(self):
        self.run_django_manage_test('lino_book/projects/gerd')
        
    def test_mathieu(self):
        self.run_django_manage_test('lino_book/projects/mathieu')
        


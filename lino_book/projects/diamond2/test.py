from unittest import TestCase
from django import VERSION
from .main.models import PizzeriaBar

# under Django 1.11 this fails with
# django.core.exceptions.FieldError: Local field u'street' in class 'PizzeriaBar' clashes with field of the same name from base class 'Pizzeria'.

class DocTest(TestCase):
    
    def test_django(self):
        p = PizzeriaBar(name="Michaels", min_age=21, specialty="Cheese",
                        pizza_bar_specific_field="Doodle")
        self.assertEqual(p.pizza_bar_specific_field, 'Doodle')
        
        if VERSION[0] == 1 and VERSION[1] == 6:
            self.check_django_16(p)
        elif VERSION[0] == 1 and VERSION[1] > 6:
            self.check_django_17(p)
        else:
            self.fail("Unsupported Django version {0}".format(VERSION))

    def check_django_16(self, p):
        
        self.assertEqual(p.name, '')

        # The `name` field has not been initialized because
        # it is being inherited from a grand-parent.
        
    def check_django_17(self, p):
        self.assertEqual(p.name, 'Michaels')
        
        

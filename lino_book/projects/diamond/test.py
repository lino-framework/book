from unittest import TestCase
from django import VERSION
from lino_book.projects.diamond.main.models import PizzeriaBar

# install the fix
from lino.core.inject import django_patch
django_patch()


class DocTest(TestCase):

    def test_django(self):
        p = PizzeriaBar(name="Michaels", min_age=21, specialty="Cheese",
                        pizza_bar_specific_field="Doodle")
        self.assertEqual(p.pizza_bar_specific_field, 'Doodle')
        
        if VERSION[0] == 1 and VERSION[1] == 6:
            self.check_django_16(p)
        else:
            self.check_django_17(p)

    def check_django_16(self, p):
        
        self.assertEqual(p.name, '')

        # The `name` field has not been initialized because
        # it is being inherited from a grand-parent.
        
    def check_django_17(self, p):
        self.assertEqual(p.name, 'Michaels')
        
        

# from lino.utils.test import DocTest

from unittest import TestCase
from django.conf import settings

class TestCase(TestCase):

    def test_languages(self):
        self.assertEqual(str(settings.SITE.languages),"(LanguageInfo(django_code='en', name='en', index=0, suffix=''), LanguageInfo(django_code='es', name='es', index=1, suffix='_es'))")



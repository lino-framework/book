"""
test whether a dump of the previous version can be restored

  $ go lydia
  $ python manage.py test tests.test_restore

"""
from lino.utils.djangotest import RemoteAuthTestCase
from django.core.management import call_command

class TestCase(RemoteAuthTestCase):
    def test_restore(self):
        call_command("run", "tests/dumps/18.8.0/restore.py", "--noinput")


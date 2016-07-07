from .a import *
SITE.verbose_name = SITE.verbose_name + " (:memory:)"
DATABASES['default']['NAME'] = ':memory:'

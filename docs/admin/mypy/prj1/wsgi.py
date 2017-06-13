import sys ; sys.path.append('/usr/local/src/lino')
from lino_local import wsgi ; wsgi(globals(), 'lino_sites.prj1.settings')

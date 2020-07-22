from lino_avanti.lib.avanti.settings import *

class Site(Site):

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('clients', 'demo_coach', 'nathalie')

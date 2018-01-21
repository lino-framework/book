from lino.api import ad, _


class Plugin(ad.Plugin):
    verbose_name = _("Virtual tables")

    def setup_main_menu(self, site, profile, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('vtables.CitiesAndInhabitants')

    

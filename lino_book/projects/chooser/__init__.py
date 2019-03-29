from lino.ad import Plugin


class Plugin(Plugin):
    def setup_main_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('chooser.Countries')
        m.add_action('chooser.Cities')
        m.add_action('chooser.Contacts')

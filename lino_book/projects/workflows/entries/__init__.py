from lino.api import ad, _


class Plugin(ad.Plugin):
    "See :class:`lino.core.plugin.Plugin`."

    verbose_name = _("Entries")

    needs_plugins = ['lino.modlib.changes', 'lino.modlib.notify']

    def setup_main_menu(self, site, user_type, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('entries.MyEntries')

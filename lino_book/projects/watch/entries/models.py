from django.db import models
from lino.api import dd
from django.utils.translation import ugettext_lazy as _

from lino.modlib.users.mixins import My, UserAuthored


class Entry(UserAuthored):

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")

    subject = models.CharField(_("Subject"), blank=True, max_length=200)
    body = dd.RichTextField(_("Body"), blank=True)
    company = dd.ForeignKey('contacts.Company')


class Entries(dd.Table):
    model = Entry

    detail_layout = """
    id user
    company
    subject
    body
    """

    insert_layout = """
    company
    subject
    """


class EntriesByCompany(Entries):
    master_key = 'company'


class MyEntries(My, Entries):
    pass


@dd.receiver(dd.post_startup)
def my_change_watchers(sender, **kw):
    """
    This site watches the changes to Partner, Company and Entry
    """
    self = sender
    
    from lino.utils.watch import watch_changes as wc
    
    # In our example we want to collect changes to Company and Entry
    # objects to their respective Partner.

    wc(self.models.contacts.Partner)
    wc(self.models.contacts.Company, master_key='partner_ptr')
    wc(self.models.entries.Entry, master_key='company__partner_ptr')

    # add two application-specific panels, one to Partners, one to
    # Companies:
    
    self.models.contacts.Companies.add_detail_tab(
        'changes', 'changes.ChangesByMaster')
    self.models.contacts.Companies.add_detail_tab(
        'entries', 'entries.EntriesByCompany')


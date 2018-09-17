## Copyright 2013-2018 Rumma & Ko Ltd
## This file is part of the Lino project.

from django.db import models
from lino.api import dd
from django.utils.translation import ugettext_lazy as _
from lino.mixins import CreatedModified
from lino.modlib.users.mixins import My, UserAuthored

from .choicelists import EntryStates

class Entry(CreatedModified, UserAuthored):
    
    workflow_state_field = 'state'
    
    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")
        
    
    subject = models.CharField(_("Subject"),blank=True,max_length=200)
    body = dd.RichTextField(_("Body"),blank=True)
    company = dd.ForeignKey('contacts.Company',blank=True,null=True)
    state = EntryStates.field(blank=True, default='new')
    
class Entries(dd.Table):
    model = Entry    
    detail_layout = """
    id user created modified
    subject
    company workflow_buttons
    body
    """
    insert_layout = """
    company
    subject
    """
    
class EntriesByCompany(Entries):
    master_key = 'company'
    column_names = "modified user subject workflow_buttons *"
    
class MyEntries(My, Entries):
    column_names = "modified subject workflow_buttons *"


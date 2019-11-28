# -*- coding: UTF-8 -*-
# Copyright 2015-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Database models for this plugin.

"""

from lino.api import dd, _
from lino.utils import join_words
from lino.mixins import  Hierarchical

from lino_xl.lib.contacts.models import *
from lino.modlib.comments.mixins import Commentable
from lino_xl.lib.phones.mixins import ContactDetailsOwner


PartnerDetail.address_box = dd.Panel("""
    name_box
    country #region city zip_code:10
    #addr1
    #street_prefix street:25 street_no street_box
    #addr2
    """, label=_("Address"))

PartnerDetail.contact_box = dd.Panel("""
    url
    phone
    gsm #fax
    """, label=_("Contact"))



class Person(Person, Commentable):
    
    class Meta(Person.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Person')
        
    def __str__(self):
        words = []
        words.append(self.first_name)
        words.append(self.last_name)
        return join_words(*words)

    def get_overview_elems(self, ar):
        elems = super(Person, self).get_overview_elems(ar)
        elems += ContactDetailsOwner.get_overview_elems(self, ar)
        return elems

    @classmethod
    def setup_parameters(cls, fields):
        fields.setdefault(
            'company', dd.ForeignKey(
                'contacts.Company', blank=True, null=True))
        super(Person, cls).setup_parameters(fields)
    
    @classmethod
    def get_simple_parameters(cls):
        for p in  super(Person, cls).get_simple_parameters():
            yield p
        yield 'company'
    
    @classmethod
    def add_param_filter(cls, qs, lookup_prefix='', company=None,
                         **kwargs):
        qs = super(Person, cls).add_param_filter(qs, **kwargs)
        if company:
            fkw = dict()
            wanted = company.whole_clan()
            fkw[lookup_prefix + 'rolesbyperson__company__in'] = wanted
            qs = qs.filter(**fkw)
        
        return qs
        

# We use the `overview` field only in detail forms, and we
# don't want it to have a label "Description":
dd.update_field(Person, 'overview', verbose_name=None)    

class Company(Company, Hierarchical, Commentable):
    
    class Meta(Company.Meta):
        app_label = 'contacts'
        abstract = dd.is_abstract_model(__name__, 'Company')
        
    def get_overview_elems(self, ar):
        elems = super(Company, self).get_overview_elems(ar)
        elems += ContactDetailsOwner.get_overview_elems(self, ar)
        return elems



class PersonDetail(PersonDetail):
    
    main = """
    overview contact_box
    contacts.RolesByPerson:30 comments.CommentsByRFC:30
    """

    contact_box = dd.Panel("""
    last_name first_name:15 
    gender #title:10 language:10 
    birth_date age:10 id:6
    """)  #, label=_("Contact"))


class CompaniesByCompany(Companies):
    label = _("Children")
    master_key = 'parent'
    column_names = 'name *'
    
class CompanyDetail(CompanyDetail):
    main = """
    overview:30 general_middle:20 CompaniesByCompany:30
    contacts.RolesByCompany:30 comments.CommentsByRFC:30
    """

    general_middle = """
    type
    parent
    language:10 id:6
    """
    

Companies.set_detail_layout(CompanyDetail())
Persons.set_detail_layout(PersonDetail())
Person.column_names = 'last_name first_name gsm email city *'
Persons.params_layout = 'observed_event start_date end_date company'

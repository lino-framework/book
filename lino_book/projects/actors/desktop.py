from .models import dd, PartnerType, Partner, Person

class Partners(dd.Table):
    model = Partner
    # no explicit `label` attribute, so take verbose_name_plural from model


class Persons(Partners):
    model = Person
    # no explicit `label` attribute, so take verbose_name_plural from model


class FunnyPersons(Persons):
    label = "Funny persons"


class MyFunnyPersons(FunnyPersons):
    # no explicit `label` attribute, so inherit from parent
    pass


PARTNER_TYPE_CUSTOMER = 1
PARTNER_TYPE_PROVIDER = 2


class TypedPartners(Partners):
    partner_type_pk = None
    
    @classmethod
    def make_instance(cls,**kw):
        kw.update(type_id=cls.partner_type_pk)
        obj = cls.model(**kw)
        return obj

    @classmethod
    def get_request_queryset(cls, ar):
        # override
        qs = super(TypedPartners, cls).get_request_queryset(ar)
        return qs.filter(type__id=cls.partner_type_pk)
        
    @classmethod
    def get_actor_label(cls):
        # override
        if cls.partner_type_pk is None:
            return super(TypedPartners, cls).get_actor_label()
        pt = PartnerType.objects.get(id=cls.partner_type_pk)
        return pt.name


class Customers(TypedPartners):
    partner_type_pk = PARTNER_TYPE_CUSTOMER


class Providers(TypedPartners):
    partner_type_pk = PARTNER_TYPE_PROVIDER

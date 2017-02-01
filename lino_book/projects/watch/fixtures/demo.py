from lino.api import rt
from lino.core.diff import ChangeWatcher
from lino.core.utils import PseudoRequest


def objects():

    Company = rt.models.contacts.Company
    
    ar = rt.login(request=PseudoRequest("robin"))

    obj = Company(name="My pub")
    obj.full_clean()
    obj.save_new_instance(ar)
    
    cw = ChangeWatcher(obj)
    obj.name = "Our pub"
    obj.save_watched_instance(ar, cw)

    obj.delete_instance(ar)

    # this is a special fixture : it creates objects as a side effect
    # but does not yield them.
    return []

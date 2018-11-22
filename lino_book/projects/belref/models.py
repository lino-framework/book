# -*- coding: UTF-8 -*-
# Copyright 2013-2016 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The :xfile:`models` module for :mod:`lino_book.projects.belref`.

"""

from lino.api import dd

concepts = dd.resolve_app('concepts')


class Main(concepts.TopLevelConcepts):
    pass


@dd.receiver(dd.post_analyze)
def my_details(sender, **kw):
    site = sender

    lst = (site.models.countries.Places,
           site.models.countries.Countries,
           site.models.concepts.Concepts)
    for t in lst:
        t.required_roles.discard(dd.SiteUser)
        t.required_roles.discard(dd.SiteStaff)

    site.models.countries.Places.set_detail_layout("""
    name country inscode
    parent type id
    PlacesByPlace
    """)

    site.models.countries.Countries.set_detail_layout("""
    isocode name short_code inscode
    countries.PlacesByCountry
    """)

# -*- coding: utf-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
Tests some behaviour of the `Client.national_id` field.

You can run only these tests by issuing::

  $ go adg
  $ python manage.py test tests.test_nullchar

Tests whether `national_id` is set to NULL (not empty string).

"""

from __future__ import unicode_literals
from __future__ import print_function


import os
from six.moves.urllib.parse import urlencode

from lino.utils.djangotest import RemoteAuthTestCase
from lino.api import dd, rt
from lino.utils.instantiator import create_row


class TestCase(RemoteAuthTestCase):
    maxDiff = None
    # override_djangosite_settings = dict(use_java=True)

    def test01(self):
        from lino.core import constants
        from lino.modlib.users.choicelists import UserTypes
        from lino.api.shell import countries, users
        
        Client = rt.models.avanti.Client

        u = users.User(username='robin',
                       user_type=UserTypes.admin,
                       language="en")
        u.save()
        self.client.force_login(u)
        
        be = countries.Country(name="Belgium", isocode="BE")
        be.save()
        
        kw = dict()
        kw.update(national_id="680601 053-29")
        kw.update(first_name="Jean")
        kw.update(middle_name="Jacques")
        kw.update(last_name="Jeffin")
        jean = create_row(Client, **kw)

        kw.update(first_name="Jo")
        kw.update(national_id="680601 054-28")
        kw.update(last_name="Jeffin")
        jo = create_row(Client, **kw)

        def grid_put(username, url, **data):
            data[constants.URL_PARAM_ACTION_NAME] = 'grid_put'
            kwargs = dict(data=urlencode(data))
            kwargs['REMOTE_USER'] = username
            response = self.client.put(url, **kwargs)
            # print(response)
            return self.check_json_result(
                response, 'rows success message')

        url = '/api/avanti/Clients/' + str(jean.pk)
        result = grid_put('robin', url, national_id="")
        self.assertEqual(result['success'], True)
        self.assertEqual(result['message'], 'Client "JEFFIN Jean (100)" has been updated.')

        jean = Client.objects.get(pk=jean.pk)
        self.assertEqual(jean.national_id, None)
        
        url = '/api/avanti/Clients/' + str(jo.pk)
        result = grid_put('robin', url, national_id="")
        self.assertEqual(result['success'], True)
        self.assertEqual(result['message'], 'Client "JEFFIN Jo (101)" has been updated.')


# -*- coding: UTF-8 -*-
# Copyright 2014-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
Runs some tests about reading eID cards.

You can run only these tests by issuing::

  $ go avanti1
  $ python manage.py test tests.test_beid

"""

from __future__ import unicode_literals
from __future__ import print_function

import os
import json

from lino.utils.djangotest import RemoteAuthTestCase
from django.utils.datastructures import MultiValueDict
from lino.utils import ssin
from lino.api import dd, rt


def readfile(name):
    fn = os.path.join(os.path.dirname(__file__), name)
    return open(fn).read()


# class WebRequest:
#     method = "POST"
#     subst_user = None
#     requesting_panel = None

#     def __init__(self, user, data):
#         self.POST = self.REQUEST = MultiValueDict(data)
#         self.user = user


class BeIdTests(RemoteAuthTestCase):
    maxDiff = None
    # override_djangosite_settings = dict(use_java=True)

    def test01(self):
        from lino.core import constants
        from django.conf import settings
        from lino.modlib.users.choicelists import UserTypes
        from lino.api.shell import countries, avanti, users

        # is it the right settings module?
        self.assertEqual(os.environ['DJANGO_SETTINGS_MODULE'],
                         'lino_book.projects.avanti1.settings.demo')

        self.assertEqual(settings.MIDDLEWARE, (
            'django.middleware.common.CommonMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'lino.core.auth.middleware.AuthenticationMiddleware',
            'lino.core.auth.middleware.WithUserMiddleware',
            'lino.core.auth.middleware.DeviceTypeMiddleware',
            'lino.core.auth.middleware.RemoteUserMiddleware',
            'lino.utils.ajax.AjaxExceptionResponse'))

        u = users.User(username='robin',
                       user_type=UserTypes.admin,
                       language="en")
        u.save()
        self.client.force_login(u)
        be = countries.Country(name="Belgium", isocode="BE")
        be.save()

        Holder = dd.plugins.beid.holder_model
        kw = dict()
        # kw.update(card_number="123456789")
        # kw.update(national_id="680601 053-29")
        kw.update(first_name="Jean-Jacques")
        # kw.update(middle_name="")
        kw.update(last_name="Jeffin")
        obj = Holder(**kw)
        obj.full_clean()
        obj.save()

        def simulate_eidreader(uuid):
            # simulate the client's eidreader posting its data to the
            # server.
            s = readfile(uuid + '.json')
            # raise Exception(repr(s))
            data = dict(card_data=s)
            url = '/eid/' + uuid
            response = self.client.post(
                url, data,
                REMOTE_USER='robin',
                HTTP_ACCEPT_LANGUAGE='en')
            result = self.check_json_result(response, 'success message')
            self.assertEqual(result, {'message': 'OK', 'success': True})

        # The following tests are based on an older simulation system developed
        # before simulate_eidreader_path was developed. TODO: convert them to
        # simulate_eidreader_path. En attendant we simply disable
        # simulate_eidreader_path here. Works as well.
        save_path = dd.plugins.beid.simulate_eidreader_path
        dd.plugins.beid.simulate_eidreader_path = None
        
        uuid = 'beid_test_1'
        simulate_eidreader(uuid)

        url = '/api/avanti/Clients'
        post_data = dict()
        # post_data.update(
        #     card_data=readfile('beid_test_1.json'))
        post_data['uuid'] = uuid
        post_data[constants.URL_PARAM_ACTION_NAME] = 'find_by_beid'

        # First attempt fails because a person with exactly the same
        # name already exists.
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')

        # result = self.check_json_result(response, 'alert success message')
        result = self.check_json_result(response)
        # raise Exception(repr(result))
        self.assertEqual(result['success'], False)
        expected = ("Sorry, I cannot handle that case: Cannot create "
                    "new client because there is already a person named "
                    "Jean-Jacques Jeffin in our database.")
        self.assertEqual(result['message'], expected)

        # Second attempt. We are reading the same card, but this time
        # there is a person with this `national_id`.
        obj.national_id = "680601 053-29"
        # obj.first_name = "Jean-Claude"
        obj.full_clean()
        obj.save()


        dlg = []
        expected = """\
Click OK to apply the following changes for JEFFIN Jean-Jacques (100) :\
<br/>Birth date : '' -> 1968-06-01
<br/>Birth place : '' -> 'Mons'
<br/>Country : None -> Country #BE ('Belgium')
<br/>Gender : None -> <Genders.male:M>
<br/>ID card valid from : None -> 2016-02-06
<br/>Locality : None -> Place #1 ('Helsinki')
<br/>Street : '' -> 'Estland'
<br/>Zip code : '' -> '1262'
<br/>eID card issuer : '' -> 'Helsinki'
<br/>eID card number : '' -> '592382784772'
<br/>eID card type : None -> <BeIdCardTypes.belgian_citizen:01>
<br/>until : None -> 2026-02-06"""

# Click OK to apply the following changes for JEFFIN Jean (100) :\
# <br/>Locality : None -> Place #1 ('Tallinn')
# <br/>Gender : None -> <Genders.male:M>
# <br/>until : None -> 2016-08-19
# <br/>Street : '' -> 'Estland'
# <br/>ID card valid from : None -> 2011-08-19
# <br/>eID card type : None -> <BeIdCardTypes.belgian_citizen:1>
# <br/>eID card issuer : '' -> 'Tallinn'
# <br/>Birth place : '' -> 'Mons'
# <br/>Country : None -> Country #BE ('Belgium')
# <br/>Birth date : '' -> 1968-06-01
# <br/>eID card number : '' -> '592345678901'
# <br/>Zip code : '' -> '1418'

        dlg.append((expected, 'yes'))
        dlg.append((
            'Client "JEFFIN Jean-Jacques (100)" has been saved.',
            None))
        self.check_callback_dialog(
            self.client.post, 'robin', url, dlg, post_data)

        obj = avanti.Client.objects.get(id=100)
        # addr = addresses.Address.objects.get(partner=obj)
        self.assertEqual(obj.city.name, "Helsinki")
        # self.assertEqual(addr.primary, True)

        # Third attempt. A person with almost same name and same
        # national_id.

        obj.national_id = "680601 053-29"
        obj.first_name = "Jean"
        obj.middle_name = "Jacques"
        obj.full_clean()
        obj.save()
        self.assertEqual(obj.national_id, "680601 053-29")
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        result = self.check_json_result(
            response,
            'xcallback success message')
        self.assertEqual(result['success'], True)
        expected = """\
Click OK to apply the following changes for JEFFIN Jean-Jacques (100) :<br/>First name : 'Jean' -> 'Jean-Jacques'
<br/>Middle name : 'Jacques' -> ''"""
        # print(result['message'])
        self.assertEqual(result['message'], expected)


        # Fourth attempt. A person with slightly different name and
        # equivalent but wrongly formatted national_id exists.  Lino
        # does not recognize this duplicate here. To avoid this case,
        # the StrangeClients table warns about wrongly formatted
        # national_id fields.

        Holder.validate_national_id = False

        ssin.parse_ssin('68060105329')
        obj.national_id = "68060105329"
        obj.first_name = "Jean Jacques"
        obj.middle_name = ""
        # obj.client_state = ClientStates.coached
        # obj.update_dupable_words()  # avoid repairable message
        obj.full_clean()
        obj.save()
        self.assertEqual(obj.national_id, "68060105329")
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        # self.assertEqual(response.content, '')
        result = self.check_json_result(
            response,
            'xcallback success message')
        self.assertEqual(result['success'], True)
        expected = "Create new client Jean-Jacques Jeffin : Are you sure?"
        # print(result['message'])
        self.assertEqual(result['message'], expected)

        # test whether we would have been warned:
        obj.update_dupable_words()  # avoid repairable message
        ar = rt.models.checkdata.ProblemsByOwner.request(
            master_instance=obj)
        obj.check_data(fix=False)
        s = ar.to_rst()
        # print(s)
        self.assertEqual(s, """\
*(★) Malformed SSIN '68060105329' must be '680601 053-29'.*
""")

        obj.check_data(fix=True)
        ar = rt.models.checkdata.ProblemsByOwner.request(
            master_instance=obj)
        s = ar.to_rst()
        # print(s)
        self.assertEqual(s, "\n")

        # Last attempt for this card. No similar person exists. Create
        # new client from eid.

        obj.first_name = "Jean-Claude"
        obj.national_id = ""
        obj.full_clean()
        obj.save()
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        # self.assertEqual(response.content, '')
        result = self.check_json_result(
            response,
            'xcallback success message')
        self.assertEqual(result['success'], True)
        expected = "Create new client Jean-Jacques Jeffin : Are you sure?"
        self.assertEqual(result['message'], expected)

        dd.plugins.beid.eidreader_timeout = 1

        # when eidreader is not installed on client, there will be no
        # incoming POST and therefore we will have a timeout.
        post_data['uuid'] = 'foo'  #
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        # self.assertEqual(response.content, '')
        result = self.check_json_result(
            response,
            'alert success message')
        self.assertEqual(result['success'], False)
        self.assertEqual(result['message'], "Abandoned after 1 seconds")

        dd.plugins.beid.eidreader_timeout = 15

        uuid = 'beid_test_0'
        simulate_eidreader(uuid)

        post_data['uuid'] = uuid
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        # self.assertEqual(response.content, '')
        result = self.check_json_result(
            response,
            'alert success message')
        self.assertEqual(result['success'], False)
        self.assertEqual(result['message'], "No card data found: Could not find any reader with a card inserted")



        if True:
            # skip the following tests because we don't yet have
            # test data for the Python eidreader.
            return

        # next card. a foreigner card with incomplete birth date

        post_data.update(card_data=readfile('beid_tests_2.txt'))
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        # self.assertEqual(response.content, '')
        result = self.check_json_result(
            response,
            'xcallback success message')
        self.assertEqual(result['success'], True)
        expected = "Create new client Marc Petitjean : Are you sure?"
        self.assertEqual(result['message'], expected)

        # next card. issued after 2015 and the photo is invalid

        post_data.update(card_data=readfile('beid_tests_3.txt'))
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        # self.assertEqual(response.content, '')
        result = self.check_json_result(
            response,
            'xcallback success message')
        self.assertEqual(result['success'], True)
        expected = "Create new client Bernd Brecht : Are you sure?"
        self.assertEqual(result['message'], expected)

        # next card. issued after 2015 and the photo is valid

        post_data.update(card_data=readfile('beid_tests_4.txt'))
        response = self.client.post(
            url, post_data,
            REMOTE_USER='robin',
            HTTP_ACCEPT_LANGUAGE='en')
        # self.assertEqual(response.content, '')
        result = self.check_json_result(
            response,
            'xcallback success message')
        self.assertEqual(result['success'], True)
        expected = "Create new client Jean Dupont : Are you sure?"
        self.assertEqual(result['message'], expected)

        dd.plugins.beid.simulate_eidreader_path = save_path

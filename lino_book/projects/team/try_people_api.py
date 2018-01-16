from apiclient.discovery import build
from oauth2client.client import OAuth2Credentials
from django.conf import settings
from datetime import datetime
import httplib2

from lino.api import rt


def doit(social):
    print("User {} authenticated by {}".format(
        social.user, social.provider))
    print(social.extra_data)
    # from social_django.utils import load_strategy
    # social = social.user.social_auth.get(provider='google-oauth2')
    # social = social.user.social_auth.get(provider='google-plus')
    # access_token = social.refresh_token(load_strategy())
    # access_token = social.get_access_token(load_strategy())
    # social.refresh_token(load_strategy())
    # print access_token
    # Get required credentials for the current GooglePlus account
    credentials = OAuth2Credentials(
        social.extra_data['access_token'],
        # access_token,
        settings.SOCIAL_AUTH_GOOGLE_PLUS_KEY,
        settings.SOCIAL_AUTH_GOOGLE_PLUS_SECRET,
        social.extra_data.get('refresh_token', ''),
        datetime.fromtimestamp(social.extra_data['auth_time']),
        None,
        'PythonSocialAuth',
        scopes=settings.SOCIAL_AUTH_GOOGLE_PLUS_SCOPE
    )

    # Get the authorized http object from GooglePlus
    http = httplib2.Http()
    http = credentials.authorize(http)

    # Create the People Service
    people_service = build(serviceName='people', version='v1', http=http)
    # Here is an example to retrieve connections (contacts) of my GooglePlus account In the following line,
    # we are selecting the 'names' and the 'emailAddresses' fields of the contact. To select more fields,
    # please refer to the Google documentation at https://developers.google.com/people/api/rest/v1/people
    # connections = people_service.people().connections().list(
    #     resourceName='people/me',
    #     personFields='names,emailAddresses,phoneNumbers').execute()
    # totalItems = connections.get('totalItems', 0)
    # print (totalItems)
    connections = people_service.people().connections().list(
        resourceName='people/me',
        # pageSize=totalItems,
        pageSize=2000,
        personFields='names,emailAddresses,phoneNumbers').execute()
    print ("User {0} have {1} connections.".format(social.user, len(connections.get('connections', ''))))
    all_contacts = connections.get('connections', [])
    print ("Name            email   ")
    # Showing all the contacts we get.
    for i, contact in enumerate(all_contacts):
        names = contact.get('names', [])
        names = ', '.join([n.get('displayName', '') for n in names])
        s = names
        for fld in ('emailAddresses', 'phoneNumbers'):
            values = []
            for a in contact.get(fld, []):
                value = a.get('value', '')
                _type = a.get('type', '')
                if _type:
                    value = '{0} ({1})'.format(value, _type)
                values.append(value)
            if len(values):
                s += ', ' + ', '.join(values)
        print("[{}] {}".format(i, s))
        # print ("{0}: {1}".format(fld, s))
        # print(contact.keys())


if __name__ == '__main__':
    for sa in rt.models.social_django.UserSocialAuth.objects.filter(
            provider="google-plus"):
        doit(sa)

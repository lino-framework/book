from apiclient.discovery import build
from oauth2client.client import OAuth2Credentials
from django.conf import settings
from datetime import datetime
import httplib2

from lino.api import rt


def doit(social):
    print("User {} authenticated by {}".format(
        social.user, social.provider))
    # print(social.extra_data)
    # Get required credentials for the current GooglePlus account
    credentials = OAuth2Credentials(
        social.extra_data['access_token'],
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
    # please refer to the Google documentation , https://developers.google.com/people/api/rest/v1/people
    connections = people_service.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses').execute()
    print ("User {0} have {1} connections.".format(social.user, len(connections.get('connections', ''))))
    all_contacts = connections.get('connections', [])
    print ("Name            email   ")
    # Showing all the contacts we get.
    for contact in all_contacts:
        emailAddresses = contact.get('emailAddresses', False) and contact.get('emailAddresses', [])[0].get('value',
                                                                                                           '') or ''
        contact_name = contact.get('names', False) and contact.get('names', False)[0].get('displayName', '') or ''
        print ("{0}            {1}".format(contact_name, emailAddresses))


if __name__ == '__main__':
    for sa in rt.models.social_django.UserSocialAuth.objects.filter(
            provider="google-plus"):
        doit(sa)

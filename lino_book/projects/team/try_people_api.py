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
    revoke_uri = None
    user_agent = 'PythonSocialAuth'

    credentials = OAuth2Credentials(
        social.extra_data['access_token'],
        settings.SOCIAL_AUTH_GOOGLE_PLUS_KEY,
        settings.SOCIAL_AUTH_GOOGLE_PLUS_SECRET,
        social.extra_data.get('refresh_token', ''),
        datetime.fromtimestamp(social.extra_data['auth_time']),
        revoke_uri,
        user_agent,
        scopes=settings.SOCIAL_AUTH_GOOGLE_PLUS_SCOPE
    )

    http = httplib2.Http()
    http = credentials.authorize(http)

    people_service = build(serviceName='people', version='v1', http=http)
    connections = people_service.people().connections().list(
        resourceName='people/me',
        pageSize=10,
        personFields='names,emailAddresses').execute()
    print ("User {0} have {1} connections.".format(social.user, len(connections.get('connections',''))))
    print (connections.get('connections',''))


if __name__ == '__main__':

    googleplus_users = rt.models.social_django.UserSocialAuth.objects.get(
        provider='google-plus')
    googleplus_users = type(googleplus_users) == list and googleplus_users or [googleplus_users]
    for sa in googleplus_users:
        doit(sa)

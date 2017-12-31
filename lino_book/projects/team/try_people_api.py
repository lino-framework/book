from apiclient.discovery import build
from oauth2client.client import OAuth2Credentials
from django.conf import settings
from datetime import datetime
import httplib2

from lino.api import rt

def doit(social):
    print()
    print("User {} authenticated by {}".format(
        social.user, social.provider))
    print(social.extra_data)
    # response = requests.get(
    #     'https://www.googleapis.com/plus/v1/people/me/people/collection',
    # 'https://www.googleapis.com/plus/v1/people/me/people/visible',
    # params={'access_token': social.extra_data['access_token']}
    # )
    # friends = response.json()['items']
    # print(friends)
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

    # contactToUpdate = people_service.people().get(resourceName=social.extra_data['user_id'],personFields='names,emailAddresses').execute()
    print (connections)


if __name__ == '__main__':
    
    # user = rt.models.users.User.objects.get(username='8618a3571d8b4237a3e60d25671d8f')
    # social = user.social_auth.get(provider='google-plus')
    for sa in rt.models.social_django.UserSocialAuth.objects().get(
            provider='google-plus'):
        doit(sa)

    

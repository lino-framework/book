import requests
from apiclient.discovery import build


from lino.api import rt

user = rt.models.users.User.objects.get(username='luc')
social = user.social_auth.get(provider='google-plus')
print(social.provider)
response = requests.get(
    'https://www.googleapis.com/plus/v1/people/me/people/collection',
    # 'https://www.googleapis.com/plus/v1/people/me/people/visible',
    params={'access_token': social.extra_data['access_token']}
)
friends = response.json()['items']
print(friends)

people_service = build(serviceName='people', version='v1', http=http)

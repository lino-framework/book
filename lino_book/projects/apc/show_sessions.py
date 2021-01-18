from lino.api.shell import *
from django.utils import timezone
from lino.core.auth import SESSION_KEY

qs = sessions.Session.objects.filter(expire_date__gt=timezone.now())
user_ids = dict()
keys = set()
for ses in qs:
  data = ses.get_decoded()
  keys |= data.keys()
  pk = data.get(SESSION_KEY, None)
  count = user_ids.get(pk, 0)
  user_ids[pk] = count + 1
for pk, count in user_ids.items():
  if pk is None:
    user = "Anonymous"
  else:
    user = users.User.objects.get(pk=pk)
  print("User {} has {} active sessions".format(user, count))

expired = sessions.Session.objects.filter(expire_date__lt=timezone.now()).count()
eternal = sessions.Session.objects.filter(expire_date__isnull=True).count()
print("Total {} expired and {} active sessions, {} users".format(
    expired, qs.count(), len(user_ids)))
#print(data.keys())
print("Keys:", keys)
if eternal > 0:
    print("Oops, there are {} eternal sessions".format(eternal))

#!/usr/bin/env python
# To use this,you need to install line_profiler
# pip install line_profiler
# Add @profile to to method we need to profile.
# And run kernprof -lv lino_profiler.py


import os
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'lino_book.projects.team.settings.demo'
)
import django
django.setup()
from lino.api.doctest import *
from django.core.servers.basehttp import get_internal_wsgi_application
from django.test.client import RequestFactory
user = rt.models.users.User.objects.get(username="robin")
# from lino.modlib.extjs.views import AdminIndex

request_factory = RequestFactory()
# user = User.objects.get()
request = request_factory.get('/')
request.session = {}
request.user = user
request._cached_user = user

app = get_internal_wsgi_application()
app.get_response(request)

# view = AdminIndex.as_view()
# view(request).render()
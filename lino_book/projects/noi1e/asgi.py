import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lino_book.projects.noi1e.settings.demo")

channel_layer = get_channel_layer()

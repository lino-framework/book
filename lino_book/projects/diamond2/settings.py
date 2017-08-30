INSTALLED_APPS = ['lino_book.projects.diamond2.main']
SECRET_KEY = "20227"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory'
    }
}

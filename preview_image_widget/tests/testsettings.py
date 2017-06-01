DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = "r4dy"

INSTALLED_APPS = [
    'preview_image_widget'
]

MIDDLEWARE_CLASSES = []

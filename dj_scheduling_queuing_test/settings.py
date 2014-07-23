ALLOWED_HOSTS = [
    '*',
]

# settings.DATABASES is improperly configured. Please supply the ENGINE value. Check settings documentation for more details.
DATABASES = {
    # You must define a 'default' database
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dj_scheduling_queuing_test.db',
    }
}

# You must set settings.ALLOWED_HOSTS if DEBUG is False.
DEBUG = True

INSTALLED_APPS = (
)

MIDDLEWARE_CLASSES = (
)

# 'Settings' object has no attribute 'ROOT_URLCONF'
ROOT_URLCONF = 'dj_scheduling_queuing_test.urls'

# The SECRET_KEY setting must not be empty.
SECRET_KEY='ZU_hds)oM$%cn$Z8%88x%97Wjx2;8`'

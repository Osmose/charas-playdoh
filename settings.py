# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *

# Logging
SYSLOG_TAG = "http_app_charas"  # Make this unique to your project.


# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'common': (
            'css/bootstrap.css',
            'css/layout.css',
            'css/charas.css',
        ),
        'home': (
            'css/slide_pagination.css',
        ),
        'generators': (
            'css/app.css',
            'css/generators.css',
        ),
        'resources': (
            'css/app.css',
            'css/resources.css',
        ),
    },
    'js': {
        'common': (
            'js/libs/jquery-1.6.3.js',
            'js/libs/bootstrap-tabs.js',
            'js/libs/bootstrap-dropdown.js',
            'js/utils.js',
        ),
        'home': (
            'js/libs/slides.jquery.js',
            'js/home.js',
        ),
        'generators': (
            'js/libs/ICanHaz.js',
            'js/libs/base64.js',
            'js/libs/canvas2image.js',
            'js/generators.js',
        ),
        'resources': (
            'js/libs/ICanHaz.js',
            'js/libs/signals.js',
            'js/libs/crossroads.js',
            'js/libs/hasher.js',
            'js/query.js',
            'js/resources.js',
        ),
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


INSTALLED_APPS = list(INSTALLED_APPS) + [
    'charas_project',
    'generators',
    'resources',
    'users',
    'tastypie',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
]

# Upload settings
def gen_resource_path(instance, filename):
    part = instance.part
    gen = part.generator

    return 'uploads/generators/%s/%s/%s' % (gen.slug, part.slug, filename)

def cr_resource_path(instance, filename):
    maker = instance.category.maker
    category = instance.category.slug

    return 'uploads/complete_resources/%s/%s/%s' % (maker, category, filename)

GENERATOR_RESOURCE_PATH = gen_resource_path
CR_RESOURCE_PATH = cr_resource_path
FRONT_PAGE_FEATURE_PATH = 'uploads/frontpage/%Y/%m'
MAX_FILEPATH_LENGTH = 100

# Add Jingo loader
TEMPLATE_LOADERS = [
    'jingo.Loader',
] + list(TEMPLATE_LOADERS)

JINGO_EXCLUDE_APPS = [
    'admin',
]

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]

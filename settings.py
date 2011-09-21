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
        'generators': (
            'css/generators.css',
        ),
    },
    'js': {
        'common': (
            'js/libs/jquery-1.6.3.js',
            'js/libs/bootstrap-tabs.js',
            'js/libs/bootstrap-dropdown.js',
        ),
        'generators': (
            'js/libs/ICanHaz.js',
            'js/libs/base64.js',
            'js/libs/canvas2image.js',
            'js/generators.js',
        ),
    }
}


INSTALLED_APPS = list(INSTALLED_APPS) + [
    'charas_project',
    'generators',
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

GENERATOR_RESOURCE_PATH = gen_resource_path
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

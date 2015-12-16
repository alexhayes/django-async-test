# -*- coding: utf-8 -*-
"""
    module.name
    ~~~~~~~~~~~~~~~
    Preamble...
"""
from __future__ import absolute_import, print_function, unicode_literals
import json

# TEST SETTINGS
import random

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Django replaces this, but it still wants it. *shrugs*
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django_async_test.tests.testapp',
)

MIDDLEWARE_CLASSES = {}

SECRET_KEY = '53cr3773rc3553cr3773rc3553cr3773rc3553cr3773rc35'

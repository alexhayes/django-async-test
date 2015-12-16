#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_async_test.tests.testapp.settings")

def runtests():
    argv = sys.argv[:1] + ['test', 'django_async_test.tests'] + sys.argv[1:]
    execute_from_command_line(argv)

runtests()

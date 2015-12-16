# -*- coding: utf-8 -*-
"""asyncio unit tests with Django transactional support."""
# :copyright: (c) 2015 Alex Hayes and individual contributors,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.


from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info_t(0, 1, 6, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/django-async-test'
__docformat__ = 'restructuredtext'

# -eof meta-

from .testcase import DjangoAsyncTestCase

# Import all of asynctest
from asynctest.case import *
from asynctest.mock import *
from asynctest.helpers import *
from asynctest.selector import *

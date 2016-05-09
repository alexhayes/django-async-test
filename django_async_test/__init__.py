# -*- coding: utf-8 -*-
"""asyncio unit tests with Django transactional support."""
# :copyright: (c) 2015 Alex Hayes and individual contributors,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.


from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info_t(0, 2, 2, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/django-async-test'
__docformat__ = 'restructuredtext'

# -eof meta-

# Import all of asynctest
from asynctest.case import *
from asynctest.mock import *
from asynctest.helpers import *
from asynctest.selector import *

# Now import our TestCase
from .testcase import TestCase

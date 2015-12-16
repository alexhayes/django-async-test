# -*- coding: utf-8 -*-
"""
    django_async_test.testcase
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Internal module reference for ``django_async_test.testcase``.


"""
import asyncio
from asynctest import TestCase as AsyncTestCase
from django.test import TestCase as DjangoTestCase


class TestCase(DjangoTestCase, AsyncTestCase):
    """
    A testcase that wraps `django.test.TestCase`_ and `asynctest.TestCase`_.

    .. _django.test.TestCase: https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.TestCase
    .. _asynctest.TestCase: http://asynctest.readthedocs.org/en/latest/asynctest.case.html#asynctest.TestCase
    """

    def __init__(self, methodName='runTest', *args, **kwargs):
        self._origTestMethodName = getattr(self, methodName)
        AsyncTestCase.__init__(self, methodName='_run_test_method',  *args, **kwargs)
        DjangoTestCase.__init__(self, methodName='_run_test_method', *args, **kwargs)

    def setUp(self):
        """
        Override setup method.

        Note that ``asynctest`` supports ``setUp`` as a coroutine however 
        :py:class:`django_async_test.TestCase` instead supports a
        ``setUpAsync`` method.
        """
        DjangoTestCase.setUp(self)

        self._init_loop()
        self.addCleanup(self._unset_loop)

        setUpAsync = getattr(self, 'setUpAsync', None)
        if setUpAsync is not None:
            if asyncio.iscoroutinefunction(setUpAsync):
                self.loop.run_until_complete(setUpAsync())
            else:
                setUpAsync()

        # don't take into account if the loop ran during setUp
        self.loop.__asynctest_ran = False

    def tearDown(self):
        """
        Override tearDown method.
        
        Note that ``asynctest`` supports ``tearDown`` as a coroutine however
        :py:class:`django_async_test.TestCase` instead supports a
        `tearDownAsync`` method.
        """
        tearDownAsync = getattr(self, 'tearDownAsync', None)
        if tearDownAsync is not None:
            if asyncio.iscoroutinefunction(tearDownAsync):
                self.loop.run_until_complete(tearDownAsync())
            else:
                tearDownAsync()

        DjangoTestCase.tearDown(self)

    def run(self, result=None):
        """
        Call `django.test.TestCase`_'s ``run`` method.

        .. _django.test.TestCase: https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.TestCase
        """
        return DjangoTestCase.run(self, result)

    def _run_test_method(self):
        return AsyncTestCase._run_test_method(self, self._origTestMethodName)



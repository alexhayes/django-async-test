# -*- coding: utf-8 -*-
"""
    django_async_test.tests.testcase
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for :py:class:`django_async_test.TestCase`.

"""
import unittest

from django.test import TestCase

from django_async_test.tests.testapp.models import ModelWithBasicField


class TestCaseTestCase(TestCase):

    def assertTests(self, tests):
        suite = unittest.TestSuite()
        suite.addTests(tests)
        result = unittest.TestResult()
        suite.run(result)

        if len(result.errors) > 0:
            for testcase, traceback in result.errors:
                print(traceback)

        if len(result.failures) > 0:
            for testcase, traceback in result.failures:
                print(traceback)

        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)

    def test_transaction_support(self):
        """
        Test transaction support of :py:class:`django_async_test.TestCase`.
        """
        from django_async_test.tests.testapp.util import DummyTestCase

        self.assertTests([
            DummyTestCase('test_transaction_support'),
            DummyTestCase('test_transaction_support')]
        )

        self.assertEqual(ModelWithBasicField.objects.count(), 0)

    def test_coroutine(self):
        """
        Test coroutine support of :py:class:`django_async_test.TestCase`.
        """
        from django_async_test.tests.testapp.util import DummyTestCase

        self.assertTests([DummyTestCase('test_coroutine')])

    def test_transactional_coroutine(self):
        """
        Test transactional coroutine support of :py:class:`django_async_test.TestCase`..
        """
        from django_async_test.tests.testapp.util import DummyTestCase

        self.assertTests([
            DummyTestCase('test_transactional_coroutine'),
            DummyTestCase('test_transactional_coroutine')]
        )

        self.assertEqual(ModelWithBasicField.objects.count(), 0)

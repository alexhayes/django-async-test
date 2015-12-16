# -*- coding: utf-8 -*-
"""
    module.name
    ~~~~~~~~~~~~~~~
    Preamble...
"""
from __future__ import absolute_import, print_function, unicode_literals

import django_async_test
from django_async_test.tests.testapp.models import ModelWithBasicField


async def ping(pong):
    return pong


async def create(name):
    return ModelWithBasicField.objects.create(name=name)


class DummyTestCase(django_async_test.TestCase):
    """
    A dummy test case that is used to test the behaviour of TestCase.
    """

    @django_async_test.ignore_loop
    def test_transaction_support(self):
        ModelWithBasicField.objects.create(name='asdf')
        self.assertEqual(ModelWithBasicField.objects.count(), 1)

    async def test_coroutine(self):
        expected = 'Hello'
        actual = await ping(expected)
        self.assertEqual(actual, expected)

    async def test_transactional_coroutine(self):
        expected = 'Hello'
        actual = await create(expected)
        self.assertEqual(actual.name, expected)

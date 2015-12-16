=================
django-async-test
=================

`asyncio`_ unit tests with `Django`_ transactional support.

It supports Django 1.8+ for Python versions 3.5+ and uses `asynctest`_ under the
covers to provide support for easily mocking coroutines.

.. image:: https://travis-ci.org/alexhayes/django-async-test.png?branch=master
    :target: https://travis-ci.org/alexhayes/django-async-test
    :alt: Build Status

.. image:: https://landscape.io/github/alexhayes/django-async-test/master/landscape.png
    :target: https://landscape.io/github/alexhayes/django-async-test/
    :alt: Code Health

.. image:: https://codecov.io/github/alexhayes/django-async-test/coverage.svg?branch=master
    :target: https://codecov.io/github/alexhayes/django-async-test?branch=master
    :alt: Code Coverage

.. image:: https://readthedocs.org/projects/django-async-test/badge/
    :target: http://django-async-test.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/django-async-test.svg
    :target: https://pypi.python.org/pypi/django-async-test
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/django-async-test.svg
    :target: https://pypi.python.org/pypi/django-async-test/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/dd/django-async-test.svg
    :target: https://pypi.python.org/pypi/django-async-test/
    :alt: Downloads


Docs
====

Available at `django-async-test.readthedocs.org`_


Installation
============

You can install django-async-test either via the Python Package Index (PyPI)
or from github.

To install using pip;

.. code-block:: bash

    $ pip install django-async-test

From github;

.. code-block:: bash

    $ pip install git+https://github.com/alexhayes/django-async-test.git


Usage
=====

`asynctest.TestCase`_ does a great job of mocking coroutines however if you're
writing tests that manipulate the database in Django you'll most likely want to
ensure that things are cleaned up after your test.

With ``django_async_test.TestCase`` you have the coroutine support of
`asynctest.TestCase`_ but with the transaction support of Django's
`django.test.TestCase`_.

.. code-block:: python

    import django_async_test

    class MyTestCase(django_async_test.TestCase):

        @django_async_test.patch('myapp.my_coroutine')
        def test_foo(self, MockMyCoroutine):

            # Mock our coroutine.
            MockMyCoroutine.return_value = 'Hello World'

            # Create an instance of MyModel
            MyModel.objects.create(...)

            ...
            ...


In the above example, the test is run inside a transaction by Django's TestCase,
thus the creation of a MyModel will be rolled back, cleaning up the database.

Also, our co-routine will be patched correctly by asynctest.


License
=======

This software is licensed under the `MIT License`. See the LICENSE_ file.


Author
======

Alex Hayes <alex@alution.com>

.. _Django: https://www.djangoproject.com/
.. _LICENSE: https://github.com/alexhayes/django-async-test/blob/master/LICENSE
.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _asynctest: https://pypi.python.org/pypi/asynctest
.. _django-async-test.readthedocs.org: http://django-async-test.readthedocs.org/en/latest/
.. _django.test.TestCase: https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.TestCase
.. _asynctest.TestCase: http://asynctest.readthedocs.org/en/latest/asynctest.case.html#asynctest.TestCase

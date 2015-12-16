=====
Usage
=====

`asynctest.TestCase`_ does a great job of mocking coroutines however if you're
writing tests that manipulate the database in Django you'll most likely want to
ensure that things are cleaned up after your test.

With ``django_async_test.TestCase`` you have the coroutine support
of `asynctest`_ combined with the transaction support of Django's
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


In the above example, the test is run inside a transaction by Django's
`django.test.TestCase`_, thus the creation of a MyModel will be rolled back,
cleaning up the database.

Also, our co-routine will be patched correctly by asynctest.

Note that decorated ``@django_async_test.patch`` above actually comes from
``asynctest`` however to avoid the extra import ``django_async_test`` imports
``asynctest.*`` into it's namespace.


========================
Differences to asynctest
========================

`asynctest`_ supports the use of ``setUp`` and ``tearDown`` methods as
coroutines in your ``TestCase``. ``django-async-test`` does not support this,
instead if you can define a ``setUpAsync`` and/or ``tearDownAsync`` method that
will be called.

This package is mostly just an integration wrapper between Django and
asynctest, you should `read the asynctest docs`_.


.. _asynctest: https://github.com/Martiusweb/asynctest
.. _asynctest.TestCase: http://asynctest.readthedocs.org/en/latest/asynctest.case.html#asynctest.TestCase
.. _django.test.TestCase: https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.TestCase
.. _read the asynctest docs: http://asynctest.readthedocs.org

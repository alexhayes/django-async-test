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

.. image:: https://readthedocs.org/projects/django-async-test/badge/?version=latest
    :target: http://django-async-test.readthedocs.org/en/latest/?badge=latest
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



Contents
--------

.. toctree::
 :maxdepth: 1

 installation
 usage
 developer
 internals/reference/index

License
-------

This software is licensed under the `MIT License`. See the `LICENSE`_.

Author
------

Alex Hayes <alex@alution.com>

.. _Django: https://www.djangoproject.com/
.. _Models: https://docs.djangoproject.com/en/stable/topics/db/models/
.. _LICENSE: https://github.com/alexhayes/django-async-test/blob/master/LICENSE
.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _asynctest: https://pypi.python.org/pypi/asynctest

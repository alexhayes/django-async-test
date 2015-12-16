Developer Documentation
=======================

Contributions
-------------

Contributions are more than welcome!

To get setup do the following;

.. code-block:: bash

    mkvirtualenv --python=/usr/bin/python3.5 django-async-test
    git clone https://github.com/alexhayes/django-async-test.git
    cd django-async-test
    pip install -r requirements/dev.txt


Running Tests
-------------

Once you've checked out you should be able to run the tests.

.. code-block:: bash

    tox


Creating Documentation
----------------------

.. code-block:: bash

    cd docs
    make clean html


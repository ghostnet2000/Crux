=============================
Third-party services examples
=============================
Third-party services examples.

Installation
============
Python packages
---------------
Install all dependencies:

.. code-block:: sh

    pip install -r requirements/dev.txt

Local development
=================
For local development, you will need the following.

**Run the local/dev server**

First terminal tab:

.. code-block:: sh

    ./manage.py runserver --traceback -v 3

Running the project
===================

First create the database if not yet created.

.. code-block:: sh

    ./manage.py migrate

Then run the server (on port 8001):

.. code-block:: sh

    ./manage.py runserver 0.0.0.0:8001 --traceback -v 3

You may now open the `http://localhost:8001/api/sms/` URL in your browser and
submit a couple of SMS messages (browsable API).

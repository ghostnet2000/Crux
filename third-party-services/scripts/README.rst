Scripts
=======
Various developer helper (shell) scripts. For development environment only.
Don't use them in production.

Prior running any of those, please install the project requirements.

.. code-block:: sh

    pip install -r requirements.txt

celery_start.sh
---------------
Start the Celery.

clean_up.sh
-----------
Removes temporary files, compiled python files, log files.

collectstatic.sh
----------------
Collect the project static.

flower_start.sh
---------------
Starts the flower (Celery task GUI and management tool).

install.sh
----------
Installs (Python) requirements, collects statics, runs migrations.

pycodestyle.sh
--------------
Checks the project code using ``pycodestyle`` package.

pylint.sh
---------
Checks the project code using ``pylint`` package.

runserver.sh
------------
Shortcut for running the Django dev server from current directory.

shell.sh
--------
Shortcut for running the Django dev shell from current directory.

test.sh
-------
Shortcut for running the tests using Django's test runner.

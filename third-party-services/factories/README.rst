Factories
=========
Project dummy data (dynamic fixtures). Extremely useful if you want to test
your application on a large data set (which you don't have or difficult to
recreate each time for each developer).

Usage examples
--------------
**Create a single ``SMSMessage`` instance**

.. code-block:: python

    import factories

    sms_message = factories.SMSMessageFactory()

**Create many (100) ``SMSMessage`` instances**

.. code-block:: python

    import factories

    sms_messages = factories.SMSMessageFactory.create_batch(100)

**Create a single ``SMSMessageFactory`` instance with pre-defined attributes**

.. code-block:: python

    sms_message = factories.SMSMessageFactory(
        recipient="+1234",
        sender="+5678",
        message="Lorem ipsum dolor sit amet."
    )

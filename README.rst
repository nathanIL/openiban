OpenIBAN - Python IBAN library
===============================

OpenIBAN is a generic library for interacting with various (currently only `openiban.com <https://openiban.com/>`_) IBAN
providers.

Off line IBAN validation

.. code-block:: python

    from openibanlib import openiban
    # By trying to initialize an IBAN object
    >>> try:
            openiban.IBAN('DE89370400440532013000')
        except IBANFormatValidationException:
            print("Invalid IBAN provided")
    # Or using a static method
    >>> openiban.IBAN.format_validate('DE89370400440532013000')
    True
    ...

On line (using an IBAN provider) validation

.. code-block:: python

    from openibanlib.providers.OpenIBAN import OpenIBAN
    ...
    
Installation
------------

To install simply (coming soon):

.. code-block:: bash

    $ pip install openiban-lib

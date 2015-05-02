'''
Created on Apr 30, 2015

@author: nabu
'''

class IBANValidationException(Exception):
    """
        Base class for IBAN validation exceptions
    """
    pass


class IBANFormatValidationException(IBANValidationException):
    """
        Raised when the IBAN validation fails
    """
    pass


class IBANConnectionTypeException(Exception):
    """
        Raised when an invalid connection type is provided
    """
    pass
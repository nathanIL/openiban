'''
Created on Apr 30, 2015

@author: nabu
'''

from openibanlib.exceptions import IBANFormatValidationException
import re


class IBAN(object):
    """
     A class for representing an IBAN
    """
    
    def __init__(self,v):
        """
            We Perform a non-costly offline IBAN validation here.
            A more serious validation is performed by the required service provider
        """
        if (self.__class__.format_validate(v)):
            self._iban = v
        else:
            raise IBANFormatValidationException("Invalid IBAN format provided: %s" % v)
    
    def __str__(self):
        """
            We are simply wrapping a str, so we delegate to str's __str__()
        """
        return str(self._iban)
    
    def __hash__(self):
        """
            We are simply wrapping a str, so we delegate to str's __hash__()
        """
        return hash(self._iban)
    
    def __eq__(self,other):
        return self.__hash__() == other.__hash__()
    
    @staticmethod
    def format_validate(ibn):
        """
            Basic IBAN validation based on: http://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
            this is before we actually send the IBAN over the network wire.
            Skipping the length part since we dont want to hardcode country specific lengths (its somewhat ugly).
        """
        def converter(c):
            if re.match("[A-Z]", c, re.IGNORECASE):
                return ord(c) - 55
            else:
                return c
        
        integered = int(''.join( [ str(v) for v in map( converter , ibn[4:] + ibn[0:4]) ] ))
        return integered % 97 == 1

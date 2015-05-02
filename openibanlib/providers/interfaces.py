'''
Created on Apr 30, 2015

@author: nabu
'''

import abc
from abc import abstractmethod
from openibanlib.exceptions import IBANConnectionTypeException
from openibanlib.openiban import IBAN

import requests_cache
requests_cache.install_cache()
import requests


class ConnectionType(object):
    """
        A class acting as an enum for HTTP protocol types (secured / non secured) used in 
        IBANProvier
    """
    HTTP  = 0
    HTTPS = 1

class IBANProvider():
    """
        A contract / abc for all IBAN service provider classes 
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, connection_type=ConnectionType.HTTP, requests_package=requests):
        """
            :param connection_type: The connection type for the 'requests_package' package
            :param requests_package: request package. defaults to 'requests'. mainly used for mocks injection
        """
        
        self.connection_type = connection_type
        self._requests_package = requests_package        
        
        if self.connection_type == ConnectionType.HTTP:
            self.PROVIDER_URL = self.PROVIDER_URL.replace("https:","http:",1)
        elif self.connection_type == ConnectionType.HTTPS:
            self.PROVIDER_URL = self.PROVIDER_URL.replace("http:","https:",1)

    @property
    def connection_type(self):
        return self._connection_type
    

    @connection_type.setter
    def connection_type(self,v):
        """
            ConnectionType type setter
            
            :param v: connection type based on ConnectionType
        """
        if filter( lambda a: getattr(ConnectionType, a) == v , dir(ConnectionType) ):
            self._connection_type = v
        else:
            raise IBANConnectionTypeException("Invalid connection type supplied")
    

    @abstractmethod
    def _validate(self,response):
        """
            Abstract method which validates the specific IBAN provider response
            Abstract method that parses the specific IBAN provider response (requests.Response object) and gets the data
            :param response: requests.Response object
            :returns: True if ok, False otherwise
        """
        pass

    @abstractmethod
    def _prepare_url(self,ibn):
        """
            Abstract method which prepares the URL for the HTTP request using PROVIDER_URL
            :param ibn: IBAN number
            :returns: the prepared and ready-to-use URL
        """
        pass

    @abstractmethod
    def _request_params(self):
        """
            Abstract method which provides the request params.
            :returns: a dict with the required params as per requests.get(,...)
        """
        pass

    @abstractmethod
    def _parse_bank_data(self,response):
        """
            Abstract method that parses the specific IBAN provider response (requests.Response object) and gets the data
            :param response: requests.Response object
            :returns: a dict containing the bank data
        """
        pass


    def _make_request(self,ibn):
        return self._requests_package.get( self._prepare_url( str(IBAN(ibn)) ), **self._request_params() )
      
            
    def get_bank_data(self,ibn):
        """
            Gets the bank data for that IBAN
            Returns a dict
        """
        return self._parse_bank_data( self._make_request(ibn) )
    
    def is_iban_valid(self,ibn):
        """
            Validates the provided IBAN
        """
        return self._validate( self._make_request(ibn) )
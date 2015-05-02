'''
Created on May 1, 2015

@author: nabu
'''

from openibanlib.providers.OpenIBAN import OpenIBAN
import openibanlib.providers.interfaces
import unittest
import requests
import requests_mock
import json
import os

TESTS_DIR=os.path.join( os.path.abspath(os.curdir), 'tests' )

class OpenIBANTest(unittest.TestCase):
    '''
        Test class for openibanlib.providers.OpenIBAN.OpenIBAN
    '''
    
    def _load_responses(self):
        responses_dir = os.path.join( TESTS_DIR, 'responses' )
        response_files = list()
                
        for dirpath, dirnames, filenames in filter( lambda e: e[0].endswith('openiban'), os.walk(responses_dir) ):
            response_files.extend( map( lambda e: os.path.join(dirpath,e), filenames ) )
        
        self._json_responses = list()
        for reponse_json in response_files:
            with open(reponse_json) as json_file:
                self._json_responses.append( json.load(json_file) )
        
        
                
    def setUp(self):
        self._load_responses()
        openibanlib.providers.interfaces.requests_cache.uninstall_cache()
    
        
    def _test_iban_param(self,method):
        
        with requests_mock.Mocker() as mock:
            oi = OpenIBAN()
            for json_response in self._json_responses:
                mock.register_uri('GET', oi._prepare_url(json_response['iban']), json=json_response )
        
            for json_response in self._json_responses:
                yield getattr(oi, method)( json_response['iban'] )        
    
    
    def test_is_iban_valid(self):
        """
            Check the return value of is_iban_valid method.
            Basically, all the .json reponses we have for this test case are True
        """
        for boolean_result in self._test_iban_param('is_iban_valid'):
            self.assertTrue(boolean_result, "Checking if IBAN is True (valid)")
    
    
    def test_get_bank_data(self):
        """
            We test only if bankCode key is in the result dict for now
        """
        for dict_result in self._test_iban_param('get_bank_data'):
            self.assertTrue('bankCode' in dict_result, "Checking if bankCode key in result")


if __name__ == "__main__":
    unittest.main()
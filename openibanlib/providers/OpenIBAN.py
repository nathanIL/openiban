'''
Created on Apr 30, 2015

@author: nabu
'''
from openibanlib.providers.interfaces import IBANProvider


class OpenIBAN(IBANProvider):
    """
        OpenIBAN provider: https://openiban.com/
    """
    PROVIDER_URL = "https://openiban.com/validate/XXXXXXXX?getBIC=true"
    
    def _request_params(self):
        return dict()

    def _validate(self,response):
        json = response.json()
        if 'valid' in json:
            return json['valid']
    
    def _parse_bank_data(self, response):
        json = response.json()
        if 'bankData' in json:
            return json['bankData']
    
    def _prepare_url(self,ibn):
        return self.PROVIDER_URL.replace( 'XXXXXXXX', ibn )
'''
Created on Apr 30, 2015

@author: nabu
'''

from openibanlib import openiban
import unittest

class IBANTest(unittest.TestCase):
    """
        Test class for openibanlib.openiban.IBAN
    """
    def setUp(self):
        self._iban_list = tuple([ { 'number': 'GB82WEST12345698765432', 'valid': True },
                                  { 'number': 'GB82WEST12345698745432', 'valid': False },
                                  { 'number': 'AL47212110090000000235698741', 'valid': True },
                                  { 'number': 'PS92PALS000000000400123456702', 'valid': True },
                                  { 'number': 'DE89370400440532013000', 'valid': True },
                                  { 'number': 'IT60X0542811101000000123456', 'valid': True },
                                  { 'number': 'ZT50X0542811101000000123456', 'valid': False },
                                  { 'number': 'DE89370400440532013000', 'valid': True },
                                  { 'number': 'IL620108000000099999499', 'valid': False },
                                  { 'number': 'IL620108000000099999999', 'valid': True } ])
    
    def test_format_validate(self):
        for iban_test in self._iban_list:
            self.assertEqual( openiban.IBAN.format_validate(iban_test['number']), iban_test['valid'],
                              "Is {0} == {1}".format(iban_test['number'],iban_test['valid']))

    def test_str_(self):
        for iban_test in filter(lambda v: v['valid'] == True, self._iban_list):
            iban = openiban.IBAN(iban_test['number'])
            self.assertTrue( str(iban) == iban_test['number'], "{0} == {1}".format(iban, iban_test['number']) )

    def test_hash_(self):
        iban1 = openiban.IBAN('GB82WEST12345698765432')
        iban2_same_as_iban1 = openiban.IBAN('GB82WEST12345698765432')
        iban3 = openiban.IBAN('DE89370400440532013000')
        
        self.assertEqual( hash(iban1) , hash("GB82WEST12345698765432"), "Testing IBAN hash equality (obj vs str)")
        self.assertEqual( hash(iban1) , hash(iban2_same_as_iban1), "Testing IBAN hash equality (obj vs str)")

    
    def test_eq_(self):
        iban1 = openiban.IBAN('GB82WEST12345698765432')
        iban2_same_as_iban1 = openiban.IBAN('GB82WEST12345698765432')
        iban3 = openiban.IBAN('DE89370400440532013000')
        
        self.assertEqual( iban1 , "GB82WEST12345698765432", "Testing IBAN equality (obj vs str)")
        self.assertEqual( iban1 , iban2_same_as_iban1, "Testing IBAN equality (obj vs obj)")
        self.assertNotEqual(iban1,"DE89370400440532013000","Testing IBAN inequality (obj vs str)")
        self.assertNotEqual(iban1,iban3,"Testing IBAN inequality (obj vs str)")        
        
if __name__ == "__main__":
    unittest.main()
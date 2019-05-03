#Basics of unit testing

import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        result = formatted_name("milan","tripathi")
        self.assertEqual(result,"Milan Tripathi")
        
    def test_first_middle_last_name(self):
        result = formatted_name("milan","abc","tripathi")
        self.assertEqual(result,"Milan Tripathi Abc")
 
if __name__ == '__main__':
    unittest.main()

"""Django test se begin hone wali files search karta hai, isliye name tests.py daala"""
from django.test import TestCase

from app.calc import add

class CalcTests(TestCase):
    
    """Just like file name, django test se start hone wale function bhi search karega isliye function name ki start test se karna mandatory hai!"""
    
    def test_add_numbers(self):
        """Test that two numbers are adding or not"""
        
        self.assertEqual(add(3,8), 11)
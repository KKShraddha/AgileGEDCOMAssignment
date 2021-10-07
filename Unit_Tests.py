import unittest
import sys
from User_Story_Gedcom import validDate

class TestDates(unittest.TestCase):
    def test_success(self):
        result = validDate("7 FEB 1940")
        print("Date is validated properly:",result)
        self.assertTrue(result)
        
        result = validDate("17 AUG 2022")
        print("Date Should be within current date:",result)
        self.assertFalse(result)

        result = validDate("28 SEP 2021")
        print("Date should be in Valid Format: YYYY-MM-DD:",result)
        self.assertTrue(result)

        result = validDate("28 AUG 2800")
        print("No Future Date:",result)
        self.assertFalse(result)

        def test_input_fail(self):
            with self.assertRaises(ValueError): validDate(15)

if __name__ == "__main__":
    unittest.main()
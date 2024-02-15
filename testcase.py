import unittest
from normal_to_roman import normal_to_roman

class TestRomanConverter(unittest.TestCase):
    
    def test_convert_single_digit(self):
        print("Test Convertion of a Single Digit:")
        self.assertEqual(normal_to_roman(1), "I")
        print("Convertion of 1 to Roman:", normal_to_roman(1))
        
        
if __name__ == "__main__":
   unittest.main()
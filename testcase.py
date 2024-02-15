import unittest
from normal_to_roman import normal_to_roman

class TestRomanConverter(unittest.TestCase):
    
    def test_convert_single_digit(self):
        print("Test Convertion of a Single Digit:")
        self.assertEqual(normal_to_roman(1), "I")
        print("Convertion of 1 to Roman:", normal_to_roman(1))
        
        self.assertEqual(normal_to_roman(5), "V")
        print("Convertion of 5 to Roman:", normal_to_roman(5))
        
        self.assertEqual(normal_to_roman(9), "IX")
        print("Convertion of 9 to Roman:", normal_to_roman(9))
        
    def test_convert_double_digit(self):
        print("Test Convertion of double digits:")
        self.assertEqual(normal_to_roman(10), "X")
        print("Convertion of 10 to Roman:", normal_to_roman(10))
        
        self.assertEqual(normal_to_roman(50), "L")
        print("Convertion of 50 to Roman:", normal_to_roman(50))
        
        self.assertEqual(normal_to_roman(99), "XCIX")
        print("Convertion of 99 to Roman:", normal_to_roman(99))
        
    def test_convert_triple_digit(self):
        print("Test Convertion of triple digit:")
        self.assertEqual(normal_to_roman(100), "C")
        print("Convertion of 100 to Roman:", normal_to_roman(100))
        
        self.assertEqual(normal_to_roman(500), "D")
        print("Convertion of 500 to Roman:", normal_to_roman(500))
        
        self.assertEqual(normal_to_roman(999), "CMXCIX")
        print("Convertion of 990 to Roman:", normal_to_roman(999))
          
        
if __name__ == "__main__":
   unittest.main()
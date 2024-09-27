""" Alisa Haniff
    Example 2: calculation testing
"""

import unittest
import calculation

class TestCalculation(unittest.TestCase):
    def test_addThreeNumbers(self):
        self.assertEqual(calculation.addThreeNumbers(1,2,3),6)
        self.assertEqual(calculation.addThreeNumbers(5,3),8)
        self.assertEqual(calculation.addThreeNumbers(9),9)
        self.assertEqual(calculation.addThreeNumbers(),0)
    
    def test_subtractTwoNumbers(self):
        self.assert_subtractTwoNumbers(calculation.subtractTwoNumbers(2,8), -6)
        self.assert_subractTwoNumbers(calculation.subtractTwoNumbers(8,2), 6)
    
    def test_divideTwoNumbers(self):
        self.assert_divideTwoNumbers(calculation.divideTwoNumbers(8,2),4)   
        self.assert_divideTwoNumbers(calculation.divideTwoNumbers(-8,2),-4)  
        self.assert_divideTwoNumbers(calculation.divideTwoNumbers(7,2),3.5)  #float comparison
       
#divison by zero exception
    def test_divideByZero(self):
        self.assertIsNone(calculation.divideTwoNumbers(10,0))
        

# non numeric testing
def test_nonNumericValues(self):
    self.assertIsNone(calculation.divideTwoNumbers("p",2))
    self.assertIsNone(calculation.divideTwoNumbers(10, "n"))    
    
# any other exceptions
def test_unexpected_exception(self):
    with self.assertRaises(Exception):
        calculation.divideTwoNumbers()        
     
     
     
  
        
if __name__=='__main__':
    unittest.main()
            
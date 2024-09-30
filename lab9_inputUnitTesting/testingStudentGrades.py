"""
Alisa HAniff
unit testing student grades
lab 9"""

import unittest
from unittest.mock import patch
import io
import studentgrade_Haniff

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['-1', '2', '85', '72'])
    @patch('sys.stdout', new_callable=io.StringIO)
    
    def test_valid_input(self, mock_stdout, mock_input):
        studentgrade_Haniff.main()
        
        output = mock_stdout.getvalue()
        
        # Check that the output contains the expected average
        self.assertIn("The class average is 83.33", output)
    
    
    def test_invalid_and_value_input(self, mock_stdout, mock_input):
        studentgrade_Haniff.main()
    
        output =mock_stdout.getvalue()    
    
        self.assertIn("Invalid input.\n", output)
        self.assertIn("Enter the number of students: \n", output)
        self.assertIn("Enter a grade for student: \n", output)
        
#test for invalid grade
        
    @patch('builtins.input', side_effect=['2', '105', '-10', '70'])
    @patch('sys.stdout', new_callable=io.StringIO)
    
    def test_invalid_grade(self,mock_stdout, mock_input):
        studentgrade_Haniff.main()
        
        output = mock_stdout.getvalue()
        self.assertIn("Grade must be between 0 and 100.",output)
        self.assertIn("The class average is 76.00", output)
        
        
        # Test for invalid value of input number os students
        
        #test for invalid value of grade
    
if __name__ == "__main__":
    unittest.main()

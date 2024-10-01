"""
Alisa HAniff
unit testing student grades
lab 9"""

import unittest
from unittest.mock import patch
import io
import studentgrade_Haniff

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '85', '82'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        studentgrade_Haniff.main()
        output = mock_stdout.getvalue()
        self.assertIn("The class average is 83.50", output)


    @patch('builtins.input', side_effect=['Peter', '2', '85', '72'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_string_as_students(self, mock_stdout, mock_input):
        studentgrade_Haniff.main()
        output = mock_stdout.getvalue()
        # Update to match the actual output from your script
        self.assertIn("Invalid input. Please enter a valid number of students.", output)

    @patch('builtins.input', side_effect=['2', 'Peter', '85', '72'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_string_as_grade(self, mock_stdout, mock_input):
        studentgrade_Haniff.main()
        output = mock_stdout.getvalue()
        # Update to match the actual output from your script
        self.assertIn("Invalid input. Please enter a valid number for the grade.", output)

    @patch('builtins.input', side_effect=['2', '105', '85', '72'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_grade(self, mock_stdout, mock_input):
        studentgrade_Haniff.main()
        output = mock_stdout.getvalue()
        self.assertIn("Grade must be between 0 and 100.", output)

    @patch('builtins.input', side_effect=['Peter', '-1', '2', '85', '72'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_and_value_input(self, mock_stdout, mock_input):
        studentgrade_Haniff.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter a valid number of students.", output)


if __name__ == "__main__":
    unittest.main()

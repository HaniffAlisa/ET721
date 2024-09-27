"""Alisa Haniff 
Unit Testing for BankAccount
"""
import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Test User", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_withdraw_negative_amount(self):
        # Test attempting to withdraw a negative amount raises a ValueError
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_deposit_negative_amount(self):
        # Test a ValueError
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_sequence_of_transactions(self):
        # Test a sequence of deposits and withdrawals 
        self.account.deposit(100)   # Balance should be 200
        self.account.withdraw(50)   # Balance should be 150
        self.account.withdraw(30)   # Balance should be 120
        self.assertEqual(self.account.get_balance(), 120)

if __name__ == "__main__":
    unittest.main()

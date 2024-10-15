"""Alisa Haniff
Project 2
Connect 4 Unit Testing"""

import unittest
from main import Connect4

class TestConnect4(unittest.TestCase):

    def test_drop_chip_full_board(self):
        game = Connect4()

        for col in range(1, 8):   #fill the entire board goes to 8 so it iterates over column 7
            for _ in range(6):
                game.drop_chip(col)
            game.switch_player() 
        for col in range(1, 8):
            self.assertFalse(game.drop_chip(col))  #columns are full, so all should return False

if __name__ == '__main__':
    unittest.main()


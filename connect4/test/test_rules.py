from connect4 import rules
import unittest


class TestCheckWin(unittest.TestCase):
    def test_check_row_1(self):
        """empty board should return false"""
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.assertEqual(rules.check_row(board, 6, 7), False)

    def test_check_row_2(self):
        """4 in a row on bottom left, should return true"""
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', 'O', 'O', 'O', ' ', ' ', ' ']]
        self.assertEqual(rules.check_row(board, 6, 7), True)

    def test_check_row_3(self):
        """4 in a row bottom right, should return true"""
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', 'O', 'O', 'O']]
        self.assertEqual(rules.check_row(board, 6, 7), True)

    def test_check_col_1(self):
        """4 in a column bottom right, should return true"""
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X']]
        self.assertEqual(rules.check_col(board, 6, 7), True)

    def test_check_col_2(self):
        """sandwiched 3 in a column, should return false"""
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', ' ', ' ', ' ']]
        self.assertEqual(rules.check_col(board, 6, 7), False)


if __name__ == "__main__":
    unittest.main(exit=False)

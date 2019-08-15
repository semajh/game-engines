import unittest
from connect4.engine import cpu


class TestCheckCPU(unittest.TestCase):
    def test_cpu_1(self):
        """
        puzzle to test if cpu will set up fork.
        X wins in 3.
        """
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', 'O', ' ', ' '],
                 [' ', ' ', ' ', 'O', 'X', ' ', 'X'],
                 [' ', ' ', ' ', 'X', 'X', 'X', 'O'],
                 [' ', 'O', ' ', 'X', 'X', 'O', 'O']]
        move, score = cpu(board, "X", 0, 1000)
        self.assertEqual(move, 5)

    def test_cpu_2(self):
        """
        test if cpu will delay inevitable loss
        X wins in 2
        """
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', 'O', ' ', ' '],
                 [' ', ' ', ' ', ' ', 'O', ' ', ' '],
                 [' ', ' ', 'X', ' ', 'X', ' ', ' '],
                 [' ', ' ', 'X', 'X', 'X', 'O', ' '],
                 [' ', 'X', 'O', 'O', 'X', 'O', ' ']]
        move, score = cpu(board, "O", 0, 1000)
        self.assertEqual(move, 1)

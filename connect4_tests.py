import connect4
import unittest


class TestCheckWin(unittest.TestCase):
    def test_check_row_1(self):
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.assertEqual(connect4.check_row(board, 6, 7), False)

    def test_check_row_2(self):
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', 'O', 'O', 'O', ' ', ' ', ' ']]
        self.assertEqual(connect4.check_row(board, 6, 7), True)

    def test_check_row_3(self):
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', 'O', 'O', 'O']]
        self.assertEqual(connect4.check_row(board, 6, 7), True)

    def test_check_col_1(self):
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                 [' ', ' ', ' ', ' ', ' ', ' ', 'X']]
        self.assertEqual(connect4.check_col(board, 6, 7), True)

    def test_check_col_2(self):
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', ' ', ' ', ' ']]
        self.assertEqual(connect4.check_col(board, 6, 7), False)


class TestCheckCPU(unittest.TestCase):
    def test_cpu_1(self):
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'O', 'O', ' ', ' '],
                 [' ', ' ', ' ', 'O', 'X', ' ', 'X'],
                 [' ', ' ', ' ', 'X', 'X', 'X', 'O'],
                 [' ', 'O', ' ', 'X', 'X', 'O', 'O']]
        move, score = connect4.cpu(board, "X", 0, 1000)
        self.assertEqual(move, 5)

    def test_cpu_2(self):
        board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', 'O', ' ', ' '],
                 [' ', ' ', ' ', ' ', 'O', ' ', ' '],
                 [' ', ' ', 'X', ' ', 'X', ' ', ' '],
                 [' ', ' ', 'X', 'X', 'X', 'O', ' '],
                 [' ', ' ', 'O', 'O', 'X', 'O', ' ']]
        move, score = connect4.cpu(board, "X", 0, 1000)
        self.assertEqual(move, 1)


if __name__ == "__main__":
    unittest.main(exit=False)

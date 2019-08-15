import cProfile
from connect4.engine import cpu


def test_1():
    """profile 1st move of engine"""
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    cProfile.runctx("print(cpu(board,'X',0, 1000))",
                    {"board": board, "cpu": cpu}, {})


if __name__ == "__main__":
    test_1()

import cProfile
import connect4


def test_1():
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    cProfile.runctx("print(cpu(board,'X',0, 1000))",
                    {"board": board, "cpu": connect4.cpu}, {})


if __name__=="__main__":
    test_1()
import cProfile
from tictactoe import tictactoe


def test_1():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    cProfile.runctx("print(cpu(board,1,0))",
                    {"board": board, "cpu": tictactoe.AI}, {})


if __name__ == "__main__":
    test_1()

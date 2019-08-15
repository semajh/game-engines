from display import show_board
from engine import cpu
from rules import do_move, check_win, find_moves


def make_move(board, piece, player):
    """Check if player is CPU or human then get input and puts piece"""
    valid = False
    col = -1
    while not valid:
        print()
        print(" player  ", player)
        if "CPU" in player:
            col, score = cpu(board, piece, 0, 100)
            print(col, score)
        else:
            col = int(input("enter the column number: "))
        if board[0][col] == " ":
            valid = True
    # check from bottom up
    board = do_move(board, col, piece)
    return board


def main():
    board = []
    # 6 rows 7 columns
    # 00 01
    # 10 11
    for i in range(6):
        board.append([])
        for j in range(7):
            board[i].append(" ")
    show_board(board)
    player1 = input("player1 name: ")
    player2 = input("player 2 name: ")
    turn = 1
    won = False
    while not won:
        player_turn = turn % 2
        if player_turn == 1:
            player = player1
            piece = "X"
        else:
            player = player2
            piece = "O"
        board = make_move(board, piece, player)
        show_board(board)
        won = check_win(board)
        if won:
            print()
            print(player, "won")
            break
        if len(find_moves(board)) == 0:
            print()
            print("draw")
            break
        turn += 1


if __name__ == "__main__":
    main()

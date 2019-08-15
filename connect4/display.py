def show_board(board):
    print("   ", end="")
    for i in range(7):
        print(i, end="   ")
    print()
    for row in range(6):
        print(row, end="  ")
        for col in range(7):
            print(board[row][col], end=" | ")
        print()
    print()

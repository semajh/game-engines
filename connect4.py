from operator import itemgetter


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


def make_move(board, piece, player):
    valid = False
    col = -1
    while not valid:
        print()
        print(" player  ", player)
        if player == "cpu":
            col, score = cpu(board, piece, 0, 100)
            print(col, score)
        else:
            col = int(input("enter the column number: "))
        if board[0][col] == " ":
            valid = True
    # check from bottom up
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            break
    return board


def check_row(board, num_rows, num_cols):
    # check if 4 in a row is horizontal(in a row)
    won = False
    for row in range(num_rows):
        for col in range(num_cols - 3):
            start = board[row][col]
            if start == " ":
                continue
            won = True
            for i in range(1, 4):
                if start != board[row][col + i]:
                    won = False
                    break

            if won:
                return won
    return won


def check_col(board, num_rows, num_cols):
    # check if 4 in a row is vertical(in a column)
    won = False
    for row in range(num_rows - 3):
        for col in range(num_cols):
            start = board[row][col]
            if start == " ":
                continue
            won = True
            for i in range(1, 4):
                if start != board[row + i][col]:
                    won = False
                    break
            if won:
                return won
    return won


def check_diagonal_down(board, num_rows, num_cols):
    # check if 4 in a row is diagonal down
    won = False
    for row in range(num_rows - 3):
        for col in range(num_cols - 3):
            start = board[row][col]
            if start == " ":
                continue
            won = True
            for i in range(1, 4):
                if start != board[row + i][col + i]:
                    won = False
                    break
            if won:
                return won
    return won


def check_diagonal_up(board, num_rows, num_cols):
    # check if 4 in a row is diagonal up
    won = False
    for row in range(3, num_rows):
        for col in range(num_cols - 3):
            start = board[row][col]
            if start == " ":
                continue
            won = True
            for i in range(1, 4):
                if start != board[row - i][col + i]:
                    won = False
                    break
            if won:
                return won
    return won


def check_win(board):
    won = check_row(board, 6, 7)
    if won:
        return won
    won = check_col(board, 6, 7)
    if won:
        return won
    won = check_diagonal_down(board, 6, 7)
    if won:
        return won
    won = check_diagonal_up(board, 6, 7)
    return won


def find_moves(board):
    moves = []
    for col in range(7):
        if board[0][col] == " ":
            moves.append(col)
    return moves


def try_move(board, col, piece):
    # check from bottom up
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            break
    return board


def undo_move(board, col, piece):
    for row in range(6):
        if board[row][col] == piece:
            board[row][col] = " "
            break
    return board


def score_board(board, my_piece, op_piece, num_rows=6, num_cols=7):
    my_score = 0
    opponent_score = 0
    # count rows
    for row in range(num_rows - 3):
        for col in range(num_cols):
            clear_for_me = True
            clear_for_op = True
            for i in range(4):
                if board[row + i][col] == my_piece:
                    clear_for_op = False
                elif board[row + i][col] == op_piece:
                    clear_for_me = False
            if clear_for_me:
                my_score += 1
            if clear_for_op:
                opponent_score += 1
    # count cols
    for row in range(num_rows):
        for col in range(num_cols - 3):
            clear_for_me = True
            clear_for_op = True
            for i in range(4):
                if board[row][col + i] == my_piece:
                    clear_for_op = False
                elif board[row][col + i] == op_piece:
                    clear_for_me = False
            if clear_for_me:
                my_score += 1
            if clear_for_op:
                opponent_score += 1
    # count diagonal down
    for row in range(num_rows - 3):
        for col in range(num_cols - 3):
            clear_for_me = True
            clear_for_op = True
            for i in range(4):
                if board[row + i][col + i] == my_piece:
                    clear_for_op = False
                elif board[row + i][col + i] == op_piece:
                    clear_for_me = False
            if clear_for_me:
                my_score += 1
            if clear_for_op:
                opponent_score += 1
    # count diagonal up
    for row in range(3, num_rows):
        for col in range(num_cols - 3):
            clear_for_me = True
            clear_for_op = True
            for i in range(4):
                if board[row - i][col + i] == my_piece:
                    clear_for_op = False
                elif board[row - i][col + i] == op_piece:
                    clear_for_me = False
            if clear_for_me:
                my_score += 1
            if clear_for_op:
                opponent_score += 1
    return my_score*1.5 - opponent_score


def cpu(board, piece, depth, previous_best_score):
    # previous_best_score is best score opponent got from me from previous try_moves
    # if returned score is higher than my_best_score opponent will ignore it as it means previous move is better
    # best_score will increase as i find better moves
    # so if best_score exceeds previous_best_score should just stop as it will get ignored anyway
    best_move = -1
    best_score = -100
    moves = find_moves(board)
    for move in moves:
        # my test make_move
        board = try_move(board, move, piece)
        won = check_win(board)
        stop = False
        if won:
            best_move = move
            my_score = 100
            stop = True
        # draw
        elif len(moves) == 1:
            my_score = 0
        elif depth > 4:
            my_score = score_board(board, piece, "X" if piece == "O" else "O")
            # stop = True

        else:
            # perfect opponent moves, opponent_score is how much he likes optimal make_move
            best_counter_move, opponent_score = cpu(board,
                                                    "X" if piece == "O" else "O",
                                                    depth + 1,
                                                    -best_score)
            my_score = -opponent_score
        board = undo_move(board, move, piece)
        # check if current move is better than previous moves
        if my_score >= best_score:
            best_move = move
            best_score = my_score
            if best_score > previous_best_score or stop:
                break

    return best_move, best_score


def main():
    board = []
    for i in range(6):
        board.append([])
        for j in range(7):
            board[i].append(" ")
    # 6 rows 7 columns
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

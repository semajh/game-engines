def check_row(board, num_rows, num_cols):
    """check if any 4 are connected horizontally(in 1 row)
        returns bool"""
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
    """check if any 4 are connected vertically(in 1 column)
        returns bool"""
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
    """check if any 4 are connected diagonally down(top left to bottom right)
        returns bool"""
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
    """check if any 4 are connected diagonally up(bottom left to top right)
        returns bool"""
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
    """check if any 4 are connected in a line
        returns bool"""
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
    """returns list of valid moves"""
    moves = []
    for col in range(7):
        if board[0][col] == " ":
            moves.append(col)
    return moves


def do_move(board, col, piece):
    """inserts the piece in the proper position(lowest free row)"""
    # check from bottom up
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            break
    return board


def undo_move(board, col, piece):
    """removes the topmost piece from that column(undoing move)"""
    for row in range(6):
        if board[row][col] == piece:
            board[row][col] = " "
            break
    return board

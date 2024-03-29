from rules import find_moves, check_win, do_move, undo_move
from operator import itemgetter


def score_weights(line):
    if line <= 0:
        return 0
    elif line <= 2:
        return 1
    elif line == 2:
        return 3
    elif line == 3:
        return 5
    else:
        return 100


def score_board(board, my_piece, op_piece, num_rows=6, num_cols=7):
    """score board benefit towards current player.
     Metric used is number of available four in a rows of current player * weighting -
     number of available for opponent."""
    my_score = 0
    opponent_score = 0
    # count rows
    for row in range(num_rows - 3):
        for col in range(num_cols):
            my_line = 0
            op_line = 0
            clear_for_me = True
            clear_for_op = True
            for i in range(4):
                if board[row + i][col] == my_piece:
                    clear_for_op = False
                    my_line += 1
                elif board[row + i][col] == op_piece:
                    clear_for_me = False
                    op_line += 1
            if clear_for_me:
                my_score += score_weights(my_line)
            if clear_for_op:
                opponent_score += score_weights(op_line)
    # count cols
    for row in range(num_rows):
        for col in range(num_cols - 3):
            my_line = 0
            op_line = 0
            clear_for_me = True
            clear_for_op = True

            for i in range(4):
                if board[row][col + i] == my_piece:
                    clear_for_op = False
                    my_line += 1
                elif board[row][col + i] == op_piece:
                    clear_for_me = False
                    op_line += 1
            if clear_for_me:
                my_score += score_weights(my_line)
            if clear_for_op:
                opponent_score += score_weights(op_line)
    # count diagonal down
    for row in range(num_rows - 3):
        for col in range(num_cols - 3):
            my_line = 0
            op_line = 0
            clear_for_me = True
            clear_for_op = True
            for i in range(4):
                if board[row + i][col + i] == my_piece:
                    clear_for_op = False
                    my_line += 1
                elif board[row + i][col + i] == op_piece:
                    clear_for_me = False
                    op_line += 1
            if clear_for_me:
                my_score += score_weights(my_line)
            if clear_for_op:
                opponent_score += score_weights(op_line)
    # count diagonal up
    for row in range(3, num_rows):
        for col in range(num_cols - 3):
            my_line = 0
            op_line = 0
            clear_for_me = True
            clear_for_op = True
            for i in range(4):
                if board[row - i][col + i] == my_piece:
                    clear_for_op = False
                    my_line += 1
                elif board[row - i][col + i] == op_piece:
                    clear_for_me = False
                    op_line += 1
            if clear_for_me:
                my_score += score_weights(my_line)
            if clear_for_op:
                opponent_score += score_weights(op_line)
    return my_score - opponent_score


def cpu(board, piece, depth, previous_best_score):
    """Takes current board state, piece it is playing as, depth(start from 0) and previous
    best score(for initial function call use 1000 so it evaluates all moves).
    Uses negamax algorithm with A/B pruning"""
    # previous_best_score is best score opponent got from me from previous try_moves
    # if returned score is higher than my_best_score opponent will ignore it as it means previous move is better
    # best_score will increase as i find better moves
    # so if best_score exceeds previous_best_score should just stop as it will get ignored anyway
    best_move = -1
    best_score = -100
    moves = find_moves(board)
    for move in moves:
        # my test make_move
        board = do_move(board, move, piece)
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
                                                    -best_score+1)
            my_score = -opponent_score
            if my_score > 10:
                my_score -= 1
            elif my_score < -10:
                my_score += 1
        board = undo_move(board, move, piece)
        # check if current move is better than previous moves
        if my_score >= best_score:
            best_move = move
            best_score = my_score
            if best_score > previous_best_score or stop:
                break

    return best_move, best_score


def test_cpu(board, piece, depth, previous_best_score):
    """Takes current board state, piece it is playing as, depth(start from 0) and previous
    best score(for initial function call use 1000 so it evaluates all moves).
    Uses negamax algorithm with A/B pruning"""
    # previous_best_score is best score opponent got from me from previous try_moves
    # if returned score is higher than my_best_score opponent will ignore it as it means previous move is better
    # best_score will increase as i find better moves
    # so if best_score exceeds previous_best_score should just stop as it will get ignored anyway
    best_move = -1
    best_score = -100
    moves = find_moves(board)
    move_scores = []
    # draw
    if len(moves) == 0:
        return -1, 0
    for move in moves:
        board = do_move(board, move, piece)
        score = score_board(board, piece, "X" if piece == "O" else "O")
        move_scores.append((move, score))
        board = undo_move(board, move, piece)
    move_scores = sorted(move_scores, key=itemgetter(1), reverse=True)
    for move, score in move_scores:
        # my test make_move
        board = do_move(board, move, piece)
        won = check_win(board)
        stop = False
        if won:
            best_move = move
            my_score = 100
            stop = True
        elif depth <= 0:
            my_score = score

        else:
            # perfect opponent moves, opponent_score is how much he likes optimal make_move
            best_counter_move, opponent_score = test_cpu(board,
                                                    "X" if piece == "O" else "O",
                                                    depth - 1,
                                                    -best_score)
            my_score = -opponent_score
            if my_score > 50:
                my_score -= 1
            elif my_score < -50:
                my_score += 1
        board = undo_move(board, move, piece)
        # check if current move is better than previous moves
        if my_score >= best_score:
            best_move = move
            best_score = my_score
            if best_score > previous_best_score or stop:
                break

    return best_move, best_score

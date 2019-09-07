def display(board):
    """displays the board.Outer list is row number,inner list is column"""
    for i in board:
        print()
        print("-"*9)
        for j in i:
            print(j, end = "  ")
    print()

def make_move(board, current_player, player1, player2, PossibleMoves):
    if current_player == 1:
        piece = "X"
        print("player 1: piece is", piece)
    else:
        piece = "O"
        print("player 2: piece is", piece)
    valid = False
    player_type = player1 if current_player == 1 else player2
    while not valid:
        print(current_player, player_type)
        if player_type == 'human':
            move = input("Enter number that you would like piece to replace: ")
            print(move)
        else:
            print("AI has played: ",end="")
            move,score = AI(board, current_player, 0)
            print(move)
            print(score)
        if move in PossibleMoves:
            board[(int(move) - 1) // 3][(int(move) - 1) % 3] = piece
            valid = True
        else:
            print("move is not valid, try again")
            break
    return board

def find_moves(board):
    moves=[]
    for row in board:
        for pos in row:
            if pos != "X" and pos != "O":
                moves.append(pos)
    return moves

def check_win(board):
    if (board[0][0] == board[1][1] == board[2][2]
        or board[0][2] == board[1][1] == board[2][0]):
            return True
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]
        or board[0][i] == board[1][i] == board[2][i]):
            return True

def AI(board, player, depth):
    if player == 1:
        piece = "X"
    else:
        piece = "O"
    best_move = -1
    best_score = -15
    opponent_worst_score = 15
    heuristic_modifier = 0
    moves = find_moves(board)
    for move in moves:
        # my test move
        board[(int(move) - 1) // 3][(int(move) - 1) % 3] = piece
        won = check_win(board)
        if won:
            best_move = move
            opponent_worst_score = -10
            board[(int(move) - 1) // 3][(int(move) - 1) % 3] = move
            break
        else:
            if len(moves) == 1:
                score = 0
            else:
                # perfect opponent moves, score is how much he likes optimal move
                best_counter_move, score = AI(board,
                                              1 if player == 2 else 2,
                                              depth + 1)
                heuristic_modifier += score/50
                if depth == 0:
                    print(move,best_counter_move, score)
            # choose move to minimize opponent's happiness with move
            if score < opponent_worst_score:
                opponent_worst_score = score
                best_move = move
        # return board to original state
        board[(int(move) - 1) // 3][(int(move) - 1) % 3] = move
    # what makes opponent unhappy makes me happy
    best_score = -opponent_worst_score
    if best_score < -1:
        best_score += 1
    elif best_score > 1:
        best_score -= 1
    return best_move, best_score - heuristic_modifier
        
        
    

def main():
    board = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]
    current_player = 1
    option = input("2 Player('2') or AI('AI'): ")
    if option == '2':
        player1 = 'human'
        player2 = 'human'
    else:
        option = input("Play as Player 1 or 2: ")
        if option == '1':
            player1 = 'human'
            player2 = 'AI'
        else:
            player1 = 'AI'
            player2 = 'human'
    won=False
    while not won:
        display(board)
        possible_moves = find_moves(board)
        if len(possible_moves) > 0:
            board = make_move(board, current_player,
                              player1, player2,
                              possible_moves)
        else:
            print("its a draw")
            break
        won = check_win(board)
        if won:
            display(board)
            if current_player == 1:
                print("player 1 wins:")
            else:
                print("player 2 wins:")
        current_player = 2 if current_player == 1 else 1
            
if __name__ == "__main__":
    main()
    

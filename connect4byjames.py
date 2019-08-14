def showboard(board):
      for rowno in range(5,-1,-1):
            print(rowno,end="  ")
            for colno in range(0,7):
                  print(board[colno][rowno], end=" |  ")
            print()
      print("  ", end=" ")
      for i in range(0,7):
            print(i, end="    ")
      print()
      return True
            
def move(board,player,player1):
      valid=False
      while not valid:
            print()
            print(" player  ", player)
            colno=int(input("enter the column number: "))
            if(board[colno][5]==" "):
                  valid=True
      for rowno in range(0,6):
            if(board[colno][rowno]==" "):
                  if(player==player1):
                        board[colno][rowno]="X"
                        break
                  else:
                        board[colno][rowno]="O"
                        break
      return board
def checkrow(board):
      #check if 4 in a row is vertical
      won=False
      for col in range(6):
            for row in range(3):
                  start=board[col][row]
                  if(start==" "):
                        break
                  won=True
                  for i in range(1,4):
                        if(start!=board[col][row+i]):
                              won=False
                              break
                  if(won):
                        return won
      return won

def checkcol(board):
      #check if 4 in a row is horizontal
      won=False
      for col in range(3):
            for row in range(6):
                  start=board[col][row]
                  if(start==" "):
                        break
                  won=True
                  for i in range(1,4):
                        if(start!=board[col+i][row]):
                              won=False
                              break
                  if(won):
                        return won
      return won

def checkdiagonaldown(board):
      #check if 4 in a row is diagonal down
      won=False
      for col in range(4,6):
            for row in range(3):
                  start=board[col][row]
                  if(start==" "):
                        break
                  won=True
                  for i in range(1,4):
                        if(start!=board[col-i][row+i]):
                              won=False
                              break
                  if(won):
                        return won
      return won

def checkdiagonalup(board):
      #check if 4 in a row is diagonal up
      won=False
      for col in range(2):
            for row in range(3):
                  start=board[col][row]
                  if(start==" "):
                        break
                  won=True
                  for i in range(1,4):
                        if(start!=board[col+i][row+i]):
                              won=False
                              break
                  if(won):
                        return won
      return won
def checkwin(board):
      won=False
      won=checkrow(board)
      if(won):
            return won
      won=checkcol(board)
      if(won):
            return won
      won=checkdiagonaldown(board)
      if(won):
            return won
      won=checkdiagonalup(board)
      return won

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
        # my test make_move
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
                # perfect opponent moves, score is how much he likes optimal make_move
                best_counter_move, score = AI(board,
                                              1 if player == 2 else 2,
                                              depth + 1)
                heuristic_modifier += score/50
                if depth == 0:
                    print(move,best_counter_move, score)
            # choose make_move to minimize opponent's happiness with make_move
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
      board=[]
      for i in range(7):
            board.append([])
            for j in range(6):
                  board[i].append(" ")
      #7 columns 6 rows
      showboard(board)
      player1=input("player1 name: ")
      player2=input("player 2 name: ")
      turn=1
      won=False
      while not won:
            if(turn%2==1):
                  player=player1
            else:
                  player=player2
            board=move(board,player,player1)
            check=showboard(board)
            won=checkwin(board)
            if(won):
                  print()
                  print(player,"won")
                  break
            turn+=1
main()

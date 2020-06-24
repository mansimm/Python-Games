
print("		Welcome to tic-tac-toe game !")

player1=input("please choose the sign for player1 (X or O) : ")

if player1=='X':
 player2='O'
else:
 player2='X'

print("		Player1 is : "+player1)
print("		Player2 is : "+player2)


def showBoard(board):
 print("	|---|---|---|")
 print("	| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
 print("	|---|---|---|")
 print("	| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
 print("	|---|---|---|")
 print("	| "+board[6]+" | "+board[7]+" | "+board[8]+" |")
 print("	|---|---|---|")

def checkWinner(board,player):
 if board[0]==player and board[1]==player and board[2]==player:
  return True
 elif board[3]==player and board[4]==player and board[5]==player:
  return True
 elif board[6]==player and board[7]==player and board[8]==player:
  return True

 elif board[0]==player and board[3]==player and board[6]==player:
  return True
 elif board[1]==player and board[4]==player and board[7]==player:
  return True
 elif board[2]==player and board[5]==player and board[8]==player:
  return True

 elif board[0]==player and board[4]==player and board[8]==player:
  return True
 elif board[2]==player and board[4]==player and board[6]==player:
  return True
 else:
  return False


def initBoard(board):
 board[0]='1'
 board[1]='2'
 board[2]='3'
 board[3]='4'
 board[4]='5'
 board[5]='6'
 board[6]='7'
 board[7]='8'
 board[8]='9'

def full(board):
 for i in range(0,9):
  if(board[i]!='X' and board[i]!='O'):
   return False
 return True

def play(board):
 player=player1
 replay=True

 while replay:

  initBoard(board)
  showBoard(board)
  while True:

   if not full(board):
    pos=int(input("player "+player+" please enter position : "))
    if(board[pos-1]==str(pos)):
     board[pos-1]=player
     win=checkWinner(board,player)     #check if win or not
     showBoard(board)
    else:
     print("This position is filled please enter another position !")
    if win:
     print("Congratulations ! "+player+" is winner ....")
     win=False
     break

    if player==player1:
     player=player2
    else:
     player=player1

   else:
    print("OOPS ! Match is tie ....")
    win=False
    break

  key=input("	Do you want to replay ?(y/n) :")
  if key=='y' or key=='Y':
   replay=True
  else:
   replay=False



board=['1','2','3','4','5','6','7','8','9']

play(board)

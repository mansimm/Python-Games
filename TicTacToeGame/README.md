# TicTacToeGame

 #Problem Statement

 Program a two-person game of Tic -Tac- Toe. The game is played on a three by three board. Each player has a marker. One player
 has an ‘X’, the other an ‘O’. Players alternate turns to place their marker on the board. The first player to get three in a 
 row either diagonally, horizontally, or vertically, wins the games. In the event all squares are taken on the board without a
 winner then it is a tie. The program should set up the game by asking which player want which marker. Players should be
 assigned with a marker of there choise ie. ‘X’ or 'O'. After the game has been completed, the program should congratulate the
 winner by name palyer1 or player2. The players should then have the option to play again. If they decide to play again, then 
 replay the game.
 
  # Winning Condition
 
 1) Player1 wins if assigned marker is three in either
    1. diagonally
    2. horizontally or
    3. vertically
 2) Player2 wins if assigned marker is three in either
    1. diagonally
    2. horizontally or
    3. vertically
   
  # Tie Condition 
 
   If all squares on board are occupied and no one won.
   
  # Output
 
  use command
    $ python3 tictac.py
    
  following will be output :
  
    (base) mansi@mansi-Vostro-15-3568:~$ python3 tictac.py
        Welcome to tic-tac-toe game !
    please choose the sign for player1 (X or O) : X
        Player1 is : X
        Player2 is : O
      |---|---|---|
      | 1 | 2 | 3 |
      |---|---|---|
      | 4 | 5 | 6 |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player X please enter position : 1
      |---|---|---|
      | X | 2 | 3 |
      |---|---|---|
      | 4 | 5 | 6 |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player O please enter position : 6
      |---|---|---|
      | X | 2 | 3 |
      |---|---|---|
      | 4 | 5 | O |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player X please enter position : 5
      |---|---|---|
      | X | 2 | 3 |
      |---|---|---|
      | 4 | X | O |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player O please enter position : 3
      |---|---|---|
      | X | 2 | O |
      |---|---|---|
      | 4 | X | O |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player X please enter position : 9
      |---|---|---|
      | X | 2 | O |
      |---|---|---|
      | 4 | X | O |
      |---|---|---|
      | 7 | 8 | X |
      |---|---|---|
    Congratulations ! X is winner ....
      Do you want to replay ?(y/n) :y
      |---|---|---|
      | 1 | 2 | 3 |
      |---|---|---|
      | 4 | 5 | 6 |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player X please enter position : 2
      |---|---|---|
      | 1 | X | 3 |
      |---|---|---|
      | 4 | 5 | 6 |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player O please enter position : 5
      |---|---|---|
      | 1 | X | 3 |
      |---|---|---|
      | 4 | O | 6 |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player X please enter position : 3
      |---|---|---|
      | 1 | X | X |
      |---|---|---|
      | 4 | O | 6 |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player O please enter position : 1
      |---|---|---|
      | O | X | X |
      |---|---|---|
      | 4 | O | 6 |
      |---|---|---|
      | 7 | 8 | 9 |
      |---|---|---|
    player X please enter position : 9
      |---|---|---|
      | O | X | X |
      |---|---|---|
      | 4 | O | 6 |
      |---|---|---|
      | 7 | 8 | X |
      |---|---|---|
    player O please enter position : 7
      |---|---|---|
      | O | X | X |
      |---|---|---|
      | 4 | O | 6 |
      |---|---|---|
      | O | 8 | X |
      |---|---|---|
    player X please enter position : 4
      |---|---|---|
      | O | X | X |
      |---|---|---|
      | X | O | 6 |
      |---|---|---|
      | O | 8 | X |
      |---|---|---|
    player O please enter position : 6
      |---|---|---|
      | O | X | X |
      |---|---|---|
      | X | O | O |
      |---|---|---|
      | O | 8 | X |
      |---|---|---|
    player X please enter position : 8
      |---|---|---|
      | O | X | X |
      |---|---|---|
      | X | O | O |
      |---|---|---|
      | O | X | X |
      |---|---|---|
    OOPS ! Match is tie ....
      Do you want to replay ?(y/n) :n
    (base) mansi@mansi-Vostro-15-3568:~$ 


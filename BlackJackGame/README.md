# BlackJackGame
Problem Statement : This is a python script that allows two player to play blackjack against a computer dealer. 

 # Terminologies
 
 1.Cards: a standard deck of playing cards is used, i.e., four suits (clubs, diamonds, spades, and hearts) and 13 different cards
 within each suit (the numbers 2 through 10, jack, queen, king, and ace). In this assignment, we will replace 10, jack, queen
 and king with a generic 'face card'. We will assume an infinite number of decks available in the pack.
 
 2. Card values: the numbered cards (2 through 9) count as their numerical value. The generic face card (replacing 10, jack,
 queen, and king) counts as 10, and the ace may count as either 1 or 11 (whichever works in the player's favor)
 
 3. Hand value: the value of a hand is the sum of the values of all cards in the hand. The values of the aces in a hand are
 such that they produce the highest value that is 21 or under (if possible). A hand where any ace is counted as 11 is called a
 soft hand. The suits of the cards do not matter in blackjack.
 
 4. Pair: the two card hand where both cards have the same value. 
 (example, two aces, a pair of sixes, and for our assignment, a pair of face cards).
 
 5. Blackjack: is a two-card hand where one card is an ace and the other card is any face card.
 
 6. Busted: the value of the hand has exceeded 21.
 
 # Rules of Play
 
 There are some slight variations on the rules and procedure of blackjack. Below is the simplified procedure that we will use for
 this game. We will not be using insurance, surrender or dealer peeking, which are options in a standard casino game.
 
 1. Each player places a bet on the hand.
 
 2. The dealer deals two cards to each player, including himself. The player's cards will be face-up. One of the dealers cards
 is face-up, but the other is face-down.
 
 3. Theplayer must do one of the following:
   Hit: the player receives one additional card (face up). A player can receive as many cards as he or she wants, but if
          the value of the player's hand exceeds 21, the player busts and loses the bet on this hand irrespective of dealer's
          hand.
   
   Stand: the player does not want any additional cards
   
 4. PayOffs 
   (a) If the player has a blackjack then she receives her bet. 
       
   (b) If the player busted, she lost her bet.
   
   (c) If the dealer busted, he lost and the dealer pays the player her bet.
       
   (d) If the value of dealer's hand is greater than player's the player loses her bet.
   
   (e) If the value of player's hand is greater than dealer's the player won and dealer pays her bet.
   
   (f) If the dealer has blackjack and the player has non-blackjack 21 the dealer wins.
   
   (g) If the value of the two hands is equal, it is a push and the player gets backher bet money.That is, no profit no loss.
       Then player is again asked wheather want to replay or not.
       
       
  # Output
  
  type command :
  
  $ python3 BlackJackGame.py
  
  output will be as follows,
  
  	(base) mansi@mansi-Vostro-15-3568:~$ python3 BlackJackGame.py

				welcome to black jack

	enter the bet >40

	 Dealers Hand
	<card hidden>
	Ten of Hearts

 	Players Hand
	Ace of Clubs Jack of Diamonds

 	do you want to hit or stand h/s -> h

	 Dealers Hand
	<card hidden>
	Ten of Hearts

	 Players Hand
	Ace of Clubs Jack of Diamonds Nine of Clubs

 	do you want to hit or stand h/s -> s

 	player choose to stand dealers turn ...

	 Dealers Hand
	<card hidden>
	Ten of Hearts

	 Players Hand
	Ace of Clubs Jack of Diamonds Nine of Clubs

	 Dealers Hand
	Four of Spades Ten of Hearts Queen of Hearts

	 Players Hand
	Ace of Clubs Jack of Diamonds Nine of Clubs

		dealer busts !!!

		the chips total of player : 140

		do you want to continue y/n ->n

		thanks for playing 
	(base) mansi@mansi-Vostro-15-3568:~$
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   

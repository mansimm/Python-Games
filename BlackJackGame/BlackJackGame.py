import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
 def __init__(self,suit,rank):
  self.suit=suit
  self.rank=rank
  self.value=values[rank]

 def __str__(self):
  return f"{self.rank} of {self.suit}"



class Deck:
 def __init__(self):
  self.deck = []  # start with an empty list
  for suit in suits:
   for rank in ranks:
    self.deck.append(Card(suit,rank))

 def __str__(self):
  in_deck="the Deck has"
  for card in self.deck:
   in_deck+= "\n"+card.__str__()
  return in_deck

 def shuffle(self):
  random.shuffle(self.deck)

 def deal(self):
  single_card=self.deck.pop()
  return single_card



class Hand:
 def __init__(self):
  self.cards = []  # start with an empty list as we did in the Deck class
  self.value = 0   # start with zero value
  self.aces = 0    # add an attribute to keep track of aces

 def add_card(self,card):
  self.cards.append(card)
  self.value+=card.value
  if card.value == 11: #if card is ace ,value of ace: 11
   self.aces+=1

 def adjust_for_ace(self):
  while self.value>21 and self.aces:
   self.value-=10
   self.aces-=1


class Chips:
 def __init__(self):
  self.total = 100  # This can be set to a default value or supplied by a user input
  self.bet = 0

 def win_bet(self):
  self.total+=self.bet
  
 def lose_bet(self):
  self.total-=self.bet



def take_bet(chips):
 while True:
  try:
   chips.bet=int(input("enter the bet >"))
   if chips.total<chips.bet:
    print(f"bet cannot exceed your chips , your chips-> {chips.value}")
   else:
    break
  except Exception as e:
   print(f"the exception of type {type(e).__init__} Arguments {e.args}")


def hit(deck,hand):
 hand.add_card(deck.deal())
 hand.adjust_for_ace()


def hit_or_stand(deck,hand):
 global playing  # to control an upcoming while loop
 while True:
  choice=input("\n do you want to hit or stand h/s -> ")
  if choice[0].lower()=='h':
   hit(deck,hand)
  elif choice[0].lower()=='s':
   print("\n player choose to stand dealers turn ...")
   playing =False
  else:
   print("enter valid input ")
   continue
  break
  

  
def show_some(player,dealer):
 print("\n Dealers Hand")
 print("<card hidden>")
 print(dealer.cards[1])
 print("\n Players Hand")
 print(*player.cards)
 
 
def show_all(player,dealer):
 print("\n Dealers Hand")
 print(*dealer.cards)
 print("\n Players Hand")
 print(*player.cards)


def player_busts(chips):
 print("\n	player busts !!!")
 chips.lose_bet()
 
def player_wins(chips):
 print("\n	player wins !!!")
 chips.win_bet()
 
def dealer_busts(chips):
 print("\n	dealer busts !!!")
 chips.win_bet()
 
def dealer_wins(chips):
 print("\n	dealer wins !!!")
 chips.lose_bet()
   
def push_game():
  print("\n	dealer and player tie its push...............")
   


while True:
 # Print an opening statement
 print("\n			welcome to black jack\n")
 # Create & shuffle the deck, deal two cards to each player
 deck=Deck()
 deck.shuffle()
 
 player_hand=Hand()
 player_hand.add_card(deck.deal())
 player_hand.add_card(deck.deal())
 
 dealer_hand=Hand()
 dealer_hand.add_card(deck.deal())
 dealer_hand.add_card(deck.deal())
 
 # Set up the Player's chips
 player_chips=Chips()
 
 # Prompt the Player for their bet
 take_bet(player_chips)
 
 # Show cards (but keep one dealer card hidden)
 show_some(player_hand,dealer_hand)
 
 while playing:  # recall this variable from our hit_or_stand function
    
   # Prompt for Player to Hit or Stand
   hit_or_stand(deck,player_hand)
    
   # Show cards (but keep one dealer card hidden)
   show_some(player_hand,dealer_hand)
    
   # If player's hand exceeds 21, run player_busts() and break out of loop
   if player_hand.value > 21: 
    player_busts(player_chips)
    break
    

 # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
 if player_hand.value <= 21:
    
  while dealer_hand.value < 17:
   hit(deck,dealer_hand)

  # Show all cards
  show_all(player_hand,dealer_hand)
  # Run different winning scenarios
   
  if dealer_hand.value > 21:
   dealer_busts(player_chips)
    
  elif dealer_hand.value < player_hand.value:
   player_wins(player_chips)
    
  elif dealer_hand.value > player_hand.value:
   dealer_wins(player_chips)
    
  else:
   push_game()
   
 # Inform Player of their chips total 
 print(f"\n	the chips total of player : {player_chips.total}")
 # Ask to play again
 choice_play=input("\n	do you want to continue y/n ->")
 if choice_play[0].lower() == 'y':
  playing = True
  continue
 else:
  print("\n	thanks for playing ")
  break
   
  


########### OUTPUT #####################
"""

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
(base) mansi@mansi-Vostro-15-3568:~$ ^C
(base) mansi@mansi-Vostro-15-3568:~$ 

"""





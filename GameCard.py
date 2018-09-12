from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck=[]
player1_cards=[]
player2_cards= []

#card enum for playing cards
class Card(IntEnum):
   TWO=2
   THREE=3
   FOUR=4
   FIVE=5
   SIX=6
   SEVEN=7
   EIGHT=8
   NINE=9
   TEN=10
   JACK=11
   QUEEN=12
   KING=13
   ACE=14
#Suits enum for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS ='hearts'
    DIAMONDS = 'diamonds'

#class to hold cards
class PlayingCard:
    def __init__(self,card_value,card_suit):
        self.card = card_value
        self.suit = card_suit

#function to create full deck

def create_deck():

    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card),Suit(suit)))
    return full_deck

#print full deck to make sure all ara ok
#create_deck()
#for i in range(0,len(full_deck)):
   # print("cards ", full_deck[i].card)
   # print("Suites ",full_deck[i].suit)
#draw single card from deck
def draw_card(deck):
    rand_card=randint(0,len(deck)-1)
    return deck.pop(rand_card)

#create_deck()
#partial_deck=list(full_deck)

#test_card = draw_card(partial_deck)
#print("random card is: ", test_card.card, test_card.suit)


#deal all the cards on the players
def deal_war():
    while(len(partial_deck)>0):
        player1_cards.append(draw_card(partial_deck))
        player2_cards.append(draw_card(partial_deck))


create_deck()
partial_deck=list(full_deck)
deal_war()

for i in range(0, len(player1_cards)):
    play = input("Do You want to play? Y/N")
    if play in ("Y","y"):
        if (player1_cards[i].card > player2_cards[i].card):
            print("Player 1 wins the hand with ",player1_cards[i].card)
            print("Player 2 loses the hand with ",player2_cards[i].card)
        if (player1_cards[i].card < player2_cards[i].card):
            print("Player 2 wins the hand with ",player2_cards[i].card)
            print("Player 1 loses the hand with ",player1_cards[i].card)
        else:
            print('war')
    else:break

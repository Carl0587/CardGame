#Carlos Ortega
#Software Development Capstone
# 09/07/18


import  random
#THIS IS THE ASCCI CODE TO GENERATE THE SUITS FOR THE DECK
clubs= "\u2663"
hearts = "\u2665"
diamonds="\u2666"
spades="\u2660"
# I CREATED 2 LISTS ONE WITH THE CARD VALUES AND ANOTHER ONE TO HOLD THE SUIT VALUES
cardRank= ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
cardSuits= (clubs,hearts,diamonds,spades)
#THIS DECK LIST WILL HOLD OUR GENERATED CARDS
deck=[]

#THIS METHOD WILL WILL USE A FOR LOOP TO COMBINE A SUIT AND A VALUE TOGETHER AND APPEND IT TO THE DECK LIST
def hand():
    for s in cardSuits:
        for c in cardRank:
            card =(s,c)
            deck.append(card)

# THIS DEAL METHOD WILL PULL A RANDOM CARD FROM THE DEC LIST AND RETURN IT
def deal():
    card = random.choice(deck)
    deck.remove(card)
    return card

hand()
# THIS FOR LOOP IS TO
for i in range(13):
     for j in range(4):
         s,c = deal()
         print(c+s)

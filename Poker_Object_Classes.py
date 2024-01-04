import random
#define a card as a number & a suit
#numbers 2-14 for 2-10, jack queen king ace
#suits 1-4, spades -> hearts -> clubs -> diamonds
class Card:
    def __init__ (self, number, suit):
        self.number = number
        self.suit = suit
        self.cardValue = self.number * 5 + self.suit

    def getSuit(self):
        return self.suit

    def getNum(self):
        return self.number
    
    def cardValue(self):
        return self.number * 5 + self.suit

#define a hand as two cards, it can be suited or offsuit
class Hand:
    def __init__ (self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        if card1.suit == card2.suit:
            self.suited = True
        else:
            self.suited = False

class Deck:
    def __init__ (self):
        self.cards = []
        for x in range(2, 15):
            for y in range(1, 5):
                self.cards.append(Card(number = x, suit = y))

    def shuffle(self):
        random.shuffle(self.cards)

class Board:
    def __init__ (self):
        self.runout = []

    def dealCard(self, currentDeck):
        self.newDeck = currentDeck.shuffle()
        self.tempRand = random.randint(0, len(self.newDeck) - 1)
        self.runout.append(self.newDeck[self.tempRand])
        self.newDeck.pop(self.tempRand)
        return self.newDeck
    
    def dealFlop(self, currentDeck1):
        return (self.dealCard(currentDeck = self.dealCard(currentDeck = self.dealCard(currentDeck = currentDeck1))))
    
    def dealTurn(self, currentDeck1):
        return self.dealCard(currentDeck=currentDeck1)
    
    def dealRiver(self, currentDeck1):
        return self.dealCard(currentDeck=currentDeck1)

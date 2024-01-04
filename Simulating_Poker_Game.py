from Poker_Object_Classes import Hand
from Poker_Object_Classes import Card
from Poker_Object_Classes import Deck
from Poker_Object_Classes import Board
import random

#a player has a hand, a position
#a position is a number from 1 -> number of players
#player's turns occur in order starting from 2, meaning
#1 is the button
class Player:
    def __init__ (self, hand, position, stack):
        self.hand = hand
        self.position = position
        self.stack = stack
        self.folded = False

    def bet(self, amount):
        self.stack -= amount

    def fold(self):
        self.folded = True

#a game has a number of players, a button, and blinds
class Game:
    def __init__ (self, numPlayers, startingstack, roundLimit):
        self.currentRound = 1
        self.maxRound = roundLimit
        self.buyins = startingstack
        self.numPlayers = numPlayers
        self.currentButton = 0
        self.gameover = False
        self.players = []
        for number in range (0, self.numPlayers):
            self.players.append(Player(hand = None, position = number, stack = self.buyins))

    def nextRound(self):
        self.currentRound += 1
        self.currentButton = (self.currentButton + 1) % self.numPlayers
        if self.currentRound > self.maxRound:
            self.gameover = True

#a round has a pot, a board, a deck
class Round:
    def __init__ (self, numPlayers):
        self.gameDeck = Deck()
        self.dealtHands = []
        for number in range (0, numPlayers):
            self.dealHand()

    def dealHand(self):
        self.tempRand = random.randint(0, len(self.gameDeck) - 1)
        self.firstCard = self.gameDeck[self.tempRand]
        self.gameDeck.pop(self.tempRand)
        self.tempRand = random.randint(0, len(self.gameDeck) - 1)
        self.secondCard = self.gameDeck[self.tempRand]
        self.gameDeck.pop(self.tempRand)
        self.dealtHands.append(Hand(card1 = self.firstCard, card2 = self.secondCard))

    #in case every player except one has folded
    def handOver(self):

    def findWinner(self):
        
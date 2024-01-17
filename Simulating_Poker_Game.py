from Poker_Object_Classes import Hand
from Poker_Object_Classes import Card
from Poker_Object_Classes import Deck
from Poker_Object_Classes import Board
from itertools import combinations
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
        self.board = Board()
        self.gameDeck = Deck()
        self.dealtHands = []
        for _ in range (0, numPlayers):
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
        numberInHand = 0
        for player in self.players:
            if player.folded == False:
                numberInHand += 1
        return numberInHand == 0

    #implemented total order for the sorted function
    def leq(self, cardA, cardB):
        if (cardA.number < cardB.number):
            return True
        elif (cardA.number > cardB.number):
            return False
        else:
            if (cardA.suit <= cardB.suit):
                return True
            else:
                return False

    def sorted(self, cards):
        sortedlist = []
        while len(cards) > 0:
            smallestCard = Card(100, 100)
            for card in cards:
                if (self.leq(card, smallestCard)):
                    smallestCard = card
            for card in cards:
                if (card.number == smallestCard.number and card.suit == smallestCard.suit):
                    sortedlist.append(card)
                    cards.remove(card)
        return sortedlist

    def evaluateHand(self, playerHand, board):
        allCards = [playerHand.card1, playerHand.card2] + board
        allHands = list(combinations(allCards, 5))
        ranking = 0
        currentBiggestFive = [11]
        for fiveCards in combinations:
            currentFive = [True]

            if (self.checkStraightFlush(self.sorted(fiveCards))[0]):
                currentFive = [1, self.checkStraightFlush[1]]
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    if (currentFive[1] > currentBiggestFive[1]):
                        currentBiggestFive = currentFive
                    
            elif (self.checkQuads(self.sorted(fiveCards))[0]):
                currentFive = [2, self.checkStraightQuads[1]]
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    if (currentFive[1] > currentBiggestFive[1]):
                        currentBiggestFive = currentFive
                    elif (currentFive[1] == currentBiggestFive[1]):
                        if (currentFive[2] > currentBiggestFive[2]):
                            currentBiggestFive = currentFive
                    
            elif (self.checkFullHouse(self.sorted(fiveCards))[0]):
                currentFive = [3, self.checkFullHouse[1], self.checkFullHouse[2]]
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    if (currentFive[1] > currentBiggestFive[1]):
                        currentBiggestFive = currentFive
                    elif (currentFive[1] == currentBiggestFive[1]):
                        if (currentFive[2] > currentBiggestFive[2]):
                            currentBiggestFive = currentFive
                    
            elif (self.checkFlush(self.sorted(fiveCards))[0]):
                currentFive = self.checkFlush(self.sorted(fiveCards))[0]
                currentFive[0] = 4
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    for i in range (1, 5):
                        if (currentFive[i] > currentBiggestFive[i]):
                            currentBiggestFive = currentFive
                            break
                        elif (currentFive[i] < currentBiggestFive[i]):
                            break
                    
            elif (self.checkStraight(self.sorted(fiveCards))[0]):
                currentFive = self.checkStraight(self.sorted(fiveCards))[0]
                currentFive[0] = 5
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    if (currentFive[1] > currentBiggestFive[1]):
                        currentBiggestFive = currentFive
                    
            elif (self.checkThreeOfAKind(self.sorted(fiveCards))[0]):
                currentFive = self.checkThreeOfAKind(self.sorted(fiveCards))[0]
                currentFive[0] = 6
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    for i in range (1, 4):
                        if (currentFive[i] > currentBiggestFive[i]):
                            currentBiggestFive = currentFive
                            break
                        elif (currentFive[i] < currentBiggestFive[i]):
                            break

            elif (self.checkTwoPair(self.sorted(fiveCards))[0]):
                currentFive = self.checkTwoPair(self.sorted(fiveCards))[0]
                currentFive[0] = 7
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    for i in range (1, 4):
                        if (currentFive[i] > currentBiggestFive[i]):
                            currentBiggestFive = currentFive
                            break
                        elif (currentFive[i] < currentBiggestFive[i]):
                            break
                    
            elif (self.checkPair(self.sorted(fiveCards))[0]):
                currentFive = self.checkTwoPair(self.sorted(fiveCards))[0]
                currentFive[0] = 8
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    for i in range (1, 5):
                        if (currentFive[i] > currentBiggestFive[i]):
                            currentBiggestFive = currentFive
                            break
                        elif (currentFive[i] < currentBiggestFive[i]):
                            break
            else:
                currentFive = self.checkTwoPair(self.sorted(fiveCards))[0]
                currentFive[0] = 9
                if (currentBiggestFive[0] > currentFive[0]):
                    currentBiggestFive = currentFive
                elif (currentFive[0] == currentBiggestFive[0]):
                    for i in range (1, 6):
                        if (currentFive[i] > currentBiggestFive[i]):
                            currentBiggestFive = currentFive
                            break
                        elif (currentFive[i] < currentBiggestFive[i]):
                            break
    
        return currentBiggestFive

    def checkStraightFlush(self, cards):
        if (self.checkFlush(cards)[0] and self.checkStraight(cards)[0]):
            highest = 0
            for card in cards:
                highest = max(highest, card.number)
            return [True, highest] #get the value of the highest card
        else:
            return [False]
    
    def checkQuads(self, cards):
        count = 0
        for card in cards:
            if (card.number == cards[0].number, cards[4].number):
                count+=1
        if (count == 4):
            return [True, card[0].number]
        
        count = 0
        for card in cards: 
            if (card.number == cards[4].number):
                count += 1
        if (count == 4):
            return [True, card[1].number, cards[0].number]
        else:
            return [False]
               
    def checkFullHouse(self, cards):
        if (self.checkThreeOfAKind[0]):
            newcards = []
            for card in cards:
                if (card.number != self.checkThreeOfAKind[1]):
                    newcards.append(card.number)
            if (newcards[1].number == newcards[2].number):
                return [True, self.checkThreOfAKind[1], newcards[1].number]
            else: 
                return [False]
        else:
            return [False]
    
    def checkFlush(self, cards):
        if (cards[0].suit == cards[1].suit):
            count = 0
            for card in cards:
                if (card.suit == cards[0].suit):
                    count+=1
            if (count == 5):
                return [True, cards[4].number, cards[3].number, cards[2].number, cards[1].number, cards[0].number]
            else:
                return [False]
        else:
            return [False]
    
    def checkStraight(self, cards):
        if (cards[4].number == 14):
            if (cards[0].number == 2 and cards[1].number == 3 and cards[2].number == 4 and cards[3].number == 5):
                return [True, 5]
        else:
            tempBool = True
            for i in range(4):
                tempBool = tempBool and (1 == cards[i + 1].number - cards[i].number)
            if (tempBool):
                return [True, cards[4].number]
            else: 
                return [False]
    
    def checkThreeOfAKind(self, cards):
        if (cards[0].number == cards[1].number == cards[2].number):
            return [True, cards[0].number, cards[4].number, cards[3].number]
        elif (cards[1].number == cards[2].number == cards[3].number):
            return [True, cards[1].number, cards[4].number, cards[0].number]
        elif (cards[2].number == cards[3].number == cards[4].number):
            return [True, cards[2].number, cards[1].number, cards[0].number]
        else:
            return [False]
    
    def checkTwoPair(self, cards):
        if (cards[4].number == cards[3].number):
            if (cards[1].number == cards[2].number):
                return [True, cards[4].number, cards[1].number, cards[0].number]
            elif (cards[1].number == cards[0].number):
                return [True, cards[4].number, cards[1].number, cards[2].number]
            else:
                return [False]
        elif (cards[3].number == cards[2].number):
            if (cards[1].number == cards[0].number):
                return [True, cards[3].number, cards[1].number, cards[4].number]
            else:
                return [False]
    
    def checkPair(self, cards):
        reversal = cards[::-1]
        for card in reversal:  
            tempcards = cards
            tempcards.remove(card)
            for card2 in tempcards:
                if (card.number == card2.number and card.suit == card2.suit):
                    return [True, card.number]
        return [False]
    
    def getHighCard(self, cards):
        return [True, cards[4].number, cards[3].number, cards[2].number, cards[1].number, cards[0].number]
    
    def findWinnerHeadsup(self):
        assert (len(self.board.runout) == 5)
        self.handEval = []
        for playerHand in self.dealtHands:
            self.handEval.add(self.evaluateHand(playerHand), self.board)
        hand1 = self.handEval[0]
        hand2 = self.handEval[1]

        if (hand1[0] < hand2[0]):
            return 0
        elif (hand1[0] > hand2[0]):
            return 1
        elif (hand1[0] == hand2[0]):
            for i in range (1, len(hand1)):
                if (hand1[i] > hand2[i]):
                    return 0
                elif (hand1[i] < hand2[i]):
                    return 1
            return 'draw'
    
        
            

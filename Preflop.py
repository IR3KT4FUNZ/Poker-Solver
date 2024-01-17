from Simulating_Poker_Game import Player, Game, Round
from Poker_Object_Classes import Board, Card, Hand, Deck
from Neural_Network_Classes import Neuron, Layer, MLP
from Neural_Network_Backprop import Number
from Preflop_Ranking import PreflopHands
import random

class NeuralNetPreflop: 
    def __init__(self):
        #inputs: preflop rank, position, current pot
        #options: fold, call, raise
        self.net = MLP(2, [8, 3])
        self.preflopRank = PreflopHands()
    
    def train(self, hand, position):
        self.inarray = [self.preflopRank.getRank(hand), position]
        self.loss = self.calcLoss(self.softmax(self.net(self.inarray)))
        self.loss.backward()
        for p in self.net.parameters:
            p.data += -0.01 * p.grad

    def softmax(self, outarray):
        self.expSum = Number(0)
        self.probabilities = []
        for x in self.net:
            self.expSum = self.expSum + x.exp(x)
        for x in outarray:
            self.probabilities.append[x/self.expSum]
        return self.probabilities

    def calcLoss(self):
        return 0

    def trainXTimes(self, numTimes):
        print(self.net.parameters)
        for _ in range(0, numTimes):
            self.train(self.randomHand(), self.randNum(2))
        print(self.net.parameters)

    def randNum(self, num):
        return random.uniform(1, num + 1) 

    def randomHand(self):
        self.deck = Deck()
        return Hand(self.deck.cards[0], self.deck.cards[1])

test = NeuralNetPreflop()
test.trainXTimes(5)
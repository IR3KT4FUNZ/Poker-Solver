#VERY FIRST implementation of the final neural network

from Simulating_Poker_Game import Player, Game, Round
from Poker_Object_Classes import Board, Card, Hand, Deck
from Neural_Network_Classes import Neuron, Layer, MLP
from Neural_Network_Backprop import Number

class NeuralNetPreflop: 
    
    def __init__(self):
        self.net = MLP(4, [10, 7])

    def calcLoss(self):


    def softmax(self, lst):
        self.expSum = Number(0)
        self.probabilities = []
        for x in lst:
            self.expSum = self.expSum + x.exp(x)
        for x in lst:
            self.probabilities.append[x/self.expSum]
        print(self.probabilities)
        return self.probabilities
    
    def getWinningOdds(self):

    def getPreflopRank(self):

    def getPosition(self):

    def getCurrentBet(self):

inLayer = [winningOdds, preflopRank, pot, stack, position, currentBet]
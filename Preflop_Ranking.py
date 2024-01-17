import numpy as np

from Poker_Object_Classes import Card
from Poker_Object_Classes import Hand
from Poker_Object_Classes import Deck

class PreflopHands:
    def __init__(self):
        self.totalHands = 169
        self.allHands = np.zeros((75, 75), dtype=int)
        self.fullDeck = Deck()
        self.fullDeck.shuffle()
        self.assess()
        
    def getRank(self, hand):
        if hand.card1.number <= hand.card2.number:
            return self.allHands[hand.card1.cardValue, hand.card2.cardValue]
        else:
            return self.allHands[hand.card2.cardValue, hand.card1.cardValue]

    def assess(self):
        for firstCard in self.fullDeck.cards:
            for secondCard in self.fullDeck.cards:
                if firstCard.number <= secondCard.number:
                    self.allHands[firstCard.cardValue, secondCard.cardValue] = self.rank(firstCard, secondCard)
                else:
                    self.allHands[firstCard.cardValue, secondCard.cardValue] = self.rank(secondCard, firstCard)

    def rank(self, card1, card2):
        self.Hand = Hand(card1, card2)
        if self.Hand.suited:
            if card1.number == card2.number:
                return 0
            
            if card1.number == 13:
                if card2.number == 14:
                    return 4
                
            elif card1.number == 12:
                if card2.number == 14:
                    return 6
                elif card2.number == 13:
                    return 7
                
            elif card1.number == 11:
                if card2.number == 14:
                    return 8
                elif card2.number == 13:
                    return 9
                elif card2.number == 12:
                    return 13
                
            elif card1.number == 10:
                if card2.number == 14:
                    return 12
                elif card2.number == 13:
                    return 14
                elif card2.number == 12:
                    return 15
                elif card2.number == 11:
                    return 16

            elif card1.number == 9:
                if card2.number == 14:
                    return 19
                elif card2.number == 13:
                    return 22
                elif card2.number == 12:
                    return 25
                elif card2.number == 11:
                    return 26
                elif card2.number == 10:
                    return 23
                
            elif card1.number == 8:
                if card2.number == 14:
                    return 24
                elif card2.number == 13:
                    return 37
                elif card2.number == 12:
                    return 43
                elif card2.number == 11:
                    return 41
                elif card2.number == 10:
                    return 38
                elif card2.number == 9:
                    return 40
                
            elif card1.number == 7:
                if card2.number == 14:
                    return 30
                elif card2.number == 13:
                    return 44
                elif card2.number == 12:
                    return 61
                elif card2.number == 11:
                    return 64
                elif card2.number == 10:
                    return 57
                elif card2.number == 9:
                    return 54
                elif card2.number == 8:
                    return 48

            elif card1.number == 6:
                if card2.number == 14:
                    return 34
                elif card2.number == 13:
                    return 53
                elif card2.number == 12:
                    return 66
                elif card2.number == 11:
                    return 79
                elif card2.number == 10:
                    return 74
                elif card2.number == 9:
                    return 68
                elif card2.number == 8:
                    return 62
                elif card2.number == 7:
                    return 48
                
            elif card1.number == 5:
                if card2.number == 14:
                    return 28
                elif card2.number == 13:
                    return 55
                elif card2.number == 12:
                    return 69
                elif card2.number == 11:
                    return 82
                elif card2.number == 10:
                    return 93
                elif card2.number == 9:
                    return 88
                elif card2.number == 8:
                    return 78
                elif card2.number == 7:
                    return 67
                elif card2.number == 6:
                    return 63

            elif card1.number == 4:
                if card2.number == 14:
                    return 32
                elif card2.number == 13:
                    return 58
                elif card2.number == 12:
                    return 71
                elif card2.number == 11:
                    return 86
                elif card2.number == 10:
                    return 95
                elif card2.number == 9:
                    return 106
                elif card2.number == 8:
                    return 94
                elif card2.number == 7:
                    return 85
                elif card2.number == 6:
                    return 70
                elif card2.number == 5:
                    return 65

            elif card1.number == 3:
                if card2.number == 14:
                    return 33
                elif card2.number == 13:
                    return 59
                elif card2.number == 12:
                    return 72
                elif card2.number == 11:
                    return 87
                elif card2.number == 10:
                    return 96
                elif card2.number == 9:
                    return 107
                elif card2.number == 8:
                    return 116
                elif card2.number == 7:
                    return 103
                elif card2.number == 6:
                    return 90
                elif card2.number == 5:
                    return 77
                elif card2.number == 4:
                    return 84

            elif card1.number == 2:
                if card2.number == 14:
                    return 39
                elif card2.number == 13:
                    return 60
                elif card2.number == 12:
                    return 75
                elif card2.number == 11:
                    return 89
                elif card2.number == 10:
                    return 98
                elif card2.number == 9:
                    return 111
                elif card2.number == 8:
                    return 118
                elif card2.number == 7:
                    return 120
                elif card2.number == 6:
                    return 110
                elif card2.number == 5:
                    return 92
                elif card2.number == 4:
                    return 97
                elif card2.number == 3:
                    return 105

        else:
            if card1.number == card2.number:
                if card1.number == 2:
                    return 52
                elif card1.number == 3:
                    return 51
                elif card1.number == 4:
                    return 50
                elif card1.number == 5:
                    return 46
                elif card1.number == 6:
                    return 36
                elif card1.number == 7:
                    return 29
                elif card1.number == 8:
                    return 21
                elif card1.number == 9:
                    return 17
                elif card1.number == 10:
                    return 10
                elif card1.number == 11:
                    return 5
                elif card1.number == 12:
                    return 3
                elif card1.number == 13:
                    return 2
                elif card1.number == 14:
                    return 1
            else:
                if card1.number == 13:
                    if card2.number == 14:
                        return 11
                         
                elif card1.number == 12:
                    if card2.number == 14:
                        return 18
                    elif card2.number == 13:
                        return 20
                
                elif card1.number == 11:
                    if card2.number == 14:
                        return 27
                    elif card2.number == 13:
                        return 31
                    elif card2.number == 12:
                        return 35
                
                elif card1.number == 10:
                    if card2.number == 14:
                        return 42
                    elif card2.number == 13:
                        return 45
                    elif card2.number == 12:
                        return 49
                    elif card2.number == 11:
                        return 47

                elif card1.number == 9:
                    if card2.number == 14:
                        return 76
                    elif card2.number == 13:
                        return 81
                    elif card2.number == 12:
                        return 83
                    elif card2.number == 11:
                        return 80
                    elif card2.number == 10:
                        return 73
                    
                elif card1.number == 8:
                    if card2.number == 14:
                        return 91
                    elif card2.number == 13:
                        return 112
                    elif card2.number == 12:
                        return 115
                    elif card2.number == 11:
                        return 108
                    elif card2.number == 10:
                        return 100
                    elif card2.number == 9:
                        return 99
                    
                elif card1.number == 7:
                    if card2.number == 14:
                        return 102
                    elif card2.number == 13:
                        return 122
                    elif card2.number == 12:
                        return 131
                    elif card2.number == 11:
                        return 129
                    elif card2.number == 10:
                        return 124
                    elif card2.number == 9:
                        return 119
                    elif card2.number == 8:
                        return 114

                elif card1.number == 6:
                    if card2.number == 14:
                        return 113
                    elif card2.number == 13:
                        return 125
                    elif card2.number == 12:
                        return 137
                    elif card2.number == 11:
                        return 147
                    elif card2.number == 10:
                        return 140
                    elif card2.number == 9:
                        return 134
                    elif card2.number == 8:
                        return 126
                    elif card2.number == 7:
                        return 121
                    
                elif card1.number == 5:
                    if card2.number == 14:
                        return 101
                    elif card2.number == 13:
                        return 128
                    elif card2.number == 12:
                        return 141
                    elif card2.number == 11:
                        return 149
                    elif card2.number == 10:
                        return 157
                    elif card2.number == 9:
                        return 150
                    elif card2.number == 8:
                        return 139
                    elif card2.number == 7:
                        return 130
                    elif card2.number == 6:
                        return 123

                elif card1.number == 4:
                    if card2.number == 14:
                        return 104
                    elif card2.number == 13:
                        return 132
                    elif card2.number == 12:
                        return 143
                    elif card2.number == 11:
                        return 152
                    elif card2.number == 10:
                        return 158
                    elif card2.number == 9:
                        return 164
                    elif card2.number == 8:
                        return 156
                    elif card2.number == 7:
                        return 145
                    elif card2.number == 6:
                        return 136
                    elif card2.number == 5:
                        return 127

                elif card1.number == 3:
                    if card2.number == 14:
                        return 109
                    elif card2.number == 13:
                        return 133
                    elif card2.number == 12:
                        return 144
                    elif card2.number == 11:
                        return 153
                    elif card2.number == 10:
                        return 160
                    elif card2.number == 9:
                        return 165
                    elif card2.number == 8:
                        return 167
                    elif card2.number == 7:
                        return 161
                    elif card2.number == 6:
                        return 148
                    elif card2.number == 5:
                        return 138
                    elif card2.number == 4:
                        return 142

                elif card1.number == 2:
                    if card2.number == 14:
                        return 117
                    elif card2.number == 13:
                        return 135
                    elif card2.number == 12:
                        return 146
                    elif card2.number == 11:
                        return 155
                    elif card2.number == 10:
                        return 162
                    elif card2.number == 9:
                        return 166
                    elif card2.number == 8:
                        return 168
                    elif card2.number == 7:
                        return 169
                    elif card2.number == 6:
                        return 163
                    elif card2.number == 5:
                        return 151
                    elif card2.number == 4:
                        return 154
                    elif card2.number == 3:
                        return 159
                else:
                    return 0

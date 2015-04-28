# A blackjack implementation to practice counting cards
# Can choose between number of decks used
# Can ask computer for help to verify you are counting correctly
# Can simulate hands to test counting strategies

# By Brian Dau

import sys, random

class Player:
    hand = ""


class User(Player):
    funds = 0

    def resetFunds(self, money = 1000):
        User.funds = money


class Dealer(Player):


class Deck:
    suits = ["c", "h", "s", "d"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    decknumber = 0
    cardshoe = []
    shoecounter = 0
    decksremaining = 0
    singledecknumer = 0
    singledeckdenom = 0

    def setDecks(self, number = 1):
        Deck.cardshoe = []
        Deck.shoecounter = 0
        Deck.decknumber = number
        while Deck.shoecounter < Deck.decknumber:
            Deck.cardshoe += [(self.x+self.y) for self.x in Deck.values for self.y in Deck.suits]
            Deck.shoecounter += 1

class Game:
    runningcount = 0
    truecount = 0
    aces = 0

    def getRunningCount():
        print("Running count is: %s" % Game.runningcount)

    def getTrueCount():
        if Deck.decknumber != 1:
            Game.truecount = Game.runningcount / Deck.decksremaining
            print("True count is: %s" % Game.truecount)
        else:
            Game.truecount = (Game.runningcount * Deck.singledeckdenom) / Deck.singledecknumer
            print("True count is: %s" % Game.truecount)

def main():



main()

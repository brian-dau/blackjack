# A blackjack implementation to practice counting cards
# Can choose between number of decks used
# Can ask computer for help to verify you are counting correctly
# Can simulate hands to test counting strategies

# By Brian Dau

import sys, random

class Player:
    hand = []
    card1 = ""
    card2 = ""
    card3 = ""
    card4 = ""
    card5 = ""


class User(Player):
    funds = 0

    def resetFunds(self, money = 1000):
        User.funds = money

    def showHand():
        print("Your hand: %s" % ', '.join(User.hand))

    def hitHand():
        pass

    def stayHand():
        pass


class Dealer(Player):
    showing = ""

    def runAI():
        pass

    def showHand():
        pass

    def hitHand():
        pass

    def stayHand():
        pass


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

    def dealCards():
        if len(Deck.cardshoe) >= 4:
            User.card1 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe)))
            User.card2 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe)))
            Dealer.card1 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe)))
            Dealer.card2 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe)))
            User.hand.extend([User.card1, User.card2])
            Dealer.hand.extend([Dealer.card1, Dealer.card2])
        else:
            print("Shuffling cards.")
            Deck.setDecks()
            Deck.dealCards()

class Game:
    prompt = ""
    runningcount = 0
    truecount = 0
    aces = 0

    def __init__(self):
        while True:
            User.resetFunds(self)
            Deck.setDecks(self)
            Game.mainMenu()
            Game.prompt = str.lower(input("> "))
            if Game.prompt == '1' or Game.prompt == 'd':
                print("Dealing cards.")
                User.hand = []
                Dealer.hand = []
                Game.playHand()
            elif Game.prompt == '2' or Game.prompt == 's':
                print("Shuffling cards.")
                Deck.setDecks()
            elif Game.prompt == '3' or Game.prompt == 'r':
                main()
            else:
                print("Command not recognized, try again.")

    def getRunningCount():
        print("Running count is: %s" % Game.runningcount)

    def getTrueCount():
        if Deck.decknumber != 1:
            Game.truecount = Game.runningcount / Deck.decksremaining
            print("True count is: %s" % Game.truecount)
        else:
            Game.truecount = (Game.runningcount * Deck.singledeckdenom) / Deck.singledecknumer
            print("True count is: %s" % Game.truecount)

    def mainMenu():
        print("1. [D]eal hand.")
        print("2. [S]huffle cards.")
        print("3. [R]eturn to main menu.")

    def playHand():
        Deck.dealCards()
        User.showHand()
        print("Dealer shows: %s" % Dealer.card1)
        while True:
            Game.playMenu()
            Game.prompt = str.lower(input("> "))
            if Game.prompt == '1' or Game.prompt == 'h':
                pass
            elif Game. prompt == '2' or Game.prompt == 's':
                pass
            else:
                print("Command not recognized, try again.")

    def playMenu():
        print("1. [H]it.")
        print("2. [S]tay.")
            

def main():
    menuprompt = ""
    print("Welcome to Blackjack")
    print("Please select a menu option below.")
    showHelp()
    while True:
        menuprompt = str.lower(input("> "))
        if menuprompt == '1' or menuprompt == 's':
            play = Game()
        elif menuprompt == '2' or menuprompt == 'q':
            print("Thanks for playing.")
            sys.exit()
        else:
            print("Command not recognized, try again.")


def showHelp():
    print("1. [S]tart a new game.")
    print("2. [Q]uit game.")


main()

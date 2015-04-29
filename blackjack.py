# A blackjack implementation to practice counting cards
# Can choose between number of decks used
# Can ask computer for help to verify you are counting correctly
# Can simulate hands to test counting strategies

# By Brian Dau

import sys, random

class Player:
    hand = []
    testhand = []
    card1 = ""
    card2 = ""
    newcard = ""
    hitcounter = 2
    blackjack = False
    ace = False
    aces = False
    firstace = 0
    besthand = 0


class User(Player):
    funds = 0

    def resetFunds(self, money = 1000):
        User.funds = money

    def showHand():
        print("Your hand: %s" % ', '.join(User.hand))

    def hitHand():
        Deck.checkDeck()
        User.newcard = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe) - 1))
        User.hand.extend([User.newcard])
        print("Drawing card: %s" % User.hand[User.hitcounter])
        User.hitcounter += 1

    def checkHand():
        User.testhand = [x[:-1] for x in User.hand]
        if 'A' in User.testhand:
            User.testhand = [x.replace('A', '1') for x in User.testhand]
            if User.testhand.count(1) == 1:
                User.ace = True
            else:
                User.aces = True
        else:
            pass
        if 'J' or 'Q' or 'K' in User.testhand:
            for x in User.testhand:
                if x == 'J':
                    User.testhand = [x.replace('J', '10') for x in User.testhand]
                elif x == 'Q':
                    User.testhand = [x.replace('Q', '10') for x in User.testhand]
                else:
                    User.testhand = [x.replace('K', '10') for x in User.testhand]
        else:
            pass
        User.testhand = [int(x) for x in User.testhand]
        if sum(User.testhand) > 21:
            print("You bust.")
            Game.handover = True
        else:
            if User.ace:
                User.testhand = [11 if x == 1 else x for x in User.testhand]
                if sum(User.testhand) < 22:
                    User.besthand = sum(User.testhand)
                else:
                    pass
            elif User.aces:
                User.firstace = User.testhand.index(1)
                User.testhand[User.firstace] = 11
                if sum(User.testhand) < 22:
                    User.besthand = sum(User.testhand)
                else:
                    pass
            else:
                User.besthand = sum(User.testhand)

    def checkBlackjack():
        User.testhand = [x[:-1] for x in User.hand]
        if 'A' in User.testhand:
            if '10' in User.testhand:
                User.blackjack = True
            elif 'J' in User.testhand:
                User.blackjack = True
            elif 'Q' in User.testhand:
                User.blackjack = True
            elif 'K' in User.testhand:
                User.blackjack = True
            else:
                User.blackjack = False
        else:
            User.blackjack = False


class Dealer(Player):

    def runAI():
        Dealer.showHand()
        Dealer.checkHand()
        while Game.handover == False:
            if Dealer.besthand > 16 and Dealer.besthand < 22:
                if Dealer.besthand > User.besthand:
                    print("Dealer has %s." % Dealer.besthand)
                    print("Dealer wins.")
                    Game.handover = True
                elif Dealer.besthand < User.besthand:
                    print("Dealer has %s." % Dealer.besthand)
                    print("Player wins.")
                    Game.handover = True
                else:
                    print("Dealer has %s." % Dealer.besthand)
                    print("You push.")
                    Game.handover = True
            else:
                Dealer.hitHand()
                Dealer.checkHand()
            

    def showHand():
        print("Dealer's hand: %s" % ', '.join(Dealer.hand))

    def hitHand():
        Deck.checkDeck()
        Dealer.newcard = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe) - 1))
        Dealer.hand.extend([Dealer.newcard])
        print("Dealer draws: %s" % Dealer.hand[Dealer.hitcounter])
        Dealer.hitcounter += 1

    def checkHand():
        Dealer.testhand = [x[:-1] for x in Dealer.hand]
        if 'A' in Dealer.testhand:
            Dealer.testhand = [x.replace('A', '1') for x in Dealer.testhand]
            if Dealer.testhand.count(1) == 1:
                Dealer.ace = True
            else:
                Dealer.aces = True
        else:
            pass
        if 'J' or 'Q' or 'K' in Dealer.testhand:
            for x in Dealer.testhand:
                if x == 'J':
                    Dealer.testhand = [x.replace('J', '10') for x in Dealer.testhand]
                elif x == 'Q':
                    Dealer.testhand = [x.replace('Q', '10') for x in Dealer.testhand]
                else:
                    Dealer.testhand = [x.replace('K', '10') for x in Dealer.testhand]
        else:
            pass
        Dealer.testhand = [int(x) for x in Dealer.testhand]
        if sum(Dealer.testhand) > 21:
            print("Dealer busts.")
            Game.handover = True
        elif sum(Dealer.testhand) == 21:
            Dealer.besthand = sum(Dealer.testhand)
        else:
            if Dealer.ace:
                Dealer.testhand = [11 if x == 1 else x for x in Dealer.testhand]
                if sum(Dealer.testhand) < 22:
                    Dealer.besthand = sum(Dealer.testhand)
                else:
                    pass
            elif Dealer.aces:
                Dealer.testhand[Dealer.firstace] = 11
                if sum(Dealer.testhand) < 22:
                    Dealer.besthand = sum(Dealer.testhand)
                else:
                    pass
            else:
                Dealer.besthand = sum(Dealer.testhand)
                    

    def checkBlackjack():
        Dealer.testhand = [x[:-1] for x in Dealer.hand]
        if 'A' in Dealer.testhand:
            if '10' in Dealer.testhand:
                Dealer.blackjack = True
            elif 'J' in Dealer.testhand:
                Dealer.blackjack = True
            elif 'Q' in Dealer.testhand:
                Dealer.blackjack = True
            elif 'K' in Dealer.testhand:
                Dealer.blackjack = True
            else:
                Dealer.blackjack = False
        else:
            Dealer.blackjack = False


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
            User.card1 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe) - 1))
            User.card2 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe) - 1))
            Dealer.card1 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe) - 1))
            Dealer.card2 = Deck.cardshoe.pop(random.randint(0, len(Deck.cardshoe) - 1))
            User.hand.extend([User.card1, User.card2])
            Dealer.hand.extend([Dealer.card1, Dealer.card2])
        else:
            print("Shuffling cards.")
            Deck.setDecks()
            Deck.dealCards()

    def checkDeck():
        if len(Deck.cardshoe) > 0:
            pass
        else:
            print("Shuffling cards.")
            Deck.setDecks()

class Game:
    prompt = ""
    runningcount = 0
    truecount = 0
    handover = False

    def __init__(self):
        while True:
            User.resetFunds(self)
            Deck.setDecks(self)
            Game.mainMenu()
            Game.prompt = str.lower(input("> "))
            if Game.prompt == '1' or Game.prompt == 'd':
                print("Dealing cards.")
                Game.playHand()
            elif Game.prompt == '2' or Game.prompt == 's':
                print("Shuffling cards.")
                Deck.setDecks(self)
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
        print("============ NEW HAND ============")
        print("1. [D]eal hand.")
        print("2. [S]huffle cards.")
        print("3. [R]eturn to main menu.")

    def playHand():
        User.hand = []
        Dealer.hand = []
        User.hitcounter = 2
        Dealer.hitcounter = 2
        User.ace = False
        User.aces = False
        Dealer.ace = False
        Dealer.aces = False
        Game.handover = False
        Dealer.blackjack = False
        User.blackjack = False
        Deck.dealCards()
        Dealer.checkBlackjack()
        User.checkBlackjack()
        if Dealer.blackjack == True:
            if User.blackjack == True:
                print("You push.")
                Game.handover = True
            else:
                print("Dealer has blackjack.")
                Game.handover = True
        elif User.blackjack == True:
            print("Blackjack!")
            Game.handover = True
        else:
            pass
        while Game.handover == False:
            User.showHand()
            print("Dealer shows: %s" % Dealer.card1)
            User.checkHand()
            Game.playMenu()
            Game.prompt = str.lower(input("> "))
            if Game.prompt == '1' or Game.prompt == 'h':
                User.hitHand()
                User.checkHand()
            elif Game. prompt == '2' or Game.prompt == 's':
                print("Your best hand is: %s" % User.besthand)
                Dealer.runAI()
            else:
                print("Command not recognized, try again.")
        User.showHand()
        Dealer.showHand()

    def playMenu():
        print("1. [H]it.")
        print("2. [S]tand.")
            

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

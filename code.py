import random

class Hand:
    def __init__(self):
        self.R = 1
        self.L = 1
    
    def getR(self):         
        return self.R
    
    def getL(self):
        return self.L
    
    def attack(self, attacker, defender, defHand):
        if attacker == 'r' and defender == 'r':
            defHand.R = defHand.R + self.R
        elif attacker == 'r' and defender == 'l':
            defHand.L = defHand.L + self.R
        elif attacker == 'l' and defender == 'l':
            defHand.L = defHand.L + self.L
        else:
            defHand.R = defHand.R + self.L

    def split(self):
        if self.R == 2 and self.L == 0:
            self.R, self.L = 1, 1
        elif self.R == 0 and self.L == 2:
            self.R, self.L = 1, 1
        elif self.R == 4 and self.L == 0:
            self.R, self.L = 2, 2
        elif self.R == 0 and self.L == 4:        
            self.R, self.L = 2, 2    

    def AI(self, player):
        if self.AIdisarm(player) == False:
            if self.AIbothzeroPriority(player) == False:
                if self.AIbothzero(player) == False:
                    if self.AIonlyzeroPriority(player) == False:
                        if self.AIonlyzero(player) == False:
                            if self.AIplayer1hand(player) == False:
                                self.AIrandom(player)

    # look to disarm a player's hand
    def AIdisarm(self, player):
        if self.R + player.R == 5:
            self.attack('r','r',player)
        elif self.R + player.L == 5:
            self.attack('r','l',player)
        elif self.L + player.R == 5:
            self.attack('l','r',player)
        elif self.L + player.L == 5:        
            self.attack('l','l',player)
        else: 
            return False

    #split if both players have one Hand and attacking = probable death 
    def AIbothzeroPriority(self, player):
        if (self.R == 0 or self.L == 0) and (player.R == 0 or player.L == 0):
            a = 0
            b = 1
            possibilitiesComputer = [self.R, self.L]
            possibilitiesPlayer = [player.R, player.L]
            #Since ycount can go up to 3, possStrings needs to repeat r and l 
            possStrings = ['r','l','r','l']
            xcount = -1
            ycount = -1
            for x in possibilitiesComputer:
                xcount = xcount + 1
                for y in possibilitiesPlayer:
                    ycount = ycount + 1
                    if (x + x + y)%5 == 0 and x != 0:
                        if x % 2 == 0:
                            a = x
                            b = y
                            self.split()
                        elif x % 2 != 0:
                            a = x
                            b = y
                            self.attack(possStrings[xcount],possStrings[ycount],player)
            #if attack or split occur, either x or y would change. a and b avoid this change. This way, the equation remains unaltered from before (line 71) and the AI won't continue to run.
            if (a + a + b)%5 != 0:
                return False
        else:
            return False

    #This must be in its own function because an elif would mess up the if sequence in AIbothzeroPriority. Ensures that computer attacks when both players have one hand.
    def AIbothzero(self, player):
        if (self.R == 0 or self.L == 0) and (player.R == 0 or player.L == 0): 
            possibilitiesComputer = [self.R, self.L]
            possibilitiesPlayer = [player.R, player.L]
            #Since ycount can go up to 3, possStrings needs to repeat r and l
            possStrings = ['r','l','r','l']
            xcount = -1
            ycount = -1   
            for x in possibilitiesComputer:
                xcount = xcount + 1
                for y in possibilitiesPlayer:
                    ycount = ycount + 1 
                    if x != 0 and y != 0:
                        self.attack(possStrings[xcount],possStrings[ycount],player)
        else: 
            return False

    #when computer has 1 hand, player has 2 hands. Looks for safest option.
    def AIonlyzeroPriority(self, player):
        if (self.R == 0 or self.L == 0) and (player.R !=0 and player.L != 0):
            #variables so the AI can move on if onlyzeroPriority doesn't execute
            a = 0
            b = 1
            possibilitiesComputer = [self.R, self.L]
            possibilitiesPlayer = [player.R, player.L]
            possStrings = ['r','l']
            xcount = -1
            ycount = -1
            for x in possibilitiesComputer:
                xcount = xcount + 1
                if x != 0:
                    for y in possibilitiesPlayer:
                        ycount = ycount + 1
                        if (x + x + y)%5 == 0:
                            if x % 2 == 0:
                                a = x
                                b = y
                                self.split()
                            elif x % 2 != 0:
                                a = x
                                b = y
                                self.attack(possStrings[xcount],possStrings[1-ycount],player)
            #if attack or split occurs, either x or y would change. a and b avoid this change. This way, the equation remains unaltered from before (line 120) and the AI won't continue to run.
            if (a + a + b)%5 != 0:
                return False
        else:
            return False 

    #This must be in its own function because an elif would mess up the loop in AIonlyzeroPriority. Ensures computer attacks when computer has one hand and player has two
    def AIonlyzero(self, player):
        if (self.R == 0 or self.L == 0) and (player.R !=0 and player.L != 0):
            list = ['r','l']
            if self.R != 0:
                self.attack('r',random.choice(list),player)
            elif self.L != 0:
                self.attack('l',random.choice(list),player)
        else:
            return False

    #Makes sure the computer won't randomly attack a user's disarmed hand if they have one.
    def AIplayer1hand(self, player):
        if (self.R != 0 and self.L != 0) and (player.R == 0 or player.L == 0):
            list = ['r','l']
            x = random.choice(list)
            if player.R != 0:
                self.attack(x,'r',player)
            elif player.L != 0:
                self.attack(x,'l',player)
        else:
            return False

    #random choice of attack
    def AIrandom(self, player):
        list = ['r','l']
        x = random.choice(list)
        y = random.choice(list)
        self.attack(x,y,player)

#ensures that swords remain < 5
def modHand(hand):    
        if hand.getR() > 5:           
            hand.R = hand.getR() % 5
        elif hand.getL() > 5:
            hand.L = hand.getL() % 5
        
#hand is dead if =5
def killHand(hand):
        if hand.getR() == 5:
            hand.R = 0
        elif hand.getL() == 5:
            hand.L = 0

#checks if player made a valid move
def validMove(user):
    move = input("\nWhat do you want to do ('attack' or 'split')? ")

    while move != 'attack' and move != 'split':
        print("That's not a valid input! Try again!")
        move = input("\nWhat do you want to do ('attack' or 'split')? ")

    #check if player has both hands. If so, they cannot split.
    while move == 'split' and (user.getR() != 0 and user.getL() != 0):
        print("You can't split right now! Try again")
        move = input("\nWhat do you want to do ('attack' or 'split')? ")
        while move != 'attack' and move != 'split':
            print("That's not a valid input! Try again!")
            move = input("\nWhat do you want to do ('attack' or 'split')? ")

    #check if player has one hand but it is odd #. If so, they cannot split
    while move == 'split' and ((user.getR() == 0 and user.getL()%2 != 0) or (user.getL() == 0 and user.getR()%2 != 0)):
        print("You can't split right now! Try again")
        move = input("\nWhat do you want to do ('attack' or 'split')? ")
        while move != 'attack' and move != 'split':
            print("That's not a valid input! Try again!")
            move = input("\nWhat do you want to do ('attack' or 'split')? ")
    return move

def checkWinner(computer, user):
    if computer.getR() == 0 and computer.getL() == 0:
        return "you"
    elif user.getR() == 0 and user.getL() == 0:
        return "computer"
    else:
        return ""

def EndGameMessage(winner):
    if winner == 'you':
        return "\nCongratulations! You beat the computer!"
    elif winner == 'computer':
        return "\nThe computer won! You definitely won't be humanity's savior when Skynet comes online!"


def main():
    print("Welcome to SWORDS!\n")
    computer = Hand()
    user = Hand()
    curPlayer = 0
    winner = ""
    print("  Player| L: ", user.getL(), "R: ", user.getR())
    print("Computer| L: ", computer.getL(), "R: ", computer.getR())

    while winner == "":
        
        if curPlayer == 0:
            print("\nIt's your turn.")
            move = validMove(user) 

            if move == 'attack':
                playerHand = input("\nChoose the hand you want to use (r or l): ")
                
                #the 4 while loops check for a valid input and if a hand can be used (both the users' and the computers' hands)
                while playerHand != 'r' and playerHand != 'l':
                    print("That's not a valid input! Try again")
                    playerHand = input("\nChoose the hand you want to use (r or l): ")
                while (playerHand == 'r' and user.getR() == 0) or (playerHand == 'l' and user.getL() == 0):
                    print("You can't use that hand! Try again")
                    playerHand = input("\nChoose the hand you want to use (r or l): ")
                
                compHand = input("Choose the hand you want to attack (r or l): ")
                while compHand != 'r' and compHand != 'l':
                    print("That's not a valid input! Try again")
                    compHand = input("\nChoose the hand you want to use (r or l): ")
                while (compHand == 'r' and computer.getR() == 0) or (compHand == 'l' and computer.getL() == 0):
                    print("You can't choose that hand! Try again")
                    compHand = input("\nChoose the hand you want to attack (r or l): ")

                user.attack(playerHand,compHand,computer)
                modHand(computer)
                killHand(computer)
            elif move == 'split': 
                user.split()

        elif curPlayer == 1:
            print("\nIt's the computer's turn.")
            computer.AI(user)
            modHand(user)
            killHand(user)
        #include print statement that tells who had a hand 'disarmed'
        curPlayer = 1 - curPlayer
        print("\n  Player| L: ", user.getL(), "R: ", user.getR())
        print("Computer| L: ", computer.getL(), "R: ", computer.getR())
        winner = checkWinner(computer, user)

    print(EndGameMessage(winner))

main()

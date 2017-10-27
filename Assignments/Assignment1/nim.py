'''
The game of Nim. This is a well-known game with a number of variants. The following variant has an interesting
winning strategy. Two players alternately take marbles from a pile. In each move, a player chooses
how many marbles to take. The player must take at least one but at most half of the marbles. Then the other 
player takes a turn. The player who takes the last marble loses. //
Write a program in which the computer plays against a human opponent. Generate a random integer
between 10 and 100 to denote the initial size of the pile. Generate a random integer between 0 and 1 
to decide whether the computer or the human takes the frst turn. Generate a random integer between 0 and 1 
to decide whether the computer plays smart or stupid. In stupid mode the computer simply takes a random
legal value (between 1 and n/2) from the pile whenever it has a turn. In smart mode the computer takes 
off enough marbles to make the size of the pile a power of two minus 1—that is, 3, 7, 15, 31, or 63. 
That is always a legal move, except when the size of the pile is currently one less than a power of two. 
In that case, the computer makes a random legal move.
You will note that the computer cannot be beaten in smart mode when it has the frst move,
unless the pile size happens to be 15, 31, or 63. Of course, a human player who has the frst turn 
and knows the winning strategy can win against the computer.
'''
from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = randint(10, 100)
turn = randint(0, 1)
strategy = randint(0, 1)


def nim():
    """
    return True if the winner is human, False if winner is computer. 
    """
    '''
    The function allows the computer to make smart moves and dumb moves at random. Dumb moves are when the computer
    takes marbles at random legal quantities, while smart moves are when the computer uses the logarithmic formula below to calculate how many
    marbles to take so that it leaves the optimal number of marbles for the computer to win. The human is free to make his/her choices as long
    as the move is legal.
    '''
    pile = randint(10, 100)                             #picks random number for starting pile in range 10-100
    turn = randint(0, 1)                                #picks random number that represents which player will have first turn
    strategy = randint(0, 1)                            #picks random number that represents the computer's strategy of playing smart or dumb
    power_two = [3,7,15,31,63]                          #list of powers of twos, winning numbers                          
    # While the game is still being played.
    print("This is the game of nim. Rules are simple: \nEach round, a player is to take a certain number of marbles. \nPlayer must at least take one marble, but cannot take more than half the number of marbles left in the pile. \nThe game ends when there are no marbles left in the pile. The player to take the last marble loses. Good luck have fun!\n")
   
    print("There are % d marbles in the pile to start.\n" % pile)
   
    while pile > 0:
        if turn == COMPUTER:
            if pile == 1:
                # Take the last marble.
                take == 1
                return True #HUMAN won since comp took last marble
            elif strategy == DUMB:
                # Take a random, legal number of marbles from the pile.
                take = randint(1,int(pile*0.5))
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                # The computer is smart, but can't make a smart move.
                # Take a random, legal number of marbles from the pile.
                take = randint(1,int(pile*0.5))
            else:
                # The computer is smart and can make a smart move.
                if pile == 2 or pile == 6 or pile == 14 or pile == 30 or pile == 62: 
                    x = int((log(pile+1))/log(2) - 2)       # Take marbles so that the pile will be be a power of 2, minus 1
                    take = pile - power_two[x]
                else:
                    take = randint(1,int(pile*0.5))
                    #the computer makes its move 

            # Update pile
            pile -= take
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            turn = HUMAN

        elif turn == HUMAN:
            if pile == 1:
                return False #Comp wins since human took last marble
            else:
                print("Your turn. The pile currently has %d marbles in it." % pile)
                take = int(input("How many marbles will you take?\n"))
                # Force the user to take a legal number of marbles.
                if pile == 1:
                    return False
                elif take > pile/2 or take < 1:
                    print("Please take a legal number of marbles.")
                    continue                                         #continues the elif until the input passes the stated condition

            # Update pile
            pile -= take
            print("The pile currently has %d marbles in it.\n" %pile)
            turn = COMPUTER

    return turn == HUMAN

if nim():
    print("You Won!")
else:
    print("The computer won!")

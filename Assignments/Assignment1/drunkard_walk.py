import math
import random

'''
Question: The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four directions 
and stumbles to the next intersection, then again randomly picks one of four directions, and so on. 
You might think that on average the drunkard doesn’t move very far because the choices cancel 
each other out, but that is actually not the case.
'''
def drunkard_walk(x,y,n):
    '''
    Function drunkard_walk takes 3 attributes: x,y to set origin of the drunk, and n to set how many turns he's going to make,
    then calculates the distance of displacement from the drunk's end point to his start point in numbers of blocks away. 
    The random function is used to generate random numbers from 0-3, each representing the direction of the drunk's turn.
    Using for loops, the function repeats itself n times, for the n number of turns the drunk man is to make. The inner function
    uses if else conditions for each possible case of number/direction generated, whereby a move north add 1 to the man's running y coordinate,
    a move south takes out 1 from the man's running y coordinate, east +1 to running x coordinate, and west -1 to running x coordinate.
    The distance/displacement is then calculated by taking the absolute value of the start point minus the end point.
    '''
    x_start = x                             #cretes new variable for x to separate from running x so to be able to calculate displacement
    y_start = y                             #cretes new variable for y to separate from running y so to be able to calculate displacement
    for i in range(n):                      #for all numbers in range n
        turn  = random.randrange(0,4)       #generates random number 0-3 to specify turning direction
        if turn == 0:                       #if turn == 0 -> North
            y += 1                          #add 1 to running y total
        elif turn == 1:                     #if turn == 1 -> South
            y -= 1                          #minus 1 from running y total
        elif turn == 2:                     #if turn == 2 -> East
            x += 1                          #add 1 to running x total
        else:                               #if turn == 3 -> West
            x -= 1                          #minus 1 from running x total
    dist = abs(x_start-x) + abs(y_start-y)  #calculate absolute difference between start point and end point
    return ("%d" % dist)                    #returns result of above formula with 1 digit format
    
x = float(input("enter x coordinate: "))    #prompts user input for x coord
y = float(input("enter y coordinate: "))    #prompts user input for y coord
n = int(input("number of turns:"))          #prompts user input for n turns
print("The drunkard started from (%d,%d)." % (x, y))
distance = drunkard_walk(x, y, n)
print("After", n, "intersections, he's",distance, "blocks from where he started.")
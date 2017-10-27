import math
import random
import turtle                       

drunk = turtle.Turtle()                    #names turtle as drunk

def drunkard_walk(x,y,n):
    '''
    Function drunkard_walk takes three attributes - x and y coordinates, and number of turns for the drunkard to take. 
    The function then uses turtle to draw the path of the drunkard's random decisions. Detailed explanations are commented on
    the side of each line of code.
    '''
    x_start = x
    y_start = y
    drunk.penup()                           #turtle doesn't draw
    drunk.goto(x_start,y_start)             #turtle moves to specified x,y
    drunk.pendown()                         #turtle starts drawing
    drunk.circle(2)                         #turtle draws circle with radius 2 to indicate origin
    for i in range(n):                      
        turn  = random.randrange(0,4)       
        if turn == 0: 
            y += 1
            drunk.setheading(90)            #sets the direction of arrow to north by turning 90deg from start arrow pointing east
        elif turn == 1:
            y -= 1
            drunk.setheading(270)           #sets the direction of arrow to south by turning 270deg from start arrow pointing east
        elif turn == 2:
            x += 1
            drunk.setheading(0)             #sets the direction of arrow to east by not turning
        else:
            x -= 1
            drunk.setheading(180)           #sets the direction of arrow to west by turning 180deg from start arrow pointing east
        drunk.fd(50)
        
    distance = abs(x_start-x) + abs(y_start-y)
    print("After", n, "intersections, he's", distance, "blocks from where he started.")
    x = x_start                             #resets x back to origin
    y = y_start                             #resets x back to origin
    print("The drunkard started from (%d,%d)." % (x, y))

drunkard_walk(50,90,10)


turtle.mainloop()                           #keeps turtle window open

print("Session 5 - Functions II")

import turtle

bear = turtle.Turtle()

print(bear)

#for i in range(4):  #the range has to be an integer
#    bear.fd(100)
#    bear.lt(90)

#for i in range(4):
#    print(i)
#
#turtle.mainloop()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(bear, 180)

#turtle.mainloop()


def polygon(t, length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(bear, 20, 8)
#polygon(bear, n=8, length=20) # this would work 

#turtle.mainloop()

import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n) #sequence of the arguments matter, if it had been t,n,length the function aint gonna run

#circle(bear, 90)

#turtle.mainloop()

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

#arc(bear,100,180)
    
#turtle.mainloop()

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """ 
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

#polyline(bear,20,20,20)
#circle(bear,70)

#turtle.mainloop()


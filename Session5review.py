import turtle
gianca = turtle.Turtle ()

print(gianca)
#turtle.mainloop() #this lets the window stay open, has to be at the bottom of the function

#gianca.fd(100) #forward in steps
#gianca.lt(90) #left in what angle
#gianca.fd(100)
#gianca.lt(90)
#gianca.fd(100)
#gianca.lt(90)
#gianca.fd(100) 

for i in range(4): #loops 4 times
    print("Hello") 

#Exercise 2
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.left(90)

#square(gianca,20)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.left(360/n)

#polygon(gianca,20, 8)

import math
def circle(t, r):
    circumference = 2*math.pi*r
    n=100
    length= circumference / n
    polygon(t, length, n)

#circle(gianca, 50)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 260
    n= int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(gianca, 8, 90)


turtle.mainloop()
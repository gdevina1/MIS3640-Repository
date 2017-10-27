import turtle
import math

import turtle
import math

gianca= turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r *angle /360
    n = int(arc_length / 3) +1
    step_length = arc_length /n
    step_angle = float(angle) / n
    polyline(t,n,step_length, step_angle)

def circle(t,r):
    arc(t, r, 360)

def shape_2(t,r):
    t.hideturtle()
    t.speed(0)
    t.pensize(6)
    circle(t,r)
    arc(t,r/2,180)
    t.setheading(0)
    #t.lt(180)
    #t.circle(-r/2, extent = 175)
    t.penup()
    arc(t,r/2,180)
    t.pendown()
    arc(t,r/2,180)
    t.penup()
    t.sety(r/3)
    t.pendown()
    circle(t,r/6)
    t.penup()
    t.sety(4/3*r)
    t.pendown()
    circle(t,r/6)



   
shape_2(gianca, 40)

turtle.mainloop()
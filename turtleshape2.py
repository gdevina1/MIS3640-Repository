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
    t.speed(100)
    t.hideturtle()
    circle(t,r)
    t.penup()
    t.sety(r)
    t.pendown()
    for i in range(6):
        circle(t, r)
        t.lt(r)
        circle(t, r)
        t.lt(r)

shape_2(gianca, 70)

turtle.mainloop()
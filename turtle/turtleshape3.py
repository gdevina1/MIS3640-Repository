import turtle
import math

import turtle
import math

gianca= turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle, x, y):
    arc_length = 2 * math.pi * r *angle /360
    n = int(arc_length / 3) +1
    step_length = arc_length /n
    step_angle = float(angle) / n
    polyline(t,n,step_length, step_angle)

def circle(t,r,x,y):
    arc(t, r, 360, x, y)

def shape_3(t,r,x,y):
    t.pensize(8)
    t.hideturtle()
    t.speed(60)
    circle(t, r, x, y-r)
    arc(t, r/2, 180, x, y)
    arc(t, r/2, 180, x, y)
    circle(t, r/6, x, y+(r/3))
    circle(t, r/6, x, y-(2*r/3))

shape_3(gianca, 100, 0, 0)


turtle.mainloop()
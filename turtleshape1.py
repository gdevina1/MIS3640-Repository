import math
import turtle

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
    
def shape_1(t, r):
    t.speed(50)
    t.hideturtle()
    circle(t,r)
    t.penup()
    t.sety(r)
    t.pendown()
    t.rt(30)
    for i in range(4):
        t.speed(50)
        t.penup()
        t.fd(r/2)
        t.pendown()
        circle(t, r*(math.sqrt(3)/6))
        t.penup()
        t.goto(0,r)
        t.lt(90)
        t.pendown()
    for i in range(4):
        t.speed(50)
        t.fd(r)
        t.lt(120)
        t.fd(r)
        t.lt(120)
        t.fd(r)
        t.rt(150)

shape_1(gianca, 100)
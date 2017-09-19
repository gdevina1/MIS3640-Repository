print("Session 4 - Functions Exercise")

import math

def quadratic(a, b, c):
        a = float(a)
        b = float(b)
        c = float(c)
        quad_calc_plus = (-b + math.sqrt((b**2)-4*a*c)/2*a)
        quad_calc_min = (-b - math.sqrt((b**2)-4*a*c)/2*a)
        print("The solution(s) to the quadratic equation:" , quad_calc_plus, ",", quad_calc_min)

quadratic(8,-8,0)

#prof's solutions

import math
def quadratic(a,b,c):
        discriminant = b**2 - 4 * a * c
        pass #to be continued

    


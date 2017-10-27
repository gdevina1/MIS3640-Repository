'''

Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.
'''
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

new_point = Point()
new_point.x = 100
new_point.y = 50


class Circle:
    '''
    Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number.
    '''


'''
Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.
'''
circle_a = Point()
circle_a.center = Point()
circle_a.center.x = 150
circle_a.center.y = 100
circle_a.radius = 75

print(circle_a.center.x,',',circle_a.center.y, ',', circle_a.radius)


def point_in_circle(circ, p):
    import math
    '''
    Write a function named point_in_circle that takes a Circle and a Point 
    and returns True if the Point lies in or on the boundary of the circle.
    '''
    distance = math.sqrt((p.x - circ.center.x)**2 + (p.y - circ.center.y)**2)
    return distance <= circ.radius

print(point_in_circle(circle_a,new_point))

'''
Write a function named rect_in_circle that takes a Circle and a Rectangle 
and returns True if the Rectangle lies entirely in or on the boundary of the circle.
'''
pass


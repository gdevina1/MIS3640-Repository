class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
#THE OBJECT IS AN INSTANCE OF A CLASS

new_point = Point()
new_point.x = 100
new_point.y = 50
# print(new_point)
# print(new_point.x, new_point.y)

# Gianca_point = Point() #GIANCA_POINT IS AN INSTANCE OF POINT
# Gianca_point.x = 50
# Gianca_point.y = 60
# print(Gianca_point.x, Gianca_point.y)

# x = Gianca_point.y #x is a variable, y is an attribute
# print(x)

# print(type(Gianca_point))
# print(isinstance(Gianca_point, object))

# import math

# print('(%g, %g)' % (my_point.x, my_point.y))
# distance = math.sqrt(my_point.x**2 + my_point.y**2)
# print(distance)

def print_point(p):
    """Print a Point object in human-readable format."""
    # print('The point is (%g, %g)' % (p.x, p.y))

new_point = Point()
new_point.x = 100
new_point.y = 50

print_point(new_point)



import math 
def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """

    distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    return distance

g_point = Point()
g_point.x = 40
g_point.y = -30
# print(distance_between_points(new_point,g_point))

# print(hasattr(g_point, 'x'))
# print(hasattr(g_point, 'z'))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """



Alex_rect = Rectangle()
Alex_rect.width = 10
Alex_rect.height = 20
Alex_rect.corner = Point()
Alex_rect.corner.x = 1
Alex_rect.corner.y = 1

# print_point(Alex_rect.corner)
# print_point(my_point)

# print(Alex_rect.corner == my_point)
# print(Alex_rect.corner is my_point)


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# print_point(find_center(Alex_rect))


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

# print(Alex_rect.width, Alex_rect.height)
# grow_rectangle(Alex_rect, -4, -10)
# print(Alex_rect.width, Alex_rect.height)


def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)

# print_rectangle(Alex_rect)
# grow_rectangle(Alex_rect, -4, -10)
# print_rectangle(Alex_rect)


def main():
    # my_point = Point()
    # print(Point.__doc__)
    # my_point.x = 3
    # my_point.y = 4
    # print('My point', end=' ')
    # print_point(my_point)

    # print('Is my_point an instance of Point?', isinstance(my_point, Point))
    # print('Is my_point an instance of Rectangle?',
    #       isinstance(my_point, Rectangle))
    # print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    # print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    # box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 0.0
    # box.corner.y = 0.0

    # print('Does box have an attribute x?', hasattr(box, 'x'))

    # print('Does box have an attribute corner?', hasattr(box, 'corner'))

    # print('Rectangle has these:', dir(box))

    # center = find_center(box)
    # print('center', end=' ')
    # print_point(center)

    # print(box.width)
    # print(box.height)
    # print('grow')
    # grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)
    pass

if __name__ == '__main__':
    main()
from Point1 import *
import copy


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """

circle_a = Point()
circle_a.center = Point()
circle_a.center.x = 150
circle_a.center.y = 100
circle_a.radius = 75

print(circle_a.center.x,',',circle_a.center.y, ',', circle_a.radius)

def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    distance = math.sqrt((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)
    return distance <= circle.radius

print(point_in_circle(new_point,circle_a))

def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    rect_w = rect.corner.x + rect.width
    rect_h = rect.corner.y + rect.height
    rect_wd = rect.corner.x - rect.width
    if not (point_in_circle(rect.corner, circle)) or not (point_in_circle(rect_w, circle)) or not (point_in_circle(rect_h, circle)) or not (point_in_circle(rect_wd, circle)):
        return False
    return True

print(rect_in_circle(Alex_rect, circle_a))

def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    rect_w = rect.corner.x + rect.width
    rect_h = rect.corner.y + rect.height
    rect_wd = rect.corner.x - rect.width
    if not ((point_in_circle(rect.corner, circle)) and not (point_in_circle(rect_w, circle)) and not (point_in_circle(rect_h, circle)) and not (point_in_circle(rect_wd, circle))):
        return False
    return True

print(rect_circle_overlap(Alex_rect, circle_a))

def main():
    # box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 50.0
    # box.corner.y = 50.0

    # print(box.corner.x)
    # print(box.corner.y)

    # circle = Circle
    # circle.center = Point()
    # circle.center.x = 150.0
    # circle.center.y = 100.0
    # circle.radius = 75.0

    # print(circle.center.x)
    # print(circle.center.y)
    # print(circle.radius)

    # print(point_in_circle(box.corner, circle))
    # print(rect_in_circle(box, circle))
    # print(rect_circle_overlap(box, circle))
    pass


if __name__ == '__main__':
    main()

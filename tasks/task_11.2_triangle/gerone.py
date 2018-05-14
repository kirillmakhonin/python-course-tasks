#!/usr/bin/env python
"""
Provides triangle class and functions for computing
triangle area using Gerones formula
"""


class TriangleError(Exception):
    """
    Exception for all things with triangles
    """
    pass


class Triangle():
    """
    Triangle class stores vertices coordinates and computes area

    >>> Triangle([(0, 0), (0, 3), (4, 0)]).area
    6.0
    """
    def __init__(self, points):
        """
        Initiate triangle with points coordinates

        :param points: vertices coordinates [(1, 2), (3, 4), (0,5)]
        :type points: list(tuple)
        """
        self.points = points

    def __setattr__(self, name, value):
        # Perform checks on setting instance.points attribute
        if name == 'points':
            self.points_valid(value) # raises TriangleError 
        super().__setattr__(name, value)

    @property
    def area(self):
        """
        Compute triangle area

        :return: Triangle area
        :rtype: float
        """
        return gerone_from_coords(*self.points)

    @staticmethod
    def points_valid(points):
        """
        Perform checks to verify triangle from points has some area,
        raises TriangleError

        :param points: vertices coordinates [(1, 2), (3, 4), (0,5)]
        :type points: list(tuple)
        :return: triangle has valid coordinates
        :rtype: bool
        :raises TriangleError: if somehow triangle points are in conflict with basic math
        """
        a = distance(points[0], points[1])
        b = distance(points[0], points[2])
        c = distance(points[1], points[2])
        if a*b*c == 0:
            raise TriangleError('Some points are in the same place')
        elif (a == b+c or b == a+c or c == a+b):
            raise TriangleError('Points on the same line')
        elif (a > b+c or b > a+c or c > a+b):
            raise TriangleError('One side is longer than sum of other two')
        return True


def gerone_from_coords(point1, point2, point3):
    """
    Compute triangle area from point coordinates

    :param point1: First point
    :type point1: tuple(float, float)
    :param point2: Second point
    :type point2: tuple(float, float)
    :param point3: Third point
    :type point3: tuple(float, float)
    :return: triangle area
    :rtype: float

    >>> gerone_from_coords((0,0), (0,3), (4,0))
    6.0
    """
    a = side_len(*point1, *point2)
    b = side_len(*point1, *point3)
    c = side_len(*point2, *point3)

    if a*b*c == 0:
        raise NotATriangle('Some points are in the same place')
    elif (a == b+c or b == a+c or c == a+b):
        raise NotATriangle('Points on the same line')
    elif (a > b+c or b > a+c or c > a+b):
        raise NotATriangle('One side is longer than sum of other two')
    return not_safe_gerone(a, b, c)


def not_safe_gerone(a, b, c):
    """
    Compute triangle area from valid sides lengths

    :param float a: first side length
    :param float b: second side length
    :param float c: third side length
    :return: float -- triangle area

    >>> not_safe_gerone(3, 4, 5)
    6.0
    """
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**(1/2)


def distance(point1, point2):
    """
    Distance between two points

    :param tuple point1: first point coordinates (1, 2)
    :param tuple point2: second point coordinates (3.0, 4)
    :return: line segment length
    :rtype: float

    >>> distance((0, 0) (3, 4.0))
    5.0
    """
    x1, y1 = point1
    x2, y2 = point2
    
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)


def point_input(num):
    """
    Input two coordinates

    :param int num: points number to print
    :return: point coordinates (x, y)
    :rtype: tuple

    doctests work poorly with promts
    """
    while True:
        try:
            x = float(input(f'{num} point x: '))
            y = float(input(f'{" "*7+" "*len(str(num))}y: '))
            break
        except ValueError:
            print('Invalid coodinate!')
    return x, y


if __name__ == '__main__':
    while True:
        # Input block
        coords = [point_input(i) for i in range(1, 4)]

        # Calculation block
        try:
            area = gerone_from_coords(*coords)
            print(f"Your triangles area: {area}")
            break
        except NotATriangle as e:
            print(e)
            continue

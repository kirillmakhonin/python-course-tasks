#!/usr/bin/env python
"""
Module computes triangle area from 3 point coordinates
using Gerones' formula
"""


class NotATriangle(Exception):
    """
    Exception for invalid triangles
    """
    pass


def gerone_from_coords(point1, point2, point3):
    """
    Compute triangle area from point coordinates

    :param point1: First point
    :type point1: tuple(float, float)
    :param point2: Second point
    :type point2: tuple(float, float)
    :param point3: Third point
    :type point3: tuple(float, float)
    :return: float -- triangle area

    >>> gerone_from_coords((0,0), (0,3), (4,0))
    5.0
    """
    a = side_len(*point1, *point2)
    b = side_len(*point1, *point3)
    c = side_len(*point2, *point3)

    if a*b*c == 0:
        raise NotATriangle('Some points are the same')
    elif (a == b+c or b == a+c or c == a+b):
        raise NotATriangle('Points on the same line')
    elif (a > b+c or b > a+c or c > a+b):
        raise NotATriangle
    return not_safe_gerone(a, b, c)


def not_safe_gerone(a, b, c):
    """
    Compute triangle area from sides' lengths

    :param float a: first side length
    :param float b: second side length
    :param float c: third side length
    :return: float -- triangle area

    >>> not_safe_gerone(3, 4, 5)
    6.0
    """
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**(1/2)


def side_len(x1, y1, x2, y2):
    """
    Side length from point coordinates


    :param float x1: first point x-axis coordinate
    :param float y1: first point y-axis coordinate
    :param float x2: second point x-axis coordinate
    :param float y2: second point y-axis coordinate
    :return: float -- line length

    >>> side_len(0,0,3,4.0)
    5.0
    """
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)


def point_input(num):
    """
    Input two coordinates

    :return: (float, float) -- coodinates
    """

    x = float(input(f'{num} point x: '))
    y = float(input(f'        y: '))
    return (x, y)


if __name__ == '__main__':
    while True:
        # Input block
        try:
            coords = [point_input(i) for i in range(1, 4)]
        except ValueError:
            print('Invalid coodinate!')
            continue

        # Calculation block
        try:
            area = gerone_from_coords(*coords)
            print(f"Your triangles area: {area}")
            break
        except NotATriangle as e:
            print(e)
            continue

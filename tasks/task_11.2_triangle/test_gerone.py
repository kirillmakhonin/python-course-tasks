#!/usr/bin/env python
from unittest.mock import patch
import unittest
import gerone


mocked_input = """0 0 0 3 4 0""".split()


@patch(target='builtins.input', side_effect=mocked_input)
class TestInput(unittest.TestCase):

    def setUp(self):
        super().setUp()
    
    def test_valid_input(self, mock):
        self.assertEqual(input(), '0')

    def test_something(*args):
        pass


class TestTriangleClass(unittest.TestCase):
    valid_points = [
            (0, 0),
            (3, 0),
            (0, 4)]
    points_on_same_line = [
            (0, 0),
            (0, 5),
            (0, 6)]
    
    def test_invalid_points_init(self):
        with self.assertRaises(gerone.TriangleError):
            gerone.Triangle(self.points_on_same_line)
    def test_valid_points_init(self):
        gerone.Triangle(self.valid_points)



if __name__ == '__main__':
    unittest.main()
    doctest.testmod(gerone)

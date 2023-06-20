#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        # Test case: Creating a rectangle with default values
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        #self.assertIsNone(r.id)

        # Test case: Creating a rectangle with custom values
        r = Rectangle(5, 5, 2, 3, 123)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 123)

    def test_getters_and_setters(self):
        r = Rectangle(10, 10)

        # Test case: Testing width getter and setter
        r.width = 20
        self.assertEqual(r.width, 20)

        # Test case: Testing height getter and setter
        r.height = 15
        self.assertEqual(r.height, 15)

        # Test case: Testing x-coordinate getter and setter
        r.x = 5
        self.assertEqual(r.x, 5)

        # Test case: Testing y-coordinate getter and setter
        r.y = 8
        self.assertEqual(r.y, 8)

    def test_area(self):
        # Test case: Calculating the area of a rectangle
        r = Rectangle(4, 6)
        self.assertEqual(r.area(), 24)

        # Test case: Calculating the area of a square
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)


if __name__ == '__main__':
    unittest.main()

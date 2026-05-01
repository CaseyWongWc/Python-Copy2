from Helpers.helpings import *

import unittest


# User-defined class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius**2


# Class to test Circle
class TestCircle(unittest.TestCase):
    def test_compute_area(self):
        c = Circle(0)
        self.assertEqual(c.compute_area(), 0.0)

        c = Circle(5)
        self.assertEqual(c.compute_area(), 78.5)

    def test_will_fail(self):
        c = Circle(5)
        self.assertLess(c.compute_area(), 0)


if __name__ == "__main__":
    unittest.main()

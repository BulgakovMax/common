import unittest
import math

from homework import Rectangle

class TestForRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rectangle1 = Rectangle(6, 8)
        self.rectangle2 = Rectangle(6, 6)
        self.rectangle3 = Rectangle(0, 0)
        

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.rectangle1.get_rectangle_perimeter(), 28)
        self.assertEqual(self.rectangle2.get_rectangle_perimeter(), 24)
        self.assertEqual(self.rectangle3.get_rectangle_perimeter(), 0)


    def test_get_rectangle_square(self):
        self.assertEqual(self.rectangle1.get_rectangle_square(), 48)
        self.assertEqual(self.rectangle2.get_rectangle_square(), 36)
        self.assertEqual(self.rectangle3.get_rectangle_square(), 0)


    def test_get_sum_of_corners(self):
        self.assertEqual(self.rectangle1.get_sum_of_corners(4), 360)
        self.assertEqual(self.rectangle1.get_sum_of_corners(1), 90)


    def test_get_sum_of_corners_false(self):
        with self.assertRaises(ValueError):
            self.rectangle1.get_sum_of_corners(5)
            self.rectangle1.get_sum_of_corners(0)
            self.rectangle1.get_sum_of_corners(-4)


    def test_get_rectangle_diagonal(self):
        self.assertEqual(round(self.rectangle1.get_rectangle_diagonal(), 10), 10.0)
        self.assertEqual(round(self.rectangle2.get_rectangle_diagonal(), 8), 8.48528137)


    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(round(self.rectangle2.get_radius_of_circumscribed_circle(), 4), 4.2426)


    def get_radius_of_circumscribed_circle_false(self):
        with self.assertRaises(ValueError):
            self.rectangle1.get_radius_of_circumscribed_circle()
            self.rectangle3.get_radius_of_circumscribed_circle()


    def test_radius_of_inscribed_circle(self):
        self.assertEqual(self.rectangle1.get_radius_of_inscribed_circle(),  math.sqrt(100) / (2 * math.sqrt(2)))


    def get_radius_of_inscribed_circle_false(self):
        with self.assertRaises(ValueError):
            self.rectangle2.get_radius_of_inscribed_circle()
        with self.assertRaises(ValueError):
            self.rectangle3.get_radius_of_inscribed_circle()


if __name__ == '__main__':
    unittest.main()
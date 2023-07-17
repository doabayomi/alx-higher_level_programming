import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_valid_attributes(self):
        # Test creating Rectangle instances with valid attributes
        rectangle1 = Rectangle(2, 3)
        self.assertEqual(rectangle1.width, 2)
        self.assertEqual(rectangle1.height, 3)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)

        rectangle2 = Rectangle(5, 10, 1, 2, 4)
        self.assertEqual(rectangle2.width, 5)
        self.assertEqual(rectangle2.height, 10)
        self.assertEqual(rectangle2.x, 1)
        self.assertEqual(rectangle2.y, 2)
        self.assertEqual(rectangle2.id, 4)

    def test_invalid_attributes(self):
        # Test creating Rectangle instances with invalid attributes
        with self.assertRaises(TypeError):
            Rectangle("2", 3)
        with self.assertRaises(TypeError):
            Rectangle(2, "3")
        with self.assertRaises(TypeError):
            Rectangle(2, 3, "1", 2)
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 1, "2")
        with self.assertRaises(ValueError):
            Rectangle(0, 3)
        with self.assertRaises(ValueError):
            Rectangle(2, -3)
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -1, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, 3, 1, -2)

    def test_area(self):
        # Test calculating the area of Rectangle instances
        rectangle1 = Rectangle(2, 3)
        self.assertEqual(rectangle1.area(), 6)

        rectangle2 = Rectangle(5, 10)
        self.assertEqual(rectangle2.area(), 50)

    def test_display(self):
        # Test displaying the Rectangle instances
        rectangle1 = Rectangle(2, 3)
        expected_output1 = "##\n \
                           ##\n \
                           ##\n"
        self.assertEqual(rectangle1.display(), None)

    def test_str(self):
        # Test string representation of Rectangle instances
        rectangle1 = Rectangle(2, 3, 1, 2, 4)
        self.assertEqual(str(rectangle1), "[Rectangle] (4) 1/2 - 2/3")

        rectangle2 = Rectangle(5, 10)
        self.assertEqual(str(rectangle2), "[Rectangle] (28) 0/0 - 5/10")

    def test_update(self):
        # Test updating attributes of Rectangle instances
        rectangle = Rectangle(2, 3)
        rectangle.update(5)
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

        rectangle.update(6, 4)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

        rectangle.update(7, 4, 5)
        self.assertEqual(rectangle.id, 7)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

        rectangle.update(8, 4, 5, 1)
        self.assertEqual(rectangle.id, 8)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 0)

        rectangle.update(9, 4, 5, 1, 2)
        self.assertEqual(rectangle.id, 9)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)

    def test_to_dictionary(self):
        # Test getting dictionary representation of Rectangle instances
        rectangle = Rectangle(2, 3, 1, 2, 4)
        expected_dict = {'id': 4, 'width': 2, 'height': 3, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_create(self):
        # Test creating instances using the create class method
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_load_from_file(self):
        # Test loading instances from file
        rectangle1 = Rectangle(2, 3, 1, 2, 4)
        rectangle2 = Rectangle(5, 10, 3, 4, 5)
        Rectangle.save_to_file([rectangle1, rectangle2])

        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles, list)
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertEqual(loaded_rectangles[0].id, 4)
        self.assertEqual(loaded_rectangles[0].width, 2)
        self.assertEqual(loaded_rectangles[0].height, 3)
        self.assertEqual(loaded_rectangles[0].x, 1)
        self.assertEqual(loaded_rectangles[0].y, 2)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[1].id, 5)
        self.assertEqual(loaded_rectangles[1].width, 5)
        self.assertEqual(loaded_rectangles[1].height, 10)
        self.assertEqual(loaded_rectangles[1].x, 3)
        self.assertEqual(loaded_rectangles[1].y, 4)


if __name__ == '__main__':
    unittest.main()

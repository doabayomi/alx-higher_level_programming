import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_rectangle(self):
        # Test creating a Rectangle instance using create() method
        rectangle_dict = {'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_create_square(self):
        # Test creating a Square instance using create() method
        square_dict = {'size': 8, 'x': 1, 'y': 2}
        square = Square.create(**square_dict)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_load_from_file(self):
        # Test loading instances from file
        rectangle1 = Rectangle(3, 4)
        rectangle2 = Rectangle(5, 6)
        rectangle_list = [rectangle1, rectangle2]
        Rectangle.save_to_file(rectangle_list)
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)

        square1 = Square(7)
        square2 = Square(9)
        square_list = [square1, square2]
        Square.save_to_file(square_list)
        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertIsInstance(loaded_squares[1], Square)

    def test_load_from_file_nonexistent(self):
        # Test loading instances from a nonexistent file
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)

        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 2)

    def test_create_invalid_attributes(self):
        # Test creating instances with invalid attribute values
        rectangle_dict = {'width': -5, 'height': 10, 'x': 2, 'y': 3}
        with self.assertRaises(ValueError):
            Rectangle.create(**rectangle_dict)

        square_dict = {'size': -8, 'x': 1, 'y': 2}
        with self.assertRaises(ValueError):
            Square.create(**square_dict)

        rectangle_dict = {'width': 8.5, 'height': 10, 'x': 2, 'y': 3}
        with self.assertRaises(TypeError):
            Rectangle.create(**rectangle_dict)

    def test_create_missing_attributes(self):
        # Test creating instances with missing attributes
        rectangle_dict = {'width': 5, 'x': 2, 'y': 3}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 3)  # Default height is 1
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

        square_dict = {'size': 8, 'y': 2}
        square = Square.create(**square_dict)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 0)  # Default x is 0
        self.assertEqual(square.y, 2)

    def test_create_extra_attributes(self):
        # Test creating instances with extra attributes
        rectangle_dict = {'width': 5, 'height': 10, 'x': 2, 'y': 3, 'bg': 'an'}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertFalse(hasattr(rectangle, 'bg'))

        square_dict = {'size': 8, 'x': 1, 'y': 2, 'weight': 2.5}
        square = Square.create(**square_dict)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertFalse(hasattr(square, 'weight'))


if __name__ == '__main__':
    unittest.main()

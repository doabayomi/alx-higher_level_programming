import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    def test_valid_attributes(self):
        # Test creating Square instances with valid attributes
        square1 = Square(2)
        self.assertEqual(square1.width, 2)
        self.assertEqual(square1.height, 2)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)

        square2 = Square(5, 1, 2, 4)
        self.assertEqual(square2.width, 5)
        self.assertEqual(square2.height, 5)
        self.assertEqual(square2.x, 1)
        self.assertEqual(square2.y, 2)
        self.assertEqual(square2.id, 4)

    def test_invalid_attributes(self):
        # Test creating Square instances with invalid attributes
        with self.assertRaises(TypeError):
            Square("2")
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)

    def test_area(self):
        # Test calculating the area of Square instances
        square1 = Square(2)
        self.assertEqual(square1.area(), 4)

        square2 = Square(5)
        self.assertEqual(square2.area(), 25)

    def test_display(self):
        # Test displaying the Square instances
        square1 = Square(2)
        expected_output1 = "##\n \
                           ##\n"
        self.assertEqual(square1.display(), None)

    def test_str(self):
        # Test string representation of Square instances
        square1 = Square(2, 1, 2, 4)
        self.assertEqual(str(square1), "[Square] (4) 1/2 - 2")

        square2 = Square(5)
        self.assertEqual(str(square2), "[Square] (38) 0/0 - 5")

    def test_update(self):
        # Test updating attributes of Square instances
        square = Square(2)
        square.update(5)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        square.update(6, 4)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        square.update(7, 4, 1)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 0)

        square.update(8, 4, 1, 2)
        self.assertEqual(square.id, 8)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_to_dictionary(self):
        # Test getting dictionary representation of Square instances
        square = Square(2, 1, 2, 4)
        expected_dict = {'id': 4, 'size': 2, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_create(self):
        # Test creating instances using the create class method
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

        square_dict2 = {'id': 2, 'size': 6}
        square2 = Square.create(**square_dict2)
        self.assertIsInstance(square2, Square)
        self.assertEqual(square2.id, 2)
        self.assertEqual(square2.width, 6)
        self.assertEqual(square2.height, 6)
        self.assertEqual(square2.x, 0)
        self.assertEqual(square2.y, 0)

    def test_load_from_file(self):
        # Test loading instances from file
        square1 = Square(2, 1, 2, 4)
        square2 = Square(5, 3, 4, 5)
        Square.save_to_file([square1, square2])

        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertIsInstance(loaded_squares[1], Square)
        self.assertEqual(loaded_squares[0].id, 4)
        self.assertEqual(loaded_squares[0].width, 2)
        self.assertEqual(loaded_squares[0].height, 2)
        self.assertEqual(loaded_squares[0].x, 1)
        self.assertEqual(loaded_squares[0].y, 2)
        self.assertEqual(loaded_squares[1].id, 5)
        self.assertEqual(loaded_squares[1].width, 5)
        self.assertEqual(loaded_squares[1].height, 5)
        self.assertEqual(loaded_squares[1].x, 3)
        self.assertEqual(loaded_squares[1].y, 4)


if __name__ == '__main__':
    unittest.main()

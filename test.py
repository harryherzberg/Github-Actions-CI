import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(1, 1), 0)

    def test_multiply_1(self):
        self.assertEqual(example.multiply(1, 1), 1)
    
    def test_divide_1(self):
        self.assertEqual(example.devide(1, 1), 1)

if __name__ == '__main__':
    unittest.main()

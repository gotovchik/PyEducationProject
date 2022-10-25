import unittest
from homework_09.code.array_diff import array_diff


class TestArray(unittest.TestCase):
    def test_array0(self):
        self.assertEqual(array_diff([1, 2], [1]), [2])

    def test_array1(self):
        self.assertEqual(array_diff([1, 6, 7], [6]), [1, 7])

    def test_array2(self):
        self.assertEqual(array_diff([1, 2, 2], [2]), [1])

    def test_array3(self):
        self.assertEqual(array_diff([3, 4], []), [3, 4])

    def test_array4(self):
        self.assertEqual(array_diff([], [4, 6]), [])


if __name__ == '__main__':
    unittest.main()

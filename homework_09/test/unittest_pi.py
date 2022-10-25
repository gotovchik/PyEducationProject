import unittest
from homework_09.code.pi import truncate


class TestTruncate(unittest.TestCase):
    def test_truncate0(self):
        self.assertEqual(truncate(5), 3.14159)

    def test_truncate1(self):
        self.assertEqual(truncate(4), 3.1415)

    def test_truncate2(self):
        self.assertEqual(truncate(3), 3.141)

    def test_truncate3(self):
        self.assertEqual(truncate(2), 3.14)


if __name__ == '__main__':
    unittest.main()

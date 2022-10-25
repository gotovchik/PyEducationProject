import unittest
from homework_09.code.pi import truncate


class TestTruncate(unittest.TestCase):
    def test_truncate(self):
        self.assertEqual(truncate(5), 3.14159)


if __name__ == '__main__':
    unittest.main()

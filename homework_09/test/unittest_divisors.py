import unittest

from homework_09.code.divisors import get_divisors


class TestDivisors(unittest.TestCase):
    def test_get_divisors_equal(self):
        self.assertEqual(get_divisors(15), 4)

    def test_get_divisors_notequal(self):
        self.assertNotEqual(get_divisors(13), 5)


if __name__ == '__main__':
    unittest.main()
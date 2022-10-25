import unittest
from homework_09.code.digits import get_digits


class TestDigits(unittest.TestCase):
    def test_get_digits_equal(self):
        self.assertEqual(get_digits(154234), [1, 5, 4, 2, 3, 4])

    def test_get_digits_notequal(self):
        self.assertNotEqual(get_digits(132134112), [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
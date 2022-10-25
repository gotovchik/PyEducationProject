import unittest

from homework_09.code.prime import is_prime


class TestPrime(unittest.TestCase):
    def test_is_prime_false(self):
        self.assertFalse(is_prime(15))

    def test_is_prime_true(self):
        self.assertTrue(is_prime(13))


if __name__ == '__main__':
    unittest.main()
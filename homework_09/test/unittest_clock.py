import unittest
from homework_09.code.clock import past


class TestClock(unittest.TestCase):
    def test_clock0(self):
        self.assertEqual(past(0, 1, 1), 61000)

    def test_clock1(self):
        self.assertEqual(past(1, 1, 1), 3661000)

    def test_clock2(self):
        self.assertEqual(past(0, 0, 0), 0)

    def test_clock3(self):
        self.assertEqual(past(1, 0, 1), 3601000)

    def test_clock4(self):
        self.assertEqual(past(1, 0, 0), 3600000)

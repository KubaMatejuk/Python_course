from unittest import TestCase
from silnia import silnia, NotIntError

class TestSilnia(TestCase):
    def test_silnia(self):
        self.assertEqual(silnia(0),2)

    def test_badargument(self):
        with self.assertRaises(NotIntError):
            silnia("dwa")
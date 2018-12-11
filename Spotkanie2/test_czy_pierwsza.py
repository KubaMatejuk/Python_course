from unittest import TestCase

from zadanie4 import czy_pierwsza


class TestCzy_pierwsza(TestCase):
    def test_czy_pierwsza(self):
        self.assertEqual(True,czy_pierwsza(5))
        self.assertEqual(False, czy_pierwsza(6))

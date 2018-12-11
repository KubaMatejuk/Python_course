from unittest import TestCase
from zadanie6 import *


class TestSuma_dzielnikow(TestCase):
    def test_suma_dzielnikow(self):
        self.assertEqual(suma_dzielnikow(6),[1,2,3])
        self.assertEqual(suma_dzielnikow(8), [1, 2, 4])

from unittest import TestCase

from vit import *


class TestVat(TestCase):
    def test_vat(self):
        list = [0.2, 0.5, 4.59, 6]
        self.assertAlmostEqual(vat_faktura(list),vat_paragon(list),1)

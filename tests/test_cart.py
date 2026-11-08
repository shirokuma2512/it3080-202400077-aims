import contextlib
import io
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.output = io.StringIO()
        self.capture = contextlib.redirect_stdout(self.output)
        self.capture.__enter__()
        self.addCleanup(self.capture.__exit__, None, None, None)

    def test_add_dvd_until_full(self):
        for number in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(self.cart.add_dvd(DigitalVideoDisc(str(number), cost=1)))
        before = list(self.cart.items)
        self.assertFalse(self.cart.add_dvd(DigitalVideoDisc("DVD 21", cost=100)))
        self.assertEqual(before, self.cart.items)
        self.assertEqual(MAX_NUMBERS_ORDERED, len(self.cart.items))
        self.assertEqual(MAX_NUMBERS_ORDERED, self.cart.total_cost())

    def test_remove_dvd(self):
        dvd = DigitalVideoDisc("The Lion King", cost=19.95)
        self.assertFalse(self.cart.remove_dvd(dvd))
        self.assertTrue(self.cart.add_dvd(dvd))
        self.assertTrue(self.cart.remove_dvd(dvd))
        self.assertEqual([], self.cart.items)
        self.assertEqual(0, self.cart.total_cost())
        self.assertFalse(self.cart.remove_dvd(dvd))

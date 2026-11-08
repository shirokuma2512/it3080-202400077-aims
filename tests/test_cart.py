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

    def test_discounted_total(self):
        self.cart.add_dvd(DigitalVideoDisc("A", cost=40))
        self.cart.add_dvd(DigitalVideoDisc("B", cost=60))
        for percent, expected in [(0, 100), (20, 80), (100, 0), (12.5, 87.5)]:
            with self.subTest(percent=percent):
                self.assertAlmostEqual(expected, self.cart.total_cost_with_discount(percent))
        self.assertEqual(100, self.cart.total_cost())
        self.assertEqual(0, Cart().total_cost_with_discount(20))

    def test_invalid_discount_percent(self):
        for percent in [-1, 100.01, 150, float("nan"), float("inf"), -float("inf")]:
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    self.cart.total_cost_with_discount(percent)

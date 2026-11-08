import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class CategorySearchTests(unittest.TestCase):
    def test_search_by_category(self):
        a = DigitalVideoDisc("The Lion King", "Animation")
        b = DigitalVideoDisc("Aladdin", "Animation")
        c = DigitalVideoDisc("Star Wars", "Science Fiction")
        items = [a, b, c]
        self.assertEqual([a, b], search_by_category(items, "ANIMATION"))
        self.assertEqual([c], search_by_category(items, "science fiction"))
        self.assertEqual([], search_by_category(items, "Anim"))
        self.assertEqual([], search_by_category([], "Animation"))
        self.assertEqual([], search_by_category(items, ""))
        self.assertEqual([a, b, c], items)

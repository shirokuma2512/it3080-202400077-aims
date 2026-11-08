import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TitleSearchTests(unittest.TestCase):
    def test_search_by_title_case_insensitive(self):
        a = DigitalVideoDisc("The Lion King")
        b = DigitalVideoDisc("Aladdin")
        c = DigitalVideoDisc("Lion documentary")
        items = [a, b, c]
        for keyword in ["lion", "LION", "LiOn"]:
            with self.subTest(keyword=keyword):
                self.assertEqual([a, c], search_by_title(items, keyword))
        self.assertEqual([], search_by_title(items, "missing"))
        self.assertEqual([], search_by_title([], "lion"))
        self.assertEqual(items, search_by_title(items, ""))
        self.assertEqual([a, b, c], items)

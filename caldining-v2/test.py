import unittest
from bs4 import BeautifulSoup
from classes import *

class WebscraperTestCase(unittest.TestCase):
    def setUp(self):
        with open('example.html', 'r') as f:
            html = f.read()
            self.soup = BeautifulSoup(html, 'html.parser')
            self.dining_halls = self.soup.find_all('li', class_='location-name')

    def test_HTMLElement(self):
        dining_halls = self.soup.find_all('li', class_='location-name')

        cafe_3 = self.dining_halls[0]

        el = HTMLElement(cafe_3)
        self.assertEqual(el.get_text(), 'Cafe 3')
        self.assertEqual(el.get_soup(), cafe_3)
        with self.assertRaises(AssertionError):
            HTMLElement('not type(soup) element')

        for el, name in zip(dining_halls, ['Cafe 3', 'Clark Kerr Campus', 'Crossroads', 'Foothill']):
            html_element = HTMLElement(el)
            self.assertEqual(str(html_element), name)

unittest.main()
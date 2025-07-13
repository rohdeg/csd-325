""" test_cities.py by Garrett Rohde
    07/13/2025
    Assignment 7.2
    Test Cases
"""

import unittest
from city_functions import city_country

class TestCities(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("milan", "italy"), "Milan, Italy")

    def test_city_country_population(self):
        self.assertEqual(city_country("london", "england", 8950000),
                         "London, England - population: 8950000")

    def test_city_country_population_language(self):
        self.assertEqual(city_country("paris", "france", 2005000, "french"),
                         "Paris, France - population: 2005000, language: French")


if __name__ == '__main__':
    unittest.main()

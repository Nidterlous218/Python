import unittest

from city_functions import city_country_name

class TestCityCountryName(unittest.TestCase):
    """Test if the function works as expected."""

    def test_city_country(self):
        name = city_country_name('santiago', 'chile')
        self.assertEqual(name, 'Santiago, Chile.')
    
    def test_city_country_population(self):
        name = city_country_name('santiago', 'chile', population = '5000000')
        self.assertEqual(name, 'Santiago, Chile - population 5000000.')

unittest.main()
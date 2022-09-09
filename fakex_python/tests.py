"""Tests for Currency Rates Library"""
from unittest import TestCase
from fakex_python.converter import CurrencyRates
from fakex_python.converter import CurrencyCodes
# from converter import CurrencyNotSupportedError

class TestCurrencyRates(TestCase):

    def setUp(self):
        self.rates = CurrencyRates()

    def test_get_rates(self):
        test_rates = self.rates.get_rates("USD")

        self.assertIsInstance(test_rates, object)
        self.assertEqual(test_rates["USD"], 1.000000)
        self.assertEqual(test_rates["JPY"], 143.909168)

        test_rates2 = self.rates.get_rates("MXN")

        self.assertIsInstance(test_rates, object)
        self.assertAlmostEqual(test_rates2["USD"], 0.050073899060233094)
        self.assertAlmostEqual(test_rates2["JPY"], 7.206093152274126)

        # Look up how to test that proper error is raised
        # self.assertRaises(
        #     CurrencyNotSupportedError, 
        #     self.rates.get_rates("fake code"))

    def test_get_rate(self):
        test_rate = self.rates.get_rate("USD", "USD")

        self.assertEqual(test_rate, 1.0)

    def test_convert(self):
        test_conversion = self.rates.convert("USD", "CAD", 100)

        self.assertEqual(test_conversion, 130.7884)


class TestCurrencyCodes(TestCase):

    def setUp(self):
        self.codes = CurrencyCodes()

    def test_get_symbol(self):
        test_symbol = self.codes.get_symbol("JPY")
        self.assertEqual(test_symbol, "¥")

        test_symbol2 = self.codes.get_symbol("EUR")
        self.assertEqual(test_symbol2, "€")

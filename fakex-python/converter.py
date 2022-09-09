from rates import USD_RATES
from symbols import CURRENCY_SYMBOLS


class CurrencyNotSupportedError(Exception):
    """Error for when currency does not exist in the db"""


class CurrencyRates:
    """Class handling currency rates and conversion"""

    def __init__(self):
        self.USD_RATES = USD_RATES
        self.CURRENCY_SYMBOLS = CURRENCY_SYMBOLS

    def get_rates(self, code_from):
        """Get rates for one currency"""

        rates = {}
        for currency_code in self.USD_RATES:
            rates[currency_code] = self._calculate_rate(
                code_from, currency_code)

        return rates

    def get_rate(self, code_from, code_to):
        """Get rate from one currency to another"""

        return self._calculate_rate(code_from, code_to)

    def convert(self, code_from, code_to, amount):
        """Convert amount from one currency to another"""

        rate = self._calculate_rate(code_from, code_to)

        return rate * amount

    def _calculate_rate(self, code_from, code_to):
        """inner function to calculate rate using USD as go between"""
        self._check_codes([code_from, code_to])
        return self.USD_RATES[code_to] / self.USD_RATES[code_from]

    def _check_codes(self, codes=[]):
        """checks if list of codes are valid (in rates object)"""
        for code in codes:
            if code not in self.CURRENCY_SYMBOLS.keys():
                raise CurrencyNotSupportedError(
                    f'{code} is not a currency supported by Fakex-Python')


class CurrencyCodes:
    """Class handling currency codes and symbols"""

    def __init__(self):
        self.CURRENCY_SYMBOLS = CURRENCY_SYMBOLS

    def get_symbol(self, code):
        return CURRENCY_SYMBOLS[code]

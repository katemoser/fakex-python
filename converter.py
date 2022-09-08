from rates import USD_RATES
from symbols import CURRENCY_SYMBOLS

class CurrencyRates:
    """Class handling currency rates and conversion"""

    def get_rates(self, code_from):
        """Get rates for one currency"""

        rates = {}
        for currency_code in USD_RATES:
            rates[currency_code] = self._calculate_rate(code_from, currency_code)/1

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
        return 1/USD_RATES[code_from] * USD_RATES[code_to]



class CurrencyCodes:
    """Class handling currency codes and symbols"""

    def get_symbol(self, code):
        return CURRENCY_SYMBOLS[code]
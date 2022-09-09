ABOUT FAKEX-PYTHON

This library was built as a backup to forex-python, in the event that the API 
goes down and our students need to use a forex library.

It uses a static list of example exchange rates and is NOT accurate or 
up-to-date. This is for practice/educational purposes only and should not be 
used in any sort of official/professional capacity.

BUILT WITH

GETTING STARTED

make a venv

pip install

```
pip install git+https://github.com/katemoser/fakex-python
```

USAGE

You can find the full documentation here: docs

Here are some examples of how to use this library:

- Initialize the CurrencyRates class

```python
from fakex_python import CurrencyRates
r = CurrencyRates()
```

- Get all exchange rates for one currency

```python
r.get_rates("JPY")

{
    'USD': 0.006948827610482746,
    'EUR': 0.006950398045522716,
    'GBP': 0.006034890007841613,
    'CAD': 0.009088260450508616,
    'AUD': 0.01028017200405189,
    'JPY': 1.0,
    'INR': 0.5538777904684988,
    'NZD': 0.01146052765727893,
    'SGD': 0.009759996666786373,
    'CHF': 0.0067457620212216084,
    'THB': 0.25358001513843786,
    'ZAR': 0.12152186857198702,
    'RUB': 0.4238489656197582,
    'HKD': 0.05454247292986921,
    'CNY': 0.04834621724725696,
    'MXN': 0.1387714506139039,
    'PHP': 0.39646674908161517,
    'TWD': 0.21486779077202364
 }
```


- Get exchange rate from one currency to another

```python
r.get_rate("JPY", "GBP")

0.006034890007841613
```

- Convert an amount from one currency to another

```python
r.convert("JPY", "GBP", 1500)

9.05233501176242
```

- Initialize the CurrencyCodes class

```python
from fakex_python import CurrencyCodes

c = CurrencyCodes()
```

- Get currency symbol from a currency code
```python
c.get_symbol("JPY")

'¥'
```
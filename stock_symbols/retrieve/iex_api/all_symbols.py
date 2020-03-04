import os

import pandas as pd

IEX_API_TOKEN = os.environ["IEX_API_TOKEN"]

ALL_SYMBOLS_IEX_API = "https://cloud.iexapis.com/stable/ref-data/symbols?format=csv&token=" + IEX_API_TOKEN
"""
ad - ADR
re - REIT
ce - Closed end fund
si - Secondary Issue
lp - Limited Partnerships
cs - Common Stock
et - ETF
wt - Warrant
oef - Open Ended Fund
cef - Closed Ended Fund
ps - Preferred Stock
ut - Unit
struct - Structured Product
"""


def get_iex_all_symbols():
	all_symbols = pd.read_csv(ALL_SYMBOLS_IEX_API)
	return all_symbols

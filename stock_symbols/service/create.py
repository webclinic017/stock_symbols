from abc import ABC, abstractmethod

import pandas as pd

from stock_symbols.global_constants import SYMBOL_COL, DB_PREF_STOCK_KW, STERLING_TRADER_PREF_STOCK_KW, STOCK_LIST_COL


class Creator(ABC):
	
	@abstractmethod
	def create(self, data: pd.DataFrame):
		pass


class ListCreator(Creator):
	
	def __init__(self):
		self.stock_lists = None
	
	def create(self, stock_data: pd.DataFrame):
		self._get_symbols(stock_data)
		self._convert_symbols()
		
		return self.stock_lists
	
	def _get_symbols(self, stock_data):
		self.stock_lists = stock_data[[SYMBOL_COL, STOCK_LIST_COL]]
	
	@abstractmethod
	def _convert_symbols(self):
		pass


class SterlingTraderListCreator(ListCreator):
	
	def _convert_symbols(self):
		self.stock_lists = self.stock_lists[SYMBOL_COL].str.replace(DB_PREF_STOCK_KW, STERLING_TRADER_PREF_STOCK_KW)

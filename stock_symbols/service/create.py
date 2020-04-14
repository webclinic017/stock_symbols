from abc import ABC, abstractmethod

import pandas as pd

from stock_symbols.global_constants import SYMBOL_COL, DB_PREF_STOCK_KW, ST_PREF_STOCK_KW, STOCK_LIST_COL, \
	IB_PREF_STOCK_KW


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
		self.stock_lists[SYMBOL_COL] = self.stock_lists[SYMBOL_COL].str.replace(DB_PREF_STOCK_KW, ST_PREF_STOCK_KW)


class InteractiveBrokersListCreator(ListCreator):
	
	def _convert_symbols(self):
		self.stock_lists[SYMBOL_COL] = self.stock_lists[SYMBOL_COL].str.replace(DB_PREF_STOCK_KW, IB_PREF_STOCK_KW)
	
	def _add_feature_cols(self):
		# todo
		# first_row = pd.DataFrame([["COLUMN", 0]])
		#
		# debt_sec_count = len(symbols)
		#
		# des_col = ["DES"] * debt_sec_count
		# type_col = ["STK"] * debt_sec_count
		# exchange_col = ["SMART/NYSE"] * debt_sec_count
		#
		# df = pd.DataFrame()
		# df[0] = des_col
		# df[1] = symbols
		# df[2] = type_col
		# df[3] = exchange_col
		#
		# df = first_row.append(df).reset_index(drop=True)
		pass
	
	def create(self, stock_data: pd.DataFrame):
		self.stock_lists = super().create(stock_data)
		self._add_feature_cols()
		
		return self.stock_lists

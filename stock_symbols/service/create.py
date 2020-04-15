from abc import ABC, abstractmethod

import pandas as pd

from stock_symbols.global_constants import SYMBOL_COL, DB_PREF_STOCK_KW, ST_PREF_STOCK_KW, STOCK_LIST_COL, \
	IB_PREF_STOCK_KW

IB_SOCK_LIST_FIRST_ROW_VAL_1 = "COLUMN"
IB_SOCK_LIST_FIRST_ROW_VAL_2 = 0


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
		self.stock_lists = stock_data[[STOCK_LIST_COL, SYMBOL_COL]]
	
	@abstractmethod
	def _convert_symbols(self):
		pass


class SterlingTraderListCreator(ListCreator):
	
	def _convert_symbols(self):
		self.stock_lists[SYMBOL_COL] = self.stock_lists[SYMBOL_COL].str.replace(DB_PREF_STOCK_KW, ST_PREF_STOCK_KW)


class InteractiveBrokersListCreator(ListCreator):
	IB_STOCK_LIST_DES_COL = "destination"
	IB_STOCK_LIST_DES_COL_VAL = "DES"
	IB_STOCK_LIST_TYPE_COL = "stock_type"
	IB_STOCK_LIST_TYPE_COL_VAL = "STK"
	IB_STOCK_LIST_EXCHANGE_COL = "exchange"
	IB_STOCK_LIST_EXCHANGE_COL_VAL = "SMART/NYSE"
	IB_STOCK_LIST_FIRST_ROW = pd.DataFrame([[IB_SOCK_LIST_FIRST_ROW_VAL_1, IB_SOCK_LIST_FIRST_ROW_VAL_2]])
	
	def create(self, stock_data: pd.DataFrame):
		self.stock_lists = super().create(stock_data)
		self._create_ib_watchlists()
		
		return self.stock_lists
	
	def _convert_symbols(self):
		self.stock_lists[SYMBOL_COL] = self.stock_lists[SYMBOL_COL].str.replace(DB_PREF_STOCK_KW, IB_PREF_STOCK_KW)
	
	def _create_ib_watchlists(self):
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
		
		self._add_feature_cols()
		self._reorder_cols()
		self._add_watchlists_header_rows()
	
	def _add_feature_cols(self):
		self.stock_lists[self.IB_STOCK_LIST_DES_COL] = self.IB_STOCK_LIST_DES_COL_VAL
		self.stock_lists[self.IB_STOCK_LIST_TYPE_COL] = self.IB_STOCK_LIST_TYPE_COL_VAL
		self.stock_lists[self.IB_STOCK_LIST_EXCHANGE_COL] = self.IB_STOCK_LIST_EXCHANGE_COL_VAL
	
	def _reorder_cols(self):
		self.stock_lists = self.stock_lists[
			[STOCK_LIST_COL, self.IB_STOCK_LIST_DES_COL, SYMBOL_COL, self.IB_STOCK_LIST_TYPE_COL,
			 self.IB_STOCK_LIST_EXCHANGE_COL]]
	
	def _add_watchlists_header_rows(self):
		self.stock_lists = self.stock_lists.groupby(STOCK_LIST_COL).apply(self._add_watchlist_header_row)
	
	def _add_watchlist_header_row(self, df):
		# todo
		pass

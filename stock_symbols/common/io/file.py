import os
from abc import ABC, abstractmethod

from stock_symbols.global_constants import STOCK_LIST_COL


class Writer(ABC):
	
	@abstractmethod
	def write(self, data):
		pass


class StockListsWriter(Writer):
	
	def __init__(self, path):
		self.path = path
	
	def write(self, stock_lists):
		stock_lists.groupby(STOCK_LIST_COL).apply(self._write_single_stock_list)
	
	def _write_single_stock_list(self, df):
		copy = df.copy()
		stock_list_name = copy[STOCK_LIST_COL].iloc[0]
		stock_list_path = os.path.join(self.path, stock_list_name + ".stk")
		copy = copy.drop([STOCK_LIST_COL], axis=1)
		copy.to_csv(stock_list_path, index=False, header=False)

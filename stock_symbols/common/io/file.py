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
		for name, group in stock_lists.groupby(STOCK_LIST_COL):
			stock_list_path = os.path.join(self.path, name + ".stk")
			stock_list = group.drop([STOCK_LIST_COL], axis=1)
			stock_list.to_csv(stock_list_path, index=False, header=False)

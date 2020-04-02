from abc import ABC, abstractmethod
import pandas as pd

from stock_symbols.common.utils import invert_dict


class StockDataTransformer(ABC):
	
	def __init__(self, stock_data):
		self.stock_data = stock_data
	
	@abstractmethod
	def transform(self):
		pass


class StockListTransformer(StockDataTransformer):
	
	def __init__(self, stock_list_map, stock_list_col=None, map_col=None, groupby=None, criteria=None, reverse=True):
		super(StockListTransformer, self).__init__()
		self.stock_list_map = stock_list_map
		self.stock_list_col = stock_list_col
		self.map_col = map_col
		self.groupby = groupby
		self.criteria = criteria
		self.reverse = reverse
	
	def _create_stock_list_name_col(self):
		inverted_list_map = invert_dict(self.stock_list_map)
		self.stock_data[self.stock_list_col] = self.stock_data[self.map_col].map(inverted_list_map)
	
	def _order_groups_by_criteria(self):
		groups = self.stock_data.groupby(self.groupby)
		ordered_groups = sorted(groups, key=self.criteria, reverse=self.reverse)
		ordered_groups = [kvp[1] for kvp in ordered_groups]
		self.stock_data = pd.concat(ordered_groups)
	
	def transform(self):
		self._create_stock_list_name_col()
		self._order_groups_by_criteria()

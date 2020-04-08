from abc import ABC, abstractmethod

from stock_symbols.retrieve.retrieve import Retriever
from stock_symbols.service.sorter import Sorter
from stock_symbols.service.transform import Transformer


class Engine(ABC):
	
	@abstractmethod
	def run(self):
		pass


class StockListEngine(Engine):
	
	def __init__(self, stock_data_retriever: Retriever, stock_data_transformer: Transformer, stock_data_sorter: Sorter):
		self.stock_data = None
		self.stock_data_retriever = stock_data_retriever
		self.stock_data_transformer = stock_data_transformer
		self.stock_data_sorter = stock_data_sorter
	
	def run(self):
		self.stock_data = self.stock_data_retriever.retrieve()
		self.stock_data = self.stock_data_transformer.transform(self.stock_data)
		self.stock_data = self.stock_data_sorter.sort(self.stock_data)
		
		return self.stock_data

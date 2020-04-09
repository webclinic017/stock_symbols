from abc import ABC, abstractmethod

from stock_symbols.common.io.file import Writer
from stock_symbols.retrieve.retrieve import Retriever
from stock_symbols.service.create import Creator
from stock_symbols.service.sort import Sorter
from stock_symbols.service.transform import Transformer


class Engine(ABC):
	
	@abstractmethod
	def run(self):
		pass


class StockListEngine(Engine):
	
	def __init__(self, stock_data_retriever: Retriever, stock_data_transformer: Transformer, stock_data_sorter: Sorter,
	             stock_list_creator: Creator, stock_list_writer: Writer):
		self.stock_data_retriever = stock_data_retriever
		self.stock_data_transformer = stock_data_transformer
		self.stock_data_sorter = stock_data_sorter
		self.stock_list_creator = stock_list_creator
		self.stock_list_writer = stock_list_writer
		self.stock_data = None
		self.stock_lists = None
	
	def run(self):
		self.stock_data = self.stock_data_retriever.retrieve()
		self.stock_data = self.stock_data_transformer.transform(self.stock_data)
		self.stock_data = self.stock_data_sorter.sort(self.stock_data)
		self.stock_lists = self.stock_list_creator.create(self.stock_data)
		self.stock_list_writer.write(self.stock_lists)

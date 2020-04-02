from stock_symbols.retrieve.stock_data import StockDataRetriever
from stock_symbols.service.stock_lists.transform.stock_data import StockListTransformer


class StockDataEngine:
	
	def __init__(self, stock_data_retriever: StockDataRetriever, stock_data_transformer: StockListTransformer):
		self.stock_data_retriever = stock_data_retriever
		self.stock_data_transformer = stock_data_transformer

from abc import ABC, abstractmethod


class StockDataRetriever(ABC):
	
	@abstractmethod
	def retrieve(self):
		pass

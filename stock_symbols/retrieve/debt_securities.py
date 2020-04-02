from stock_symbols.repository.debt_securities.debt_sec_data.debt_sec import DebtSecRepo
from stock_symbols.retrieve.stock_data import StockDataRetriever


class DebtSecRetriever(StockDataRetriever):
	
	def __init__(self):
		self.debt_sec_repo = DebtSecRepo()
	
	def retrieve(self):
		return self.debt_sec_repo.get_all_data()

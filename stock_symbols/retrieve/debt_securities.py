from stock_symbols.repository.debt_securities.debt_sec_data.debt_sec import DebtSecRepo
from stock_symbols.retrieve.retrieve import Retriever


class DebtSecRetriever(Retriever):
	
	def __init__(self, debt_sec_repo):
		self.debt_sec_repo = debt_sec_repo
	
	def retrieve(self):
		return self.debt_sec_repo.get_all_data()

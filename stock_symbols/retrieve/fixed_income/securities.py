from stock_symbols.repository.fixed_income.data.securities import FixedIncomeSecRepo
from stock_symbols.retrieve.retrieve import Retriever


class FixedIncomeSecRetriever(Retriever):
	
	def __init__(self, fixed_income_repo):
		self.fixed_income_repo = fixed_income_repo
	
	def retrieve(self):
		return self.fixed_income_repo.get_all_data()

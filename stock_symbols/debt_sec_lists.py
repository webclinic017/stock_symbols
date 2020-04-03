from stock_symbols.repository.debt_securities.debt_sec_data.debt_sec import DebtSecRepo
from stock_symbols.retrieve.debt_securities import DebtSecRetriever


def main():
	debt_sec_retriever = DebtSecRetriever(DebtSecRepo())
	

if __name__ == '__main__':
	main()

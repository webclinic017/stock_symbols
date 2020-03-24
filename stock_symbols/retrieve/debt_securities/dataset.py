from stock_symbols.repository.debt_securities.debt_sec_data.debt_sec import get_debt_sec_db_table


def retrieve_debt_sec_dataset():
	debt_sec = get_debt_sec_db_table()
	return debt_sec

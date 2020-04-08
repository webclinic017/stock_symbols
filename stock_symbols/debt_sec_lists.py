from stock_symbols.global_constants import *
from stock_symbols.repository.debt_securities.debt_sec_data.debt_sec import DebtSecRepo
from stock_symbols.retrieve.debt_securities import DebtSecRetriever
from stock_symbols.service.engine import StockListEngine
from stock_symbols.service.sorter import StockGroupsSorter
from stock_symbols.service.transform import StockListTransformer


def main():
	list_cols = ["symbol", "coupon_rate", "sector", "industry", "company_name", "month_3_aver_vol"]
	
	debt_sec_retriever = DebtSecRetriever(DebtSecRepo())
	debt_sec_transformer = StockListTransformer(DEBT_SEC_LIST_COLS, DEBT_SEC_STOCK_LISTS_INDUSTRY_MAP,
	                                            map_col=INDUSTRY_COL)
	debt_sec_sorter = StockGroupsSorter(sort_by=DEBT_SEC_SORT_BY_COLS, ascending=DEBT_SEC_ASC_SORT,
	                                    groupby=COMPANY_NAME_COL, criteria=lambda kvp: len(kvp[1]))
	
	debt_sec_st_engine = StockListEngine(debt_sec_retriever, debt_sec_transformer, debt_sec_sorter)
	
	stock_data = debt_sec_st_engine.run()


if __name__ == '__main__':
	main()

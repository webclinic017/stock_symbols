from stock_symbols.common.io.file import StockListsWriter
from stock_symbols.global_constants import *
from stock_symbols.repository.fixed_income.data.securities import FixedIncomeSecRepo
from stock_symbols.retrieve.fixed_income.securities import FixedIncomeSecRetriever
from stock_symbols.service.create import SterlingTraderListCreator
from stock_symbols.service.engine import StockListEngine
from stock_symbols.service.sort import StockGroupsSorter
from stock_symbols.service.transform import ListNamesTransformer


def main():
	# fi=fixed income
	fi_retriever = FixedIncomeSecRetriever(FixedIncomeSecRepo())
	fi_transformer = ListNamesTransformer(FI_LIST_COLS, FI_STOCK_LISTS_INDUSTRY_MAP, map_col=INDUSTRY_COL)
	fi_sorter = StockGroupsSorter(sort_by=FI_SORT_BY_COLS, ascending=FI_ASC_SORT, groupby=COMPANY_NAME_COL,
	                              criteria=lambda kvp: len(kvp[1]))
	# st=sterling_trader
	st_list_creator = SterlingTraderListCreator()
	st_list_writer = StockListsWriter(ST_FI_LISTS_PATH)
	fi_st_engine = StockListEngine(fi_retriever, fi_transformer, fi_sorter, st_list_creator, st_list_writer)
	fi_st_engine.run()
	
	# ib_list_creator = None
	# ib_list_writer = StockListsWriter()
	# fi_ib_engine = StockListEngine(fi_retriever, fi_transformer, fi_sorter, ib_list_creator, ib_list_writer)
	# fi_ib_engine.run()


if __name__ == '__main__':
	main()

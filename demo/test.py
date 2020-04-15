import pandas as pd

from stock_symbols.repository.fixed_income.data.securities import FixedIncomeSecRepo
from stock_symbols.retrieve.fixed_income.securities import FixedIncomeSecRetriever


def invert_dict(dic):
	return dict((val, key) for key in dic for val in dic[key])


debt_sec = FixedIncomeSecRetriever(FixedIncomeSecRepo()).retrieve()

debt_sec["symbol"] = debt_sec["symbol"].str.replace("-P", "p")

debt_sec = debt_sec[["symbol", "coupon_rate", "sector", "industry", "company_name", "month_3_aver_vol"]]

debt_sec = debt_sec.sort_values(["sector", "industry", "company_name", "coupon_rate"],
                                ascending=(True, True, True, False))

# debt_sec.to_csv("demo/debt_sec.csv", index=False)

# ordered = debt_sec.groupby(["sector", "industry"]).size().sort_values(ascending=False)

inverted = invert_dict(stock_list_industries_map)

debt_sec["stock_list"] = debt_sec["industry"].map(inverted)
stock_lists = debt_sec[["stock_list", "company_name", "symbol", "coupon_rate"]]

first_row = pd.DataFrame([["COLUMN", 0]])

for name, group in x:
	print(name)
	print(group)
	print()


def order_company_name_groups_by_size(df):
	groups = df.groupby("company_name")
	sorted_groups = sorted(groups, key=lambda kvp: len(kvp[1]), reverse=True)
	df_groups = [kvp[1] for kvp in sorted_groups]
	sorted_df = pd.concat(df_groups)
	return sorted_df


stock_lists = stock_lists.groupby("stock_list").apply(order_company_name_groups_by_size).reset_index(drop=True)

stock_lists.groupby("stock_list").apply(
	lambda df: write_to_file(df["symbol"], STOCK_LIST_FILE_PATH + df["stock_list"][0] + ".stk"))

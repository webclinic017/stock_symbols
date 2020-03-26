import pandas as pd

from stock_symbols.retrieve.debt_securities.dataset import retrieve_debt_sec_dataset

stock_list_map = {"reits": ["Real Estate Investment Trusts"],
                  "banks": ["Major Banks", "Regional Banks"]}

debt_sec = retrieve_debt_sec_dataset()

debt_sec = debt_sec[["symbol", "coupon_rate", "company_name", "sector", "industry", "month_3_aver_vol"]]

# sectors = pd.Series(debt_sec["sector"].unique())
# industries = pd.Series(debt_sec["industry"].unique())

# nans = debt_sec[debt_sec.isnull().any(axis=1)]
ordered = debt_sec.groupby(["sector", "industry"]).size().sort_values(ascending=False)

debt_sec = debt_sec.set_index(["sector", "industry"])
ind = debt_sec.loc[("Finance", "Property/Casualty Insurance")]
finance = debt_sec[(debt_sec.index.get_level_values(0) == "Finance") & (
		debt_sec.index.get_level_values(1) != "Real Estate Investment Trusts")]

finance = finance.sort_index(level=[1])

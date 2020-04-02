import pandas as pd

from stock_symbols.common.io.file import write_to_file
from stock_symbols.retrieve.debt_securities.dataset import retrieve_debt_sec_dataset

stock_list_industries_map = {
	"banks": ["Major Banks", "Regional Banks", "Investment Banks/Brokers", "Financial Conglomerates", "Savings Banks"],
	"insurance": ["Multi-Line Insurance", "Life/Health Insurance", "Property/Casualty Insurance", "Specialty Insurance",
	              "Insurance Brokers/Services"],
	"other_financial": ["Investment Trusts/Mutual Funds", "Finance/Rental/Leasing", "Investment Managers"],
	"reits": ["Real Estate Investment Trusts", "Real Estate Development"],
	"electric_commun": ["Electric Utilities", "Major Telecommunications", "Specialty Telecommunications",
	                    "Wireless Telecommunications", "Water Utilities"],
	"transport": ["Marine Shipping", "Air Freight/Couriers", "Trucking"],
	"oil_gas": ["Oil & Gas Production", "Oil Refining/Marketing", "Oil & Gas Pipelines", "Gas Distributors",
	            "Oilfield Services/Equipment", "Contract Drilling"],
	"other": ["Agricultural Commodities/Milling", "Miscellaneous Commercial Services", "Homebuilding", "Motor Vehicles",
	          "Recreational Products", "Tools & Hardware", "Beverages: Alcoholic", "Household/Personal Care",
	          "Movies/Entertainment", "Other Consumer Services", "Wholesale Distributors",
	          "Electronic Equipment/Instruments", "Semiconductors", "Biotechnology", "Medical Specialties",
	          "Precious Metals", "Chemicals: Specialty", "Electrical Products", "Industrial Conglomerates",
	          "Industrial Machinery", "Office Equipment/Supplies", "Trucks/Construction/Farm Machinery",
	          "Internet Retail", "Specialty Stores", "Information Technology Services", "Internet Software/Services",
	          "Packaged Software", "NoData"]
}

STOCK_LIST_FILE_PATH = "/home/hristocr/googledrive/Trading/stock_sorters_gen/"


def invert_dict(dic):
	return dict((val, key) for key in dic for val in dic[key])


debt_sec = retrieve_debt_sec_dataset()

debt_sec["symbol"] = debt_sec["symbol"].str.replace("-P", "p")

debt_sec = debt_sec[["symbol", "coupon_rate", "sector", "industry", "company_name", "month_3_aver_vol"]]

debt_sec = debt_sec.sort_values(["sector", "industry", "company_name", "coupon_rate"],
                                ascending=(True, True, True, False))

# debt_sec.to_csv("demo/debt_sec.csv", index=False)

# ordered = debt_sec.groupby(["sector", "industry"]).size().sort_values(ascending=False)

inverted = invert_dict(stock_list_industries_map)

debt_sec["stock_list"] = debt_sec["industry"].map(inverted)
stock_lists = debt_sec[["stock_list", "company_name", "symbol", "coupon_rate"]]


def order_company_name_groups_by_size(df):
	groups = df.groupby("company_name")
	sorted_groups = sorted(groups, key=lambda kvp: len(kvp[1]), reverse=True)
	df_groups = [kvp[1] for kvp in sorted_groups]
	sorted_df = pd.concat(df_groups)
	return sorted_df


stock_lists = stock_lists.groupby("stock_list").apply(order_company_name_groups_by_size).reset_index(drop=True)

stock_lists.groupby("stock_list").apply(
	lambda df: write_to_file(df["symbol"], STOCK_LIST_FILE_PATH + df["stock_list"][0] + ".stk"))

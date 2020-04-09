import os

SYMBOL_COL = "symbol"
COUPON_RATE_COL = "coupon_rate"
SECTOR_COL = "sector"
INDUSTRY_COL = "industry"
COMPANY_NAME_COL = "company_name"
MONTH_3_AVER_VOL_COL = "month_3_aver_vol"
STOCK_LIST_COL = "stock_list"

STOCK_LISTS_PATH = os.environ["STOCK_LISTS_FILE_PATH"]
FI_DIR = "fixed_income"
FI_LISTS_PATH = os.path.join(STOCK_LISTS_PATH, FI_DIR)

FI_STOCK_LISTS_INDUSTRY_MAP = {
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

FI_LIST_COLS = ["symbol", "coupon_rate", "sector", "industry", "company_name", "month_3_aver_vol"]
FI_SORT_BY_COLS = ["sector", "industry", "company_name", "coupon_rate"]
FI_ASC_SORT = (True, True, True, False)

DB_PREF_STOCK_KW = "-P"
STERLING_TRADER_PREF_STOCK_KW = "p"

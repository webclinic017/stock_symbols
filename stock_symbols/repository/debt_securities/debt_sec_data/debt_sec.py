import pandas as pd
from sqlalchemy import exc

from stock_symbols.repository.debt_securities.db_conn import db_conn, DB_CONN_ERROR
from stock_symbols.repository.debt_securities.debt_sec_data.constants import DEBT_SEC_TABLE_NAME, DEBT_SEC_DATA_SCHEMA

DEBT_SEC_RETRIEVE_SUCC_MSG = "Debt sec table successfully retrieved!"


def get_debt_sec_db_table():
	try:
		df = pd.read_sql_table(DEBT_SEC_TABLE_NAME, db_conn, schema=DEBT_SEC_DATA_SCHEMA)
		print(DEBT_SEC_RETRIEVE_SUCC_MSG)
		return df
	except exc.DBAPIError as e:
		print(DB_CONN_ERROR, e)
	except Exception as e:
		print(str(e))

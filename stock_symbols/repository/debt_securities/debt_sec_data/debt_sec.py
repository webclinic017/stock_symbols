import pandas as pd
from sqlalchemy import exc

from stock_symbols.repository.debt_securities.db_conn import db_conn, DB_CONN_ERROR
from stock_symbols.repository.debt_securities.debt_sec_data.constants import DEBT_SEC_TABLE_NAME, DEBT_SEC_DATA_SCHEMA
from stock_symbols.repository.repository import BaseRepo

DEBT_SEC_RETRIEVE_SUCC_MSG = "Debt sec table successfully retrieved!"


class DebtSecRepo(BaseRepo):
	
	def __init__(self):
		self.conn = db_conn
	
	def get_all_data(self):
		try:
			df = pd.read_sql_table(DEBT_SEC_TABLE_NAME, self.conn, schema=DEBT_SEC_DATA_SCHEMA)
			print(DEBT_SEC_RETRIEVE_SUCC_MSG)
			return df
		except exc.DBAPIError as e:
			print(DB_CONN_ERROR, e)
		except Exception as e:
			print(str(e))




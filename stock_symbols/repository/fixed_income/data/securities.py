import pandas as pd
from sqlalchemy import exc

from stock_symbols.repository.fixed_income.db_conn import db_conn, DB_CONN_ERROR
from stock_symbols.repository.fixed_income.data.constants import FI_SEC_TABLE_NAME, FI_SEC_DATA_SCHEMA
from stock_symbols.repository.repository import BaseRepo

FI_SEC_RETRIEVE_SUCC_MSG = "Fixed income table successfully retrieved!"


class FixedIncomeSecRepo(BaseRepo):
    
    def __init__(self):
        self.conn = db_conn
    
    def get_all_data(self):
        try:
            df = pd.read_sql_table(FI_SEC_TABLE_NAME, self.conn, schema=FI_SEC_DATA_SCHEMA)
            print(FI_SEC_RETRIEVE_SUCC_MSG)
            return df
        except exc.DBAPIError as e:
            print(DB_CONN_ERROR, e)
        except Exception as e:
            print(str(e))

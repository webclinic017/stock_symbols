from sqlalchemy import create_engine
import os

DB_CONN_ERROR = "Unable to connect to database."

DEBT_SEC_PSQL_PORT = os.environ["DEBT_SEC_PSQL_PORT"]
DEBT_SEC_PSQL_USERNAME = os.environ["DEBT_SEC_PSQL_USERNAME"]
DEBT_SEC_PSQL_PASSWORD = os.environ["DEBT_SEC_PSQL_PASSWORD"]
DEBT_SEC_PSQL_IP_ADDRESS = os.environ["DEBT_SEC_PSQL_IP_ADDRESS"]
DEBT_SEC_PSQL_DBNAME = os.environ["DEBT_SEC_PSQL_DBNAME"]

postgres_str = 'postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=DEBT_SEC_PSQL_USERNAME,
                                                                                       password=DEBT_SEC_PSQL_PASSWORD,
                                                                                       ipaddress=DEBT_SEC_PSQL_IP_ADDRESS,
                                                                                       port=DEBT_SEC_PSQL_PORT,
                                                                                       dbname=DEBT_SEC_PSQL_DBNAME)

db_conn = create_engine(postgres_str)

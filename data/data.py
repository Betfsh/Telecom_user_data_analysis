import pandas as pd
from sqlalchemy import create_engine

def df_from_database(chunksize=None):
    database_name = 'Telecom'
    table_name = 'xdr_data'
    
    connection_params = {
        "host": "localhost",
        "user": "postgres",
        "password": "pogres",
        "port": "5432",
        "database": database_name
    }
    
    engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")
    
    sql_query = f"SELECT * FROM {table_name}"
    
    if chunksize:
        df_chunks = pd.read_sql(sql_query, con=engine, chunksize=chunksize)
        df = pd.concat(df_chunks)
    else:
        df = pd.read_sql(sql_query, con=engine)
    
    return df
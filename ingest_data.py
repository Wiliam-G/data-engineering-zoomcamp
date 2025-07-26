import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = "output_parquet"

    os.system(f"wget {url} -O {parquet_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    # print(pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine))

    # ### Inserindo os dados no postgres em lotes de 100k

    batch_size = 100_000
    df = pd.read_parquet(parquet_name, engine='pyarrow')

    for i in range(0, len(df), batch_size):
        t_start = time()
        print(f"Inserindo dados do lote {i + 1}")
        batch = df.iloc[i:i+batch_size]
        batch.to_sql(name="yellow_taxi_data", con=engine, if_exists="append", index=False)
        t_end = time()
        print(f"Concluído! Levou {t_end - t_start} segundos")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data do Postgres')
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name')
    parser.add_argument('--table_name', help='table name where we will put the data')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)

    # file = 'yellow_tripdata_2021-01.csv'
    # chunk_size = 100_000

    # for i, chunk in enumerate(pd.read_csv(file, chunksize=chunk_size)):
    #     t_start = time()
    #     chunk.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    #     chunk.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    #     get_ipython().run_line_magic('time', "chunk.to_sql(name='{table_name}', con=engine, if_exists='append', index=False)")
    #     t_end = time()
    #     print(f'Lote {i + 1} inserido, levou {t_end - t_start} segundos')

# df_parquet = pd.read_parquet('yellow_tripdata_2021-01.parquet')

# df_parquet.count()

# Converte .parquet para .csv
# df_parquet.to_csv('yellow_tripdata_2021-01.csv', index=False)

# df = pd.read_csv('yellow_tripdata_2021-01.csv')

# ### Configura o sqlalchem para conexão com o postgres, criação da tabela e inserção dos dados



# user
# password
# host
# port
# database name
# table name
# url of the csv



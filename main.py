# csv -> ler infos -> comparar com db -> retornar id db -> salvar csv
import os
import pandas as pd
import numpy as np
import multiprocessing as mp
import pymysql.cursors

FILENAME = './assets/clients_cities.csv'
CHUNKSIZE = 4000

def process_frame(df):
    return len(df)

def process_db_data(df):
    # Connect to the database
    connection = pymysql.connect(host=os.environ.get('DB_HOST'),
                                user=os.environ.get('DB_USERNAME'),
                                password=os.environ.get('DB_PASSWORD'),
                                database=os.environ.get('DB_NAME'),
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM city"
            cursor.execute(sql)
            cities = cursor.fetchall()

            # teste = df.loc[df['city'].isin(cities)]
            labels = ['name', 'id']
            cities = pd.DataFrame.from_records(cities, columns=labels)

            df["id_city"] = np.where(cities["name"] == df["name"], cities["id"], 0)

            # for city in df:
                
                # teste = df.loc[df['city'] == cities[city]]
                # print(teste)
                # if (city["name"] == df) {

                # }
                # print(city["name"])
    

if __name__ == '__main__':
    reader = pd.read_csv(FILENAME)
    pool = mp.Pool(4) # 4 processes

    # print(reader)

    # funclist = []
    # for df in reader:
    #     f = pool.apply_async(process_frame, [df])
    #     print(f.get())
    #     funclist.append(f)
    
    # result = 0
    # for f in funclist:
    #     print(f.get())
        # result += f.get(timeout=0.01)
        
    # print("Linhas %d"%(result))

    process_db_data(reader)
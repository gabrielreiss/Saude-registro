import os
import sqlalchemy
import pandas as pd
import time
from datetime import date
from datetime import datetime

BASE_DIR = 'F:\Aprendendo python\Saude'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname( os.path.abspath(__file__) ) ))
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SQL_DIR = os.path.join( BASE_DIR, 'src', 'sql' )
print(BASE_DIR)


str_connection = 'sqlite:///' + os.path.join(DATA_DIR, 'saude.db' )
engine = sqlalchemy.create_engine( str_connection )
connection = engine.connect()

print("Bem vindo ao programa de registro de saúde do Gabriel")
try:
    oxi = input("Adicione o valor do Oxímetro: ")
    if oxi is not '':
        data = str(date.today().strftime("%Y-%m-%d"))
        hora = str(datetime.now().strftime("%H:%M"))
        bat = input("Adicione o valor do Batimento Cardíaco: ")
        temp = input("Adicione o valor da temperatura: ") 

        dic = {
            "data": data,
            "hora": hora,
            "oximetro": oxi,
            "batimento_cardiaco": bat,
            "temperatura": temp
        }
            
        df_tmp = pd.DataFrame.from_dict(data = [dic])

        print("Salvando dados no banco...")
        df_tmp.to_sql(  "saude",
                        connection,
                        if_exists='append',
                        index=False )
        print("Dados salvos no banco com sucesso!")
except:
    pass

df = pd.read_sql_table("saude", connection)
print(df.tail())

time.sleep(60)
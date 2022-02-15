import pandas as pd
import sqlite3

df=pd.read_csv('data_0354_20220215.csv') # 삼성전자 주가 csv자료. 날짜/가격/시가총액/상장주식수
cons = sqlite3.connect('./samsung.db')

df.to_sql('samsung.db',cons,index=False,if_exists='replace')
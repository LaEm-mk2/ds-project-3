import pandas as pd
from pymongo import MongoClient

df=pd.read_csv('data_0354_20220215.csv') # 삼성전자 주가 csv자료. 날짜/가격/시가총액/상장주식수


HOST = 'da-sa-09-lim.l8wsw.mongodb.net'
USER = 'mrnobody'
PASSWORD = 'mrnobody123'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'stock_prediction'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority" #3점은 포기하고 2점이라도 받는다!


client = MongoClient(MONGO_URI)

database = client[DATABASE_NAME]

collection = database[COLLECTION_NAME]

collection.insert_many(df)
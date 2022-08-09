from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import requests



from pymongo import MongoClient


client = MongoClient("mongodb://pranank:1234@cluster0-shard-00-00.nmwpq.mongodb.net:27017,cluster0-shard-00-01.nmwpq.mongodb.net:27017,cluster0-shard-00-02.nmwpq.mongodb.net:27017/?ssl=true&replicaSet=atlas-rd4r0q-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('crypto_db')
records = db.bitcoin



class Crypto:

    def get_top_5(self):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start':'1',
          'limit':'50',
          'convert':'USD'
        }
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': '4596956d-495b-4a49-9545-d512e63aa4ff',
        }

        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        records.insert_one(data)
        return data['data']
        

   



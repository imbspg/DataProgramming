from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json, random
import requests
from flask_pymongo import PyMongo
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time





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
        

app = Flask(__name__)



app.config["MONGO_DBNAME"] = 'crypto_db '
app.config["MONGO_URI"] = 'mongodb://pranank:1234@cluster0-shard-00-00.nmwpq.mongodb.net:27017,cluster0-shard-00-01.nmwpq.mongodb.net:27017,cluster0-shard-00-02.nmwpq.mongodb.net:27017/?ssl=true&replicaSet=atlas-rd4r0q-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo = PyMongo(app)


crypto  = Crypto()


@app.route("/")
def hello():

    results = crypto.get_top_5()


    for result in results:
        result['quote']['USD']['price'] = '$ ' + "{:.2f}".format(result['quote']['USD']['price'])


    return render_template('index2.html', **locals())
    

@app.route("/team")
def team():
        return render_template('team.html', **locals())
    


@app.route("/piechart")
def piechart():
        return render_template('piechart.html', **locals())


#@app.route("/info")
#def data():
    
    #return jsonify ({'results' : sample(range(1,10), 2)})
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')



 
from pymongo import MongoClient
from BlockChainTx.Support.webinterface import apiget


class Server:

    def __init__(self):
        self.dbclient = MongoClient('mongodb://localhost:27017')
        db = client.cryptolist

    def test():
        client = MongoClient('mongodb://localhost:27017')
        db = client.pymongo_test
        posts = db.posts
        # post_data = {
        #     'title': 'Python and MongoDB',
        #     'content': 'PyMongo is fun, you guys',
        #     'author': 'Scott'
        # }
        # result = posts.insert_one(post_data)
        # print('One post: {0}'.format(result.inserted_id))
        bills_post = posts.find_one({'author': 'Scott'})
        print(bills_post)

    def getSingle(ticker,querystr):
        db = self.dbclient.cryptolist
        data = db.find_one({"ticker": ticker})
        if querystr == "24h":
            return 0
        elif querystr == "price":
            return 0
        elif querystr == "cap":
            return 0
        elif querystr == "1h"
            return 0

    def setOne(ticker):
        db = self.dbclient.cryptolist

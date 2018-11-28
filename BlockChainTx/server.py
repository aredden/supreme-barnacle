from pymongo import MongoClient
from BlockChainTx.Support.webinterface import WebInterface as web

class Server:

#**************************************************
#
#**************************************************
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["BlockChainTx"]
        self.cids = self.db["CoinIds"]
        self.cdata = self.db["CoinData"]

    def test(self):
        return 0
        #
        # client = MongoClient("mongodb://localhost:27017")
        # db = client.pymongo_test
        # posts = db.posts
        # post_data = {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"}
        #
        # # result = posts.insert_one(post_data)
        # # print("One post: {0}".format(result.inserted_id))
        # bills_post = posts.find_one({"author": "Scott"})
        # print(bills_post)

    def getByTicker(self, ticker, querystr):
        data = db.find_one({"symbol": ticker})
        if querystr == "24h":
            return 0
        elif querystr == "price":
            return 0
        elif querystr == "cap":
            return 0
        elif querystr == "1h":
            return 0

    def close(self):
        self.client.close()

#**************************************************
#   Loads coin data for 'coin' from CoinGecko API &
#   inserts into BlockChainTx.coinData collection.
#**************************************************

    def set_coindata(self, coin):
        data = web.getcoinData(coin)
        print (data)
        key = {

        }

    def list_ids(self):
        return 0


#**************************************************
#   Loads {coinid, symbol, name} from BlockChainTx.CoinIds
#   collection and returns the data. Throws no match error.
#**************************************************
    def get_id(self, coin):
        result = self.cids.find_one({"symbol":coin})
        print(result)
        try:
            return result["coinid"]
        except:
            print("Error: no coinid matches for " + coin)


#**************************************************
#   loads in id's from CoinGecko API {coinid, symbol, name}
#   and inserts data into BlockChainTx.CoinIds mongodb
#   collection. Do not use unless reinstall.
#**************************************************
    def reset_ids(self):
        #
        # Initialize database and GET request from WebInterface
        #
        coinDict = web.coinslistGET()
        for x in coinDict:
            data = {
            "coinid": x["id"],
            "symbol": x["symbol"],
            "name": x["name"]
            }
            result = self.cids.insert_one(data)
            print(result)

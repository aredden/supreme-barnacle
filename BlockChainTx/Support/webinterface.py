from urllib.request import urlopen
import json


class WebInterface:

    def coinslistGET() -> dict:
        #load
        html = urlopen("https://api.coingecko.com/api/v3/coins/list")
        return json.loads(html.read().decode())

    def getcoinPrice(coin):
        html = urlopen("https://api.coingecko.com/api/v3/coins/")
        htmlData = json.loads(html.read().decode())
        table = htmlData['data']
        meta = htmlData['metadata']
        return table['1']['quotes']['USD']['price']
    ### My Code ###
    #print(htmlData)

    def getcoinData(coin):
        query = "https://api.coingecko.com/api/v3/coins/" + coin
        html = urlopen(query)
        return json.loads(html.read().decode())

from urllib.request import urlopen
from json import loads


class webinterface:

    def initdb():
        #load
        html = urlopen("https://api.coingecko.com/api/v3/coins/list")
        htmlData = json.loads(html.read().decode())
        print(htmlData)


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
        html = urlopen()

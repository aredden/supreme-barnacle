from urllib.request import urlopen
import json


#**************************************************
#   Example 6: How to create html object that must be html.read()
#**************************************************

def initdb():
    #load
    html = urlopen("https://api.coinmarketcap.com/v2/ticker/")
    htmlData = json.loads(html.read().decode())
    file = open('coindb.bdf','w')
    coinData = htmlData['data']
    file.write(coinData)


def getcoinPrice(coin):
    html = urlopen("https://api.coinmarketcap.com/v2/ticker/")
    htmlData = json.loads(html.read().decode())
    table = htmlData['data']
    meta = htmlData['metadata']
    return table['1']['quotes']['USD']['price']
### My Code ###
#print(htmlData)

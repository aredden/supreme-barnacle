from urllib.request import urlopen
import json


def populateDB():
    resetGeckoDB()
    html = urlopen("https://api.coingecko.com/api/v3/coins/list")
    htmlData = json.loads(html.read().decode())
    file = open('Coins.txt','w')
    for x in htmlData:
        writeDBLinesGecko(x,file);
    file.close()


def writeDBLinesGecko(d, f):
    k = d.keys()
    for x in k:
        f.write(d[x]+" ")
    f.write("\n")
    return


def resetGeckoDB():
    import os
    if os.path.exists("Coins.txt"):
        os.remove("Coins.txt")
    if os.path.exists("Prices.txt"):
        os.remove("Prices.txt")

#**************************************************
# @params str representing coin name
# @return null
#   updates price via contacting CoinGecko & writing to db file.
#**************************************************
def updateSpecificPrice(Coins):
    file = open('Prices.txt','w')
    html = urlopen("https://api.coingecko.com/api/v3/coins/list")
populateDB()

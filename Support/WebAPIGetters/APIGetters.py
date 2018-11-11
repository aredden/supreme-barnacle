from urllib.request import urlopen
import json


# Load data from GET request
html = urlopen("https://api.coinmarketcap.com/v2/ticker/")

htmlData = json.loads(html.read())

print(htmlData)

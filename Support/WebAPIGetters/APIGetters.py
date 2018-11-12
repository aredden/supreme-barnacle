from urllib.request import urlopen
import json


#**************************************************
#   Example 6: How to create html object that must be html.read
#**************************************************

html = urlopen("https://api.coinmarketcap.com/v2/ticker/")
htmlData = json.loads(html.read())

### My Code ###
print(htmlData)
table = htmlData['data']
for x in table:
    print(x['name'])

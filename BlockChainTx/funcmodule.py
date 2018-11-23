from .Support import APIGetters as apiget
from .test import tests
from BlockChainTx.Support.APIGetters import getcoinPrice as gcp
from BlockChainTx.Support.dbscript import initdb
from BlockChainTx.queries import query

def run():

    name = input("Hello, What is your name?\n")
    inpt = input("\nHello {}!\nWould you like to see Bitcoin price? Y/N/test/query\n".format(name))
    if inpt.lower() == 'y':

#**************************************************
# TODO: links to APIGetters.py in Support/? !!!!!!!!!!!!!!!!
#**************************************************

        initdb()
        webInfo = gcp("Bitcoin")
        print("\n...Doing Stuff")
        print(webInfo)

    elif inpt.lower() == "test":
        x = input("which test? ['db', ]")
        tests(x)
    elif inpt.lower() == "query":
        x = input("Enter query string: [coin name/ ticker] [price,lastupdate,24h]\n")
        args = x.split(" ")
        if(args.__len__() > 2):
            print("Error: expected two input words, got {}".format(args.__len__())
        query(x)
    else:
        print('\nDoing Nothing')

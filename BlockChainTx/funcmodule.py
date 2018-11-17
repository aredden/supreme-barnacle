from .Support import APIGetters as apiget

def run():

    name = input("Hello, What is your name?\n")
    num = input("\nHello {}!\nWould you like to see Bitcoin price? Y/N\n".format(name))
    if num.lower() == 'y':

#**************************************************
# TODO: links to APIGetters.py in Support/? !!!!!!!!!!!!!!!!
#**************************************************
        from BlockChainTx.Support.APIGetters import getcoinPrice as gcp
        from BlockChainTx.Support.dbscript import initdb
        initdb()
        webInfo = gcp("Bitcoin")
        print("\n...Doing Stuff")
        print(webInfo)

    else:
        print('\nDoing Nothing')

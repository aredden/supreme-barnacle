import BlockChainTx.server as srv



def serverintloop():

    server = srv.Server()
    inpt = input("Input cmd <rids/gid/quit>:\n")
    if inpt == "quit":
        server.close()
        return
    if inpt == "rids":
        if input("are you sure?\n>>> ") == "yes":
            server.reset_ids()
    if inpt == "gid":
        inpt2 = input("\nid>>> ")
        server.get_id(inpt2)
    serverintloop()


def run():

    inpt = input("\nHello!\nWould you like to see Bitcoin price? Y/N/test/query/server\n")
    if inpt.lower() == 'y':
        print("doing stuff [nothing]")
    elif inpt.lower() == "test":
        x = input("Not set up")
        tests(x)
#**************************************************
#TODO: Finish 'query'
#**************************************************
    elif inpt.lower() == "query":
        x = input("Enter query string: [coin name/ ticker] [price,lastupdate,24h]\n")
        args = x.split(" ")
        if(args.__len__() > 2):
            print("Error: expected two input words, got {}".format(args.__len__()))
    elif inpt.lower() == "server":
        serverintloop()
    elif inpt.lower() == "q":
        pass
    else:
        run()

import os
import os.path as path


def readKeys():
    #**************************************************
    # TODO: Move Keys.txt and make more private.
    #**************************************************
    path = 'Keys.txt'
    file = open(path, 'r')
    fkeys = file.readlines()
    keys = []
    for x in fkeys:
        x = x.split(" ", 1)
        tup = (x[0], x[1][:-2])
        keys.append(tup)
    file.close()
    print(keys)
    return keys

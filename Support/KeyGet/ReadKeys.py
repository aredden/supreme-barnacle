import os

#   @params none
#   @return keys from Keys.txt in /Src/
def readKeys():
    file = open('Keys.txt', 'r')
    fkeys = file.readlines()
    keys = []
    for x in fkeys:
        x = x.split(" ", 1)
        tup = (x[0], x[1][:-2])
        keys.append(tup)
    file.close()
    return keys

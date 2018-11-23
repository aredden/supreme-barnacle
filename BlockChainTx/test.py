#from ReadKeys import readKeys
import time
from .DBconnect import database

def dbtests():
    db = database
    db.test()

def tests(test):
    if test == "db":
        dbtests()
    else:
         return

import pymongo
from pymongo import MongoClient
import urllib.parse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
user = urllib.parse.quote_plus('adam2')
pas = urllib.parse.quote_plus('hl5jsBQVe7mIlO6V')
uri = f"mongodb+srv://adam:Work123!@#cluster0.f6mndat.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server

client = MongoClient(uri, username=user, password =pas)

mydb=client["fakeData"]
collection=mydb["FakeCID"]
#Need to change this to get the specific users Database/collection


def getPollutant():
    
res=collection.find({"Sensor":"Gas"})
print(res)
for hello in res:
    print(hello)


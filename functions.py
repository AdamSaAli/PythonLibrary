import pymongo
from pymongo import MongoClient
import urllib.parse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#from gui import getUserPollutant
#import pprint

#maybe I should import pprint to print the data in a nicer format

user = urllib.parse.quote_plus('adam2')
pas = urllib.parse.quote_plus('hl5jsBQVe7mIlO6V')
uri = f"mongodb+srv://adam:Work123!@#cluster0.f6mndat.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server

client = MongoClient(uri, username=user, password =pas)

mydb=client["fakeData"]
collection=mydb["FakeCID"]
#Need to change this to get the specific users Database/collection


def getPollutant():
    #pollutant = getUserPollutant()
    #This will work when I tie the gui with the functions  
    pollutant = "PM"
    #the spelling is very important so make sure to double check that
    res=collection.find({"Sensor":f"{pollutant}"})
    print(list(res))
    
    return res
    #I will probably need to send this back to gui file to display it

def getSpecificTime():
    
    return

def getSpecificUnit():
    #this needs to be able to return more than one unit if need be
    #collection=mydb["FakeCID"] I am going to have to be able to insert all the units the user could want into the FakeCID spot
    #Im thinking in the gui file when returning the users units I store them in a list and return that
    #then I could iterate over the list and insert those into the spot 
    return

#res=collection.find({"Sensor":"Gas"})
#print(res)
#for hello in res:
#    print(hello)

hi = getPollutant()
#print(hi)
#print("HIHIHIHI")

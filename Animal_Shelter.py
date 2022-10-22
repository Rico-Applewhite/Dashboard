from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('localhost:41385')
        self.database = self.client.ACC
        self.database.authenticate(username, password, source = 'ACC')

# Complete this create method to implement the C in CRUD.
    def create(self, newData):
        if newData is not None:
            self.database.animals.insert(newData)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. 
    def read(self, findData):
        if findData is not None:
            foundData = self.database.animals.find_one(findData)
            return foundData
        else: 
            raise Exception("Nothing to search for, data paramete is empty")
            return Exception

# Create method to implement the U in CRUD. 
    def update(self, thisData, newData):
        if thisData is not None:
            self.database.animals.update(thisData,newData)
            foundData = self.database.animals.find_one(newData)
            return dumps(foundData)

        else:
            raise Exception("Nothing to search for, data parameter is empty")
            return Exception    
    
# Create method to implement the D in CRUD. 
    def delete(self, thisData):
        if thisData is not None:
            self.database.animals.remove(thisData)
            removedData= self.database.animals.find(thisData)
            return dumps(removedData)
        else:
            raise Exception("Nothing to search for, data parameter is empty")
            return Exception
        
# Create method to implement the Read All. 
    def read_all(self, findData):
        if findData is not None:
            foundData = self.database.animals.find(findData)
            return foundData
        else: 
            raise Exception("Nothing to search for, data paramete is empty")
            return Exception  
    
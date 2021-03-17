from flask_pymongo import pymongo

class Config():

    
    CONNECTION_STRING = "mongodb+srv://pensedatabase:iePhei4a@cluster0-mvnvv.mongodb.net/test?retryWrites=true&w=majority"
#CONNECTION_STRING = "mongodb+srv://pensedatabase:iePhei4a@cluster0.mvnvv.mongodb.net/pensedatabase?retryWrites=true&w=majority"

    #client = pymongo.MongoClient(CONNECTION_STRING)
#db = client.get_database('pensedatabase')
#user_collection = pymongo.collection.Collection(db, 'frases')

#mongodb+srv://pensedatabase:<password>@cluster0.mvnvv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
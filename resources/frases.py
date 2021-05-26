import sqlite3
import pymongo
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.frase import FraseModel

from db import Config

class Frases(Resource):
    
    @jwt_required()
    def get(self, name):
        retorno = []
        db = pymongo.MongoClient(Config.CONNECTION_STRING)
        #client = pymongo.MongoClient(CONNECTION_STRING)
        
        query = {"autor": name + "/"}
    
        frases  = db.pensedatabase.frasesnovas.find(query).sort("_id", pymongo.DESCENDING).limit(100)
        #frases = db.pensedatabase.frases.find().limit(10)
        print(frases)
        for frase in frases:
            retorno.append({"frase": frase['frase'], "_id": str(frase['_id'])})

        db.close()
        
        return {'autor': name, 'frases': retorno}
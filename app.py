from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from bson import ObjectId
from flask_jwt import JWT, jwt_required
import pymongo

from security import authenticate, identity
from user import UserRegister

from db import Config

import db


app = Flask(__name__)
app.secret_key = "8Tb1JM2-lF',qM$.GVl^eaQ8UakLgAhp*#i8O;kG~$&i3IW!7r\]@J6z/j8U@CY"
api = Api(app)

jwt = JWT(app, authenticate, identity)  #/auth

class Frases(Resource):
    
    @jwt_required()
    def get(self, name):
        retorno = []
        db = pymongo.MongoClient(Config.CONNECTION_STRING)
        #client = pymongo.MongoClient(CONNECTION_STRING)
        
        query = {"autor": name + "/"}
    
        frases  = db.pensedatabase.frasesnovas.find(query).sort("_id", pymongo.DESCENDING).limit(100)
        #frases = db.pensedatabase.frases.find().limit(10)

        for frase in frases:
            retorno.append({"frase": frase['frase'], "_id": str(frase['_id'])})

        db.close()
        
        return {'autor': name, 'frases': retorno}

api.add_resource(Frases, '/frases/<string:name>')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
pp.run(port=8000)

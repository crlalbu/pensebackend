from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymongo

from db import Config

import db


app = Flask(__name__)
api = Api(app)

class Frases(Resource):
    

    def get(self, name):
        retorno = []
        db = pymongo.MongoClient(Config.CONNECTION_STRING)
        #client = pymongo.MongoClient(CONNECTION_STRING)
        
        query = {"autor": name + "/"}
    
        frases  = db.pensedatabase.frases.find(query).sort("_id", pymongo.DESCENDING).limit(100)
        #frases = db.pensedatabase.frases.find().limit(10)

        for frase in frases:
            retorno.append({"frase": frase['frase']})

        db.close()

        return {'auto': name, 'frases': retorno}

api.add_resource(Frases, '/frases/<string:name>')

app.run(port=5000)
# @app.route('/')
# def flask_mongodb_altas():
#     return "flask mongodb altas!"

# @app.route('/teste')
# def teste():
    
#     frases = db.client.pensedatabase.frases.find().limit(10)
    
#     retorno = {}
#     for frase in frases:
        
#         retorno = {"autor": frase['autor'], "frase": frase['frase']}
            
        
#     return retorno

# @app.route('/author/<string:name>')
# def getAuthor(name):
#     retorno = []
#     query = {"autor": name + "/"}
#     print(query)
#     frases  = db.client.pensedatabase.frases.find(query).sort("_id", pymongo.DESCENDING).limit(10)
    
#     for frase in frases:
#         retorno.append({"frase": frase['frase']})
        

#     return jsonify(retorno)

# @app.route('/myfrases', 'POST')
# def favFrase():
#     pass

# @app.route('favoriteFrases')
# def getFavoriteFrases():
#     pass

# def get moreScored():
#     pass
#     # for x in teste:
# def get myFavorites():
#     pass

# def get myAuthors():
#     pass
#     #return f"{retorno}"


# if __name__ == '__main__':
#     app.run(port=8000)

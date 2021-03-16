from flask import Flask, jsonify, request
import pymongo

import db


app = Flask(__name__)

@app.route('/')
def flask_mongodb_altas():
    return "flask mongodb altas!"

@app.route('/teste')
def teste():
    #CONNECTION_STRING = "mongodb+srv://pensedatabase:iePhei4a@cluster0-mvnvv.mongodb.net/test?retryWrites=true&w=majority"
    #client = pymongo.MongoClient(CONNECTION_STRING)
    #print(client.list_database_names())
    #frase = client.pensedatabase.frases.find_one()
    frases = db.client.pensedatabase.frases.find().limit(10)
    #$teste = db.user_collection.find().limit(1)
    retorno = {}
    for frase in frases:
        retorno = {"autor": frase['autor'], "frase": frase['frase']}
            
        
    return jsonify(retorno)

@app.route('/author/<string:name>')
def getAuthor(name):
    retorno = []
    query = {"autor": name + "/"}
    print(query)
    frases  = db.client.pensedatabase.frases.find(query).sort("_id", pymongo.DESCENDING).limit(10)
    
    for frase in frases:
        retorno.append({"frase": frase['frase']})
        

    return jsonify(retorno)

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


if __name__ == '__main__':
    app.run(port=8000)

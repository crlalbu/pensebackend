from flask import Flask
from flask_restful import  Api
from bson import ObjectId
from flask_jwt import JWT
import pymongo

from security import authenticate, identity
from resources.user import UserRegister
from resources.frases import Frases



import db


app = Flask(__name__)
app.secret_key = "8Tb1JM2-lF',qM$.GVl^eaQ8UakLgAhp*#i8O;kG~$&i3IW!7r\]@J6z/j8U@CY"
api = Api(app)

jwt = JWT(app, authenticate, identity)  #/auth



api.add_resource(Frases, '/frases/<string:name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import Config
    app.run(host="0.0.0.0")


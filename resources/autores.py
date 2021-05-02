import sqlite3
import pymongo
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.frase import FraseModel
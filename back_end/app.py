from flask_cors import CORS
from flask import Flask
from config import *
from CNN3D import CNN3D
from Data import Data

app = Flask(__name__)
CNN3D = CNN3D()

CORS(app, resources={r"/*": {"origins": OROGINS}})

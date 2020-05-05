from flask_cors import CORS
from flask import Flask
from config import *
from CNN3D import CNN3D
app = Flask(__name__)
cnn3d = CNN3D()
CORS(app, resources={r"/*": {"origins": OROGINS}})

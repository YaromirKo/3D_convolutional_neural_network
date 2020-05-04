from flask_cors import CORS
from flask import Flask
from config import *

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": OROGINS}})

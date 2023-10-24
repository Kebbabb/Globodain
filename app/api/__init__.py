from flask import Blueprint
from flask import Flask
from app import app

_api = Blueprint('api',__name__,template_folder='templates')
app.config["MONGO_URI"] = "mongodb://localhost:27017/Test"

from . import routes
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from models.main import *
from controllers import *
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

@app.route("/", methods=["GET", "POST"])
def index():
    app.logger.debug("Shantanu")
    return "Hello World!", 200
  

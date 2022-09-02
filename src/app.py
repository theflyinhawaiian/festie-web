from flask import Flask
from src.v1.api import api_v1

app = Flask(__name__)

app.register_blueprint(api_v1, url_prefix="/api/v1")
from flask import Flask
from src.extensions import db, bcrypt
from src.v1.api import api_v1
from src.auth import auth

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:localdev@localhost/festie-db'
    # TODO: Probably don't have this committed to source control
    app.config['SECRET_KEY'] = "\x8dvts\x8d\r\xe3+\xec\x0cK\x19\xdf,\x11\xfe\xf4\xff\xa40sOG\xf9\x89\x1b\xcb\xc9\xb7\x06\xbcd"

    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    return app
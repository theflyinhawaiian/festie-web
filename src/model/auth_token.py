import jwt
import datetime
from flask import current_app

class AuthToken:
    @staticmethod
    def encode_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(
                token, 
                current_app.config.get('SECRET_KEY'),
                algorithms='HS256'
                )
            return payload['sub']
        except Exception as e:
            return e